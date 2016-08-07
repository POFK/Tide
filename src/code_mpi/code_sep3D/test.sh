#!/bin/bash
#sh Torun_one.sh
mpirun -hostfile node_hostfile python sep_get_bin1d.py 10 /project/mtx/output/tides10/test2_wiener_mode/haloS1.00_Wiener.hdf5 /project/mtx/output/tides10/test2_wiener_mode/Wiener.txt
#python sep_get_bin1d.py 10 /project/mtx/output/tides10/test/haloS1.25_Wiener.hdf5 /project/mtx/output/tides10/test/Wiener.txt
cat /project/mtx/output/tides10/test2_wiener_mode/Wiener.txt
 
