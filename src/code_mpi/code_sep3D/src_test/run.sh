#!/bin/bash
# tides10; outputDir; halo field
stime=1.5m
#=======To test wiener and smooth========
#python sep_Pk.py  10 0.0048_3D_NoGau_s1.25_NoWiener 0.000halo_0.0048.hdf5 
#python sep_Pk.py  10 0.0024_3D_NoGau_s1.25_NoWiener 0.000halo_0.0024.hdf5 
#python sep_Pk.py  10 0.0012_3D_NoGau_s1.25_NoWiener 0.000halo_0.0012.hdf5 

#
#
#

python sep_Pk.py  test_4.8_s1.25_Wph_biasConstant
python sep_Pk.py  test_4.8_s1.25_Wpd_biasVariable
python sep_Pk.py  test_4.8_s1.25_Wpd_biasConstant
