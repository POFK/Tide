#!/bin/bash
# tides10; outputDir; halo field
stime=1.5m
#================================================================================

#================================================================================
#./sep_run.sh 10 CIC_0.0024_3D_NoGau_s1.0_Wiener_cut1.0 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 11 CIC_0.0024_3D_NoGau_s1.0_Wiener_cut1.0 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 12 CIC_0.0024_3D_NoGau_s1.0_Wiener_cut1.0 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 13 CIC_0.0024_3D_NoGau_s1.0_Wiener_cut1.0 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 14 CIC_0.0024_3D_NoGau_s1.0_Wiener_cut1.0 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 15 CIC_0.0024_3D_NoGau_s1.0_Wiener_cut1.0 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 16 CIC_0.0024_3D_NoGau_s1.0_Wiener_cut1.0 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 17 CIC_0.0024_3D_NoGau_s1.0_Wiener_cut1.0 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 18 CIC_0.0024_3D_NoGau_s1.0_Wiener_cut1.0 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 19 CIC_0.0024_3D_NoGau_s1.0_Wiener_cut1.0 0.000halo_cic_0.0024.hdf5
#================================================================================

#./sep_run.sh 10 CIC_0.0024_3D_NoGau_s1.0_Wiener_cut1.0 0.000halo_cic_0.0024.hdf5

#./sep_run.sh 10 massbin2_0.0024_combine_diffW 0.000halo_cic_0.0024.hdf5
#./sep_run.sh 10 massbin2_0.0003_combine_cross     0
#./sep_run.sh 10 massbin2_0.0003_m1   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_1.hdf5
#./sep_run.sh 10 massbin2_0.0003_m2   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_2.hdf5


#========================== mass bin ============================================
#./sep_run.sh 10 massbin2_0.0003_m1   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_1.hdf5
#./sep_run.sh 11 massbin2_0.0003_m1   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_1.hdf5
#./sep_run.sh 12 massbin2_0.0003_m1   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_1.hdf5
#./sep_run.sh 13 massbin2_0.0003_m1   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_1.hdf5
#./sep_run.sh 14 massbin2_0.0003_m1   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_1.hdf5
#./sep_run.sh 15 massbin2_0.0003_m1   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_1.hdf5
#./sep_run.sh 16 massbin2_0.0003_m1   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_1.hdf5
#./sep_run.sh 17 massbin2_0.0003_m1   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_1.hdf5
#./sep_run.sh 18 massbin2_0.0003_m1   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_1.hdf5
#./sep_run.sh 19 massbin2_0.0003_m1   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_1.hdf5
#
#./sep_run.sh 10 massbin2_0.0003_m2   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_2.hdf5
#./sep_run.sh 11 massbin2_0.0003_m2   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_2.hdf5
#./sep_run.sh 12 massbin2_0.0003_m2   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_2.hdf5
#./sep_run.sh 13 massbin2_0.0003_m2   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_2.hdf5
#./sep_run.sh 14 massbin2_0.0003_m2   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_2.hdf5
#./sep_run.sh 15 massbin2_0.0003_m2   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_2.hdf5
#./sep_run.sh 16 massbin2_0.0003_m2   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_2.hdf5
#./sep_run.sh 17 massbin2_0.0003_m2   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_2.hdf5
#./sep_run.sh 18 massbin2_0.0003_m2   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_2.hdf5
#./sep_run.sh 19 massbin2_0.0003_m2   massbin_0.0003_m2/massbin2_0.000halo_0.0003_cic_2.hdf5
#
#python sep_combineWden.py    10    massbin2_0.0003_combine_cross  0
#python sep_combineWden.py    11    massbin2_0.0003_combine_cross  0
#python sep_combineWden.py    12    massbin2_0.0003_combine_cross  0
#python sep_combineWden.py    13    massbin2_0.0003_combine_cross  0
#python sep_combineWden.py    14    massbin2_0.0003_combine_cross  0
#python sep_combineWden.py    15    massbin2_0.0003_combine_cross  0
#python sep_combineWden.py    16    massbin2_0.0003_combine_cross  0
#python sep_combineWden.py    17    massbin2_0.0003_combine_cross  0
#python sep_combineWden.py    18    massbin2_0.0003_combine_cross  0
#python sep_combineWden.py    19    massbin2_0.0003_combine_cross  0
#
#
#./sep_run.sh                 10    massbin2_0.0003_combine_cross  0
#./sep_run.sh                 11    massbin2_0.0003_combine_cross  0
#./sep_run.sh                 12    massbin2_0.0003_combine_cross  0
#./sep_run.sh                 13    massbin2_0.0003_combine_cross  0
#./sep_run.sh                 14    massbin2_0.0003_combine_cross  0
#./sep_run.sh                 15    massbin2_0.0003_combine_cross  0
#./sep_run.sh                 16    massbin2_0.0003_combine_cross  0
#./sep_run.sh                 17    massbin2_0.0003_combine_cross  0
#./sep_run.sh                 18    massbin2_0.0003_combine_cross  0
#./sep_run.sh                 19    massbin2_0.0003_combine_cross  0
#
#
#python sep_combineWkappa.py   10    massbin2_0.0003_combine_diffW  0
#python sep_combineWkappa.py   11    massbin2_0.0003_combine_diffW  0
#python sep_combineWkappa.py   12    massbin2_0.0003_combine_diffW  0
#python sep_combineWkappa.py   13    massbin2_0.0003_combine_diffW  0
#python sep_combineWkappa.py   14    massbin2_0.0003_combine_diffW  0
#python sep_combineWkappa.py   15    massbin2_0.0003_combine_diffW  0
#python sep_combineWkappa.py   16    massbin2_0.0003_combine_diffW  0
#python sep_combineWkappa.py   17    massbin2_0.0003_combine_diffW  0
#python sep_combineWkappa.py   18    massbin2_0.0003_combine_diffW  0
#python sep_combineWkappa.py   19    massbin2_0.0003_combine_diffW  0

#./sep_run.sh                 10    massbin2_0.0024_combine_diffW  0
#./sep_run.sh                 11    massbin2_0.0024_combine_diffW  0
#./sep_run.sh                 12    massbin2_0.0024_combine_diffW  0
#./sep_run.sh                 13    massbin2_0.0024_combine_diffW  0
#./sep_run.sh                 14    massbin2_0.0024_combine_diffW  0
#./sep_run.sh                 15    massbin2_0.0024_combine_diffW  0
#./sep_run.sh                 16    massbin2_0.0024_combine_diffW  0
#./sep_run.sh                 17    massbin2_0.0024_combine_diffW  0
#./sep_run.sh                 18    massbin2_0.0024_combine_diffW  0
#./sep_run.sh                 19    massbin2_0.0024_combine_diffW  0
#
#./sep_run.sh                 10    massbin2_0.0003_combine_diffW  0
#./sep_run.sh                 11    massbin2_0.0003_combine_diffW  0
#./sep_run.sh                 12    massbin2_0.0003_combine_diffW  0
#./sep_run.sh                 13    massbin2_0.0003_combine_diffW  0
#./sep_run.sh                 14    massbin2_0.0003_combine_diffW  0
#./sep_run.sh                 15    massbin2_0.0003_combine_diffW  0
#./sep_run.sh                 16    massbin2_0.0003_combine_diffW  0
#./sep_run.sh                 17    massbin2_0.0003_combine_diffW  0
#./sep_run.sh                 18    massbin2_0.0003_combine_diffW  0
#./sep_run.sh                 19    massbin2_0.0003_combine_diffW  0

#./sep_run.sh                 10    massbin2_0.0003_combine_diffW_test4wienerOnebyone  0
#./sep_run.sh                 11    massbin2_0.0003_combine_diffW_test4wienerOnebyone  0
#./sep_run.sh                 12    massbin2_0.0003_combine_diffW_test4wienerOnebyone  0
#./sep_run.sh                 13    massbin2_0.0003_combine_diffW_test4wienerOnebyone  0
#./sep_run.sh                 14    massbin2_0.0003_combine_diffW_test4wienerOnebyone  0
#./sep_run.sh                 15    massbin2_0.0003_combine_diffW_test4wienerOnebyone  0
#./sep_run.sh                 16    massbin2_0.0003_combine_diffW_test4wienerOnebyone  0
#./sep_run.sh                 17    massbin2_0.0003_combine_diffW_test4wienerOnebyone  0
#./sep_run.sh                 18    massbin2_0.0003_combine_diffW_test4wienerOnebyone  0
#./sep_run.sh                 19    massbin2_0.0003_combine_diffW_test4wienerOnebyone  0

#========================== mass bin  END =======================================
