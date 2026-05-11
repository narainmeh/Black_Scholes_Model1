import numpy as np
from scipy.stats import norm
from py_vollib.black_scholes import black_scholes as bs


def d1_d2(S, K, r, sigma, T):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return d1, d2


def blackScholes(r, S, K, T, sigma, type="c"):
    d1, d2 = d1_d2(S, K, r, sigma, T)

    if type == "c":
        price = S * norm.cdf(d1, 0, 1) - K * np.exp(-r * T) * norm.cdf(d2, 0, 1)
    elif type == "p":
        price = K * np.exp(-r * T) * norm.cdf(-d2, 0, 1) - S * norm.cdf(-d1, 0, 1)
    else:
        print("Press 'p' for put or 'c' for call option.")
        return None

    return {
        "my_price": float(price),
        "vollib_price": float(bs(type, S, K, T, r, sigma))
    }
