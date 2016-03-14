#!/bin/bash
#usage:
#sh run.sh /home/mtx/data/tide/haloes/0.000halo_0.0024.bin /home/mtx/data/tide/haloes/outdata/halo_0024/
com=`date '+%Y/%m/%d_%H:%M:%S'`
echo '------------------------------------------------------------------------------------------'
echo '**************************************'$com'******************************************'
#mpirun -hostfile node_hostfile python uwkappa_Gau.py           $@
mpirun -hostfile node_hostfile python uwkappa_1_smooth.py      $@
mpirun -hostfile node_fat      python uwkappa_2_Gau.py         $@
#mpirun -hostfile node_hostfile python uwkappa_3_uwkappa.py     $@
mpirun -hostfile node_fast python get_bin1d.py 0.000den00_Pk_halo.hdf5 PS_haloDD    $@

#mpirun -hostfile node_fast python get_bin2d.py $@
#mpirun -hostfile node_hostfile python get_bin2d_rsd.py $@
#mpirun -hostfile node_fat python mv_result.py  $@
#mpirun -hostfile node_hostfile python wkkappa.py    $@
#mpirun -hostfile node_fast python get_bin1d.py 0.000den00_Pk_delta_kappa.hdf5 PS_DK  $@
#mpirun -hostfile node_fast python get_bin1d.py 0.000den00_Pk_kappa.hdf5 PS_KK        $@
#mpirun -hostfile node_fast python get_bin1d.py 0.000den00_Pk_delta.hdf5 PS_DD        $@

#mpirun -hostfile node_fast python compare_bias.py bias.hdf5 compare_bias            $@

rm result_b
rm result_W
com=`date '+%Y/%m/%d_%H:%M:%S'`
echo '**************************END IN:    '$com'******************************************'
