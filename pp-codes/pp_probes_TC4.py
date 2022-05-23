import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

file_exp1='202002/WAVE_1.dat'
file_exp2='202002/WAVE_2.dat'
file_exp3='202002/WAVE_3.dat'
file_exp4='202002/WAVE_4.dat'
file_exp5='202002/WAVE_5.dat'
file_exp6='202002/WAVE_6.dat'

H0=1
label0='Exprimental data'

# SE and SV
file_num1='data/SE/2D/TC4_test/energy.txt'
file_num2='data/SV/2D/TC4_test/energy.txt'
label1='SE'
label2='SV'

'''# Compare the new version with the old version 
scheme='SV'
file_num1='data_old(MSA)/'+scheme+'/2D/TC4_Mar/energy.txt'
file_num2='data/'+scheme+'/2D/TC4_test/energy.txt'
label1= scheme+'(old)'
label2= scheme
'''
save_path_1='data/Probes_123.png'
save_path_2='data/Probes_456.png'

def probe_num(p_num_h,H0):
	p_num=[]
	for i in range(len(p_num_h)):
		p_num.append(p_num_h[i]-H0)
	return p_num

t_exp  = np.loadtxt(file_exp1, usecols=0)
p1_exp = np.loadtxt(file_exp1, usecols=1)
p2_exp = np.loadtxt(file_exp2, usecols=1)
p3_exp = np.loadtxt(file_exp3, usecols=1)
p4_exp = np.loadtxt(file_exp4, usecols=1)
p5_exp = np.loadtxt(file_exp5, usecols=1)
p6_exp = np.loadtxt(file_exp6, usecols=1)

t_num1  = np.loadtxt(file_num1, usecols=0)
p1_num_h1 = np.loadtxt(file_num1, usecols=2)
p2_num_h1 = np.loadtxt(file_num1, usecols=3)
p3_num_h1 = np.loadtxt(file_num1, usecols=4)
p4_num_h1 = np.loadtxt(file_num1, usecols=5)
p5_num_h1 = np.loadtxt(file_num1, usecols=6)
p6_num_h1 = np.loadtxt(file_num1, usecols=7)

t_num2  = np.loadtxt(file_num2, usecols=0)
p1_num_h2 = np.loadtxt(file_num2, usecols=2)
p2_num_h2 = np.loadtxt(file_num2, usecols=3)
p3_num_h2 = np.loadtxt(file_num2, usecols=4)
p4_num_h2 = np.loadtxt(file_num2, usecols=5)
p5_num_h2 = np.loadtxt(file_num2, usecols=6)
p6_num_h2 = np.loadtxt(file_num2, usecols=7)

p1_num1=probe_num(p1_num_h1,H0)
p2_num1=probe_num(p2_num_h1,H0)
p3_num1=probe_num(p3_num_h1,H0)
p4_num1=probe_num(p4_num_h1,H0)
p5_num1=probe_num(p5_num_h1,H0)
p6_num1=probe_num(p6_num_h1,H0)

p1_num2=probe_num(p1_num_h2,H0)
p2_num2=probe_num(p2_num_h2,H0)
p3_num2=probe_num(p3_num_h2,H0)
p4_num2=probe_num(p4_num_h2,H0)
p5_num2=probe_num(p5_num_h2,H0)
p6_num2=probe_num(p6_num_h2,H0)

plt.figure(num=1, figsize=(13,9),constrained_layout=True)
ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)

ax1.set_title('Probe 1: x=10m', fontsize=20)
ax1.set_xlabel('Time [s]',fontsize=14)
ax1.set_ylabel('$\eta$ [m]',fontsize=14)
ax1.plot(t_exp,p1_exp,'r-', label=label0)
ax1.plot(t_num1,p1_num1,'b-', label=label1)
ax1.plot(t_num2,p1_num2,'c--', label=label2)
ax1.set_xlim([0,120])
ax1.legend(loc='upper left',fontsize=13)
ax1.grid()

ax2.set_title('Probe 2: x=20m', fontsize=20)
ax2.set_xlabel('Time [s]',fontsize=14)
ax2.set_ylabel('$\eta$ [m]',fontsize=14)
ax2.plot(t_exp,p2_exp,'r-',label=label0)
ax2.plot(t_num1,p2_num1,'b-',label=label1)
ax2.plot(t_num2,p2_num2,'c--',label=label2)
ax2.set_xlim([0,120])
ax2.legend(loc='upper left',fontsize=13)
ax2.grid()

ax3.set_title('Probe 3: x=40m', fontsize=20)
ax3.set_xlabel('Time [s]',fontsize=14)
ax3.set_ylabel('$\eta$ [m]',fontsize=14)
ax3.plot(t_exp,p3_exp,'r-',label=label0)
ax3.plot(t_num1,p3_num1,'b-',label=label1)
ax3.plot(t_num2,p3_num2,'c--',label=label2)
ax3.set_xlim([0,120])
ax3.legend(loc='upper left',fontsize=13)
ax3.grid()

plt.show()
#plt.savefig(save_path_1,dpi=300)

plt.figure(num=2, figsize=(13,9),constrained_layout=True)
ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)

ax1.set_title('Probe 4: x=49.5m', fontsize=20)
ax1.set_xlabel('Time [s]',fontsize=14)
ax1.set_ylabel('$\eta$ [m]',fontsize=14)
ax1.plot(t_exp,p4_exp,'r-', label=label0)
ax1.plot(t_num1,p4_num1,'b-', label=label1)
ax1.plot(t_num2,p4_num2,'c--', label=label2)
ax1.set_xlim([0,120])
ax1.legend(loc='upper left',fontsize=13)
ax1.grid()

ax2.set_title('Probe 5: x=50m', fontsize=20)
ax2.set_xlabel('Time [s]',fontsize=14)
ax2.set_ylabel('$\eta$ [m]',fontsize=14)
ax2.plot(t_exp,p5_exp,'r-',label=label0)
ax2.plot(t_num1,p5_num1,'b-',label=label1)
ax2.plot(t_num2,p5_num2,'c--',label=label2)
ax2.set_xlim([0,120])
ax2.legend(loc='upper left',fontsize=13)
ax2.grid()

ax3.set_title('Probe 6: x=54m', fontsize=20)
ax3.set_xlabel('Time [s]',fontsize=14)
ax3.set_ylabel('$\eta$ [m]',fontsize=14)
ax3.plot(t_exp,p6_exp,'r-',label=label0)
ax3.plot(t_num1,p6_num1,'b-',label=label1)
ax3.plot(t_num2,p6_num2,'c--',label=label2)
ax3.set_xlim([0,120])
ax3.legend(loc='upper left',fontsize=13)
ax3.grid()

plt.show()
#plt.savefig(save_path_2,dpi=300)