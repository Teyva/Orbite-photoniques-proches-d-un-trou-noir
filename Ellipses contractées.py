# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:19:04 2023

@author: victo
"""
import matplotlib.pyplot as plt
import numpy as np

T=np.linspace(0,2*np.pi,100)
a=1
e_e=0.5
c=3e8

def r(e):
    return (a*(1-e**2))/(1-e*np.cos(T))

def y_pos(e):
    return a*(np.sqrt(1-e**2))*np.sqrt(1-(x/a)**2)
def y_neg(e):
    return -a*(np.sqrt(1-e**2))*np.sqrt(1-(x/a)**2)

x=np.linspace(-a,a,100)

xc,yc=r(e_e)*np.cos(T),r(e_e)*np.sin(T)

plt.figure(1,figsize=(8,8))
plt.plot(x,y_pos(0),'k',label='$\epsilon$=0.0')
plt.plot(x,y_neg(0),'k',)
plt.plot(x,y_pos(e_e),'k',linestyle='--',label='$\epsilon$=0.5')
plt.plot(x,y_neg(e_e),'k',linestyle='--')
plt.plot(x,y_pos(0.8),'k',linestyle='-.',label='$\epsilon$=0.8')
plt.plot(x,y_neg(0.8),'k',linestyle='-.')
plt.plot(x,y_pos(0.9),'k',linestyle=':',label='$\epsilon$=0.9')
plt.plot(x,y_neg(0.9),'k',linestyle=':')
plt.plot(x,y_pos(1),'k',linestyle=(0, (1, 10)),label='$\epsilon$=1')
plt.plot(x,y_neg(1),'k',linestyle=(0, (1, 10)))
#plt.plot(xc-a*e_e,yc,'k')
plt.plot(0,0,'ko')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ellipses de différentes excentricités')
plt.legend()
plt.savefig('ellipses.png')



#%%

contrx0=y_pos(0)/y_pos(0)
contrx02=y_pos(0.2)/y_pos(0)
contrx03=y_pos(0.3)/y_pos(0)
contrx04=y_pos(0.4)/y_pos(0)
contrx05=y_pos(e_e)/y_pos(0)
contrx06=y_pos(0.6)/y_pos(0)
contrx07=y_pos(0.7)/y_pos(0)
contrx08=y_pos(0.8)/y_pos(0)
contrx09=y_pos(0.9)/y_pos(0)
contrx095=y_pos(0.95)/y_pos(0)
contrx099=y_pos(0.99)/y_pos(0)
contrx1=y_pos(1)/y_pos(0)

plt.figure(2)
plt.plot(x,contrx0,label='$\epsilon$=0.0')
plt.plot(x,contrx05,label='$\epsilon$=0.5')
plt.plot(x,contrx07,label='$\epsilon$=0.7')
plt.plot(x,contrx08,label='$\epsilon$=0.8')
plt.plot(x,contrx09,label='$\epsilon$=0.9')
plt.plot(x,contrx095,label='$\epsilon$=0.95')
plt.plot(x,contrx099,label='$\epsilon$=0.99')
plt.plot(x,contrx1,label='$\epsilon$=1')
plt.legend(loc='lower right')
plt.xlabel('Axe perpendiculaire à la vitesse')
plt.ylabel('Facteur de contraction de la longeur')
plt.savefig('contraction_epsilon.png')



contr0=contrx0[50]
contr02=contrx02[50]
contr03=contrx03[50]
contr04=contrx04[50]
contr05=contrx05[50]
contr06=contrx06[50]
contr07=contrx07[50]
contr08=contrx08[50]
contr09=contrx09[50]
contr095=contrx095[50]
contr099=contrx099[50]
contr1=contrx1[50]



def delta(fac):
    gam=fac**-1
    v=c*np.sqrt(1-1/(gam)**2)
    return v


v0=delta(contr0)
v02=delta(contr02)
v03=delta(contr03)
v04=delta(contr04)
v05=delta(contr05)
v06=delta(contr06)
v07=delta(contr07)
v08=delta(contr08)
v09=delta(contr09)
v095=delta(contr095)
v099=delta(contr099)
v1=delta(contr1)

contr=np.array([0,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,0.99,1])
v=np.array([v0,v02,v03,v04,v05,v06,v07,v08,v09,v095,v099,v1])/3e8

plt.figure(3)
plt.plot(contr,v,'ko',markersize=5)
#plt.plot([0,1],[0.2,0.2],'k',linestyle='--')
#plt.plot([0.2,0.2],[0,1],'k',linestyle='--')

plt.xlabel('excentricité $\epsilon$')
plt.ylabel(r'Facteur $\beta$ ')
plt.title(r'Facteur $\beta$ pour changer un cercle en ellipse')
plt.savefig('vitesse.png')


#%%%







