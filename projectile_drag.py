import numpy as np
import matplotlib.pyplot as plt
g = 9.81
k = 0.005
v0 = 30
angle = 45
dt = 0.01
theta = np.radians(angle)
vx = v0 * np.cos(theta)
vy = v0 * np.sin(theta)
x = 0
y = 0
xs = [x]
ys = [y]
while y >= 0:
    speed = np.sqrt(vx**2 + vy**2)
    ax = -k * speed * vx
    ay = -g - k * speed * vy
    vx = vx + ax * dt
    vy = vy + ay * dt
    x = x+ vx * dt
    y = y + vy * dt
    xs.append(x)
    ys.append(y)
t = np.linspace(0, 2 * (v0 * np.sin(theta)) / g, 100)
x_ideal = v0 * np.cos(theta) * t
y_ideal = v0 * np.sin(theta) * t - 0.5 * g * t**2
plt.plot(x_ideal, y_ideal, label="no drag")
plt.plot(xs, ys, label="with drag")
plt.xlabel("distance (m)")
plt.ylabel("height (m)")
plt.title("projectile with air drag")
plt.grid(True)
plt.legend()
plt.savefig("drag.png", dpi=150)
plt.show()
