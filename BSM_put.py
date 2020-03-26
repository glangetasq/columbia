from BSM_tools import *
from scipy.optimize import newton


def price(S, K, t, T, sigma, r=0, q=0):
    
    d1, d2 = d(S, K, t, T, sigma, r, q)

    p = K * exp( - r * (T-t) ) * norm.cdf(-d2)
    p -= S * exp( - q * (T-t) ) * norm.cdf(-d1)

    return p


def delta(S, K, t, T, sigma, r=0, q=0):

    d1, d2 = d(S, K, t, T, sigma, r, q)

    return exp( - q * (T-t) ) * ( norm.cdf(d1) - 1)


def imp_vol(Price, S, K, t, T, r=0, q=0):

    def f(sigma):

        return price(S, K, t, T, sigma, r, q) - Price

    return newton(f, 0.3)


def implied_volatility(Price, S, K, t, T, r=0, q=0):

    return imp_vol(Price, S, K, t, T, r, q)
