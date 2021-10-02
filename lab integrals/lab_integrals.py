#26 var
import numpy as np
from sympy import *
from scipy.integrate import quad
from sympy.plotting import plot
import matplotlib.pyplot as plt
init_printing(use_unicode=False, wrap_line=False)
x = Symbol('x')
y = Symbol('y')
t = Symbol('t')
ax = plt.axes()
plt.xlim(0, 10)
plt.ylim(-6, 14)

#8.1
def f2( y ):
    return 8-2*y-y**2+2*y+3
print(8.1)
print(quad(f2, -5, 1))
#8.2
def f3( x ):
    return pow(np.cos(2*x),2)*8
I=quad(f3, 0, np.pi/4)
print(8.2)
print(I)
#8.3
x=4*(t-sin(t))
y=2*(1-cos(t))
ds=y*sqrt(x.diff(t)**2+y.diff(t)**2)
DS=lambdify(t, ds, "numpy")
s=2*np.pi*quad(DS, 0, 2*np.pi)[0]
print(8.3)
print(s)
#8.4x8_1_1
def f4( x ):
    return 1-np.arccos(x)+np.sqrt(1-x**2)
print(8.4)
print(quad(f4, 0, 9/16))
#8.5
x=log(1+sin(2*t))-log(cos(2*t))
y=2*(1-cos(t))
ds=y*sqrt(x.diff(t)**2+y.diff(t)**2)
DS=lambdify(t, ds, "numpy")
s=2*np.pi*quad(DS, np.pi/8, np.pi/9)[0]
print(8.5)
print(s)

y8_1 = np.linspace(-10, 10, 100)
x8_1_1 = np.power(y8_1, 2) - 2*y8_1 + 3
ax.plot(x8_1_1, y8_1, color='b', linewidth=3)

x8_1_2 = 8 -2*y8_1
ax.plot(x8_1_2, y8_1, color='r', linewidth=3)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.show()
x_2=np.linspace(0, 2*np.pi, 1000)
y_2=pow(np.cos(2*x_2),2)
plt.polar(x_2, y_2)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.show()
