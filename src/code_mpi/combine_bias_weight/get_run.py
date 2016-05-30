#!/usr/bin/env python
# coding=utf-8
from Get_Inf.get_bias import *
plt.rcParams['legend.frameon'] = False
i=10
in_dir='/project/mtx/data/tides%s/'%str(i)
filename1='0.000delta.bin'
filename2='highmass1_0.0012.bin'
filename3='highmass2_0.0012.bin'
filename4='highmass3_0.0012.bin'
filename5='highmass4_0.0012.bin'
out_dir='/project/mtx/output/tides%s/'%str(i)

file=[filename2,filename3,filename4,filename5]
label=['$\delta_1$','$\delta_2$','$\delta_3$','$\delta_4$']
color=['r.-','b.-','g.-','m.-',]
for i in np.arange(len(file)):
    b=get_bias(dir=out_dir+file[i][:-4]+'_1.25_NoGau/',color=color[i],label=label[i],cut_off=9)
    print b
plt.figure('bias')
plt.xlabel('k')
plt.ylabel('bias')
plt.xlim([0.004,2.5])
plt.legend()
plt.show()
#plt.savefig('./png/bias.png')

