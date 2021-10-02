# 27 Variant
#first plot
#x**2+(y+3)**2=1
import matplotlib.pyplot as plt
import numpy as np
ax=plt.gca()
ax.set_xlim((-5, 5))
ax.set_ylim((-5, 5))
circle1=plt.Circle((0, -3), 1, fill=False, color='yellow', linewidth=2)
ax.add_artist(circle1)
#second plot
# 41*x**2+24*x*y+9*y**2+24*x+18*y-36=0
xlist=np.linspace(-10, 10, 100)
ylist=np.linspace(-10, 10, 100)
x, y=np.meshgrid(xlist, ylist)
z=(41*x**2+24*x*y+9*y**2+24*x+18*y-36)
plt.contour(x, y, z, 0, colors="b")
#third plot
# 32*x**2+52*x*y-7*y**2-180=0
z=(32*x**2+52*x*y-7*y**2-180)
plt.contour(x, y, z, 0, colors="k")
plt.show()

