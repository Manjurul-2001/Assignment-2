import numpy as np
import sympy as sp
x,y=sp.symbols('x y')
f=y**2*sp.cos(x-y)
fx=sp.diff(f,x)
fy=sp.diff(f,y)
fxx=sp.diff(fx,x)
fyy=sp.diff(fy,y)
fxy=sp.diff(fx,y)
fyx=sp.diff(fy,x)
if fxx+fyy==0:
    print("Laplace's equations satisfy")
else:
    print("Laplace equations is not satisfy")
if fxy-fyx==0:
    print("Cauchy Riemann equations satisfy")
else:
    print("Cauchy Riemann equations is not satisfy")
print(fxy)
print(fyx)
