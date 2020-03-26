import numpy as np
from scipy.stats import norm
from math import *


def d(S, K, t, T, sigma, r=0, q=0):

    try:
        top = log(S/K) + ( r - q + sigma ** 2 / 2) * (T-t)
        bot = sigma * sqrt(T-t)
    except:
        print("S = {}\nK = {}\nT-t = {}".format(S, K, T-t))

    d1 = top / bot
    d2 = d1 - sigma * sqrt(T-t)

    return d1, d2


def gbm(ini, step, drift, vol):

    top = ( drift - vol**2 / 2) * step + vol * sqrt(step) * np.random.normal(0, 1)

    return ini * exp(top)


def path(ini, x_axis, drift, vol):
    
    path = [ ini ]
    
    x_axis = np.array( x_axis )
    DT = x_axis[1:] - x_axis[:-1]

    for dt in DT:
        
        path.append( gbm(path[-1], dt, drift, vol) )
        
    return path     
