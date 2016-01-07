#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<fftw3.h>

#define PI   3.141592653 // the value of PI

#define nc   1024        // number of cells per dimension 
#define cnc  (nc/2 + 1)  // number of cells in x axis in complex output 
#define box  1200.       // box size in unit of Mpc/h
#define kf   (2.*PI/box) // fundamental frequency

char path[80]    = {"../../tides00/0.000deng1.25.bin"};
char pathout[80] = {"../../tides00/0.000dengx1.25.bin"}; 
 
int index_f (int k, int j, int i);
int index_k (int k, int j, int i);
/*==============================*/
int main (void)  {
    fftw_complex *deltak;
    double *deltar;
    double *deltars;
    fftw_plan plan;
    fftw_plan plans;
    int nn = 1024;    // 768 could be changed to nc
    int cn2= nn/2 + 1;
    int N  = nn*nn*nn;
    int Nc = nn*nn*cn2;

    deltak = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * Nc);
    deltar = (double *) fftw_malloc(N * sizeof(double));
    deltars= (double *) fftw_malloc(N * sizeof(double));
    plan = fftw_plan_dft_r2c_3d(nn, nn, nn, deltar, deltak, FFTW_ESTIMATE);
    plans= fftw_plan_dft_c2r_3d(nn, nn, nn, deltak, deltars,FFTW_ESTIMATE);
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
                deltar[index_0] = input;
            }
        }
    }
   printf("Finish reading...\n");
/*===Finishing reading data===*/

    fftw_execute(plan);
    printf("Finish fftw for the first time...\n");
/*===Finishing FFTW one===*/

    double r_part, i_part;
    int    x, y, z;
    double k2, factor, window;

    for(k = 0; k < nn; k++)  {
        printf("complicate process~~~%d\n", k);
        for(j = 0; j < nn; j++)  {
            for(i = 0; i < cn2; i++)  {
                index_0 = index_k(k, j, i); //index to find that element
                r_part  = deltak[index_0][0];
                i_part  = deltak[index_0][1];
                x = i;     // index to calculating wavenumber
                if(j < cn2) y = j; else y = (nn - j)*(-1.);
                if(k < cn2) z = k; else z = (nn - k)*(-1.);
                k2 = x*x + y*y + z*z;
              
                //factor = (-1.)*k2*kf*kf*R*R/2.;
                window = 1.;
                deltak[index_0][0] = i_part*window*kf*x*(-1.);
                deltak[index_0][1] = r_part*window*kf*x;
           }
        }
    }

    fftw_execute(plans);
/*===Multiplying  window function===*/

    FILE *OUT = fopen(pathout, "wb");
    
    printf("Begin to output...\n");
    for(k = 0; k < nn; k++)  {
        for(j = 0; j < nn; j++)  {
            for(i = 0; i < nn; i++)  {
                index_0 = index_f(k, j, i);
                input   = deltars[index_0]/pow(nc, 3);
                fwrite(&input, 4, 1, OUT);
            }
        }
    }

/*============================*/ 
    fftw_destroy_plan(plan);
    fftw_destroy_plan(plans);
    fftw_free(deltak);
    fftw_free(deltar);
    fftw_free(deltars);

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
