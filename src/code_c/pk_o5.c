#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<fftw3.h>

#define PI   3.141592653 // the value of PI

#define nc   1024        // number of cells per dimension in one node 
#define cnc  (nc/2 + 1)  // number of cells in x dimension in complex output 
#define box  1200.       // box size of the cube from one node
#define bins 10          // number of bins for power spectrum
#define kf   (2.*PI/box) // fundamental frequency 

char path[80]    = {"../../tides05/0.000den00.bin"};
char pathout[80] = {"output/0.000pk2d05_up.dat"}; 

long int index_f (long int k, long int j, long int i);
long int index_k (long int k, long int j, long int i);
/*==============================*/
int main (void) 
{
    fftw_complex *deltak;
    double *deltar;
    fftw_plan plan;
    long int nn = 1024;    // This needs to be changed to the value of nc
    long int cn2= nn/2 + 1;
    long int N  = nn*nn*nn;
    long int Nc = nn*nn*cn2;

    deltak = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * Nc);
    deltar = (double *) fftw_malloc(N * sizeof(double));
    plan = fftw_plan_dft_r2c_3d(nn, nn, nn, deltar, deltak, FFTW_ESTIMATE);
/*===Finishing FFTW initialization===*/

    long int i, j, k, index_0;
    float input;
    FILE *DEN = fopen(path, "rb");
    printf("Reading..\n");
    for(k = 0; k < nn; k++)  {
        for(j = 0; j < nn; j++)  {
            for(i = 0; i < nn; i++)  {
                index_0 = index_f(k, j, i);
                fread(&input, 4, 1, DEN);
                deltar[index_0] = input - 1.;
            }
        }
    }

   printf("Finish reading...\n");
/*===Finishing reading data===*/

   double r_part, i_part, deltak2;

    fftw_execute(plan);
    printf("Finish fftw...\n");

    for(k = 0; k < nn; k++)  {
        printf("Squareing...%d\n", k);
        for(j = 0; j < nn; j++)  {
            for(i = 0; i < cn2; i++)  {
                index_0 = index_k(k, j, i);
                r_part  = deltak[index_0][0];
                i_part  = deltak[index_0][1];
                deltak2 = r_part*r_part + i_part*i_part;
                deltak[index_0][0] = deltak2;
            }
        }
    }
    printf("Finish square...\n");
/*===Finishing FFTW & Calculating module===*/

    long int x, y, z, ka, kb;
    double   k2, k_mag, kv2, kv_mag, kz2, kz_mag, logk, logkv, logkz, Dlogk;
    double   sincx, sincy, sincz, window;
    long int count[bins][bins] = {0.};
    double   k_bin[bins][bins] = {0.};
    double   p_bin[bins][bins] = {0.};

    Dlogk = (log10(nn/2) - log10(1))/bins; //Calculating spacing in log bins
    printf("%f\t%f\t%d\t%f\t\n", log10(nn/2), log10(1), bins, Dlogk);
    printf("%d\t%d\n", nn, nn/2);

    for(k = 0; k < nn; k++)  {
        printf("complicate process~~~%d\n", k);
        for(j = 0; j < nn; j++)  {
            for(i = 0; i < cn2; i++)  {
                index_0 = index_k(k, j, i); //index to find that element

                x = i;     // index to calculating wavenumber
                if(j < cn2) y = j; else y = nn - j;
                if(k < cn2) z = k; else z = nn - k;
                k2 = x*x + y*y + z*z;
                kv2 = x*x + y*y;
                kz2 = z*z;
                if (k2 == 0) continue;
                if (kv2 == 0) {
                    kb = 0;
                }
                else {
                    kv_mag = sqrt(kv2);
                    logkv  = log10(kv_mag);
                    kb     = logkv/Dlogk;
                }
                if (kz2 == 0) {
                    ka = 0;
                }
                else {
                    kz_mag = sqrt(kz2);
                    logkz  = log10(kz_mag);
                    ka     = logkz/Dlogk;
                }

                if(ka >= bins) continue;
                if(kb >= bins) continue;

                if(x == 0) sincx = 1.; else sincx = sin(PI*x/nn)/(PI*x/nn);
                if(y == 0) sincy = 1.; else sincy = sin(PI*y/nn)/(PI*y/nn);
                if(z == 0) sincz = 1.; else sincz = sin(PI*z/nn)/(PI*z/nn);
                window = pow(sincx, 2)*pow(sincy, 2)*pow(sincz, 2);

                count[ka][kb] = count[ka][kb] + 1;
                k_bin[ka][kb] = k_bin[ka][kb] + k_mag;
                p_bin[ka][kb] = p_bin[ka][kb] + deltak[index_0][0]/window;
            }
        }
    }
    printf("finish bins...\n");

    for(i = 0; i < bins; i++)  {
        for(j = 0; j < bins; j++) {
        printf("avaraging bins...%d\n", i);
        k_bin[i][j] = k_bin[i][j]/count[i][j];
        p_bin[i][j] = p_bin[i][j]/count[i][j];

//        k_bin[i] = k_bin[i]*kf;
        p_bin[i][j] = p_bin[i][j]*pow(box, 3)/pow(nn, 6);
//        p_bin[i] = p_bin[i]*pow(box, 3)/pow(nn, 6)*pow(k_bin[i], 3)/2./PI/PI;
        }
    }
/*===Deconvolving window function & Caculating power specturm in bins===*/

    FILE *OUT = fopen(pathout, "w");
    for(i = 0; i < bins; i++)  {
        for(j = 0; j < bins; j++)   {
        fprintf(OUT, "%e\t", p_bin[i][j]);
        //printf("Outputing...%d\n", i);
        }
        fprintf(OUT, "\n");
    }
/*============================*/ 
    fftw_destroy_plan(plan);
    fftw_free(deltak);
    fftw_free(deltar);

    return 0;
}
/*============== End ==============*/

long int index_f (long int k, long int j, long int i)
{
    long int n = (k*nc + j)*nc + i;
    return n;
}

long int index_k (long int k, long int j, long int i)
{
    long int n = (k*nc + j)*cnc + i;
    return n;
}
