import numpy as np
import matplotlib.pyplot as plt



start = np.array([0, 0])
steps = np.random.uniform(-2, 2, size=(60, 2))
path = start + np.cumsum(steps, axis=0)

first_position = path[0]
final_position = path[-1]

displacement = np.linalg.norm(final_position - start)
distance = np.sum(np.linalg.norm(steps, axis=1))
ratio = displacement / distance

average_X = np.mean(path[:, 0])
average_Y = np.mean(path[:, 1])


average_path = np.mean(path, axis=0)

##########Speed Calculation##########
dt = 0.2

time = np.arange(60) * dt

speed = np.linalg.norm(steps, axis=1) / dt

min_speed = np.min(speed)
max_speed = np.max(speed)
average_speed = np.mean(speed)

sprint_speed = speed[speed > 10]
walking = speed[speed < 4]
steady = speed[(speed >= 4) & (speed <= 10)]




#############################################
y = path[:, 1]
x = path[:, 0]

figure, axes = plt.subplots(3, 2, figsize=(10, 10))


axes[0, 0].plot(x, y, color="#ff8f0f", linewidth=1.7, label='Path')
axes[0, 0].scatter(x[0], y[0], color='green', s=100, label='Start')
axes[0, 0].scatter(x[-1], y[-1], color='red', s=100, label='End')
axes[0, 0].set_title('PATH', color='#0fa7ff', fontsize=16, fontweight='bold')
axes[0, 0].set_xlabel('X', color="#0fa7ff", fontsize=13, fontweight='bold')
axes[0, 0].set_ylabel('Y', color='#0fa7ff', fontsize=13, fontweight='bold')
axes[0, 0].grid(True, which='both', color='#0fa7ff', linestyle='--', linewidth=1)
axes[0, 0].legend()


axes[0, 1].bar(['Displacement', 'Distance', 'Ratio'], [displacement, distance, ratio], color=['#0fa7ff', '#ff8f0f', '#a3ff0f'])
axes[0, 1].set_title('DISPLACEMENT VS DISTANCE', color='#0fa7ff', fontsize=16, fontweight='bold')
axes[0, 1].set_ylabel('Value', color='#0fa7ff', fontsize=13, fontweight='bold')
axes[0, 1].set_xlabel('Metrics', color='#0fa7ff', fontsize=13, fontweight='bold')
axes[0, 1].grid(True, which='both', color='#0fa7ff', linestyle='--', linewidth=1)
axes[0, 1].text(0, displacement + 0.1, f'{displacement:.2f}', ha='center', va='bottom', color='#0fa7ff', fontweight='bold')
axes[0, 1].text(1, distance + 0.1, f'{distance:.2f}', ha='center', va='bottom', color='#ff8f0f', fontweight='bold')
axes[0, 1].text(2, ratio + 0.1, f'{ratio:.2f}', ha='center', va='bottom', color="#ff0f0f", fontweight='bold')
axes[0, 1].set_ylim(0, max(displacement, distance, ratio) + 1)


axes[1, 0].hist(x, bins=10, color="#0fa7ff", edgecolor='black')
axes[1, 0].set_title('DISTRIBUTION OF X COORDINATES', color='#0fa7ff', fontsize=16, fontweight='bold')
axes[1, 0].set_xlabel('X', color="#0fa7ff", fontsize=13, fontweight='bold')
axes[1, 0].set_ylabel('Frequency', color='#0fa7ff', fontsize=13, fontweight='bold')
axes[1, 0].grid(True, which='both', color='#0fa7ff', linestyle='--', linewidth=1)


axes[1, 1].hist(y, bins=10, color="#ff8f0f", edgecolor='black')
axes[1, 1].set_title('DISTRIBUTION OF Y COORDINATES', color='#0fa7ff', fontsize=16, fontweight='bold')
axes[1, 1].set_xlabel('Y', color="#0fa7ff", fontsize=13, fontweight='bold')
axes[1, 1].set_ylabel('Frequency', color='#0fa7ff', fontsize=13, fontweight='bold')
axes[1, 1].grid(True, which='both', color='#ff8f0f', linestyle='--', linewidth=1)

axes[2, 0].plot(time, speed, color="#a3ff0f")
axes[2, 0].scatter(time, speed, color="#86d409")
axes[2, 0].set_title('DISTRIBUTION OF SPEED', color='#0fa7ff', fontsize=16, fontweight='bold')
axes[2, 0].set_xlabel('Speed', color="#0fa7ff", fontsize=13, fontweight='bold')
axes[2, 0].set_ylabel('Frequency', color='#0fa7ff', fontsize=13, fontweight='bold')
axes[2, 0].grid(True, which='both', color='#a3ff0f', linestyle='--', linewidth=1)


labels = ['Sprint Speed', 'Steady Speed', 'Walking']
values = [
    len(sprint_speed),
    len(steady),
    len(walking)
]

axes[2, 1].pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
axes[2, 1].set_title('Speed Variations', color='#0fa7ff', fontsize=16, fontweight='bold')


plt.tight_layout()
plt.show()