import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return -(x-2)*(x-8)+40

x=np.linspace(0,10)

y=func(x)

fig, ax=plt.subplots()

plt.plot(x,y,'r',linewidth = 1)

plt.show()