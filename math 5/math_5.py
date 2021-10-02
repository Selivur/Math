import numpy as np  
from matplotlib import pyplot as plt 
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle,	Rectangle
#26 variant
#x**2+x*2+5=0
#у Координату не задано, це означає, що вона статична, и графік відповідає прямій, паралельній осі у.
plt.style.use('seaborn-pastel') 
fig = plt.figure()
ax = plt.axes(xlim=(-30, 30), ylim=(0, 50))
line, = ax.plot([], [], lw=3)
ii=0
def init():
    circle =  Circle((5, 5), 7,	color='r')
    ax.add_artist(circle)
    line.set_data([], [])
    return line,
def animate(i):
    if i>=50:
        x = np.linspace(-20, 20, 100)
        y= 100-i
        line.set_data(x, y)
        return line,
                
    x = np.linspace(-20, 20, 100)
    y= i
    line.set_data(x, y)
    return line,
 
anim = FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)

anim.save('sine_wave.gif', writer='pillow')
plt.show()

