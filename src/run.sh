#!/bin/bash
sleep 40m
nohup python cal_gamma.py &
sleep 80m
nohup python cal_cappa.py &
