import numpy as np
import matplotlib.pyplot as plt
import math

n = 1.5
n2 = 1/1.5

theta_i = np.radians(np.linspace(0, 90, 300))

# reflectance
def r_TE(t):
    num = np.cos(t) - np.sqrt(n*n - np.sin(t) ** 2)
    denom = np.cos(t) + np.sqrt(n*n - np.sin(t) ** 2)
    return (num/denom)**2

def r_TM(t):
    num = -n*n*np.cos(t) + np.sqrt(n*n - np.sin(t) ** 2)
    denom = n*n*np.cos(t) + np.sqrt(n*n - np.sin(t) ** 2)
    return (num/denom)**2

def r_TE_i(t):
    num = np.cos(t) - np.sqrt(n2*n2 - np.sin(t) ** 2)
    denom = np.cos(t) + np.sqrt(n2*n2 - np.sin(t) ** 2)
    return (num/denom)**2

def r_TM_i(t):
    num = -n2*n2*np.cos(t) + np.sqrt(n2*n2 - np.sin(t) ** 2)
    denom = n2*n2*np.cos(t) + np.sqrt(n2*n2 - np.sin(t) ** 2)
    return (num/denom)**2


plt.figure(figsize=(9, 6))

plt.plot(theta_i, r_TE(theta_i), label='r_TE_external')
plt.plot(theta_i, r_TM(theta_i), label='r_TM_external')

plt.plot(theta_i, r_TE_i(theta_i), label='r_TE_internal')
plt.plot(theta_i, r_TM_i(theta_i), label='r_TM_internal')


plt.xlabel("Angle of Incidence, theta (radians)")
plt.ylabel("Reflectance")
plt.legend()
plt.grid(True)
plt.show()