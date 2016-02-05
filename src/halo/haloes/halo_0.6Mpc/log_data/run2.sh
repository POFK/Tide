#!/bin/bash
name_2=bias_smooth2.5_m3
name1='/home/mtx/data/tide/halo_new/outdata/log_data/'
name2='/home/mtx/data/tide/halo_new/outdata/log_data/'
echo $name1'0.000halo00_wfPk_kappa.hdf5' $name2'PS_KK'
################################################################################
#python result.py $name_1 $name_2
#mpirun -hostfile node_hostfile python get_bin2d1.py $name_1 $name_2

mpirun -hostfile myhostfile python get_bin2d2.py
python get_wfPk.py
mpirun -hostfile node_hostfile python get_bin1d.py $name1'0.000halo00_wfPk_kappa.hdf5' $name2'PS_KK'
mpirun -hostfile node_hostfile python get_bin1d.py $name1'0.000halo00_wfPk_delta.hdf5' $name2'PS_DD'
mpirun -hostfile node_hostfile python get_bin1d.py $name1'0.000halo00_wfPk_delta_kappa.hdf5' $name2'PS_DK'
mpirun -hostfile node_hostfile python get_bin1d.py $name1'0.000halo00_Pk_halo.hdf5' $name2'PS_haloDD'
echo 'step 2 ok' 
