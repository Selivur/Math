#26 var
import numpy as np
from scipy.integrate import quad
x = np.Symbol('x')
С="+С"
#4.1 a
def f1(x):
  return np.sqrt(np.cos(x), 5)*np.sin(x)**2
i=quad(f1)
print()


