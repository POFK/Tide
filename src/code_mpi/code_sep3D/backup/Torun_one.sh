#!/bin/bash
# tides10; outputDir; halo field
stime=1.5m
#======= 3D tides =======================
#./sep_run.sh 10 0.0024_3D_NoGau_s1.25_NoWiener 0.000halo_0.0024.hdf5
#./sep_run.sh 10 LOW_0.0024_3D_NoGau_s1.25_NoWiener 0.000halo_0.0024_LOW.hdf5
#./sep_run.sh 10 0.0024_3D_NoGau_s1.25_NoWiener 0.000halo_0.0024.hdf5
#./sep_run.sh 10 LOW_0.0024_3D_NoGau_s1.25_4test 0.000halo_0.0024_LOW.hdf5
#./sep_run.sh 10 0.0024_3D_NoGau_s1.25_Ptot_4test_mode3 0.000halo_0.0024.hdf5
#./sep_run.sh 10 LOW_0.0024_3D_NoGau_s1.25_Ptot_4test 0.000halo_0.0024_LOW.hdf5
#./sep_run.sh 10 combian_4_inverseBias halo_combina_inverseBias_4bin.hdf5 
#./sep_run.sh 10 combian_4_inverseBias_Gau halo_combina_inverseBias_4bin.hdf5 

#=======To test wiener and smooth========
#./sep_run.sh 10 0.0048_3D_NoGau_s1.25_Wiener 0.000halo_0.0048.hdf5 

#./sep_run.sh 10 0.0024_3D_NoGau_s1.25_Wiener 0.000halo_0.0024.hdf5 
#./sep_run.sh 10 0.0012_3D_NoGau_s1.25_Wiener 0.000halo_0.0012.hdf5 

#./sep_run.sh 10 0.0048_3D_NoGau_Wiener_noSmooth 0.000halo_0.0048.hdf5 
#./sep_run.sh 10 0.0024_3D_NoGau_Wiener_noSmooth 0.000halo_0.0024.hdf5 
#./sep_run.sh 10 0.0012_3D_NoGau_Wiener_noSmooth 0.000halo_0.0012.hdf5 

#time ./sep_run.sh 10 0.0048_3D_NoGau_Wiener_Smooth1.00 0.000halo_0.0048.hdf5
#time ./sep_run.sh 10 0.0048_3D_NoGau_Wiener_Smooth1.10 0.000halo_0.0048.hdf5
#time ./sep_run.sh 10 0.0048_3D_NoGau_Wiener_Smooth0.80 0.000halo_0.0048.hdf5


#./sep_run.sh 10 CIC_0.0048_3D_NoGau_s1.25_NoWiener 0.000halo_0.0048_cic1.hdf5
#./sep_run.sh 11 CIC_0.0048_3D_NoGau_s1.25_NoWiener 0.000halo_0.0048_cic1.hdf5
#./sep_run.sh 12 CIC_0.0048_3D_NoGau_s1.25_NoWiener 0.000halo_0.0048_cic1.hdf5
#./sep_run.sh 13 CIC_0.0048_3D_NoGau_s1.25_NoWiener 0.000halo_0.0048_cic1.hdf5
#./sep_run.sh 14 CIC_0.0048_3D_NoGau_s1.25_NoWiener 0.000halo_0.0048_cic1.hdf5
#./sep_run.sh 15 CIC_0.0048_3D_NoGau_s1.25_NoWiener 0.000halo_0.0048_cic1.hdf5
#./sep_run.sh 16 CIC_0.0048_3D_NoGau_s1.25_NoWiener 0.000halo_0.0048_cic1.hdf5
#./sep_run.sh 17 CIC_0.0048_3D_NoGau_s1.25_NoWiener 0.000halo_0.0048_cic1.hdf5
#./sep_run.sh 18 CIC_0.0048_3D_NoGau_s1.25_NoWiener 0.000halo_0.0048_cic1.hdf5
#./sep_run.sh 19 CIC_0.0048_3D_NoGau_s1.25_NoWiener 0.000halo_0.0048_cic1.hdf5

#./sep_run.sh 10 combineMassbin_0.0024_test combine_2bins/0.000halo_cic_0.0024_mbin2.hdf5
./sep_run.sh 10 combineMassbin_0.0024 combine_2bins/0.000halo_cic_2binsCombine.hdf5
#==============Cut off===================
#time ./sep_run.sh 10 0.0048_3D_NoGau_Wiener_Smooth1.25_cut0.8 0.000halo_0.0048.hdf5
