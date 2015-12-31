#!/bin/bash
echo '################################################################################'
echo '\n'
sh run.sh tides00
#sh run.sh tides01
#echo 'tides01 step1 ok'
#sh run.sh tides02
#echo 'tides02 step1 ok'
#sh run.sh tides03
#echo 'tides03 step1 ok'
#sh run.sh tides04
#echo 'tides04 step1 ok'
#sh run.sh tides05
#echo 'tides05 step1 ok'
#################################################################################
#python cal_bw.py tides00 smooth2.5 # calculation b w 
cp ~/data/tide/outdata/tides00/halo/bias_smooth3.00/result_b ./
cp ~/data/tide/outdata/tides00/halo/bias_smooth3.00/result_W ./
#################################################################################
sh run2.sh tides00
#sh run2.sh tides01
#echo 'tides01 step2 ok'
#sh run2.sh tides02
#echo 'tides02 step2 ok'
#sh run2.sh tides03
#echo 'tides03 step2 ok'
#sh run2.sh tides04
#echo 'tides04 step2 ok'
#sh run2.sh tides05
#echo 'tides05 step2 ok'
echo '\n'
echo '################################################################################'
