import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

def energy_r(en_tot):
    en_r = []
    for i in range(len(en_tot)):
        en_r.append(en_tot[i]-en_tot[0])
    return en_r

scheme='SE'

# MSA vs FWF
file_1='data_old(MSA)/'+scheme+'/3D/TC3_be_pa_dt2/energy.txt'
file_2='data/'+scheme+'/3D/TC3_dt2_full/energy.txt' 
label1='MSA('+scheme+')'
label2='FWF('+scheme+')'

'''# MSA using the updated code vs original results
file_1='data/'+scheme+'/3D/TC3_dt2_MSA/energy.txt'
file_2='data_old(MSA)/'+scheme+'/3D/TC3_be_pa_dt2/energy.txt'
label1='new MSA('+scheme+')'
label2='original('+scheme+')'
'''
save_path_1='data/TC3_vs_3b('+scheme+').png'

time_1   =np.loadtxt(file_1, usecols=0)
en_tot_1 =np.loadtxt(file_1, usecols=1)
h0_1      =np.loadtxt(file_1, usecols=3)
hLy_1     =np.loadtxt(file_1, usecols=4)

time_2   =np.loadtxt(file_2, usecols=0)
en_tot_2 =np.loadtxt(file_2, usecols=1)
h0_2      =np.loadtxt(file_2, usecols=3)
hLy_2     =np.loadtxt(file_2, usecols=4)

en_1 = energy_r(en_tot_1)
en_2 = energy_r(en_tot_2)

plt.figure(num=1, figsize=(10,8),constrained_layout=True)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)

ax1.set_title('Energy variations ($\Delta t=0.002$s)', fontsize=20)
ax1.set_xlabel('Time [s]',fontsize=14)
ax1.set_ylabel('E(t) [J]',fontsize=14)
ax1.plot(time_1,en_1,'b-',label=label1)
ax1.plot(time_2,en_2,'r--',label=label2)
ax1.legend(loc='best',fontsize=14)
#ax1.grid()
axins1 = ax1.inset_axes((0.43, 0.15, 0.5, 0.6))
axins1.plot(time_1,en_1,'b-',label=label1)
axins1.plot(time_2,en_2,'r--',label=label2)
axins1.set_xlim((13-0.5), (13+0.5))
mark_inset(ax1, axins1, loc1=2, loc2=1, fc='none', ec='black', lw=0.5)
if scheme=='SE':
    axins1.set_ylim(0.038, 0.0395)
else:
    axins1.set_ylim(0.03875, 0.03876)

ax2.set_title('Water depth at the right-hand vertices', fontsize=20)
ax2.set_xlabel('Time [s]',fontsize=14)
ax2.set_ylabel('$h(x,y,t)$ [m]',fontsize=14)
ax2.plot(time_1,h0_1, 'b-', label=label1+', $h(L_x,0,t)$')
ax2.plot(time_1,hLy_1,'b-.',label=label1+', $h(L_x,L_y,t)$')
ax2.plot(time_2,h0_2, 'r--',label=label2+', $h(L_x,0,t)$')
ax2.plot(time_2,hLy_2,'r:', label=label2+', $h(L_x,L_y,t)$')
ax2.legend(loc='best',fontsize=14)
ax2.grid()

plt.show()
#plt.savefig(save_path_1,dpi=300)