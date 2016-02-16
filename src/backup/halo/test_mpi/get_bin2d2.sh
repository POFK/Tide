#!/bin/bash
name=$@
mpirun -hostfile node_hostfile python get_bin2d2_1.py $name
python get_bin2d2_2.py $name

