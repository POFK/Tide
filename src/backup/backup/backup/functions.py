"""
    Public Function are defined here


"""
# public module
import numpy as np
import scipy as sp
import os
import gc
import string
from scipy import integrate
from math import *
from map import physical_gridding as gridding
import copy
#import fftw3 as FFTW
#import pyfftw.FFTW as FFTW

# kiyo module
from core import algebra
from utils import distance
from utils import fftutil

# li module
#import MakePower

class BOX(object):
    def __init__(self, imap1, imap2, weight1, weight2):
        self.imap1 = imap1
        self.imap2 = imap2
        self.weight1 = weight1
        self.weight2 = weight2

    def mapping_to_xyz(self):
        #self.box_bin, self.boxunit = get_box_xyz(self.imap1, self.boxshape)

        #self.ibox1, self.nbox1 = get_box(self.box_bin, self.imap1, self.weight1)
        #self.ibox2, self.nbox2 = get_box(self.box_bin, self.imap2, self.weight2)

        self.flag_nan(target="map")
        gridding_method = gridding.physical_grid_largeangle
        #gridding_method = gridding.physical_grid

        ## shift test 
        #print "Shift 2 pixels for testing "
        #self.imap2[:, 2:, :] = self.imap2[:, :-2, :]
        #self.imap2[:, :2, :] = 0.
        #self.weight2[:, 2:, :] = self.weight2[:, :-2, :]
        #self.weight2[:, :2, :] = 0.

        self.ibox1, ibox1_info = gridding_method(self.imap1, refinement=1, order=1)
        self.ibox2, ibox2_info = gridding_method(self.imap2, refinement=1, order=1)
        self.nbox1, nbox1_info = gridding_method(self.weight1, refinement=1, order=1)
        self.nbox2, nbox2_info = gridding_method(self.weight2, refinement=1, order=1)

        self.ibox1 = algebra.make_vect(self.ibox1, ibox1_info['axes'])
        self.ibox2 = algebra.make_vect(self.ibox2, ibox2_info['axes'])
        self.nbox1 = algebra.make_vect(self.nbox1, nbox1_info['axes'])
        self.nbox2 = algebra.make_vect(self.nbox2, nbox2_info['axes'])

        self.ibox1.info = ibox1_info
        self.ibox2.info = ibox2_info
        self.nbox1.info = nbox1_info
        self.nbox2.info = nbox2_info

        self.boxshape = []
        self.boxunit = []
        for i in range(self.ibox1.ndim):
            self.boxshape.append(self.ibox1.shape[i])
            axis_name = self.ibox1.axes[i]
            axis = self.ibox1.get_axis(axis_name)
            delta_axis = np.fabs(axis[1] - axis[0])
            self.boxunit.append(delta_axis)
        #axis = self.ibox1.get_axis()
        #self.boxunit = [self.ibox1.info['freq_delta'],
        #                self.ibox1.info['ra_delta'], 
        #                self.ibox1.info['dec_delta']]

    def flag_nan(self, target="box"):
        if target == "box":
            self.ibox1[np.isnan(self.ibox1)] = 0.
            self.ibox2[np.isnan(self.ibox2)] = 0.
            self.nbox1[np.isnan(self.ibox1)] = 0.
            self.nbox1[np.isnan(self.nbox1)] = 0.
            self.nbox2[np.isnan(self.ibox2)] = 0.
            self.nbox2[np.isnan(self.nbox2)] = 0.
            self.ibox1[np.isinf(self.ibox1)] = 0.
            self.ibox2[np.isinf(self.ibox2)] = 0.
            self.nbox1[np.isinf(self.ibox1)] = 0.
            self.nbox1[np.isinf(self.nbox1)] = 0.
            self.nbox2[np.isinf(self.ibox2)] = 0.
            self.nbox2[np.isinf(self.nbox2)] = 0.
        elif target == "map":
            self.imap1[np.isnan(self.imap1)] = 0.
            self.imap2[np.isnan(self.imap2)] = 0.
            self.weight1[np.isnan(self.imap1)] = 0.
            self.weight1[np.isnan(self.weight1)] = 0.
            self.weight2[np.isnan(self.imap2)] = 0.
            self.weight2[np.isnan(self.weight2)] = 0.
            self.imap1[np.isinf(self.imap1)] = 0.
            self.imap2[np.isinf(self.imap2)] = 0.
            self.weight1[np.isinf(self.imap1)] = 0.
            self.weight1[np.isinf(self.weight1)] = 0.
            self.weight2[np.isinf(self.imap2)] = 0.
            self.weight2[np.isinf(self.weight2)] = 0.

            self.weight1[self.weight1 < 1.e-20] = 0.
            self.weight2[self.weight2 < 1.e-20] = 0.

    def subtract_mean(self):
        self.ibox1 = self.ibox1 - self.ibox1.flatten().mean()
        self.ibox2 = self.ibox2 - self.ibox2.flatten().mean()

    def subtract_weighted_mean(self):
        mean1 = np.sum(np.sum(self.ibox1, -1), -1)
        mean1_weight = np.sum(np.sum(self.nbox1, -1), -1)
        mean1_weight[mean1_weight==0] = np.inf
        mean1 /= mean1_weight
        #print "Max and Min of weighted mean1 : ", mean1.max(), mean1.min()
        self.ibox1 -= mean1[:, None, None]

        mean2 = np.sum(np.sum(self.ibox2, -1), -1)
        mean2_weight = np.sum(np.sum(self.nbox2, -1), -1)
        mean2_weight[mean2_weight==0] = np.inf
        mean2 /= mean2_weight
        self.ibox2 -= mean2[:, None, None]
        #print "Max and Min of weighted mean2 : ", mean1.max(), mean2.min()

    def get_overdensity(self, map, sel):

        sel[sel==0] = np.inf
        map = map/sel - 1.
        sel[sel == np.inf] = 0.

        return map
        
    @classmethod
    def estimate_ps_3d(self, data,window="blackman"):

#        #self.flag_nan(target="box")
#
#        #window_function = fftutil.window_nd(self.nbox1.shape, name=window)
#        #window_function = fftutil.window_nd((self.nbox1.shape[0],), name=window)
#        window_func = getattr(np, window)
#        window_function = window_func(self.nbox1.shape[0])
#        #self.nbox1 *= window_function[:, None, None]
#        #self.nbox2 *= window_function[:, None, None]
#
#        self.ibox1 *= self.nbox1
#        self.ibox2 *= self.nbox2
#
#
#        #self.subtract_mean()
#        #self.subtract_weighted_mean()
#
#        normal = np.sum(self.nbox1 * self.nbox2)
#        delta_v = np.prod(self.boxunit)
#
#        #  iput_1 = np.zeros(self.boxshape, dtype=complex)
#        #  oput_1 = np.zeros(self.boxshape, dtype=complex)
        #  iput_1.imag = 0.
        #  iput_1.real = self.ibox1
        #  #plan_1 = FFTW.Plan(iput_1, oput_1, direction='forward', flags=['measure'])
        #  #FFTW.execute(plan_1)
        #  oput_1 = np.fft.fftn(iput_1)

        #  iput_2 = np.zeros(self.boxshape, dtype=complex)
        #  oput_2 = np.zeros(self.boxshape, dtype=complex)
        #  iput_2.imag = 0.
        #  iput_2.real = self.ibox2
        #  #plan_2 = FFTW.Plan(iput_2, oput_2, direction='forward', flags=['measure'])
        #  #FFTW.execute(plan_2)
        #  oput_2 = np.fft.fftn(iput_2)

        #  oput_1 = np.fft.fftshift(oput_1)
        #  oput_2 = np.fft.fftshift(oput_2)

        oput_1 = np.fft.fftshift(np.fft.fftn(data))
#       oput_2 = np.fft.fftshift(np.fft.fftn(self.ibox2))

        self.ps_3d  = np.abs(oput_1)**2
        self.ps_3d *= (1.2*10**3/1024)**3
        self.ps_3d /= 1024.**3

        del oput_1
        gc.collect()
    @classmethod
    def get_k_bin_centre(self):
        #print self.boxunit
        k_bin_x = 2. * np.pi * np.fft.fftshift(np.fft.fftfreq(1024,
                                                              1./1024))
#       k_bin_y = 2. * np.pi * np.fft.fftshift(np.fft.fftfreq(self.boxshape[1],
#                                                             self.boxunit[1]))
#       k_bin_z = 2. * np.pi * np.fft.fftshift(np.fft.fftfreq(self.boxshape[2],
#                                                             self.boxunit[2]))
        k_bin_y=k_bin_x
        k_bin_z=k_bin_x



        return k_bin_x, k_bin_y, k_bin_z
    @classmethod
    def convert_ps_to_unitless(self):

        print "convert power to unitless", 
        k_bin_x, k_bin_y, k_bin_z = self.get_k_bin_centre()

        k_bin_r = np.sqrt( (k_bin_x**2)[:, None, None] + 
                           (k_bin_y**2)[None, :, None] + 
                           (k_bin_z**2)[None, None, :] )

        import scipy.special
        ndim = 3.
        factor = 2. * np.pi ** (ndim / 2.) / scipy.special.gamma(ndim / 2.)
        factor /= (2. * np.pi) ** ndim

        #self.ps_3d = self.ps_3d * k_bin_r**3 / 2. / np.pi**2
        self.ps_3d = self.ps_3d * k_bin_r ** ndim * factor
    @classmethod
    def convert_3dps_to_1dps(self, k_edges):

        print "convert 3d power ot 1d power",
        print self.boxshape
        k_bin_x, k_bin_y, k_bin_z = self.get_k_bin_centre()

        k_bin_r = np.sqrt( (k_bin_x**2)[:, None, None] + 
                           (k_bin_y**2)[None, :, None] + 
                           (k_bin_z**2)[None, None, :] )

        ps_3d_flatten = copy.deepcopy(self.ps_3d.flatten())
        k_bin_r = k_bin_r.flatten()[np.isfinite(ps_3d_flatten)]
        ps_3d_flatten = ps_3d_flatten[np.isfinite(ps_3d_flatten)]

        kn_1d, edges = np.histogram(k_bin_r, k_edges)
        ps_1d, edges = np.histogram(k_bin_r, k_edges, weights=ps_3d_flatten)

        kn_1d = kn_1d.astype(float)
        #kn_1d[kn_1d==0] = np.inf
        ps_1d[kn_1d != 0] /= kn_1d[kn_1d != 0] 
        ps_1d[kn_1d == 0] = 0.
        #kn_1d[kn_1d==np.inf] = 0.

        self.kn_1d = kn_1d
        self.ps_1d = ps_1d


BOX.estimate_ps_3d(data='/home/mtx/data/tide/0.000den00.bin')
