import sympy as sp 
x,y,z,r,theta,t,h,phi=sp.symbols('x y z r theta t h phi')
#(a)
av_t=sp.integrate(sp.integrate(10-8*x**2-2*y**2,(y,0,2)),(x,0,1))/2
print(f'average tempature:',av_t)
#(b)
x_t,y_t,z_t=sp.cos(t),sp.sin(t),t
integral=(x_t*y_t+z_t**3)*sp.sqrt(sp.diff(x_t,t)**2+sp.diff(y_t,t)**2+sp.diff(z_t,t)**2)
line_integal=sp.integrate(integral,(t,0,sp.pi))
print(f'line integal:',line_integal)
#(c)
roh=r**2
m=sp.integrate((roh*r),(r,0,r),(theta,0,2*sp.pi),(z,0,h))
print(f'mass:',m)
#(d)
F_x,F_y=sp.exp(y),x*sp.exp(y)
if sp.diff(F_y,x)==sp.diff(F_x,y):
    print("The field is conservative")
else:
    print("The field is not conservative")
phi=sp.integrate(F_x,x)
w=phi.subs({x:-1,y:0})-phi.subs({x:1,y:0})
print(f'potential function:',phi)
print(f'work done:',w)


