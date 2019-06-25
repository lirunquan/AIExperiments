import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

Xi = np.array([6.19, 2.51, 7.29, 7.01, 5.7, 2.66, 3.98, 2.5, 9.1, 4.2])
Yi = np.array([5.25, 2.83, 6.41, 6.71, 5.1, 4.23, 5.05, 1.98, 10.5, 6.3])

def fun(p, x):
	k, b = p
	return k*x+b

def error(p, x, y):
    return fun(p, x)-y


p0 = [0, 0]

Para = leastsq(error, p0, args=(Xi, Yi))
k, b = Para[0]
plt.figure(figsize=(8, 6))
plt.scatter(Xi, Yi, color="red", label="Simple points", linewidths=3)
x = np.linspace(0, 10, 1000)
y = k*x+b
plt.plot(x, y, color="orange", label="Fitting line", linewidth=2)
plt.legend()
plt.show()