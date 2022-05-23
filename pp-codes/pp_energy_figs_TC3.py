import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def energy_r(en_tot):
    en_r = []
    for i in range(len(en_tot)):
        en_r.append(en_tot[i]-en_tot[0])
    return en_r

MSA = False

if MSA:
    file_SE1='data_old(MSA)/SE/3D/TC3_be_pa_dt1/energy.txt' # dt=0.001s
    file_SE2='data_old(MSA)/SE/3D/TC3_be_pa_dt2/energy.txt' # dt=0.002s
    file_SV1='data_old(MSA)/SV/3D/TC3_be_pa_dt1/energy.txt'
    file_SV2='data_old(MSA)/SV/3D/TC3_be_pa_dt2/energy.txt'
    save_path_1='data/TC3_energy_1(MSA).png'
    save_path_2='data/TC3_energy_2(MSA).png'
    title =' (MSA)'
else: # full weak forms
    file_SE1='data/SE/3D/TC3_dt1_full/energy.txt' # dt=0.001s
    file_SE2='data/SE/3D/TC3_dt2_full/energy.txt' # dt=0.002s
    file_SV1='data/SV/3D/TC3_dt1_full/energy.txt'
    file_SV2='data/SV/3D/TC3_dt2_full/energy.txt'
    save_path_1='data/TC3_energy_1(FWF).png'
    save_path_2='data/TC3_energy_2(FWF).png'
    title =' (FWF)'

label1='E($\Delta t$)'
label2='E(2$\Delta t$)'

t_stop=5.670 # when the R_t=0 for the first time
ts=round(t_stop/0.002)
print(ts)

time1_SE   =np.loadtxt(file_SE1, usecols=0)
en_tot1_SE =np.loadtxt(file_SE1, usecols=1)

time2_SE   =np.loadtxt(file_SE2, usecols=0)
en_tot2_SE =np.loadtxt(file_SE2, usecols=1)

time1_SV   =np.loadtxt(file_SV1, usecols=0)
en_tot1_SV =np.loadtxt(file_SV1, usecols=1)

time2_SV   =np.loadtxt(file_SV2, usecols=0)
en_tot2_SV =np.loadtxt(file_SV2, usecols=1)

en1_SE = energy_r(en_tot1_SE)
en2_SE = energy_r(en_tot2_SE)

en1_SV = energy_r(en_tot1_SV)
en2_SV = energy_r(en_tot2_SV)

plt.figure(num=1, figsize=(9,8),constrained_layout=True)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)

ax1.set_title('(a) Energy variations with the symplectic-Euler scheme'+title, fontsize=16)
ax1.set_xlabel('Time [s]',fontsize=14)
ax1.set_ylabel('E(t) [J]',fontsize=14)
ax1.plot(time1_SE,en1_SE,'r-',label=label1)
ax1.plot(time2_SE,en2_SE,'b--',label=label2)
ax1.legend(loc='best',fontsize=14)
ax1.grid()

ax2.set_title('(b) Energy variations with the Störmer-Verlet scheme'+title, fontsize=16)
ax2.set_xlabel('Time [s]',fontsize=14)
ax2.set_ylabel('E(t) [J]',fontsize=14)
ax2.plot(time1_SV,en1_SV,'r-',label=label1)
ax2.plot(time2_SV,en2_SV,'b--',label=label2)
ax2.legend(loc='best',fontsize=14)
ax2.grid()

plt.savefig(save_path_1,dpi=300)

# in the absence of wavemaker motion

plt.figure(num=2, figsize=(9,8),constrained_layout=True)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)

ax1.set_title('(a) Energy variations with the symplectic-Euler scheme'+title, fontsize=16)
ax1.set_xlabel('Time [s]',fontsize=14)
ax1.set_ylabel('E(t)-E($t_{stop}$) [J]',fontsize=14)
ax1.plot(time1_SE[ts:],en1_SE[ts:]-en1_SE[ts],'c-',label=label1)
ax1.plot(time2_SE[ts:],en2_SE[ts:]-en2_SE[ts],'b-',label=label2)
ax1.plot(time1_SE[ts:],2*(en1_SE[ts:]-en1_SE[ts]),'r--',label='2'+label1)
ax1.set_xlim(time1_SE[ts],time1_SE[-1])
ax1.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
ax1.legend(loc='upper right',fontsize=14,framealpha=0.9)
ax1.grid()

ax2.set_title('(b) Energy variations with the Störmer-Verlet scheme'+title, fontsize=16)
ax2.set_xlabel('Time [s]',fontsize=14)
ax2.set_ylabel('E(t)-E($t_{stop}$) [J]',fontsize=14)
ax2.plot(time1_SV[ts:],en1_SV[ts:]-en1_SV[ts],'c-',label=label1)
ax2.plot(time2_SV[ts:],en2_SV[ts:]-en2_SV[ts],'b-',label=label2)
ax2.plot(time1_SV[ts:],4*(en1_SV[ts:]-en1_SV[ts]),'r--',label='4'+label1)
ax2.set_xlim(time1_SV[ts],time1_SV[-1])
ax2.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
ax2.legend(loc='upper right',fontsize=14,framealpha=0.9)
ax2.grid()

plt.savefig(save_path_2,dpi=300)