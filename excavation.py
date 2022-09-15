
import numpy as np
import math
X4=0.1008
X3=0.0016
X13=0.025
G2=10
F2=45
X5=5
X12=1.622
X6=90
X7=0.0032
X11=0.0896
C2=0.75
E2=2100



print("start")


reg_force=X4*X13*((np.cos(G2*np.pi/180)*(np.cos(G2*np.pi/180) + ((np.sin(F2*np.pi/180))**2-(np.sin(G2*np.pi/180))**2)**0.5)/(1 - np.sin(F2*np.pi/180)))*math.exp((2*X5*np.pi/180 - np.pi+ G2*np.pi/180 + np.arcsin(np.sin(G2*np.pi/180)/np.sin(F2*np.pi/180)))*np.tan(F2*np.pi/180)))*(1 + 1/np.cos(X5*np.pi/180)*np.tan(G2*np.pi/180))*(X13*4*X12*C2*1000/2 +E2*1/np.tan(F2*np.pi/180)) + X4*X3*((np.cos(G2*np.pi/180)*(np.cos(G2*np.pi/180) +((np.sin(F2*np.pi/180))**2 - (np.sin(G2*np.pi/180))**2)**0.5)/(1 - np.sin(F2*np.pi/180)))*math.exp((2*X6*np.pi/180 - np.pi + G2*np.pi/180 + np.arcsin(np.sin(G2*np.pi/180)/np.sin(F2*np.pi/180)))*np.tan(F2*np.pi/180)))*(1 +np.tan(G2*np.pi/180)*1/np.tan(X6*np.pi/180))*(X3*X12*C2*1000/2 + E2*1/np.tan(F2*np.pi/180) + X13*0.01*X12*C2*1000*(1-np.sin(F2*np.pi/180))/(1+np.sin(F2*np.pi/180)))+ X13*((np.cos(G2*np.pi/180)*(np.cos(G2*np.pi/180) + ((np.sin(F2*np.pi/180))**2 - (np.sin(G2*np.pi/180))**2)**0.5)/(1 - np.sin(F2*np.pi/180)))*math.exp((2*np.pi/2 - np.pi + G2*np.pi/180 + np.arcsin(np.sin(G2*np.pi/180)/np.sin(F2*np.pi/180)))*np.tan(F2*np.pi/180)))*(2*X7 + 4*X11*np.tan(G2*np.pi/180))*(X13*0.01*X12*C2*1000/2 + 1/E2*np.tan(F2*np.pi/180))


reg_volume = 1

reg_distance = 1/(X4*X13*8)


print(reg_force)

exc_energy = reg_distance * reg_force

print(exc_energy)
