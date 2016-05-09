#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
def init_plotting():
    plt.rcParams['figure.figsize'] = (8, 6)
    plt.rcParams['font.size'] = 12
#   plt.rcParams['font.family'] = 'Times New Roman'
#   plt.rcParams['font.family'] = 'sans-serif'
#   plt.rcParams['font.family'] = 'fantasy'
    plt.rcParams['axes.labelsize'] = plt.rcParams['font.size']
    plt.rcParams['axes.titlesize'] = 1.5*plt.rcParams['font.size']
    plt.rcParams['legend.fontsize'] = plt.rcParams['font.size']
    plt.rcParams['xtick.labelsize'] = plt.rcParams['font.size']
    plt.rcParams['ytick.labelsize'] = plt.rcParams['font.size']
#   plt.rcParams['savefig.dpi'] = 2*plt.rcParams['savefig.dpi']
    plt.rcParams['savefig.dpi'] = 600
#   plt.rcParams['xtick.major.size'] = 3
#   plt.rcParams['xtick.minor.size'] = 3
#   plt.rcParams['xtick.major.width'] = 1
#   plt.rcParams['xtick.minor.width'] = 1
#   plt.rcParams['ytick.major.size'] = 3
#   plt.rcParams['ytick.minor.size'] = 3
#   plt.rcParams['ytick.major.width'] = 1
#   plt.rcParams['ytick.minor.width'] = 1
    plt.rcParams['legend.frameon'] = False
#    plt.rcParams['legend.loc'] = 'center left'
    plt.rcParams['axes.linewidth'] = 1
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['top'].set_color('none')
    plt.gca().xaxis.set_ticks_position('bottom')
    plt.gca().yaxis.set_ticks_position('left')

print 'plt.legend(bbox_to_anchor = (0.0, 0.1))'
init_plotting()
plt.close('all')
