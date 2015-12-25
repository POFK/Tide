#!/bin/bash
#name='tides00'
name=$@
name1='/home/mtx/data/tide/outdata/'$name'/'
name2='/home/mtx/data/tide/outdata/'$name'/'
echo $name1'0.000den00_wfPk_kappa.hdf5' $name2'PS_KK'
################################################################################
python result.py $name
mpirun -hostfile myhostfile python get_bin2d2.py $name
#python get_wfPk.py $name
#mpirun -hostfile myhostfile python get_bin1d.py $name1'0.000den00_wfPk_kappa.hdf5' $name2'PS_KK'
#mpirun -hostfile myhostfile python get_bin1d.py $name1'0.000den00_wfPk_delta.hdf5' $name2'PS_DD'
#mpirun -hostfile myhostfile python get_bin1d.py $name1'0.000den00_wfPk_delta_kappa.hdf5' $name2'PS_DK'

