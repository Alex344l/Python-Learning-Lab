import numpy as np

position = np.array([0.0, 0.0])



steps = np.random.uniform(-2, 2, size=(10000, 2))

starting_position = np.array([0.0, 0.0])

position = position + np.cumsum(steps, axis=0)

number_of_steps = position.shape[0]
final_position = position[-1]

distance = np.linalg.norm(final_position - starting_position)

average_x = np.average(position[:, 0])
average_y = np.average(position[:, 1])

standard_deviation_x = np.std(position[:, 0])
standard_deviation_y = np.std(position[:, 1])

runner_simulation = {
    "number_of_steps": number_of_steps,
    "final_position": final_position,
    "distance": distance,
    "average_x": average_x,
    "average_y": average_y,
    "standard_deviation_x": standard_deviation_x,
    "standard_deviation_y": standard_deviation_y
}


print("Runner Simulation Results:")
print(f"Number of Steps: {runner_simulation['number_of_steps']}")
print(f"Final Position: {runner_simulation['final_position']}")
print(f"Distance from Starting Position: {runner_simulation['distance']}")
print(f"Average X Position: {runner_simulation['average_x']}")
print(f"Average Y Position: {runner_simulation['average_y']}")
print(f"Standard Deviation of X Position: {runner_simulation['standard_deviation_x']}")
print(f"Standard Deviation of Y Position: {runner_simulation['standard_deviation_y']}")