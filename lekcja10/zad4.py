import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl

x= np.arange(0,30.1,0.1)
ys= 2+ np.sin(x)
ys2= np.sin(-x)

mpl.plot(x,ys,label='sin(x)')
mpl.plot(x,ys2,label='sin(x)')
mpl.xlabel('x')
mpl.ylabel('sin(x)')
mpl.title('Wykres sin(x), sin(x)')
mpl.legend(loc=6)
mpl.show()