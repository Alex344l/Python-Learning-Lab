import numpy as np
import matplotlib

start = np.array([0.0, 0.0])



movement = np.random.uniform(2.0, -1.0, size=(1000, 2)) 

position = start + np.cumsum(movement, axis=0)

speeds = np.random.uniform(2.0, 8.0, size=(100,))


average_speed = np.mean(speeds)
fastest_speed = np.max(speeds)
slowest_speed = np.min(speeds)

#return speed above 6
above_6 = speeds[speeds > 6]
stand = np.std(speeds)


gps = np.array([
    [40.7128, -74.0060],
    [40.7130, -74.0055],
    [40.7134, -74.0050],
    [40.7140, -74.0045],
    [40.7145, -74.0040]
])

starting_loc = gps[0]
ending_loc = gps[-1]
average_lattitude = np.mean(gps[:, 0])
average_longitude = np.mean(gps[:, 1])
southernmost = np.argmin(gps[:, 0])
northernmost = np.argmax(gps[:, 0])

noise = np.random.normal(0, 0.0001, gps.shape)

noisy_gps = gps + noise

diff = np.abs(gps - noisy_gps)

#window size of 3
window = 3
weights = np.ones(window) / window

#Apply to latitude (colum 0) and longitude (column 1) smoothly
filtered_lat = np.convolve(noisy_gps[:, 0], weights, mode='valid')
filtered_lon = np.convolve(noisy_gps[:, 1], weights, mode='valid')

filtered_gps = np.column_stack((filtered_lat, filtered_lon))


#distance betweem each movements
step_distance = np.linalg.norm(movement, axis=1)

#Great for calculating distance between checkpoints
cumulative_distance = np.insert(np.cumsum(step_distance), 0, 0.0)

#distance from start ----> finish : current radius and doesn't account for turns or path
displacement = np.linalg.norm(ending_loc - start)

#path distance : take account for each turn
total_dis = np.sum(step_distance)

final_position = position[1]
first_position = position[0]

furthest = np.argmax(position)

#print(position)
#print(step_distance)
#print(cumulative_distance)
print(displacement)
print(total_dis)
print(first_position, final_position)
print(furthest)
print("///////////////////////////////////////////////")
print(average_speed)
print(fastest_speed)
print(slowest_speed)
print(above_6)
print(stand)
print("////////////////////////////////////////////////")
#print(noise)
print(filtered_gps)