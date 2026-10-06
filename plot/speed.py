import numpy as np
import matplotlib.pyplot as plt

speeds = np.random.uniform(1, 30, 200)



average_speed = np.mean(speeds)
maximum_speed = np.max(speeds)
minimum_speed = np.min(speeds)

sprint_indices = np.where(speeds >= 20)[0]
sprint_speeds = speeds[sprint_indices]

low_indices = np.where(speeds <= 10)[0]
low_speeds = speeds[low_indices]

plt.figure(figsize=(10, 6))

plt.plot(speeds, label='Speed', color="#f78720", linewidth=1.7)


plt.axhline(y=average_speed, color='blue', linewidth=2, label=f"Average Speed({average_speed:.2f})")
plt.axhline(y=minimum_speed, color='red', linewidth=2, label=f"Minimum Speed({minimum_speed:.2f})")
plt.axhline(y=maximum_speed, color='green', linewidth=2, label=f"Maximum Speed({maximum_speed:.2f})")


plt.scatter(sprint_indices, sprint_speeds, color="#e20aff", marker='*', s=80)
plt.scatter(low_indices, low_speeds, color="#fa1a70", s=80, marker='*')

plt.title('SPEED GRAPH', fontweight='bold', color='green', fontsize=16)
plt.ylabel('SPEED', fontweight='bold', color='green', fontsize=13)
plt.xlabel('VARIATION', fontweight='bold', color='green', fontsize=13)
plt.grid(True, which='both', color='green', linestyle='--', linewidth=1)

plt.legend(['Speed', 'Average Speed', 'MAximum Speed', 'Minimum Speed'],  loc='upper left', fontsize=10, title_fontsize='13', shadow=True, fancybox=True, facecolor="#2ef068", edgecolor='#000000')

plt.tight_layout()
plt.show()