#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<fftw3.h>

#define PI   3.141592653 // the value of PI

#define nc   1024        // number of cells per dimension 
#define cnc  (nc/2 + 1)  // number of cells in x axis in complex output 
#define box  1200.       // box size in unit of Mpc/h
#define kf   (2.*PI/box) // fundamental frequency

char path1[80] = {"../../tides05/0.000wgam110.bin"};
char path2[80] = {"../../tides05/0.000wgam210.bin"};
char pathout1[80] = {"../../tides05/0.000uwkappa10.bin"};
char pathout2[80] = {"../../tides05/0.000uwkappb10.bin"};
 
int index_f (int k, int j, int i);
int index_k (int k, int j, int i);
/*==============================*/
int main (void)  {
    fftw_complex *gamma1k;
    fftw_complex *gamma2k;
    double *gamma1r;
    double *gamma2r;
    fftw_plan plan1;
    fftw_plan plan2;
    fftw_plan plana;
    fftw_plan planb;
    int nn = 1024;    // this needs to be changed to nc
    int cn2= nn/2 + 1;
    int N  = nn*nn*nn;
    int Nc = nn*nn*cn2;

    gamma1k = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * Nc);
    gamma2k = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * Nc);
    gamma1r = (double *) fftw_malloc(N * sizeof(double));
    gamma2r = (double *) fftw_malloc(N * sizeof(double));
    plan1 = fftw_plan_dft_r2c_3d(nn, nn, nn, gamma1r, gamma1k, FFTW_ESTIMATE);
    plan2 = fftw_plan_dft_r2c_3d(nn, nn, nn, gamma2r, gamma2k, FFTW_ESTIMATE);
    plana = fftw_plan_dft_c2r_3d(nn, nn, nn, gamma1k, gamma1r, FFTW_ESTIMATE);
    planb = fftw_plan_dft_c2r_3d(nn, nn, nn, gamma2k, gamma2r, FFTW_ESTIMATE);
/*===Finishing FFTW initialization===*/

    int i, j, k, index_0;
    float ga1, ga2;

    FILE *GAM1 = fopen(path1, "rb");
    FILE *GAM2 = fopen(path2, "rb");
 
    printf("Reading..\n");
    for(k = 0; k < nn; k++)  {
        for(j = 0; j < nn; j++)  {
            for(i = 0; i < nn; i++)  {
                index_0 = index_f(k, j, i);
                fread(&ga1, 4, 1, GAM1);
                fread(&ga2, 4, 1, GAM2);
                gamma1r[index_0] = ga1;
                gamma2r[index_0] = ga2;
            }
        }
    }
   printf("Finish reading...\n");
/*===Finishing reading data===*/

    fftw_execute(plan1);
    fftw_execute(plan2);
    printf("Finish fft for the first time...\n");
/*===Finishing FFTW one===*/

    double r_part1, i_part1;
    double r_part2, i_part2;
    int    x, y, z;
    double k2, k_mag, kv2, kv_mag, k1hat, k2hat;
    double factor1, factor2, weight;

    for(k = 0; k < nn; k++)  {
        printf("complicate process~~~%d\n", k);
        for(j = 0; j < nn; j++)  {
            for(i = 0; i < cn2; i++)  {
                index_0 = index_k(k, j, i); //index to find that element
                r_part1 = gamma1k[index_0][0];
                i_part1 = gamma1k[index_0][1];
                r_part2 = gamma2k[index_0][0];
                i_part2 = gamma2k[index_0][1];
  
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
                    gamma1k[index_0][0] = 0.;
                    gamma1k[index_0][1] = 0.;
                    gamma2k[index_0][0] = 0.;
                    gamma2k[index_0][1] = 0.;
                }
                else  {
                k1hat  = x/kv_mag;
                k2hat  = y/kv_mag;
                factor1 = (pow(k1hat, 2) - pow(k2hat, 2)) * 2. * k2/kv2;
                factor2 = (2.*k1hat*k2hat) * 2. *k2/kv2;
                weight  = pow((kv2/k2), 2);
                gamma1k[index_0][0] = (factor1*r_part1+factor2*r_part2);
                gamma1k[index_0][1] = (factor1*i_part1+factor2*i_part2); 
                gamma2k[index_0][0] = (-factor2*r_part1+factor1*r_part2);
                gamma2k[index_0][1] = (-factor2*i_part1+factor1*i_part2);
                }
           }
        }
    }
    fftw_execute(plana);
    fftw_execute(planb);
    printf("Finishig IFFT ......\n");
/*===Multiplying  window function===*/

    FILE *KAP  = fopen(pathout1, "wb");
    FILE *KAPU = fopen(pathout2, "wb");
   
    float out1, out2;
    printf("Begin to output...\n");
    for(k = 0; k < nn; k++)  {
        for(j = 0; j < nn; j++)  {
            for(i = 0; i < nn; i++)  {
                index_0 = index_f(k, j, i);
                out1 = gamma1r[index_0]/pow(nc, 3);
                out2 = gamma2r[index_0]/pow(nc, 3);
                fwrite(&out1, 4, 1, KAP);
                fwrite(&out2, 4, 1, KAPU);
            }
        }
    }
/*============================*/ 
    fftw_destroy_plan(plan1);
    fftw_destroy_plan(plan2);
    fftw_destroy_plan(plana);
    fftw_destroy_plan(planb);
    fftw_free(gamma1k);
    fftw_free(gamma2k);
    fftw_free(gamma1r);
    fftw_free(gamma2r);

    return 0;
}
/*============== End ==============*/

int index_f (int k, int j, int i)
{
    int n = (k*nc + j)*nc + i;
    return n;
}

int index_k (int k, int j, int i)
{
    int n = (k*nc + j)*cnc + i;
    return n;
}
