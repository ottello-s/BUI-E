import numpy as np
import matplotlib.pyplot as plt
f1 = lambda x: x**2 -1 
f2 = lambda x: -2*x +2 

xValues = np.linspace(-4, 4) 

yValues_1 = f1(xValues)
yValues_2 = f2(xValues)


plt.plot(xValues, yValues_1, "r")