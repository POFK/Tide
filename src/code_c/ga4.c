#include<stdio.h>
#include<math.h>
#include<stdlib.h>

#define nc   1024         // number of cells per dimension

int index_f (int k, int j, int i);
/*==============================*/
int main(void)  {
    float input, dx, dy;
    float out1, out2;
    int   i, j, k;

    char pathx[80] = {"../../tides04/0.000wdengdx1.25.bin"};
    char pathy[80] = {"../../tides04/0.000wdengdy1.25.bin"};
    
    FILE *DENX = fopen(pathx, "rb");
    FILE *DENY = fopen(pathy, "rb");

    FILE *GAM1 = fopen("../../tides04/0.000wgam1gd1.25.bin", "wb");
    FILE *GAM2 = fopen("../../tides04/0.000wgam2gd1.25.bin", "wb");

    printf("Reading&Outputing...\n");
    for(k = 0; k < nc; k++)  {
        for(j = 0; j < nc; j++)  {
            for(i = 0; i < nc; i++)  {
                fread(&dx,    4, 1, DENX);
                fread(&dy,    4, 1, DENY);
                out1 = dx*dx - dy*dy;
                out2 = 2.*dx*dy;
                fwrite(&out1, 4, 1, GAM1);
                fwrite(&out2, 4, 1, GAM2);
            }
        }
    }
    printf("End...\n");

    return 0;
}


int index_f (int k, int j, int i)
{
        int n = (k*nc + j)*nc + i;
            return n;
}
