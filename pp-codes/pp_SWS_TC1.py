import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

scheme='SE' # 'SE' or 'SV'
file_1='data/'+scheme+'/2D/TC1_standing_wave/energy.txt'
file_2='data/'+scheme+'/2D/TC1_standing_wave_dt2/energy.txt'

save_path='data/TC1_'+scheme+'.png'

Lx = 2.0*np.pi
res_x=0.05
Nx = round(Lx/res_x) 
dx = Lx/Nx 

Aa = 0.01
Bb = 0.01
m1 = 2
k1 = 2*np.pi*m1/Lx
g  = 9.81
kH0 = np.arccosh(0.5*g)
H0 = kH0/k1
w = math.sqrt(2*k1*np.sinh(kH0))
Tw = 2*np.pi/w

t1   =np.loadtxt(file_1, usecols=0)
en1  =np.loadtxt(file_1, usecols=1)
h1   =np.loadtxt(file_1, usecols=2)
phis1=np.loadtxt(file_1, usecols=3)
phib1=np.loadtxt(file_1, usecols=4)

t2   =np.loadtxt(file_2, usecols=0)
en2  =np.loadtxt(file_2, usecols=1)
h2   =np.loadtxt(file_2, usecols=2)
phis2=np.loadtxt(file_2, usecols=3)
phib2=np.loadtxt(file_2, usecols=4)

en01=[]
for i in range(len(en1)):
	en01.append(en1[i]-en1[0])

en02=[]
for j in range(len(en2)):
	en02.append(en2[j]-en2[0])
en02=np.array(en02) #double all the elements in an array by using *


he = H0 + np.cos(k1*0) * (Aa*np.cos(w*t1) + Bb*np.sin(w*t1))
phise = np.cos(k1*0) * 2 * np.cosh(k1*H0) * (-Aa*np.sin(w*t1) + Bb*np.cos(w*t1))/w
phibe = np.cos(k1*0) * 2 * (-Aa*np.sin(w*t1) + Bb*np.cos(w*t1))/w  

title_size=16

plt.figure(num=1, figsize=(7,9),constrained_layout=True)
ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)

ax1.set_xlabel('Time [s]',fontsize=12)
ax1.set_ylabel('E(t) [J]',fontsize=12)
ax1.plot(t1,en01,'b-',label='$E(\Delta t)$')
ax1.plot(t2,en02,'c-',label='$E(\Delta t/2)$')
if scheme=='SE':
	ax1.set_title('Energy variations (symplectic-Euler scheme)', fontsize=title_size)
	ax1.plot(t2,2*en02,'r--',label='$2E(\Delta t/2)$')
else:
	ax1.set_title('Energy variations (Störmer-Verlet scheme)', fontsize=title_size)
	ax1.plot(t2,4*en02,'r--',label='$4E(\Delta t/2)$')
ax1.legend(loc='upper right')
ax1.set_xticks(np.arange(0, 3*Tw+0.01, Tw))
ax1.set_xticklabels(['0', r'$T_p$', r'2$T_p$', r'3$T_p$'])
ax1.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
ax1.grid()

ax2.set_title('$h(x=0,t)$', fontsize=title_size)
ax2.set_xlabel('Time [s]',fontsize=12)
ax2.set_ylabel('h [m]',fontsize=12)
ax2.plot(t1,he,'b-',label='"Exact Linear"')
ax2.plot(t1,h1,'r--',label='Numerical')
#ax2.plot(t2,h2,'g-.',label='Numerical(dt/2)')
ax2.legend(loc='upper right')
ax2.set_xticks(np.arange(0, 3*Tw+0.01, Tw))
ax2.set_xticklabels(['0', r'$T_p$', r'2$T_p$', r'3$T_p$'])
ax2.grid()

ax3.set_title('$\phi(x=0,z,t)$', fontsize=title_size)
ax3.set_ylabel('$\phi$',fontsize=12)
ax3.set_xlabel('Time [s]',fontsize=12)
ax3.plot(t1,phise,'b-',label='"Exact linear", $z=H_0$')
ax3.plot(t1,phis1,'r--',label='Numerical, $z=H_0$')
ax3.plot(t1,phibe,'g-',label='"Exact linear", $z=0$')
ax3.plot(t1,phib1,'y--',label='Numerical, $z=0$')
ax3.legend(loc='upper left')
ax3.set_xticks(np.arange(0, 3*Tw+0.01, Tw))
ax3.set_xticklabels(['0', r'$T_p$', r'2$T_p$', r'3$T_p$'])
ax3.grid()

plt.show()
#plt.savefig(save_path,dpi=300)