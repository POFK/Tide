#!/bin/bash
# tides10; outputDir; halo field
stime=1.5m
#======= 3D tides =======================
#time ./sep_run.sh 10 test_3D_Gau 0.000halo_0.0048.hdf5
#time ./sep_run.sh 10 test_3D_Gau_ori 0.000halo_0.0048.hdf5
#time ./sep_run.sh 9 test_3D_No_Gau 0.000halo_0.0048.hdf5
#time ./sep_run.sh 13 test_3D_No_Gau 0.000halo_0.0048.hdf5  
##sleep 5m
#time ./sep_run.sh 14 test_3D_No_Gau 0.000halo_0.0048.hdf5 
##sleep 5m
#time ./sep_run.sh 15 test_3D_No_Gau 0.000halo_0.0048.hdf5 

#time ./sep_run.sh 10 combina_4bin_biasW_3D_Gau halo_combina_bias_4bin.hdf5 &
#sleep 5s
#time ./sep_run.sh 10 0.0048_3D_Gau 0.000halo_0.0048.hdf5
#time ./sep_run.sh 10 0.0048_S2.5_3D_Gau 0.000halo_0.0048.hdf5

#======= 3D tides cut-off ===============
#======= 3D tides =======================
# step 1
time ./sep_run1.sh 10 0.0048_3D_Gau_s2.5 0.000halo_0.0048.hdf5 
time ./sep_run1.sh 11 0.0048_3D_Gau_s2.5 0.000halo_0.0048.hdf5 
time ./sep_run1.sh 12 0.0048_3D_Gau_s2.5 0.000halo_0.0048.hdf5 
time ./sep_run1.sh 13 0.0048_3D_Gau_s2.5 0.000halo_0.0048.hdf5 
time ./sep_run1.sh 14 0.0048_3D_Gau_s2.5 0.000halo_0.0048.hdf5 
time ./sep_run1.sh 15 0.0048_3D_Gau_s2.5 0.000halo_0.0048.hdf5 
# step 2
time ./sep_run2.sh 10 0.0048_3D_Gau_s2.5 0.000halo_0.0048.hdf5 
time ./sep_run2.sh 11 0.0048_3D_Gau_s2.5 0.000halo_0.0048.hdf5 
time ./sep_run2.sh 12 0.0048_3D_Gau_s2.5 0.000halo_0.0048.hdf5 
time ./sep_run2.sh 13 0.0048_3D_Gau_s2.5 0.000halo_0.0048.hdf5 
time ./sep_run2.sh 14 0.0048_3D_Gau_s2.5 0.000halo_0.0048.hdf5 
time ./sep_run2.sh 15 0.0048_3D_Gau_s2.5 0.000halo_0.0048.hdf5 
