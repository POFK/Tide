#!/bin/bash

#!/bin/bash
#sh run_norsd_1.sh /home/mtx/data/tide/haloes2/0.000halo_0.0048.bin /project/mtx/output/tides00/halo_0.0048/
#================================================================================
INPUT='/project/mtx/data/'
OUTPUT='/project/mtx/output/'

sh run_norsd_1.sh $INPUT'tides10/0.000halo_0.0048.bin' $OUTPUT'tides10/halo_0.0048/' $INPUT'tides10/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides10/0.000halo_0.0048.bin' $OUTPUT'tides10/halo_0.0048/' $INPUT'tides10/0.000delta.bin'
sh run_norsd_1.sh $INPUT'tides11/0.000halo_0.0048.bin' $OUTPUT'tides11/halo_0.0048/' $INPUT'tides11/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides11/0.000halo_0.0048.bin' $OUTPUT'tides11/halo_0.0048/' $INPUT'tides11/0.000delta.bin'
sh run_norsd_1.sh $INPUT'tides12/0.000halo_0.0048.bin' $OUTPUT'tides12/halo_0.0048/' $INPUT'tides12/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides12/0.000halo_0.0048.bin' $OUTPUT'tides12/halo_0.0048/' $INPUT'tides12/0.000delta.bin'
sh run_norsd_1.sh $INPUT'tides13/0.000halo_0.0048.bin' $OUTPUT'tides13/halo_0.0048/' $INPUT'tides13/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides13/0.000halo_0.0048.bin' $OUTPUT'tides13/halo_0.0048/' $INPUT'tides13/0.000delta.bin'
sh run_norsd_1.sh $INPUT'tides14/0.000halo_0.0048.bin' $OUTPUT'tides14/halo_0.0048/' $INPUT'tides14/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides14/0.000halo_0.0048.bin' $OUTPUT'tides14/halo_0.0048/' $INPUT'tides14/0.000delta.bin'
sh run_norsd_1.sh $INPUT'tides15/0.000halo_0.0048.bin' $OUTPUT'tides15/halo_0.0048/' $INPUT'tides15/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides15/0.000halo_0.0048.bin' $OUTPUT'tides15/halo_0.0048/' $INPUT'tides15/0.000delta.bin'

#python  get_bias_wiener.py $OUTPUT'tides10/halo_0.0048/' $OUTPUT'tides11/halo_0.0048/' $OUTPUT'tides12/halo_0.0048/' $OUTPUT'tides13/halo_0.0048/' $OUTPUT'tides14/halo_0.0048/' $OUTPUT'tides15/halo_0.0048/' 


#================================================================================
