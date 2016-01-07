#include<stdio.h>
#include<math.h>
#include<stdlib.h>

#define nc  1024

int main(void)  {
    int i;
    int num = pow(nc, 3);
    float input;

    float *density;
    density = (float *) malloc(sizeof(float) * num);
       
    FILE *IN1 = fopen("../../tides05/0.000dens1.25.bin", "rb");
    FILE *OU1 = fopen("../../tides05/0.000densg1.25.bin", "wb");

    for (i = 0; i < num; i++)  {
        if ((i+1)%(nc*nc) == 0) printf("Reading...%d\n", (i+1)/nc/nc);
        fread(&input, 4, 1, IN1);

 /*       input = input - 1.;
        
        if(input <= 0) {
            density[i] = input;
        }
        else {
            density[i] = log(1. + input);
        }
*/      
        if(input <= 1) {
            density[i] = input - 1.;
        }
        else {
            density[i] = log(input);
        }
    }
    
    for (i = 0; i < num; i++)  {
        if ((i+1)%(nc*nc) == 0) printf("Outputing..%d\n", (i+1)/nc/nc);
        fwrite(&density[i], 4, 1, OU1);
    }

    return 0;
/*=============*/
}
