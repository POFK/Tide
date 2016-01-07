gcc recon.c -lm -L/opt/fftw-3.3.3/lib -lfftw3 -I/opt/fftw-3.3.3/include -L/opt/gsl-1.15-gcc-4.4.6/lib -lgsl -lgslcblas -I/opt/gsl-1.15-gcc-4.4.6/include -o lp
./lp
