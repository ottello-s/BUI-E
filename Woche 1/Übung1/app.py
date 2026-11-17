print("Hello")

import matplotlib.pyplot as plt
import numpy as np
# Daten für den Plot
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel="Zeit (s)", ylabel="Spannung (mV)", title="Graph")
ax.grid()
plt.show