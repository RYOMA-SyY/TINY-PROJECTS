import numpy as np
import matplotlib.pyplot as plt
def newton(f, df, x0, precision):
    correcteur = f(x0) / df(x0)
    while np.abs(correcteur) > precision:
        x0 = x0 - correcteur
        correcteur = f(x0) / df(x0)
    return x0

print(newton(lambda x: x*x-4*x+3, lambda x:2*x-4,5,1e-6))