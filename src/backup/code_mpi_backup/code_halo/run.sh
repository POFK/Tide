#!/bin/bash
com=`date '+%Y/%m/%d_%H:%M:%S'`
echo '------------------------------------------------------------------------------------------'
echo '**************************************'$com'******************************************'
mpirun -hostfile node_hostfile python uwkappa_Gau.py
#mpirun -hostfile node_hostfile python uwkappa_1_smooth.py
#mpirun -hostfile fat python uwkappa_2_Gau.py
#mpirun -hostfile node_hostfile python uwkappa_3_uwkappa.py
mpirun -hostfile node_faster python get_bin2d.py
cp /home/mtx/data/tide/outdata/test/result_b ./
cp /home/mtx/data/tide/outdata/test/result_W ./
mpirun -hostfile node_hostfile python wkkappa.py
mpirun -hostfile node_faster python get_bin1d.py 0.000den00_Pk_delta_kappa.hdf5 PS_DK
mpirun -hostfile node_faster python get_bin1d.py 0.000den00_Pk_kappa.hdf5 PS_KK
mpirun -hostfile node_faster python get_bin1d.py 0.000den00_Pk_delta.hdf5 PS_DD
mpirun -hostfile node_faster python get_bin1d.py 0.000den00_Pk_halo.hdf5 PS_haloDD
com=`date '+%Y/%m/%d_%H:%M:%S'`
echo '**************************END IN:    '$com'******************************************'
