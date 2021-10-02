from sympy import *
t = symbols('t')
x = symbols('x')
y = symbols('y')
z = symbols('z')
plot_parametric(t*cos(t), t*sin(t), (t, 0, 40), line_color='g')
#3.1 and 3.2
f1 = sqrt((5*x**2-20)/4)
f2 = -3/5*sqrt(24-2*x-x**2)
str=latex(S(' sqrt((5*x**2-20)/4) , -3/5*sqrt(24-2*x-x**2) ',evaluate=False))
p = plot((f1, (x, -10, 10)), (f2, (x, -10, 10)),
title='$'+str+'$', show=False)
p[0].line_color = 'blue'
p[1].line_color = 'red'
p.show()
#4.1
plotting.plot3d((2*x**2-y**2-4*x-2*y+1)/6, (x, -100, 100), (y, -100, 100))

