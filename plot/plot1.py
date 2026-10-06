import numpy as np
import matplotlib.pyplot as plt


start = np.array([0.0, 0.0])
steps = np.random.uniform(-22, 22, size=(200, 2))

path = start + np.cumsum(steps, axis=0)



first_position = path[0]
final_position = path[-1]


latitude = path[:, 0]
longitude = path[:, 1]

plt.plot(longitude, latitude, marker='o', markersize=4, markerfacecolor="#40c9ff", markeredgecolor='#40c9ff', linewidth=3, color="#a10bc7", label='Path')
plt.scatter(first_position[1], first_position[0], marker='^', color="green",  s=100, label='Start Position')
plt.scatter(final_position[1], final_position[0], marker='^',color="red", s=100, label='Final Position')
plt.title('Random Path Simulation', fontsize=16, fontweight='bold', color="#662AF3")
plt.xlabel('Longitude', fontsize=13, fontweight='bold', color="#662AF3") 
plt.ylabel('Latitude', fontsize=13, fontweight='bold', color="#662AF3")
plt.grid(True, which='both', linestyle='dotted', linewidth=1.5, color="#1cc7e6")


plt.show()
