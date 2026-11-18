import numpy as np
import matplotlib.pyplot as plt
g = 9.81
v0 = 60
angle = 45
theta = np.radians(angle)
vx = v0 * np.cos(theta)
vy = v0 * np.sin(theta)
t_flight = 2* vy / g
t = np.linspace(0, t_flight, 100)
x = vx * t
y = vy * t - 0.5 * g * t**2
plt.plot(x, y)
plt.xlabel("distance (m)")
plt.ylabel("height (m)")
plt.title("projectile motion")
plt.grid(True)
plt.show()
