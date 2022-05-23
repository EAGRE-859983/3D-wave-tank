import os.path
import numpy as np
import math
import matplotlib.pyplot as plt

def get_h(file_name,file_path):
	file = os.path.join(file_path, file_name)
	h_Lx_0 = np.loadtxt(file, usecols=2)[-9]
	h_Lx_Ly= np.loadtxt(file, usecols=2)[-1]
	return h_Lx_0,h_Lx_Ly

dx     = 'h0025'
scheme = 'SV'
t_end  = 7.0
dt_save= 0.002
save_path='data/'+dx+'_end_TC2vsTC2b.png'

# MSA vs FWF
file_path_1 ='data_old(MSA)/'+scheme+'/3D/TC2_be_pa_'+dx+'_t2/' # MSA
file_path_2 ='data/'+scheme+'/3D/TC2b_'+dx+'_t2_full/'       # FWF
energy_file_1=file_path_1+'energy.txt'
energy_file_2=file_path_2+'energy.txt'

'''# MSA using the updated code vs original results
file_path_1 ='data_TC2(MSA)/'+scheme+'/3D/TC2_be_pa_'+dx+'_t2/' 
file_path_2 ='data/'+scheme+'/3D/TC2_'+dx+'_t2_MSA/' 
energy_file_1=file_path_1+'energy.txt'
energy_file_2=file_path_2+'energy.txt'
'''


time=np.arange(0,t_end,dt_save)

time1   =np.loadtxt(energy_file_1, usecols=0)
en_tot1 =np.loadtxt(energy_file_1, usecols=1)

time2   =np.loadtxt(energy_file_2, usecols=0)
en_tot2 =np.loadtxt(energy_file_2, usecols=1)

en1 = []
for i in range(len(en_tot1)):
    en1.append(en_tot1[i]-en_tot1[0])

en2 = []
for i in range(len(en_tot2)):
    en2.append(en_tot2[i]-en_tot2[0])

h0_t_1,hLy_t_1=[],[]
h0_t_2,hLy_t_2=[],[]

for t in time:
	tt = format(t, '.3f')
	file1 = dx+'_'+tt+'.txt'
	file2 = 'h_'+tt+'.txt'
	h0_1,hLy_1 = get_h(file1, file_path_1)
	h0_2,hLy_2 = get_h(file2, file_path_2)
	#print(h0,hLy)
	h0_t_1.append(h0_1)
	hLy_t_1.append(hLy_1)
	h0_t_2.append(h0_2)
	hLy_t_2.append(hLy_2)


fig, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
fig.set_size_inches(10,9)
fig.set_tight_layout(True)

ax1.set_title('Energy variations', fontsize=20)
ax1.set_ylabel('E(t) [J]',fontsize=14)
ax1.plot(time1[:-1],en1[:-1],'b-',label='MSA')
ax1.plot(time2[:-1],en2[:-1],'r--',label='FWF')
ax1.legend(loc='best',fontsize=14)
ax1.grid()

ax2.set_title('Water depth at the right-hand vertices', fontsize=20)
ax2.set_xlabel('Time [s]',fontsize=14)
ax2.set_ylabel('$h_{ex}(x,y,t)$ [m]',fontsize=14)
ax2.plot(time,h0_t_1, 'b-', label='MSA, $h_{ex}(L_x,0,t)$')
ax2.plot(time,hLy_t_1,'b-.',label='MSA, $h_{ex}(L_x,L_y,t)$')
ax2.plot(time,h0_t_2, 'r--',label='FWF, $h_{ex}(L_x,0,t)$')
ax2.plot(time,hLy_t_2,'r:', label='FWF, $h_{ex}(L_x,L_y,t)$')
ax2.legend(loc='best',fontsize=14)
ax2.grid()

plt.show()
#plt.savefig(save_path,dpi=300)
