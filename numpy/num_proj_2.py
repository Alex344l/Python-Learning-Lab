import numpy as np

start = np.array([0.0, 0.0])

steps = np.random.uniform(2, -2, size=(100, 2))

path = start + np.cumsum(steps, axis=0)



#==========================Path==============================#
starting_position = path[0]
final_position = path[-1]

average_X = np.mean(path[:, 0])
average_Y = np.mean(path[:, 1])

minimum_X = np.min(path[:, 0])
maximum_X = np.max(path[:, 0])

minimum_Y = np.min(path[:, 1])
maximum_Y = np.max(path[:, 1])

#distance
displacement = np.linalg.norm(final_position - start)
path_distance = np.sum(np.linalg.norm(steps, axis=1))

#every consecutive distance
cons_dis = np.insert(np.cumsum(np.linalg.norm(steps, axis=1)), 0, 0.0)

furthest_distance = np.argmax(path)


#=========================GPS==============================#
noise = np.random.normal(0, 0.0001, path.shape)
gps_path = path + noise

gps_error = np.linalg.norm(path - gps_path, axis=1)

average_error = np.mean(gps_error)
maximum_error = np.max(gps_error)
minimum_error = np.min(gps_error)
std_error = np.std(gps_error)
worst_error = np.argmax(gps_error)
most_accurate = np.argmin(gps_error)


#################################################################
#window size 3
window = 3
weights = np.ones(window) /window

filtered_lat = np.convolve(gps_path[:,0], weights, mode='valid')
filtered_lon = np.convolve(gps_path[:, 1], weights, mode='valid')

filtered_gps = np.column_stack((filtered_lat, filtered_lon))
####################################################################



##############################################################
#=======================Speed==============================#
speeds = np.random.uniform(2, 7, size=(100,))


average_speed = np.mean(speeds)
maximum_speed = np.max(speeds)
minimum_speed = np.min(speeds)
high_speeds = speeds[speeds > 5.0]
std_speeds = np.std(speeds)

#converting from m/s to km/h
speeds_in_kmh = speeds * 3.6

sprint = speeds > 5.0

##############################################################
#=========================Coins==============================#
coins = np.random.uniform(2, -2, size=(20, 2))

#add a new axis to path so (path - coins) doesn't return ValueError
#because path and coins aren't the same shape, broadcating them would return error
coin_distance = np.linalg.norm(
    path[:, np.newaxis, :] - coins,
    axis=2
)

closest_distances_coins = np.min(coin_distance, axis=0)
nearest_coin = np.argmin(closest_distances_coins)

furthest_distance_coins = np.max(coin_distance, axis=0)
furthest_coin = np.argmin(furthest_distance_coins)

average_coin_distance = np.mean(closest_distances_coins)

coin_collected = closest_distances_coins <= 2

collected = np.sum(coin_collected)

coin_count = coins.shape[0]

percentage_collected = (collected / coin_count) * 100
percentage_collected_round = np.round(percentage_collected, 2)


#########################################################
#====================Checkpoints========================#
checkpoints = np.array([
    [5, -5],
    [-10, 15],
    [20, -5]
])

#calculate the closest distance from each checkpoint to the path
closest_distances_checkpoints = np.min(np.linalg.norm(path[:, np.newaxis, :] - checkpoints, axis=2), axis=0)
#check on whether the checkpoint was reached or not
checkpoint_reached = closest_distances_checkpoints <= 3







print(displacement)
print(path_distance)
print(average_error, maximum_error, minimum_error, std_error, worst_error)
print(coin_distance)
print(nearest_coin)
print(collected,"/", coin_count)
print(percentage_collected_round,"%")


