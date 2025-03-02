import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
from sympy import symbols, cos, sin 
s=symbols('s')
def r(s):
    t=s/np.sqrt(2)
    return np.array([cos(t),sin(t),t])
s_final=10
start=r(0)
end=r(s_final)
t_val=np.linspace(0,10,200)
x_val,y_val,z_val=np.cos(t_val),np.sin(t_val),t_val
fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111,projection='3d')
ax.plot(x_val,y_val,z_val)
ax.scatter(*start,color='r',label='(1,0,0)')
ax.scatter(*end,color='g',label='end 10 units')
ax.set_label("X")
ax.set_label("Y")
ax.set_label("Z")
plt.show()
print("For 10 units:",end)
print(r(s))

