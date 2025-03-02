import numpy as np
import matplotlib.pyplot as plt
from sympy import diff,sin,cos,tan,atan,symbols
t1=2
x1,y1,z1=np.log(t1),np.exp(-t1),t1^3
dx1,dy1,dz1=1/t1,-np.exp(-t1),3*t1^2
print(f'x={x1}+{dx1}*t')
print(f'y={y1}+{dy1}*t')
print(f'z={z1}+{dz1}*t')
t1=1/3
x1,y1,z1=2*np.cos(np.pi*t1),2*np.sin(np.pi*t1),3*t1
dx1,dy1,dz1=-2*np.pi*np.sin(np.pi*t1),2*np.pi*np.cos(np.pi*t1),3
print(f'x={x1}+{dx1}*t')
print(f'y={y1}+{dy1}*t')
print(f'z={z1}+{dz1}*t')
