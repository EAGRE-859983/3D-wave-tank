import os.path
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from statistics import mean

def get_h(file_name,file_path):
	file = os.path.join(file_path, file_name)
	h = np.loadtxt(file, usecols=2)
	return h

def L2norm(h,h_ex):
	summ=0
	for i in range(len(h)):
		summ=(h[i]-h_ex[i])**2+summ
	L2=math.sqrt(summ)
	return L2

def Lifnorm(h,h_ex):
	Lif=np.amax(abs(h-h_ex))
	return Lif

def average(n0,n1,listname):
	ave_list=listname[n0:n1+1:1]
	return mean(ave_list)

dx_ex='h0025'
scheme='SE'
file_path_ex ='data/'+scheme+'/3D/TC2b_'+dx_ex+'_t2_full/' #1
file_path_005='data/'+scheme+'/3D/TC2b_h005_t2_full/'      #2
file_path_01 ='data/'+scheme+'/3D/TC2b_h01_t2_full/'       #3
save_path='data/TC2b_norms_'+scheme+'('+dx_ex+').png'

t_end  = 7.0
dt_save= 0.002
time=np.arange(0,t_end,dt_save)

#average value
ave0 = 4.0
ave1 = t_end
n0 = round(ave0/dt_save)
n1 = round(ave1/dt_save)

L2_005,L2_01,Li_005,Li_01=[],[],[],[]

for t in time:
	tt = format(t, '.3f')
	file_1 = 'h_'+tt+'.txt'
	file_2 = 'h_'+tt+'.txt'
	file_3 = 'h_'+tt+'.txt'
	h_1 = get_h(file_1, file_path_ex)
	h_2 = get_h(file_2, file_path_005)
	h_3 = get_h(file_3, file_path_01)

	eL2_005 = L2norm(h_2,h_1)
	eL2_01 = L2norm(h_3,h_1)
	eLi_005 = Lifnorm(h_2,h_1)
	eLi_01 = Lifnorm(h_3,h_1)

	L2_005.append(eL2_005)
	L2_01.append(eL2_01)
	Li_005.append(eLi_005)
	Li_01.append(eLi_01)


L2_005_ave = average(n0,n1,L2_005)
L2_01_ave = average(n0,n1,L2_01)
Li_005_ave = average(n0,n1,Li_005)
Li_01_ave = average(n0,n1,Li_01)

bL2, bLi = [],[]
for i in range(len(time)):
	bL2.append((math.log(L2_01[i])-math.log(L2_005[i]))/(math.log(2)))
	bLi.append((math.log(Li_01[i])-math.log(Li_005[i]))/(math.log(2)))

#math.log(x[, base]): with one argument, return the natural logarithm of x (to base e).

bL2_ave = average(n0,n1,bL2)
bLi_ave = average(n0,n1,bLi)

print(f'Order of convergence based on L_2 norm (averaged between {ave0}s and {ave1}s): {bL2_ave}')
print(f'Order of convergence based on L_infinity norm (averaged between {ave0}s and {ave1}s): {bLi_ave}')

diff_2 = math.log(L2_005_ave)-bL2_ave*math.log(0.05)
diff_i = math.log(Li_005_ave)-bLi_ave*math.log(0.05)

fig = plt.figure(figsize=(10,6), constrained_layout=True)
gs = fig.add_gridspec(6, 16)

ax1= fig.add_subplot(gs[0:3,0:10])
ax2= fig.add_subplot(gs[0:3,10:15])
ax3= fig.add_subplot(gs[3:6,0:10])
ax4= fig.add_subplot(gs[3:6,10:15])

ax1.set_title('Order of convergence with the $L^\infty$-norm', fontsize=14)
ax1.set_xlabel('Time[s]',fontsize=11)
ax1.set_ylabel(r'$\beta$',fontsize=11)
ax1.plot(time, bLi, color='blue',linestyle='-',label=r'$\beta$')
ax1.axhline(y=bLi_ave, color='red',label='Average of the last 3s')
ax1.legend(loc='lower right',fontsize=11)

ax2.set_title('$\Vert h-h_{ex}\Vert_\infty$: Convergence of order '+format(bLi_ave,'.2f'), fontsize=14)
ax2.set_xlabel(r'ln($\Delta x$)',fontsize=11)
ax2.set_ylabel(r'ln($\mathcal{E}$)',fontsize=11)
ax2.plot([math.log(0.05),math.log(0.1)],[bLi_ave*math.log(0.05)+diff_i,bLi_ave*math.log(0.1)+diff_i],'-',label=format(bLi_ave,'.2f')+r'ln($\Delta x$)'+f'{diff_i:+.2f}')
ax2.plot([math.log(0.05),math.log(0.1)],[math.log(Li_005_ave),math.log(Li_01_ave)],'r*', markersize=10,label=r'ln($\mathcal{E}$)')
ax2.legend(loc='lower right',fontsize=11)

ax3.set_title('Order of convergence with the $L^2$-norm', fontsize=14)
ax3.set_xlabel('Time[s]',fontsize=11)
ax3.set_ylabel(r'$\beta$',fontsize=11)
ax3.plot(time,bL2,color='blue',linestyle='-',label=r'$\beta$')
ax3.axhline(y=bL2_ave, color='red',label='Average of the last 3s')
ax3.legend(loc='lower right',fontsize=11)

ax4.set_title('$\Vert h-h_{ex}\Vert_2$: Convergence of order '+format(bL2_ave,'.2f'), fontsize=14)
ax4.set_xlabel(r'ln($\Delta x$)',fontsize=11)
ax4.set_ylabel(r'ln($\mathcal{E}$)',fontsize=11)
ax4.plot([math.log(0.05),math.log(0.1)],[bL2_ave*math.log(0.05)+diff_2,bL2_ave*math.log(0.1)+diff_2],'-',label=format(bL2_ave,'.2f')+r'ln($\Delta x$)'+f'{diff_2:+.2f}')
ax4.plot([math.log(0.05),math.log(0.1)],[math.log(L2_005_ave),math.log(L2_01_ave)],'r*', markersize=10,label=r'ln($\mathcal{E}$)')
ax4.legend(loc='lower right',fontsize=11)

plt.show()
#plt.savefig(save_path,dpi=300)