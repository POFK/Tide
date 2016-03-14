#!/bin/bash
#================================================================================
INPUT='/project/mtx/data/'
OUTPUT='/project/mtx/output/'
smooth='_1.25_rsd'

sh run_rsd.sh $INPUT'tides10/0.000halo_0.0048_rsd3.bin' $OUTPUT'tides10/halo_0.0048'$smooth'/' $INPUT'tides10/0.000delta.bin'
sh run_rsd.sh $INPUT'tides11/0.000halo_0.0048_rsd3.bin' $OUTPUT'tides11/halo_0.0048'$smooth'/' $INPUT'tides11/0.000delta.bin'
sh run_rsd.sh $INPUT'tides12/0.000halo_0.0048_rsd3.bin' $OUTPUT'tides12/halo_0.0048'$smooth'/' $INPUT'tides12/0.000delta.bin'
sh run_rsd.sh $INPUT'tides13/0.000halo_0.0048_rsd3.bin' $OUTPUT'tides13/halo_0.0048'$smooth'/' $INPUT'tides13/0.000delta.bin'
sh run_rsd.sh $INPUT'tides14/0.000halo_0.0048_rsd3.bin' $OUTPUT'tides14/halo_0.0048'$smooth'/' $INPUT'tides14/0.000delta.bin'
sh run_rsd.sh $INPUT'tides15/0.000halo_0.0048_rsd3.bin' $OUTPUT'tides15/halo_0.0048'$smooth'/' $INPUT'tides15/0.000delta.bin'

python  get_bias_wiener.py $OUTPUT'tides10/halo_0.0048'$smooth'/' $OUTPUT'tides11/halo_0.0048'$smooth'/' $OUTPUT'tides12/halo_0.0048'$smooth'/' $OUTPUT'tides13/halo_0.0048'$smooth'/' $OUTPUT'tides14/halo_0.0048'$smooth'/' $OUTPUT'tides15/halo_0.0048'$smooth'/' 

sh run_norsd_2.sh $INPUT'tides10/0.000halo_0.0048_rsd3.bin' $OUTPUT'tides10/halo_0.0048'$smooth'/' $INPUT'tides10/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides11/0.000halo_0.0048_rsd3.bin' $OUTPUT'tides11/halo_0.0048'$smooth'/' $INPUT'tides11/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides12/0.000halo_0.0048_rsd3.bin' $OUTPUT'tides12/halo_0.0048'$smooth'/' $INPUT'tides12/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides13/0.000halo_0.0048_rsd3.bin' $OUTPUT'tides13/halo_0.0048'$smooth'/' $INPUT'tides13/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides14/0.000halo_0.0048_rsd3.bin' $OUTPUT'tides14/halo_0.0048'$smooth'/' $INPUT'tides14/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides15/0.000halo_0.0048_rsd3.bin' $OUTPUT'tides15/halo_0.0048'$smooth'/' $INPUT'tides15/0.000delta.bin'

#================================================================================
