#!/bin/bash
name_1=$@
name_2=bias_smooth2.5_m4
name1='/home/mtx/data/tide/outdata/'$name_1'/halo/'$name_2'/'
name2='/home/mtx/data/tide/outdata/'$name_1'/halo/'$name_2'/'
echo $name1'0.000halo00_wfPk_kappa.hdf5' $name2'PS_KK'
################################################################################
#python result.py $name_1 $name_2
#mpirun -hostfile node_hostfile python get_bin2d1.py $name_1 $name_2
mpirun -hostfile myhostfile python get_bin2d2.py $name_1 $name_2
python get_wfPk.py $name_1 $name_2
mpirun -hostfile node_hostfile python get_bin1d.py $name1'0.000halo00_wfPk_kappa.hdf5' $name2'PS_KK'
mpirun -hostfile node_hostfile python get_bin1d.py $name1'0.000halo00_wfPk_delta.hdf5' $name2'PS_DD'
mpirun -hostfile node_hostfile python get_bin1d.py $name1'0.000halo00_wfPk_delta_kappa.hdf5' $name2'PS_DK'
mpirun -hostfile node_hostfile python get_bin1d.py $name1'0.000halo00_Pk_halo.hdf5' $name2'PS_haloDD'
echo 'step 2 ok' 
