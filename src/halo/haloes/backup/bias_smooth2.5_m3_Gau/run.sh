#!/bin/bash
#name='tides00'
name_1=$@
name_2=bias_smooth2.5_m3_gau
name1='/home/mtx/data/tide/outdata/'$name_1'/halo/'$name_2'/'
name2='/home/mtx/data/tide/outdata/'$name_1'/halo/'$name_2'/'
echo $name1'0.000halo00_wfPk_kappa.hdf5' $name2'PS_KK'
################################################################################
#python result.py $name_1 $name_2
#python result2.py $name_1 $name_2
python result3.py $name_1 $name_2
mpirun -hostfile node_hostfile python get_bin2d1.py $name_1 $name_2
echo 'step 1 ok'
#python get_wfPk.py $name_1 $name_2
#mpirun -hostfile myhostfile python get_bin1d.py $name1'0.000halo00_wfPk_kappa.hdf5' $name2'PS_KK'
#mpirun -hostfile myhostfile python get_bin1d.py $name1'0.000halo00_wfPk_delta.hdf5' $name2'PS_DD'
#mpirun -hostfile myhostfile python get_bin1d.py $name1'0.000halo00_wfPk_delta_kappa.hdf5' $name2'PS_DK'

