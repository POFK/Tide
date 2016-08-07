#!/bin/bash
# tides10; outputDir; halo field
stime=1.5m
#======= 3D tides to test ===============
#time ./sep_run.sh 10 test_4.8_s0.8_Wpd_biasConstant 0.000halo_cic_0.0048.hdf5
#time ./sep_run.sh 10 test_4.8_s0.8_Wpd_biasVariable 0.000halo_cic_0.0048.hdf5
#time ./sep_run.sh 10 test_4.8_s0.8_Wph_biasConstant 0.000halo_cic_0.0048.hdf5

#time ./sep_run.sh 10 test_2.4_s1.0_Wph_biasConstant 0.000halo_cic_0.0024.hdf5
#time ./sep_run.sh 10 test_2.4_s0.9_Wpd_biasConstant 0.000halo_cic_0.0024.hdf5
#========================================

#./sep_run.sh 10 CIC_0.0048_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0048.hdf5
#./sep_run.sh 11 CIC_0.0048_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0048.hdf5
#./sep_run.sh 12 CIC_0.0048_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0048.hdf5
#./sep_run.sh 13 CIC_0.0048_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0048.hdf5
#./sep_run.sh 14 CIC_0.0048_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0048.hdf5
#./sep_run.sh 15 CIC_0.0048_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0048.hdf5
#./sep_run.sh 16 CIC_0.0048_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0048.hdf5
#./sep_run.sh 17 CIC_0.0048_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0048.hdf5
#./sep_run.sh 18 CIC_0.0048_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0048.hdf5
#./sep_run.sh 19 CIC_0.0048_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0048.hdf5
#
#./sep_run.sh 10 CIC_0.0036_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0036.hdf5
#./sep_run.sh 11 CIC_0.0036_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0036.hdf5
#./sep_run.sh 12 CIC_0.0036_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0036.hdf5
#./sep_run.sh 13 CIC_0.0036_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0036.hdf5
#./sep_run.sh 14 CIC_0.0036_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0036.hdf5
#./sep_run.sh 15 CIC_0.0036_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0036.hdf5
#./sep_run.sh 16 CIC_0.0036_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0036.hdf5
#./sep_run.sh 17 CIC_0.0036_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0036.hdf5
#./sep_run.sh 18 CIC_0.0036_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0036.hdf5
#./sep_run.sh 19 CIC_0.0036_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0036.hdf5
#
#./sep_run.sh 10 CIC_0.0024_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 11 CIC_0.0024_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 12 CIC_0.0024_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 13 CIC_0.0024_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 14 CIC_0.0024_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 15 CIC_0.0024_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 16 CIC_0.0024_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 17 CIC_0.0024_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 18 CIC_0.0024_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 19 CIC_0.0024_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0024.hdf5
#
#./sep_run.sh 10 CIC_0.0012_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0012.hdf5
#./sep_run.sh 11 CIC_0.0012_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0012.hdf5
#./sep_run.sh 12 CIC_0.0012_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0012.hdf5
#./sep_run.sh 13 CIC_0.0012_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0012.hdf5
#./sep_run.sh 14 CIC_0.0012_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0012.hdf5
#./sep_run.sh 15 CIC_0.0012_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0012.hdf5
#./sep_run.sh 16 CIC_0.0012_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0012.hdf5
#./sep_run.sh 17 CIC_0.0012_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0012.hdf5
#./sep_run.sh 18 CIC_0.0012_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0012.hdf5
#./sep_run.sh 19 CIC_0.0012_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0012.hdf5


#======= bias weighting =================

#./sep_run.sh 10 massbin4biasWeight_halo_cic_0.0012_1 massbin_0.000halo_cic_0.0012_1.hdf5
#./sep_run.sh 10 massbin4biasWeight_halo_cic_0.0012_2 massbin_0.000halo_cic_0.0012_2.hdf5
#./sep_run.sh 11 massbin4biasWeight_halo_cic_0.0012_1 massbin_0.000halo_cic_0.0012_1.hdf5
#./sep_run.sh 11 massbin4biasWeight_halo_cic_0.0012_2 massbin_0.000halo_cic_0.0012_2.hdf5
#./sep_run.sh 12 massbin4biasWeight_halo_cic_0.0012_1 massbin_0.000halo_cic_0.0012_1.hdf5
#./sep_run.sh 12 massbin4biasWeight_halo_cic_0.0012_2 massbin_0.000halo_cic_0.0012_2.hdf5
#./sep_run.sh 13 massbin4biasWeight_halo_cic_0.0012_1 massbin_0.000halo_cic_0.0012_1.hdf5
#./sep_run.sh 13 massbin4biasWeight_halo_cic_0.0012_2 massbin_0.000halo_cic_0.0012_2.hdf5
#./sep_run.sh 14 massbin4biasWeight_halo_cic_0.0012_1 massbin_0.000halo_cic_0.0012_1.hdf5
#./sep_run.sh 14 massbin4biasWeight_halo_cic_0.0012_2 massbin_0.000halo_cic_0.0012_2.hdf5
#./sep_run.sh 15 massbin4biasWeight_halo_cic_0.0012_1 massbin_0.000halo_cic_0.0012_1.hdf5
#./sep_run.sh 15 massbin4biasWeight_halo_cic_0.0012_2 massbin_0.000halo_cic_0.0012_2.hdf5
#./sep_run.sh 16 massbin4biasWeight_halo_cic_0.0012_1 massbin_0.000halo_cic_0.0012_1.hdf5
#./sep_run.sh 16 massbin4biasWeight_halo_cic_0.0012_2 massbin_0.000halo_cic_0.0012_2.hdf5
#./sep_run.sh 17 massbin4biasWeight_halo_cic_0.0012_1 massbin_0.000halo_cic_0.0012_1.hdf5
#./sep_run.sh 17 massbin4biasWeight_halo_cic_0.0012_2 massbin_0.000halo_cic_0.0012_2.hdf5
#./sep_run.sh 18 massbin4biasWeight_halo_cic_0.0012_1 massbin_0.000halo_cic_0.0012_1.hdf5
#./sep_run.sh 18 massbin4biasWeight_halo_cic_0.0012_2 massbin_0.000halo_cic_0.0012_2.hdf5
#./sep_run.sh 19 massbin4biasWeight_halo_cic_0.0012_1 massbin_0.000halo_cic_0.0012_1.hdf5
#./sep_run.sh 19 massbin4biasWeight_halo_cic_0.0012_2 massbin_0.000halo_cic_0.0012_2.hdf5

#./sep_run.sh 10 massbin4biasWeight_halo_cic_0.0012_2massbin_m1 combine_2bins/0.000halo_cic_0.0012_2binsCombine_m1.hdf5
#./sep_run.sh 10 massbin4biasWeight_halo_cic_0.0012_2massbin_m2 combine_2bins/0.000halo_cic_0.0012_2binsCombine_m2.hdf5
./sep_run.sh 10 massbin4biasWeight_halo_cic_0.0012_2massbin_m3 combine_2bins/0.000halo_cic_0.0012_2binsCombine_m2.hdf5

