#26 var
import numpy as np
from sympy import *
from scipy.integrate import quad
from sympy.plotting import plot
import matplotlib.pyplot as plt
init_printing(use_unicode=False, wrap_line=False)
x = Symbol('x')
y = Symbol('y')
ax = plt.axes()
plt.xlim(0, 10)
plt.ylim(-6, 14)
#1.1
print(integrate(sqrt(x**2, 5)*sqrt(x**2, 3), x))
print("+С")
#1.2
print(integrate((x-5)/(x**2+7), x))
print("+С")
#4.1 a
print(integrate(sqrt(pow(cos(x),3), 5)*pow(sin(x),5), x))
print("+С")
#4.1 b
print(integrate(1/(25-cos(x)**2), x))
print("+С")
#4.1 с
print(integrate(cos(5*x)*cos(8*x), x))
print("+С")
#26
def f1( x ):
 return pow(x, 3)/pow(1+x**2, 2/3)
print(quad(f1, np.sqrt(7), np.sqrt(26)))
#8.1
def f2( y ):
 return 8-2*y-y**2+2*y+3
print(quad(f2, -5, 1))
#8.2
def f3( x ):
 return pow(np.cos(2*x),2)
I=quad(f3, 0, np.pi/2)
print(I*4)
#8.4x8_1_1
def f4( x ):
 return 1-np.arccos(x)+np.sqrt(1-x**2)
print(quad(f4, 0, 9/16))


y8_1 = np.linspace(-10, 10, 100)
x8_1_1 = np.power(y8_1, 2) - 2*y8_1 + 3
ax.plot(x8_1_1, y8_1, color='b', linewidth=3)

x8_1_2 = 8 -2*y8_1
ax.plot(x8_1_2, y8_1, color='r', linewidth=3)

plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.legend(loc='best')
plt.show()