import numpy as np
import matplotlib.pyplot as plt
import math

n = 1.5
theta = np.linspace(0, 90, 300)
theta_i = np.radians(theta)

def r_TE(t):
    num = np.cos(t) - np.sqrt(n*n - np.sin(t) ** 2)
    denom = np.cos(t) + np.sqrt(n*n - np.sin(t) ** 2)
    return num/denom

def r_TM(t):
    num = -n*n*np.cos(t) + np.sqrt(n*n - np.sin(t) ** 2)
    denom = n*n*np.cos(t) + np.sqrt(n*n - np.sin(t) ** 2)
    return num/denom

def t_TE(t):
    num = 2*np.cos(t)
    denom = np.cos(t) + np.sqrt(n*n - np.sin(t) ** 2)
    return num/denom

def t_TM(t): 
    num = 2*n*np.cos(t)
    denom = n*n*np.cos(t) + np.sqrt(n*n - np.sin(t) ** 2)
    return num/denom

plt.figure(figsize=(9, 6))

plt.plot(theta_i, r_TE(theta_i), label='r_TE')
plt.plot(theta_i, r_TM(theta_i), label='r_TM')
plt.plot(theta_i, t_TE(theta_i), label='t_TE')
plt.plot(theta_i, t_TM(theta_i), label='t_TM')
plt.xlabel("Angle of Incidence, theta (radians)")

plt.legend()
plt.grid(True)

plt.xlim(0, np.pi/2)
plt.show()

