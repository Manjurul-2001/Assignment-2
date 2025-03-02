import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,2*np.pi,100)
t1=np.pi/4
t2=np.pi
x_val=5*np.cos(t)
y_val=4*np.sin(t)
r1=np.array([5*np.cos(t1),4*np.sin(t1)])
r2=np.array([5*np.cos(t2),4*np.sin(t2)])
tanget1=np.array([-5*np.sin(t1),4*np.cos(t1)])
tanget2=np.array([-5*np.sin(t2),4*np.cos(t2)])
plt.plot(x_val,y_val)
plt.quiver(0,0,r1[0],r1[1],angles='xy',scale_units='xy',scale=1,color='r')
plt.quiver(0,0,r2[0],r2[1],angles='xy',scale_units='xy',scale=1,color='g')
plt.quiver(r1[0],r1[1],tanget1[0],tanget1[1],angles='xy',scale_units='xy',scale=1,color='r')
plt.quiver(r2[0],r2[1],tanget2[0],tanget2[1],angles='xy',scale_units='xy',scale=1,color='g')
plt.show()
