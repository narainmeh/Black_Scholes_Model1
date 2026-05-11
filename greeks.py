import numpy as np
from scipy.stats import norm
from py_vollib.black_scholes.greeks.analytical import delta, gamma, theta, vega, rho
from black_scholes import d1_d2


def delta_value(r, S, K, T, sigma, type="c"):
    d1, d2 = d1_d2(S, K, r, sigma, T)

    if type == "c":
        my_delta = norm.cdf(d1, 0, 1)
    elif type == "p":
        my_delta = norm.cdf(d1, 0, 1) - 1
    else:
        print("Press 'p' for put or 'c' for call option.")
        return None

    vollib_delta = delta(type, S, K, T, r, sigma)
    return float(my_delta), float(vollib_delta)


def gamma_value(r, S, K, T, sigma, type="c"):
    d1, d2 = d1_d2(S, K, r, sigma, T)

    my_gamma = norm.pdf(d1, 0, 1) / (S * sigma * np.sqrt(T))
    vollib_gamma = gamma(type, S, K, T, r, sigma)

    return float(my_gamma), float(vollib_gamma)


def theta_value(r, S, K, T, sigma, type="c"):
    d1, d2 = d1_d2(S, K, r, sigma, T)

    if type == "c":
        my_theta = (
            -(S * norm.pdf(d1, 0, 1) * sigma) / (2 * np.sqrt(T))
            - r * K * np.exp(-r * T) * norm.cdf(d2, 0, 1)
        )
    elif type == "p":
        my_theta = (
            -(S * norm.pdf(d1, 0, 1) * sigma) / (2 * np.sqrt(T))
            + r * K * np.exp(-r * T) * norm.cdf(-d2, 0, 1)
        )
    else:
        print("Press 'p' for put or 'c' for call option.")
        return None

    vollib_theta = theta(type, S, K, T, r, sigma)
    return float(my_theta), float(vollib_theta)


def vega_value(r, S, K, T, sigma, type="c"):
    d1, d2 = d1_d2(S, K, r, sigma, T)

    my_vega = S * norm.pdf(d1, 0, 1) * np.sqrt(T)
    vollib_vega = vega(type, S, K, T, r, sigma)

    return float(my_vega), float(vollib_vega)


def rho_value(r, S, K, T, sigma, type="c"):
    d1, d2 = d1_d2(S, K, r, sigma, T)

    if type == "c":
        my_rho = K * T * np.exp(-r * T) * norm.cdf(d2, 0, 1)
    elif type == "p":
        my_rho = -K * T * np.exp(-r * T) * norm.cdf(-d2, 0, 1)
    else:
        print("Press 'p' for put or 'c' for call option.")
        return None

    vollib_rho = rho(type, S, K, T, r, sigma)
    return float(my_rho), float(vollib_rho)