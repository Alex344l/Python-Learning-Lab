import numpy as np

temperature = np.array([-5, 72, 75, 71, 68, 77, 80, 74, 15, 10, 0, -15, -30])

speed_ms = np.array([4.5, 4.8, 5.1, 5.7, 6.0])

positions = np.array([
        [0, 0],
        [2, 1],
        [4, 3],
        [7, 5],
        [9, 8]
])


speed_kmh = speed_ms * 3.6
average_speed_kmh = np.mean(speed_kmh)
std_deviation_speed = np.std(speed_kmh)
max_speed = np.max(speed_kmh)
min_speed = np.min(speed_kmh)



highest_temperature = np.max(temperature)
lowest_temperature = np.min(temperature)
average_temperature = np.mean(temperature)
temperature_changes = temperature.shape[0]
temp_size = temperature.size
temp_heat = temperature[temperature > 75]
extreme_cold = temperature[temperature <= 0]
decent_temp = temperature[(temperature >= 50) & (temperature <= 75)]



number_of_positions = positions.shape[0]
starting_posions = positions[0]
final_positions = positions[1]
X_coordinates = positions[:, 0]
Y_coordinates = positions[:, 1]
average_x = np.mean(X_coordinates)
average_y = np.mean(Y_coordinates)
distances = np.linalg.norm(positions, axis=1)
furthest = np.argmax(positions)


print("---------------------------------------------------")
print("---------------------------------------------------")
print("speed in m/s: ", speed_ms)
print("Speed in Km/h: ", speed_kmh)
print("Average speed in km/h: ", average_speed_kmh)
print("acceleration: ", std_deviation_speed)
print("Max speed: ", max_speed)
print("Min speed: ", min_speed)
print("---------------------------------------------------")
print("///////////////////////////////////////////////////")
print("---------------------------------------------------")
print("Highest temperature: ", highest_temperature)
print("Lowest temperature: ", lowest_temperature)
print("Average temperature: ", average_temperature)
print("Temp above 75: ", temp_heat)
print("Number of temp: ", temp_size)
print("Extreme Cold: ", extreme_cold)
print("Stable temp: ", decent_temp)
print("---------------------------------------------------")
print("///////////////////////////////////////////////////")
print("---------------------------------------------------")
print("Number of positions: ", number_of_positions)
print("Starting positions: ", starting_posions)
print("Final positions: ", final_positions)
print("X coordinates: ", X_coordinates)
print("Y coordinates: ", Y_coordinates)
print("Average X values: ", average_x)
print("Average Y values: ", average_y)
print("Distance: ", np.round(distances))
print("Furthest from the starting point: ", furthest)
print("---------------------------------------------------")
print("---------------------------------------------------")

