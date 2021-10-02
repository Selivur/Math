from sympy import *
x=Symbol('x')
y = Function('y')
z = Function('z')
#eq=Eq(z(x).diff(x),2*x*(z(x)+1)/(x**2+1))
#eq1=Eq(y(x).diff(x),z(x))
#pprint(dsolve(eq,z(x))) 
#rez=dsolve((eq,eq1))
#display(rez[0]) 

#eq = (Eq(Derivative(y(x),x), z(x)), Eq(Derivative(z(x),x), 2*x*(z(x)+1)/(x**2+1)))
#rez=dsolve(eq)
#display(list(rez))


eq=Eq(y(x).diff(x),(y(x)**2/x**2+10*y(x)**2/x**2+10)/3)
pprint(dsolve(eq,y(x))) 