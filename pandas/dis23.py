import numpy as np
import matplotlib.pyplot as plt


dt = 0.2
path = np.random.uniform(1, 5, size=(200, 2))

time = np.arange(200) * dt

step_distance = np.linalg.norm(path, axis=1)


velocity = step_distance / dt


plt.figure(figsize=(9, 6))

plt.plot(time, velocity, color="#0fff2f", linewidth=1.7, label='Tiem')
plt.title('VELOCITY GRAPH', color='#0fa7ff', fontsize=16, fontweight='bold')
plt.xlabel('TIME', color="#0fa7ff", fontsize=13, fontweight='bold')
plt.ylabel('VELOCITY', color='#0fa7ff', fontsize=13, fontweight='bold')
plt.grid(True, which='both', color='#0fa7ff', linestyle='--', linewidth=1)


plt.legend()
plt.show()