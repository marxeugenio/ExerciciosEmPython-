from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def dy_dt(y, t):
    return -y + 1

y0 = 0
t = np.linspace(0, 10, 100)
y = odeint(dy_dt, y0, t)

plt.plot(t, y)
plt.show()
