import sympy as sp
import numpy as py
import matplotlib.pyplot as plt
#a(i)
x,y,z=sp.symbols('x y z')
f=x**2+4*y**2+z**2-18
grad_f=sp.Matrix([sp.diff(f,var) for var in (x,y,z)])
points={x:1,y:2,z:1}
