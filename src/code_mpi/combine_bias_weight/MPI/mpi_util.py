#!/usr/bin/env python
# coding=utf-8
from mpi4py import MPI

comm=MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()
