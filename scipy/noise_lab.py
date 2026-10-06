import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from scipy.stats import norm


# ================================
# LOAD DATA
# ================================

df = pd.read_csv("error_lab_files/02_gps_variable_noise.csv")

coordinates = pd.DataFrame({
    "latitude": df["latitude"],
    "longitude": df["longitude"]
}).to_numpy()


# ================================
# LOCAL VARIABILITY
# ================================

window = 3
local_variabilities = []


for i in range(len(coordinates) - window + 1):

    window_data = coordinates[i:i + window]

    local_std = np.std(window_data, axis=0)

    local_variability = np.linalg.norm(local_std)

    local_variabilities.append(local_variability)


local_variabilities = np.array(local_variabilities)


low_threshold = np.percentile(local_variabilities, 50)
high_threshold = np.percentile(local_variabilities, 90)

filter_windows = []

for variability in local_variabilities:

    if variability < low_threshold:
        window = 3
    elif variability < high_threshold:
        window = 5
    else: 
        window = 7

    filter_windows.append(window)
filter_windows = np.array(filter_windows)


filtered_coords = []


for i in range(len(coordinates)):

    variability_index = min(i, len(local_variabilities) - 1)

    variability = local_variabilities[variability_index]

    filter_window = filter_windows[variability_index]

    # Make sure the window doesn't go outside the dataset
    start = max(0, i - filter_window // 2)
    end = min(len(coordinates), i + filter_window // 2 + 1)

    local_data = coordinates[start:end]

    # Average latitude and longitude separately
    filtered_point = np.mean(local_data, axis=0)

    filtered_coords.append(filtered_point)


filtered_coords = np.array(filtered_coords)

errors = np.linalg.norm(filtered_coords - coordinates, axis=1)

density = norm.pdf(errors)

    

fig, ax = plt.subplots()

# Histogram
ax.hist(
    errors,
    bins=15,
    density=True,
    alpha=0.35,
    color="#ff6b6b",
    edgecolor="none"
)
ax.axvline(
    np.median(errors),
    linestyle="--",
    color="#4dead1",
    label="median"
)
ax.axvline(
    np.mean(errors),
    linestyle="--",
    color="#3d49ea",
    label="mean"
)

# KDE
kde = gaussian_kde(errors)

x = np.linspace(errors.min(), errors.max(), 500)
y = kde(x)

ax.plot(
    x,
    y,
    color="#a10bc7",
    linewidth=2
)

ax.fill_between(
    x,
    y,
    alpha=0.35,
    color="#ff3f3f"
)

ax.set_title("GPS Error Distribution")
ax.set_xlabel("GPS Error")
ax.set_ylabel("Density")
ax.legend()

plt.show()

