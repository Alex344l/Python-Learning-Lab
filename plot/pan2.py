import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("p1.csv")


#datetime
datetime = np.array([df["timestamp"]])

datetime = pd.to_datetime(df["timestamp"])
df["date"] = datetime.dt.date
df["time"] = datetime.dt.time

dt = datetime.diff().dt.total_seconds()


#Coordinates
coords = pd.DataFrame({
   "latitude": df["latitude"],
   "longitude": df["longitude"]
})

coords = coords.to_numpy()


#GPS Error
noise = np.random.normal(0, 0.0001, coords.shape)
gps_path = coords + noise
gps_errors = np.linalg.norm(coords - gps_path, axis=0)

gps_lat = gps_path[:, 0]
gps_lon = gps_path[:, 1]

average_error = np.mean(gps_errors)
maximum_error = np.max(gps_errors)
minimum_error = np.min(gps_errors)
std_error = np.std(gps_errors)

window = 3
weights = np.ones(window) / window

filtered_lat = np.convolve(gps_path[:, 0], weights, mode='valid')
filtered_lon = np.convolve(gps_path[:, 1], weights, mode='valid')
filtered_gps = np.column_stack((filtered_lat, filtered_lon))


latitudes = coords[0]
longitudes = coords[1]

Starting_position = coords[:, 0]
Final_position = coords[:, -1]

#distance 
#Haversine Formula
def find_distance(coord):

   coord_rad = np.radians(coord)
   lats = coord_rad[0]
   lons = coord_rad[1]


   radius_miles = 3959

   lat_dif = np.diff(lats)
   lon_dif = np.diff(lons)


 #Route distance 

   a_route = np.sin(lat_dif / 2) ** 2 + np.cos(lats[: -1]) * np.cos(lats[1:]) * np.sin(lon_dif / 2) ** 2
   c_route = 2 * np.arctan2(np.sqrt(a_route), np.sqrt(1 - a_route))
   
   Route_distance = np.sum(radius_miles * c_route)

 #Displacement
   dif_lat_disp = lats[-1] - lats[0]
   dif_lon_disp = lons[-1] - lons[0]

   a_disp = np.sin(dif_lat_disp / 2) ** 2 + np.cos(lats[0]) * np.cos(lats[-1]) * np.sin(dif_lon_disp / 2) ** 2
   c_disp = 2 * np.arctan2(np.sqrt(a_disp), np.sqrt(1 - a_disp))

   Displacement = radius_miles * c_disp



   return Route_distance, Displacement

movement = find_distance(filtered_gps)
movement2 = find_distance(coords)

distance = movement[0]
displacement = movement[1]
movement_ratio = displacement / distance

distance2 = movement2[0]
distance2 = movement2[1]

###################################################################
#Velocity Calculation
Velocity = distance / np.sum(dt)

average_velocity = np.mean(Velocity)
std_velocity = np.std(Velocity)
max_velocity = np.max(Velocity)
min_velocity = np.min(Velocity)

#///////////////////////////////////////////////////////////////////
#Weather Data
weather = np.array([
         df["temperature_c"],
         df["humidity_pct"],
         df["pressure_hpa"]
])

temp = weather[0]
humidity = weather[1]
pressure = weather[2]


print(filtered_gps)



#Ploting
figure, axes = plt.subplots(3, 2, figsize=(10, 10))

axes[0, 0].plot(gps_lat, gps_lon, color = "#ffda0a", linewidth=2, label="Coordinates")
axes[0, 0].scatter(gps_lat[0], gps_lon[0], marker='^', s=50, color="#32921a", label="Start")
axes[0, 0].scatter(gps_lat[-1], gps_lon[-1], marker="o", s=50, color="#3f0aff", label="End")
axes[0, 0].set_title("COORDINATES", fontsize=16, color="#4beaf0", fontweight='bold')
axes[0, 0].set_xlabel("LATITUDES", fontsize=12, color="#4beaf0", fontweight='bold')
axes[0, 0].set_ylabel("LONGITUDES", fontsize=12, color="#4beaf0", fontweight='bold')
axes[0, 0].grid(True, which='both', color="#4beaf0", linestyle='--', linewidth=1.5)
axes[0, 0].legend()

axes[0, 1].plot(filtered_lat, filtered_lon, color="#ff0af3", linewidth=2, label="Filterd Coordinates")
axes[0, 1].scatter(filtered_lat[0], filtered_lon[0], marker='^', s=50, color="#32921a", label="Start")
axes[0, 1].scatter(filtered_lat[-1], filtered_lon[-1], marker='o', s=50, color="#3f0aff", label="end")
axes[0, 1].grid(True, which='both', color="#4beaf0", linestyle='--', linewidth=1.5)

axes[1, 0].plot(filtered_gps, color="#4b0aff", label="GPS Error")
axes[1, 0].grid(True, which='both', color="#4beaf0", linestyle='--', linewidth=1.5)
axes[1, 0].set_title("GPS ERROR", fontsize=16, color="#4beaf0", fontweight='bold')
axes[1, 0].set_xlabel("TIMESTAMPS", fontsize=12, color="#4beaf0", fontweight='bold')
axes[1, 0].set_ylabel("ERROR", fontsize=12, color="#4beaf0", fontweight='bold')
axes[1, 0].legend()

axes[1, 1].plot(Velocity, color="#4b0aff", linewidth=1.5, label="Velocity")
axes[1, 1].set_title("VELOCITY", fontsize=16, color="#4beaf0", fontweight='bold')
axes[1, 1].set_xlabel("TIMESTAMPS", fontsize=12, color="#4beaf0", fontweight='bold')
axes[1, 1].set_ylabel("VELOCITY", fontsize=12, color="#4beaf0", fontweight='bold')
axes[1, 1].grid(True, which='both', color="#4beaf0", linestyle='--', linewidth=1.5)
axes[1, 1].legend()

axes[2, 0].plot(temp, color="#4b0aff", linewidth=1.5, label="Temperature")
axes[2, 0].set_title("TEMPERATURE", fontsize=16, color="#4beaf0", fontweight='bold')
axes[2, 0].set_xlabel("TIMESTAMPS", fontsize=12, color="#4beaf0", fontweight='bold')
axes[2, 0].set_ylabel("TEMPERATURE", fontsize=12, color="#4beaf0", fontweight='bold')
axes[2, 0].grid(True, which='both', color="#4beaf0", linestyle='--', linewidth=1.5)
axes[2, 0].legend()

print("Velocity:", Velocity)
print("Average Velocity:", average_velocity)
print("Standard Deviation of Velocity:", std_velocity)
print("Maximum Velocity:", max_velocity)
print("Minimum Velocity:", min_velocity)
plt.tight_layout()
plt.show()

#print(distance, displacement, movement_ratio)
#print(weather)