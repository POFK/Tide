#!/bin/bash
# tides10; outputDir; halo field
stime=1.5m
#================================================================================
#./sep_run.sh 10 test_0.000halo_0.0003_cic_wienerConst_s1.0 massbin_0.0003_m4/0.000halo_cic_0.0003.hdf5
#./sep_run.sh 10 test_0.000halo_0.0003_cic_wienerPh_s1.0 massbin_0.0003_m4/0.000halo_cic_0.0003.hdf5


#./sep_run.sh 10 massbin4_0.0048_m1  massbin_0.0048_m4/massbin4_0.000halo_0.0048_cic_1.hdf5
#./sep_run.sh 10 massbin4_0.0048_m2  massbin_0.0048_m4/massbin4_0.000halo_0.0048_cic_2.hdf5
#./sep_run.sh 10 massbin4_0.0048_m3  massbin_0.0048_m4/massbin4_0.000halo_0.0048_cic_3.hdf5
#./sep_run.sh 10 massbin4_0.0048_m4  massbin_0.0048_m4/massbin4_0.000halo_0.0048_cic_4.hdf5

#./sep_run.sh 10 massbin4_0.0003_combine_bE1  massbin_0.0003_m4/massbin4_0.0003_b.hdf5
#./sep_run.sh 10 massbin4_0.0003_combine_bE2  massbin_0.0003_m4/massbin4_0.0003_b2.hdf5
#./sep_run.sh 10 massbin4_0.0003_combine_bE-1  massbin_0.0003_m4/massbin4_0.0003_b-1.hdf5

#./sep_run.sh 10 massbin4_0.0048_combine_bE1  combine_massbin_kIndependentWieneredDelta/massbin4_0.0048_WS_b1.hdf5

#./sep_run.sh 10 massbin4_0.0003_combine_wienerKindependent_bE1_noWiener_test  combine_massbin_kIndependentWieneredDelta/massbin4_0.0003_WS_b1_m1noW4test.hdf5
#./sep_run.sh 10 massbin4_0.0003_combine_wienerKindependent_bE2_noWiener  combine_massbin_kIndependentWieneredDelta/massbin4_0.0003_WS_b2.hdf5
#./sep_run.sh 10 massbin4_0.0003_combine_wienerKindependent_bE1_noWiener2  combine_massbin_kIndependentWieneredDelta/massbin4_0.0003_WS_b1.hdf5
#./sep_run.sh 10 massbin4_0.0003_combine_wienerPh_bE1_noWiener  combine_massbin_PhWieneredDelta/massbin4_0.0003_WS_b1.hdf5
#./sep_run.sh 10 massbin4_0.0003_combine_wienerPh_bE2  massbin_0.0003_m4/massbin4_0.0003_b2.hdf5
#./sep_run.sh 10 massbin4_0.0003_combine_wienerPh_bE-1  massbin_0.0003_m4/massbin4_0.0003_b-1.hdf5


#./sep_run.sh 10 massbin10_0.0003_combine_wienerKindependent_bE0_noWiener  combine_massbin_kIndependentWieneredDelta/massbin10_0.0003_WS_b0.hdf5
#./sep_run.sh 10 massbin10_0.0003_combine_wienerKindependent_bE1_noWiener  combine_massbin_kIndependentWieneredDelta/massbin10_0.0003_WS_b1.hdf5
#./sep_run.sh 10 massbin10_0.0003_combine_wienerKindependent_bE2_noWiener  combine_massbin_kIndependentWieneredDelta/massbin10_0.0003_WS_b2.hdf5
#./sep_run.sh 10 massbin10_0.0003_combine_wienerKindependent_bE1_Wiener  combine_massbin_kIndependentWieneredDelta/massbin10_0.0003_WS_b1.hdf5

#./sep_run.sh 10 massbin4_0.0024_m1   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_1.hdf5
#./sep_run.sh 10 massbin4_0.0024_m2   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_2.hdf5
#./sep_run.sh 10 massbin4_0.0024_m3   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_3.hdf5
#./sep_run.sh 10 massbin4_0.0024_m4   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_4.hdf5
#
#./sep_run.sh 11 massbin4_0.0024_m1   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_1.hdf5
#./sep_run.sh 11 massbin4_0.0024_m2   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_2.hdf5
#./sep_run.sh 11 massbin4_0.0024_m3   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_3.hdf5
#./sep_run.sh 11 massbin4_0.0024_m4   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_4.hdf5
#
#./sep_run.sh 12 massbin4_0.0024_m1   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_1.hdf5
#./sep_run.sh 12 massbin4_0.0024_m2   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_2.hdf5
#./sep_run.sh 12 massbin4_0.0024_m3   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_3.hdf5
#./sep_run.sh 12 massbin4_0.0024_m4   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_4.hdf5
#
#./sep_run.sh 13 massbin4_0.0024_m1   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_1.hdf5
#./sep_run.sh 13 massbin4_0.0024_m2   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_2.hdf5
#./sep_run.sh 13 massbin4_0.0024_m3   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_3.hdf5
#./sep_run.sh 13 massbin4_0.0024_m4   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_4.hdf5
#
#./sep_run.sh 14 massbin4_0.0024_m1   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_1.hdf5
#./sep_run.sh 14 massbin4_0.0024_m2   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_2.hdf5
#./sep_run.sh 14 massbin4_0.0024_m3   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_3.hdf5
#./sep_run.sh 14 massbin4_0.0024_m4   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_4.hdf5
#
#./sep_run.sh 15 massbin4_0.0024_m1   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_1.hdf5
#./sep_run.sh 15 massbin4_0.0024_m2   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_2.hdf5
#./sep_run.sh 15 massbin4_0.0024_m3   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_3.hdf5
#./sep_run.sh 15 massbin4_0.0024_m4   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_4.hdf5
#
#./sep_run.sh 16 massbin4_0.0024_m1   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_1.hdf5
#./sep_run.sh 16 massbin4_0.0024_m2   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_2.hdf5
#./sep_run.sh 16 massbin4_0.0024_m3   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_3.hdf5
#./sep_run.sh 16 massbin4_0.0024_m4   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_4.hdf5
#
#./sep_run.sh 17 massbin4_0.0024_m1   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_1.hdf5
#./sep_run.sh 17 massbin4_0.0024_m2   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_2.hdf5
#./sep_run.sh 17 massbin4_0.0024_m3   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_3.hdf5
#./sep_run.sh 17 massbin4_0.0024_m4   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_4.hdf5
#
#./sep_run.sh 18 massbin4_0.0024_m1   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_1.hdf5
#./sep_run.sh 18 massbin4_0.0024_m2   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_2.hdf5
#./sep_run.sh 18 massbin4_0.0024_m3   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_3.hdf5
#./sep_run.sh 18 massbin4_0.0024_m4   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_4.hdf5
#
#./sep_run.sh 19 massbin4_0.0024_m1   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_1.hdf5
#./sep_run.sh 19 massbin4_0.0024_m2   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_2.hdf5
#./sep_run.sh 19 massbin4_0.0024_m3   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_3.hdf5
#./sep_run.sh 19 massbin4_0.0024_m4   massbin_0.0024_m4/massbin4_0.000halo_0.0024_cic_4.hdf5
#
#================================================================================
#./sep_run.sh 10 CIC_0.0003_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0003.hdf5
#./sep_run.sh 11 CIC_0.0003_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0003.hdf5
#./sep_run.sh 12 CIC_0.0003_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0003.hdf5
#./sep_run.sh 13 CIC_0.0003_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0003.hdf5
#./sep_run.sh 14 CIC_0.0003_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0003.hdf5
#./sep_run.sh 15 CIC_0.0003_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0003.hdf5
#./sep_run.sh 16 CIC_0.0003_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0003.hdf5
#./sep_run.sh 17 CIC_0.0003_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0003.hdf5
#./sep_run.sh 18 CIC_0.0003_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0003.hdf5
#./sep_run.sh 19 CIC_0.0003_3D_NoGau_s1.0_Wiener 0.000halo_cic_0.0003.hdf5
#================================================================================


./sep_run.sh 10 massbin2_0.0003_combine_diffW 0.000halo_cic_0.0003.hdf5
./sep_run.sh 10 massbin2_0.0003_combine_cross     0
./sep_run.sh 10 massbin2_0.0003_m1   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_1.hdf5
./sep_run.sh 10 massbin2_0.0003_m2   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_2.hdf5

