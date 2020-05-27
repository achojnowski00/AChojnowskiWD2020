import matplotlib.pyplot as mpl
import numpy as np
import pandas as pd


lista1 = [1/x for x in range(1,21)]
lista2 = [x for x in range(1,21)]
mpl.plot(lista2, lista1, label='x^-1')

mpl.axis([1, 20, 0, 1])

mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.legend()

mpl.show()