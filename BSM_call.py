from BSM_tools import d
from math import exp, sqrt, pi
from scipy.optimize import newton
from scipy.stats import norm

def price(S, K, t, T, sigma, r=0, q=0):
    
    d1, d2 = d(S, K, t, T, sigma, r, q)

    p = S * exp( - q * (T-t) ) * norm.cdf(d1)
    p -= K * exp( - r * (T-t) ) * norm.cdf(d2)

    return p


def delta(S, K, t, T, sigma, r=0, q=0):

    d1, d2 = d(S, K, t, T, sigma, r, q)

    return exp( - q * (T-t) ) * norm.cdf(d1)


def gamma(S, K, t, T, sigma, r=0, q=0):

    d1, d2 = d(S, K, t, T, sigma, r, q)

    top = exp(-q*(T-t)) * norm.pdf(d1)
    bot = S * sigma * sqrt(T-t)

    return top / bot


def imp_vol(Price, S, K, t, T, r=0, q=0):

    def f(sigma):

        return price(S, K, t, T, sigma, r, q) - Price

    return newton(f, 0.3)


def implied_volatility(Price, S, K, t, T, r=0, q=0):

    return imp_vol(Price, S, K, t, T, r, q)
