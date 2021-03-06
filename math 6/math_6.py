#26 var
from sympy import *
print("№1,1")
z=symbols('z')
z=((1+2*I)/(1+2*I))**4+I**18/2*I
z=expand(z)
print(z)
print("№1,2")
z=(sqrt(3)/2+0.5*I)**14
z=expand(z)
print(z)
def my_sqrt(z):
   x, y = symbols('x y', real=True)
   sol = solve((x+I*y)**3 - z, (x, y))
   print( sol[0][0] + sol[0][1]*I )
   print( sol[1][0] + sol[1][1]*I )
   print( sol[2][0] + sol[2][1]*I )
print("№1,3")
my_sqrt(-216*I)

print("2.1")
x=symbols('x')
print(limit((5*x**2-11*x+2)/(10*x**2+3*x-1),x,0.2))
print(limit((sqrt(3*x-4)-sqrt(4-x))/(2*x**2-3*x-2),x,2))
print("2.2")
print(limit((2-x)/(cos(pi*x/4)),x,2))
print(limit((sin(5*x)-sin(3*x))/(sin(2*x)),x,pi))
print("2.3")
print(limit((pow(2, 5*x)-pow(2, -x))/3*x,x,0))
print(limit(pow((2*x-3)/(2*x-1),3*x/2*x**2+3),x,oo))

print("4.1")
y = symbols('y')
print(diff((cos(sqrt(1+x*3))+sqrt(cos(x))),x))
print("4.3")
y=diff(x-atan(1/x),x)
z=diff(x**3-atan(1/x**2),x)
print(y/z)
print("4.4")
y=diff((ln(x+1))**((ln(x))**2),x)
print(y)