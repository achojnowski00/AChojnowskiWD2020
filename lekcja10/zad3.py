import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl

x= np.arange(0,30.1,0.1)
ys= np.sin(x)
yc= np.cos(x)

mpl.plot(x,ys,label='sin(x)')
mpl.plot(x,yc,label='cos(x)')
mpl.ylabel('y')
mpl.xlabel('x')
mpl.legend()
mpl.show()