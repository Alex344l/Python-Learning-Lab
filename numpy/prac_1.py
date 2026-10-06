import numpy as np


position = np.array([
    [0, 0],
    [2, 3],
    [5, 4],
    [8, 7],
    [10, 10]
])

speed = np.array([4.2, 5.1, 6.3, 3.8, 7.2, 5.7])


movement = np.array([5, -3])

#new_position = position + movement

number_of_rows = position.shape[0]

x_position = position[:, 0]
y_position = position[:, 1]

first_position = position[0]
final_position = position[-1]

distance = np.linalg.norm(final_position - first_position)

print(speed >= 5)

    


print("X positions:", x_position, "Y positions:", y_position)
print("First position:", first_position)
print("Number of positions:", number_of_rows)
print("Distance:", distance)
print("Final position:", final_position)
print(position.ndim)

#print("Original position:", position)

#print("New position:", new_position)

