#!/usr/bin/env python
# coding=utf-8
from TIDES import Tide
import numpy as np
from Pk import pk_cro_bin as pk
from Pk import get_bin1d 
i=10
in_dir='/project/mtx/data/tides%s/'%str(i)
filename1='0.000delta.bin'
filename2='0.000halo_0.0012.bin'
filename3='highmass2_0.0012.bin'
filename4='highmass3_0.0012.bin'
filename5='highmass4_0.0012.bin'
out_dir='/project/mtx/output/tides%s/'%str(i)

for file in [filename2,filename3,filename4,filename5]:
#   print out_dir+file[:-4]+'_1.25_NoGau/'
    pk.pk_cro(Input1=in_dir+filename1,Input2=in_dir+file,output=out_dir+file[:-4]+'_1.25_NoGau/'+'0.000den00_Pk_delta_halo.hdf5')
    get_bin1d.get_bin1d(out_dir+file[:-4]+'_1.25_NoGau/'+'0.000den00_Pk_delta_halo.hdf5',out_dir+file[:-4]+'_1.25_NoGau/'+'PS_DH',bins=20)

