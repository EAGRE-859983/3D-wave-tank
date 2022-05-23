import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

file_exp1='202002/PistonMotion.dat'
file_exp2='202002/PistonVelocity.dat'

file_num1='data/SV/2D/TC4_test_22Mar/energy.txt'

label1='Measurements'
label2='Interpolations(SV)'

save_path='data/Wavemaker_SE.png'

t_exp  = np.loadtxt(file_exp1, usecols=0)
R_exp  = np.loadtxt(file_exp1, usecols=1)
Rt_exp = np.loadtxt(file_exp2, usecols=1)

t_num  = np.loadtxt(file_num1, usecols=0)
R_num  = np.loadtxt(file_num1, usecols=8)
Rt_num = np.loadtxt(file_num1, usecols=9)

plt.figure(num=1, figsize=(12,8),constrained_layout=True)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)

ax1.set_title('Wavemaker motion', fontsize=20)
ax1.set_xlabel('Time [s]',fontsize=14)
ax1.set_ylabel('R(t) [m]',fontsize=14)
ax1.plot(t_exp,R_exp,'b-', label=label1)
ax1.plot(t_num,R_num,'r--', label=label2)
ax1.legend(loc='best',fontsize=14)
ax1.grid()

ax2.set_title('Wavemaker Velocity', fontsize=20)
ax2.set_xlabel('Time [s]',fontsize=14)
ax2.set_ylabel('dR(t)/dt [m/s]',fontsize=14)
ax2.plot(t_exp,Rt_exp,'b-',label=label1)
ax2.plot(t_num,Rt_num,'r--',label=label2)
ax2.legend(loc='best',fontsize=14)
ax2.grid()

plt.show()
#plt.savefig(save_path,dpi=300)