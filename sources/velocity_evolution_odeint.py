import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# these numbers are dimensionless and using only the mass ratio.
m1 = 10.0 # mass of black hole 1
m2 = 5.0 # mass of black hole 2

m = m1 + m2 # total mass of the system
mu = (m1 * m2) / m # reduced mass

# function shows how orbital velocity increase over time due to
# gravitational-wave energy loss.
def dv_dt(v, t):
    if v <= 0.5:
        return (32 / 5) * (mu / m ** 2) * v ** 9
    else:
        return 0.0

v0 = 0.3 # initial orbital velocity
t = np.linspace(0, 19750, 20000) # uniform time array

v = odeint(dv_dt, v0, t) # solve ODE
t_plot = t / 1000 # rescaled time values to make it easier to read

# visualisation (graph)
plt.plot(t_plot, v, color = 'red')
plt.xlabel(r"Time ($GM/c^{3} \times 10^{3}$)")
plt.ylabel("v(t)")
plt.title("Orbital Velocity Evolution of a Binary Black Hole Inspiral")
plt.show()