#!/usr/bin/env python
# coding=utf-8
from TIDES import *
from mpi4py import MPI
import os
import sys

comm=MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()
#===================   INIT  ====================================================
DirNum=sys.argv[1]
DIRNAME=sys.argv[2]
FILEINPUT=sys.argv[3]
#Sigma=np.float(sys.argv[4])
Input='/project/mtx/data/tides'+DirNum+'/'+FILEINPUT   #0.000halo_0.0048.hdf5'
InputDelta='/project/mtx/data/tides'+DirNum+'/0.000delta.hdf5'
dir='/project/mtx/output/tides'+DirNum+'/'+DIRNAME+'/'
ResultDir='./result/'+dir[20:]
NAME='halo'
#Shotnoise=208.172029124
#Shotnoise=415.314231603
#bias=0.965146
Shotnoise=None
#CutOff=0.8
CutOff=None
Gaussian=0
SmoothWienerOfShotnoise=True
############################
N=1024
L=1.2*10**3
H=L/N
Sigma=1.0
nthreads=16 #fftw threads number
bins=10
WienerMode=2  # mode1: Ph, mode2: Pd, k-independent bias, mode3: pd, k-dependent bias
#================
Kf=2*np.pi/L
fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
fnc=np.arange(N/2+1)
mpi_fn=np.array_split(fn,size)
mpi_index=np.array_split(np.arange(N),size)
#======================== cut-off par ===========================================
if CutOff!=None:
    PathCutoff=Input
    PathCutoffOut=dir+NAME+'_cut_K%f.hdf5'%CutOff
#======================== smooth par ============================================
if CutOff!=None:
    PathSinput=PathCutoffOut
else:
    PathSinput=Input
PathOfINF=dir+'data.inf'
PathSoutput=dir+NAME+'S%.2f'%Sigma
SmoothHaloNbar=True      # if halo data, set True

SmoothWindowOfTophat=True
SmoothSaveWienerHalo=False
SmoothSaveSmoothedData=True
#======================== wdeng  par ============================================
PathGwinput=PathSoutput+'.hdf5'
if Gaussian:
    PathGwinput=dir+NAME+'Gau.hdf5'
PathGwoutput=dir+NAME+'_'
GwSaveGwData=True
#======================== gamma  par ============================================
PathGammainput=PathGwoutput
PathGammaoutput=dir+NAME+'_'
#======================== kappa  par ============================================
PathKappainput=PathGammaoutput
PathKappaoutput=dir+NAME+'_kappax_'
KappaWith3D=True
KappaWith2D=True
#======================== runPk0 par ============================================
#usage:  Path_pk1_run:  [data1 path, is data1 halo, data2 path, is data2 halo]
RunPk0Num=3      #  The Pk number to calculate 

Path_Pk0_Input=np.array([
    [InputDelta,0,InputDelta,0,'cic','cic'],                        # Pk_dd
    [InputDelta,0,Input,1,'cic','cic'],                              # Pk_dh 
#   [InputDelta,0,PathKappaoutput+'3D.hdf5',0,'cic',0],         # Pk_dk 
    [Input,1,Input,1,'cic','cic'],                                    # Pk_hh 
#   [Input,1,PathKappaoutput+'3D.hdf5',0,'cic',0],               # Pk_hk 
#   [PathKappaoutput+'3D.hdf5',0,PathKappaoutput+'3D.hdf5',0,0,0]# Pk_kk 
    ])

#Path_Pk0_Input=np.array([    # for calculating combined density fields' Power spectra
#    [InputDelta,0,InputDelta,0,'cic','cic'],                        # Pk_dd
#    [InputDelta,0,Input,0,'cic','0'],                              # Pk_dh 
##   [InputDelta,0,PathKappaoutput+'3D.hdf5',0,'cic',0],         # Pk_dk 
#    [Input,0,Input,0,'0','0'],                                    # Pk_hh 
##   [Input,1,PathKappaoutput+'3D.hdf5',0,'cic',0],               # Pk_hk 
##   [PathKappaoutput+'3D.hdf5',0,PathKappaoutput+'3D.hdf5',0,0,0]# Pk_kk 
#    ])

Path_Pk0_Output=np.array([
    dir+'Pk'+'_DD.hdf5',
    dir+'Pk'+'_DH.hdf5', 
#   dir+'Pk'+'_DK.hdf5', 
    dir+'Pk'+'_HH.hdf5', 
#   dir+'Pk'+'_HK.hdf5', 
#   dir+'Pk'+'_KK.hdf5'
    ])
#======================== runPk1 par ============================================
#usage:  Path_pk1_run:  [data1 path, is data1 halo, data2 path, is data2 halo]
RunPk1Num=2      #  The Pk number to calculate 
Path_Pk1_Input=np.array([
#   [InputDelta,0,InputDelta,0,'cic','cic'],                        # Pk_dd
#   [InputDelta,0,Input,1,'cic','cic'],                              # Pk_dh 
    [InputDelta,0,PathKappaoutput+'3D.hdf5',0,'cic',0],         # Pk_dk 
#   [Input,1,Input,1,'cic','cic'],                                    # Pk_hh 
#   [Input,1,PathKappaoutput+'3D.hdf5',0,'cic',0],               # Pk_hk 
    [PathKappaoutput+'3D.hdf5',0,PathKappaoutput+'3D.hdf5',0,0,0]# Pk_kk 
    ])
Path_Pk1_Output=np.array([
#   dir+'Pk'+'_DD.hdf5',
#   dir+'Pk'+'_DH.hdf5', 
    dir+'Pk'+'_DK.hdf5', 
#   dir+'Pk'+'_HH.hdf5', 
#   dir+'Pk'+'_HK.hdf5', 
    dir+'Pk'+'_KK.hdf5'
    ])

#======================== get2d_bin par==========================================
PathBin2dInput1=dir+'Pk'+'_DD.hdf5'
PathBin2dInput2=dir+'Pk'+'_DK.hdf5'
PathBin2dInput3=dir+'Pk'+'_KK.hdf5'
PathBin2dOutput=dir
#======================== wkkappa   par==========================================
#PathWkkappaInput1=PathKappaoutput+'2D.hdf5'
PathWkkappaInput1=PathKappaoutput+'3D.hdf5'
PathWkkappaBias=ResultDir+'result_b'       #load bias
PathWkkappaWiener=ResultDir+'result_W'     #load wiener filter
#PathWkkappaOutput=dir+NAME+'_wfkappa_2d.hdf5'
PathWkkappaOutput=dir+NAME+'_wfkappa_3d.hdf5'
#======================== get1d_bin par==========================================
PathBin1dInput1=dir+'Pk'+'_DD.hdf5'
PathBin1dOutput1=dir+'Pk'+'_DD'
PathBin1dInput2=dir+'Pk'+'_DK.hdf5'
PathBin1dOutput2=dir+'Pk'+'_DK'
PathBin1dInput3=dir+'Pk'+'_KK.hdf5'
PathBin1dOutput3=dir+'Pk'+'_KK'
PathBin1dInput4=dir+'Pk'+'_DH.hdf5'
PathBin1dOutput4=dir+'Pk'+'_DH'
PathBin1dInput5=dir+'Pk'+'_HK.hdf5'
PathBin1dOutput5=dir+'Pk'+'_HK'
PathBin1dInput6=dir+'Pk'+'_HH.hdf5'
PathBin1dOutput6=dir+'Pk'+'_HH'
#======================== plot result par========================================
PathPlot1=dir+'Pk_'
#======================== runPk2 par ============================================
#usage:  Path_pk1_run:  [data1 path, is data1 halo,  data2 path, is data2 halo, window]
RunPk2Num=2      #  The Pk number to calculate 
Path_Pk2_Input=np.array([
#   [InputDelta,0,InputDelta,0,'cic','cic'],                        # Pk_dd
    [InputDelta,0,PathWkkappaOutput,0,'cic',0],         # Pk_dk 
#   [Input,1,PathWkkappaOutput,0,'cic',0],               # Pk_hk 
    [PathWkkappaOutput,0,PathWkkappaOutput,0,0,0]# Pk_kk 
    ])
Path_Pk2_Output=np.array([   # pk of wkkappa and delta, halo ...
#   dir+'Pk'+'_DD.hdf5',
    dir+'Pk'+'_DK.hdf5', 
#   dir+'Pk'+'_HK.hdf5', 
    dir+'Pk'+'_KK.hdf5'
    ])
