#!/bin/bash
#========================================================
num=$1
dir=$2
halo_input=$3
python sep_checkDir.py   $num $dir $halo_input 
#========================================================
python sep_cutoff.py  $num $dir $halo_input 
python sep_runPk0.py                                   $num $dir $halo_input 
python sep_run_bin1d0.py                               $num $dir $halo_input 
mpirun -hostfile node_hostfile python sep_smooth.py    $num $dir $halo_input 
python gau.py                                          $num $dir $halo_input 
mpirun -hostfile node_fat      python sep_wden.py      $num $dir $halo_input 
mpirun -hostfile node_hostfile python sep_gamma.py     $num $dir $halo_input 
mpirun -hostfile node_hostfile python sep_kappa_3d.py  $num $dir $halo_input 
python sep_runPk1.py                                   $num $dir $halo_input 
python sep_run_bin1d4BiasNoise.py                      $num $dir $halo_input 
mpirun -hostfile node_hostfile python sep_get_bin2d.py $num $dir $halo_input 
python remove.py      $num $dir $halo_input 
##========================================================
##python get_wiener_bias.py $num $dir $halo_input 
#python get_wiener_bias_all.py $num $dir $halo_input 
##========================================================
#mpirun -hostfile node_hostfile python sep_wkkappa.py   $num $dir $halo_input 
#python sep_runPk2.py                                   $num $dir $halo_input 
#python sep_run_bin1d.py $num $dir $halo_input 
#python plot_result.py $num $dir $halo_input 
##python remove.py      $num $dir $halo_input 
