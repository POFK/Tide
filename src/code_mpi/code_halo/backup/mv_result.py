#!/usr/bin/env python
# coding=utf-8
from parameter import *
from subprocess import call
call('cp %sresult_b ./'%Outfile,shell=True)
call('cp %sresult_W ./'%Outfile,shell=True)
