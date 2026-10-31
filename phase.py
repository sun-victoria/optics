import numpy as np
import matplotlib.pyplot as plt
import math

n2 = 1.5
n1 = 1
n = 1/1.5

# Brewster's angle
t_p = np.arctan(n)
# Critical angle (found w Snell's Law)
t_c = np.radians(41.8103149)

theta_deg = np.linspace(0, 90, 500)
theta = np.radians(theta_deg)

def phi_TM(t):
    if t<t_p:
        return 0
    elif t_p<t<t_c:
        return np.pi
    else:
        return -2*np.arctan(np.sqrt(np.sin(t)**2 - n**2)/(n*n*np.cos(t))) + np.pi


def phi_TE(t):
    if t<t_c:
        return 0
    else:
        return -2*np.arctan(np.sqrt(np.sin(t)**2 - n**2)/(np.cos(t)))

phi_TM_values = [phi_TM(t) for t in theta]
phi_TE_values = [phi_TE(t) for t in theta]

# plt.figure(figsize=(8, 5))
# plt.plot(theta_deg, phi_TM_values, label='TM')
# plt.axvline(np.degrees(t_p), linestyle='--', label='Brewster angle')
# plt.axvline(np.degrees(t_c), linestyle=':', label='Critical angle')

# plt.ylim(-np.pi, np.pi + 0.1)
# plt.xlim(0, 90)
# plt.xlabel('Incident angle (degrees)')
# plt.ylabel('Phase shift (rad)')
# plt.title('TM Phase Shift')
# plt.grid(True)
# plt.legend()
# plt.show()

plt.figure(figsize=(8, 5))
plt.plot(theta_deg, phi_TE_values, label='TE')
plt.axvline(np.degrees(t_p), linestyle='--', label='Brewster angle')
plt.axvline(np.degrees(t_c), linestyle=':', label='Critical angle')

plt.ylim(-np.pi, np.pi + 0.1)
plt.xlim(0, 90)
plt.xlabel('Incident angle (degrees)')
plt.ylabel('Phase shift (rad)')
plt.title('TE Phase Shift')
plt.grid(True)
plt.legend()
plt.show()


  