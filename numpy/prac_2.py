import numpy as np


gps = np.array([
    [10.0, 20.0],
    [10.2, 20.3],
    [10.5, 20.7],
    [10.9, 21.0],
    [11.2, 21.4]
])


latitude = gps[:, 0]
longitude = gps[:,1]

start_position = gps[0]
final_position = gps[-1]

average_latitude = np.average(np.round(latitude))
average_longitude = np.average(np.round(longitude))

minimum_latitude = np.min(latitude)
maximum_longitude = np.max(longitude)

noise = np.random.normal(0, 0.1, gps.shape)
accurate_data = gps - noise

print("Latitude: ", latitude)
print("Longitude: ", longitude)
print("Start position: ", start_position)
print("Final position: ", final_position)
print("Average latitude: ", average_latitude)
print("Average longitude: ", average_longitude)
print("Minimum latitude: ", minimum_latitude)
print("Maximum longitude: ", maximum_longitude)

print("GPS data: ", gps)
print("Acurate data: ", accurate_data)
