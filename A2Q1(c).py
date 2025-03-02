import numpy as np
import matplotlib.pyplot as plt
from sympy import diff,sin,cos,tan,atan,symbols
theta=symbols('theta')
theta_val=np.linspace(0,6*np.pi,200)
t_val=np.atan(theta_val)
v=np.array([3,cos(theta),2*theta])
a=np.array([0,-sin(theta),2])
print("velocity:",v)
print("acceleration:",a)
plt.plot(theta_val,t_val)
plt.xlabel('t')
plt.ylabel('theta(t)')
plt.title('theta(t) vs t')
plt.show()
