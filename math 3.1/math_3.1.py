# 27 Variant
#first plot
import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(0,2*np.pi,3000) 
r = np.sqrt(72*np.cos(2*t))
plt.polar(t,r,linewidth=2,color='red')
#second plot
r = 4*np.cos(5*t)
plt.polar(t,r,linewidth=2,color='b')
plt.show()


