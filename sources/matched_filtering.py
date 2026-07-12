import numpy as np
from scipy.signal import correlate
import matplotlib.pyplot as plt

dt = 0.001 # how often the signal is sampled
t = np.arange(0, 2, dt) # time array from 0 to 2 seconds

f = 10.0 # controls how fast the wave oscillates
t0 = 1 # t0 sets where the signal is centered in time (half of total time)

# creates a sine wave and wrap it in a smooth symmetric envelope
# the 0.1 makes the signal weak so it is hard to see in noise
h = (np.sin(2 * np.pi * f * t) * np.exp(-(t-t0)**2)) * 0.1

sigma = 1.0 # controls how strong the noise is

# creates gaussian/random noise with same length as the signal
noise = np.random.normal(0, sigma, len(t))

x = noise.copy() # copy of noise
x += h # adds weak signal to the noise

# computes the size of the signal, accounting for noise strength
norm = np.sqrt(np.sum((h * h) / (sigma* sigma)) * dt)
h_hat = h / norm # normalise the signal so comparisons are fair

# slide template across data and measures similarity
R = correlate(x, h_hat, mode="full") * dt

snr = np.max(R) # height of the largest peak
peak_index = np.argmax(R) # find the index where the peak occurs

# convert array index into a physical time shift
tau_index = peak_index - (len(h)-1)
tau = tau_index * dt

# graph
plt.plot(R, color="red")
plt.xlabel("Shift index")
plt.ylabel("Matched filter output")
plt.title("Matched Filtering Detection of a Weak Signal in Gaussian Noise")
plt.show()
