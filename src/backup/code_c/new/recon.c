#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<fftw3.h>
#include<gsl/gsl_interp.h>
#include<gsl/gsl_spline.h>
#include<gsl/gsl_errno.h>

#define PI   3.141592653 // the value of PI

#define nc   1024        // number of cells per dimension 
#define cnc  (nc/2 + 1)  // number of cells in x axis in complex output 
#define box  1200.       // box size in unit of Mpc/h
#define kf   (2.*PI/box) // fundamental frequency
#define ic   500          // number of filters

char path[80] =    {"/home/mtx/data/tide/outdata/old_test/c_test_data/0.000deng1.25.bin"};
char pathout[80] = {"/home/mtx/data/tide/outdata/old_test/c_test_data/0.000uwkappa1.25.bin"};

char patf[80]    = {"./filter/coeffz0.dat"};
double k_initial[ic] = {0.};
double f_initial[ic] = {0.};
 
int index_f (int k, int j, int i);
int index_k (int k, int j, int i);
/*==============================*/
int main (void)  {
    fftw_complex *a1k;
    fftw_complex *a2k;
    double *a1r;
    double *a2r;
    fftw_plan plan;
    fftw_plan planx;
    fftw_plan plany;
    fftw_plan plan1;
    fftw_plan plan2;
    fftw_plan plank;
    int nn = 1024;    // 768 could be changed to nc
    int cn2= nn/2 + 1;
    int N  = nn*nn*nn;
    int Nc = nn*nn*cn2;

    a1k = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * Nc);
    a2k = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * Nc);
    a1r = (double *) fftw_malloc(N * sizeof(double));
    a2r = (double *) fftw_malloc(N * sizeof(double));
    plan = fftw_plan_dft_r2c_3d(nn, nn, nn, a1r, a1k, FFTW_ESTIMATE);
    planx= fftw_plan_dft_c2r_3d(nn, nn, nn, a1k, a1r, FFTW_ESTIMATE);
    plany= fftw_plan_dft_c2r_3d(nn, nn, nn, a2k, a2r, FFTW_ESTIMATE);
    plan1= fftw_plan_dft_r2c_3d(nn, nn, nn, a1r, a1k, FFTW_ESTIMATE);
    plan2= fftw_plan_dft_r2c_3d(nn, nn, nn, a2r, a2k, FFTW_ESTIMATE);
    plank= fftw_plan_dft_c2r_3d(nn, nn, nn, a1k, a1r, FFTW_ESTIMATE);
/*===Finishing FFTW initialization===*/

    int i, j, k, index_0;
    float input;
    FILE *DEN = fopen(path, "rb");
    printf("Reading..\n");
    for(k = 0; k < nn; k++)  {
        for(j = 0; j < nn; j++)  {
            for(i = 0; i < nn; i++)  {
                index_0 = index_f(k, j, i);
                fread(&input, 4, 1, DEN);
                a1r[index_0] = input;
            }
        }
    }
   printf("Finish reading data...\n");

   FILE *FIL = fopen(patf, "rb");
   for(i = 0; i < ic; i++)  {
       fscanf(FIL, "%lf %lf\n", &k_initial[i], &f_initial[i]);
   }
    gsl_interp_accel   *acc    = gsl_interp_accel_alloc();
    gsl_spline         *spline = gsl_spline_alloc (gsl_interp_cspline, ic);
    gsl_spline_init (spline, k_initial, f_initial, ic);
/*===Finishing reading data===*/

    fftw_execute(plan);
    printf("Finish fftw for the first time...a1r-->a1k\n");
/*===Finishing FFTW one===*/

    double r_part, i_part;
    int    x, y, z;
    double k2, k_mag, window;

    for(k = 0; k < nn; k++)  {
        //printf("complicate process~~~%d\n", k);
        for(j = 0; j < nn; j++)  {
            for(i = 0; i < cn2; i++)  {
                index_0 = index_k(k, j, i); //index to find that element
                r_part  = a1k[index_0][0];
                i_part  = a1k[index_0][1];
                x = i;     // index to calculating wavenumber
                if(j < cn2) y = j; else y = (nn - j)*(-1.);
                if(k < cn2) z = k; else z = (nn - k)*(-1.);
                k2 = x*x + y*y + z*z;
                k_mag = sqrt(k2)*kf;
               
                if ((k_mag > 50) || (k_mag < 3e-3)) {
                    window = 1.;
                }
                else {
                    window = gsl_spline_eval (spline, k_mag, acc);
                }

                a1k[index_0][0] = i_part*window*kf*x*(-1.);
                a1k[index_0][1] = r_part*window*kf*x;
                a2k[index_0][0] = i_part*window*kf*y*(-1.);
                a2k[index_0][1] = r_part*window*kf*y;
            }
        }
    }

    fftw_execute(planx);
    fftw_execute(plany);
    printf("Finish fftw for the second time...derivatives\n");
/*===Multiplying  window function===*/

    double gamma1, gamma2;
    for(k = 0; k < nc; k++)  {
        for(j = 0; j < nc; j++)  {
            for(i = 0; i < nc; i++)  {
                index_0 = index_f(k, j, i);
                gamma1 = pow(a1r[index_0], 2) - pow(a2r[index_0], 2);
                gamma2 = 2.*a1r[index_0]*a2r[index_0];
                a1r[index_0] = gamma1/pow(nc, 6);
                a2r[index_0] = gamma2/pow(nc, 6);
            }
        }
    }
    fftw_execute(plan1);
    fftw_execute(plan2);
    printf("Finish fftw for the third time...tidal shear\n");
/*===Generating tidal shear fields===*/

    double r_part1, i_part1, r_part2, i_part2;
    double kv2, kv_mag, k1hat, k2hat, factor1, factor2;
    
    for(k = 0; k < nn; k++)  {
        //printf("complicate process~~~%d\n", k);
        for(j = 0; j < nn; j++)  {
            for(i = 0; i < cn2; i++)  {
                index_0 = index_k(k, j, i); //index to find that element
                r_part1 = a1k[index_0][0];
                i_part1 = a1k[index_0][1];
                r_part2 = a2k[index_0][0];
                i_part2 = a2k[index_0][1];
                
                x = i;     // index to calculating wavenumber
                if(j < cn2) y = j; else y = (nn - j)*(-1.);
                if(k < cn2) z = k; else z = (nn - k)*(-1.);
                k2     = x*x + y*y + z*z;
                k_mag  = sqrt(k2);
                kv2    = x*x + y*y;
                kv_mag = sqrt(kv2);
                // add something about kv2 = 0 case
                //
                if (kv2 == 0) {
                    a1k[index_0][0] = 0.;
                    a1k[index_0][1] = 0.;
                }
                else  {
                    k1hat  = x/kv_mag;
                    k2hat  = y/kv_mag;
                    factor1 = (pow(k1hat, 2) - pow(k2hat, 2)) * 2. * k2/kv2;
                    factor2 = (2.*k1hat*k2hat) * 2. *k2/kv2;
                    a1k[index_0][0] = (factor1*r_part1+factor2*r_part2);
                    a1k[index_0][1] = (factor1*i_part1+factor2*i_part2);
                }
            }
        }
    }
    fftw_execute(plank);
    printf("Finishig IFFT ......Generating kappa\n");
/*===Generating kappa field ===*/

    FILE *OUT = fopen(pathout, "wb");
    
    printf("Begin to output...\n");
    for(k = 0; k < nn; k++)  {
        for(j = 0; j < nn; j++)  {
            for(i = 0; i < nn; i++)  {
                index_0 = index_f(k, j, i);
                input   = a1r[index_0]/pow(nc, 3);
                fwrite(&input, 4, 1, OUT);
            }
        }
    }
/*============================*/ 
    fftw_destroy_plan(plan);
    fftw_destroy_plan(planx);
    fftw_destroy_plan(plany);
    fftw_destroy_plan(plan1);
    fftw_destroy_plan(plan2);
    fftw_destroy_plan(plank);   
    fftw_free(a1k);
    fftw_free(a2k);
    fftw_free(a1r);
    fftw_free(a2r);
    gsl_spline_free (spline);
    gsl_interp_accel_free (acc);

    return 0;
}
/*============== End ==============*/

int index_f (int k, int j, int i)  {
    int n = (k*nc + j)*nc + i;
    return n;
}

int index_k (int k, int j, int i)  {
    int n = (k*nc + j)*cnc + i;
    return n;
}


