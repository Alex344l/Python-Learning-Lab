import numpy as np



start = np.array([0.0, 0.0])

steps = np.random.uniform(-2, 3, size=(100, 2))

position = start + np.cumsum(steps, axis=0)


num_steps = position.shape[0]

start_position = position[0]
final_position = position[-1]

total_dis = np.sum(np.linalg.norm(steps, axis=1))
displacement = np.linalg.norm(final_position - start)

average_X = np.mean(position[:, 0])
average_Y = np.mean(position[:, 1])

furthest_point = np.argmax(position)


#gps noise
noise = np.random.normal(0, 0.0001, position.shape)

noisy_gps = position + noise

gps_error = np.linalg.norm(position - noisy_gps, axis=1)
average_error = np.mean(gps_error)
max_gps_error = np.max(gps_error)
min_gps_error = np.min(gps_error)
std_dev_gps_error = np.std(gps_error)


print("====== IRG RUNNER SIMULATOR ======")
print("   ")
print("Number of steps: ", num_steps)
print("   ")
print("Starting position: ", start_position)
print("Final position: ", final_position)
print("   ")
print("Total distance traveled: ", total_dis)
print("Displacement: ", displacement)
print("     ")
print("Average X: ", average_X)
print("Average Y: ", average_Y)
print("     ")
print("Furthest point: ", furthest_point)
print("     ")
print("Average GPS error: ", average_error)
print("Max GPS error: ", max_gps_error)
print("Min GPS error: ", min_gps_error)
print("     ")    
print("Standard Deviation of GPS error: ", std_dev_gps_error)     