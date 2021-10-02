# 26 Variant
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#I will solve it by parametric equation
fig = plt.figure()  # Square figure
ax = fig.add_subplot(111, projection='3d')

coefs = (2**2, 4**2, 5**2)  # Coefficients in  x**2/a**2 +  y**2/b**2 +  z**2/c**2 = 1 

rx, ry, rz = 1/np.sqrt(coefs)

# Set of all spherical angles:
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

# Cartesian coordinates that correspond to the spherical angles:
# (this is the equation of an ellipsoid):
x = rx * np.outer(np.cos(u), np.sin(v))
y = ry * np.outer(np.sin(u), np.sin(v))
z = rz * np.outer(np.ones_like(u), np.cos(v))

# Plot:
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')
ax.plot([0,0],[0,0],[-0.6,0.6],color='magenta',alpha=1,linewidth=2,antialiased=True,linestyle='-')
ax.plot([-0.6,0.6],[0,0],[0,0],color='magenta',alpha=1,linewidth=2,antialiased=True,linestyle='-')
ax.plot([0,0],[-0.6,0.6],[0,0],color='magenta',alpha=1,linewidth=2,antialiased=True,linestyle='-')
plt.show()