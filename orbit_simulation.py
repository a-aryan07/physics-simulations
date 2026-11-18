import numpy as np
import matplotlib.pyplot as plt
GM = 3.986e14
R_earth = 6.371e6
def simulate(speed_factor, dt=1.0, steps=40000):
    r = np.array([R_earth + 400e3, 0.0])
    v = np.array([0.0, speed_factor * np.sqrt(GM / np.linalg.norm(r))])
    path = []
    for _ in range(steps):
        a = -GM * r / np.linalg.norm(r)**3
        v = v + a * dt
        r = r + v * dt
        if np.linalg.norm(r) < R_earth:
            break
        path.append(r.copy())
    return np.array(path)
for f in [0.8, 1.0, 1.3, 1.5]:
    p = simulate(f)
    plt.plot(p[:, 0], p[:, 1], label=f"{f} x circular speed")
plt.gca().add_patch(plt.Circle((0, 0), R_earth, color="skyblue"))
plt.gca().set_aspect("equal", adjustable="box")
plt.xlim(-5e7, 5e7)
plt.ylim(-5e7, 5e7)
plt.legend()
plt.title("Satellite orbits at different launch speeds")
plt.savefig("orbits.png", dpi=150)
plt.show()
