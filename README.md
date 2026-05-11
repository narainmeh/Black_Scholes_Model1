# Black-Scholes Option Pricing Model

Python project for implementing the Black-Scholes model from scratch for pricing European call and put options, including the full set of core Greeks, and comparing it with `py_vollib`. It also includes live stock price input from Yahoo Finance.

## Overview

The project was developed by me (Narain) with the main intention of understanding the mathematical pricing of options and the application of option measures. It brings together the theory, Python code, and Yahoo Finance stock prices into a single option model. 

**The model calculates:**

- Call option price
- Put option price
- Delta
- Gamma
- Theta
- Vega
- Rho

## Features

- Black-Scholes model implemented from scratch
- Calculating Greeks from scratch
- Comparison with `py_vollib`
- Live stock price input from Yahoo Finance

## Black-Scholes Formula

$$
C = S_t \Phi(d_1) - K e^{-rt} \Phi(d_2)
$$

$$
d_1 = \frac{\ln(S_t / K) + (r + \sigma^2 / 2)t}{\sigma \sqrt{t}}
$$

$$
d_2 = d_1 - \sigma \sqrt{t}
$$


## 3D Visualization

Another component of the project is an interactive 3D Black-Scholes surface constructed using Plotly.

The plot displays the way that the value of a European call option varies in relation to the price of the underlying stock and days to maturity.

- X-Axis: Underlying Stock Price

- Y-Axis: Days to Maturity

- Z-Axis: Theoretical Call Option Value


The dot indicated in the plot is the current input, and the entire surface is the way the price varies according to various market situations.

Such visualization enables us to observe the option sensitivity rather than just having the price output.

## Project Structure

```bash
black-scholes-model/
│
├── black_scholes.py
├── greeks.py
├── main.py
├── requirements.txt
└── README.md


