import sympy as sp
x,y,z,r,theta,phi=sp.symbols('x y z r theta phi')
#(a)
F_xy=sp.Matrix([sp.exp(x)-y**3,sp.cos(y)+x**3])
M,N=F_xy[0],F_xy[1]
dN_dx,dM_dy=sp.diff(N,x),sp.diff(M,y)
intergal=dN_dx-dM_dy
w=sp.integrate(intergal.subs({x:r*sp.cos(theta),y:r*sp.sin(theta)})*r,(r,0,1),(theta,0,2*sp.pi))
print(f"work done:",w)
#(b)
F_x=x**2
F_thetaphi=F_x.subs({x:sp.sin(theta)*sp.cos(phi)})
ds=sp.sin(theta)
surface_integral=sp.integrate(F_thetaphi*ds,(theta,0,sp.pi),(phi,0,2*sp.pi))
print(f"surface_integral",surface_integral)

