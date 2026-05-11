import yfinance as yf
from black_scholes import blackScholes
from greeks import delta_value, gamma_value, theta_value, vega_value, rho_value

ticker = "AAPL" # ticker
stock = yf.Ticker(ticker) # get stock data 

hist = stock.history(period="5d")
S = float(hist["Close"].dropna().iloc[-1]) # gets last closing price of the stock and turns it to a float.

K = 200.0  # strike price
T = 1.0    # time to maturity in years
r = 0.0412 # risk-free interest rate
sigma = 0.25  # volatility of the stock

print(f"Ticker: {ticker}")
print(f"Stock Price (S): {S:.6f}") 
print(f"Strike Price (K): {K}")
print(f"Time to Maturity (T): {T}")
print(f"Risk-Free Rate (r): {r}")
print(f"Volatility (sigma): {sigma}")

# Call Option Check

print("\n=== CALL OPTION CHECK ===")
price_call = blackScholes(r, S, K, T, sigma, "c")
print(f"Call Price (my / vollib): {price_call['my_price']:.6f} / {price_call['vollib_price']:.6f}")

d_my_c, d_lib_c = delta_value(r, S, K, T, sigma, "c")
print(f"Call Delta (manual / vollib): {d_my_c:.6f} / {d_lib_c:.6f}")

g_my_c, g_lib_c = gamma_value(r, S, K, T, sigma, "c")
print(f"Call Gamma (manual / vollib): {g_my_c:.6f} / {g_lib_c:.6f}")

t_my_c, t_lib_c = theta_value(r, S, K, T, sigma, "c")
print(f"Call Theta (manual / vollib): {t_my_c:.6f} / {t_lib_c:.6f}")

v_my_c, v_lib_c = vega_value(r, S, K, T, sigma, "c")
print(f"Call Vega (manual / vollib): {v_my_c:.6f} / {v_lib_c:.6f}")

rho_my_c, rho_lib_c = rho_value(r, S, K, T, sigma, "c")
print(f"Call Rho (manual / vollib): {rho_my_c:.6f} / {rho_lib_c:.6f}")

# Put Option Check

print("\n=== PUT OPTION CHECK ===")
price_put = blackScholes(r, S, K, T, sigma, "p")
print(f"Put Price (my / vollib): {price_put['my_price']:.6f} / {price_put['vollib_price']:.6f}")

d_my_p, d_lib_p = delta_value(r, S, K, T, sigma, "p")
print(f"Put Delta (manual / vollib): {d_my_p:.6f} / {d_lib_p:.6f}")

g_my_p, g_lib_p = gamma_value(r, S, K, T, sigma, "p")
print(f"Put Gamma (manual / vollib): {g_my_p:.6f} / {g_lib_p:.6f}")

t_my_p, t_lib_p = theta_value(r, S, K, T, sigma, "p")
print(f"Put Theta (manual / vollib): {t_my_p:.6f} / {t_lib_p:.6f}")

v_my_p, v_lib_p = vega_value(r, S, K, T, sigma, "p")
print(f"Put Vega (manual / vollib): {v_my_p:.6f} / {v_lib_p:.6f}")

rho_my_p, rho_lib_p = rho_value(r, S, K, T, sigma, "p")
print(f"Put Rho (manual / vollib): {rho_my_p:.6f} / {rho_lib_p:.6f}")