#!/bin/bash
#sh run_norsd_1.sh /home/mtx/data/tide/haloes2/0.000highmass2_0.0012.bin /project/mtx/output/tides00/highmass2_0.0012/
#================================================================================
INPUT='/project/mtx/data/'
OUTPUT='/project/mtx/output/'
smooth='_1.25'

sh run_norsd_1.sh $INPUT'tides10/highmass2_0.0012.bin' $OUTPUT'tides10/highmass2_0.0012'$smooth'/' $INPUT'tides10/0.000delta.bin'
sh run_norsd_1.sh $INPUT'tides11/highmass2_0.0012.bin' $OUTPUT'tides11/highmass2_0.0012'$smooth'/' $INPUT'tides11/0.000delta.bin'
sh run_norsd_1.sh $INPUT'tides12/highmass2_0.0012.bin' $OUTPUT'tides12/highmass2_0.0012'$smooth'/' $INPUT'tides12/0.000delta.bin'
sh run_norsd_1.sh $INPUT'tides13/highmass2_0.0012.bin' $OUTPUT'tides13/highmass2_0.0012'$smooth'/' $INPUT'tides13/0.000delta.bin'
sh run_norsd_1.sh $INPUT'tides14/highmass2_0.0012.bin' $OUTPUT'tides14/highmass2_0.0012'$smooth'/' $INPUT'tides14/0.000delta.bin'
sh run_norsd_1.sh $INPUT'tides15/highmass2_0.0012.bin' $OUTPUT'tides15/highmass2_0.0012'$smooth'/' $INPUT'tides15/0.000delta.bin'

python  get_bias_wiener.py $OUTPUT'tides10/highmass2_0.0012'$smooth'/' $OUTPUT'tides11/highmass2_0.0012'$smooth'/' $OUTPUT'tides12/highmass2_0.0012'$smooth'/' $OUTPUT'tides13/highmass2_0.0012'$smooth'/' $OUTPUT'tides14/highmass2_0.0012'$smooth'/' $OUTPUT'tides15/highmass2_0.0012'$smooth'/' 

sh run_norsd_2.sh $INPUT'tides10/highmass2_0.0012.bin' $OUTPUT'tides10/highmass2_0.0012'$smooth'/' $INPUT'tides10/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides11/highmass2_0.0012.bin' $OUTPUT'tides11/highmass2_0.0012'$smooth'/' $INPUT'tides11/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides12/highmass2_0.0012.bin' $OUTPUT'tides12/highmass2_0.0012'$smooth'/' $INPUT'tides12/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides13/highmass2_0.0012.bin' $OUTPUT'tides13/highmass2_0.0012'$smooth'/' $INPUT'tides13/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides14/highmass2_0.0012.bin' $OUTPUT'tides14/highmass2_0.0012'$smooth'/' $INPUT'tides14/0.000delta.bin'
sh run_norsd_2.sh $INPUT'tides15/highmass2_0.0012.bin' $OUTPUT'tides15/highmass2_0.0012'$smooth'/' $INPUT'tides15/0.000delta.bin'

#================================================================================
