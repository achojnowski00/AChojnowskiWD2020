import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl

x= range(1,21)
y= [1/y for y in x]
mpl.plot(x,y,'g:>',label='f(x)=1/x')
mpl.axis([1, len(x), 0, 1])
mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.xticks(np.arange(0,21,2.5))
mpl.title('Wykres funkcji f(x) gdzie x ϵ [1, 20]')
mpl.legend()

mpl.show()