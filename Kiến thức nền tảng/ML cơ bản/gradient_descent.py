from __future__ import division, print_function, unicode_literals
import math
import numpy as np
import matplotlib.pyplot as plt

# f(x) = x*x + 5sin(x)

# tinh dao ham
def grad(x):
    return 2*x + 5*np.cos(x)

#gia tri cua f(x)
def cost(x):
    return x*x+5*np.sin(x)

#phan chinh gradient desent
def myGD1(x0, eta):
    x = [x0]
    for i in range(100):
        x_new = x[-1] - eta*grad(x[-1])
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    return(x, i)

(x1, i) = myGD1(-5, .1)
print(x1[-1], i)
