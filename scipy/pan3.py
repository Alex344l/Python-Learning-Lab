import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import circmean



def load_data(file_path):

    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


data = load_data("p1.csv")

def clean_data(data):

    """
    Clean the data by removing rows with missing values.

    Parameters:
    data (pd.DataFrame): The DataFrame to clean.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """

    data = data.dropna()
    data = data.drop_duplicates()


    for column in data.columns:

        if data[column].dtype == 'object':
            data[column] = data[column].str.strip()
            data[column] = data[column].astype("category")

        elif data[column].dtype in ['int64', 'float64']:
            data[column] = data[column].fillna(data[column].median())

        else:
            pass

    data = data.dropna()
    data = data.reset_index(drop=True)

    return data


data = clean_data(data)
data.index = pd.RangeIndex(start=1, stop=len(data) + 1, name='Index')


#Weather data
temp = data["temperature_c"] * 9/5 + 32
pressure_psi = data["pressure_hpa"] * 0.000145038
humidity = data["humidity_pct"]

date_time = pd.to_datetime(data["timestamp"])
date = date_time.dt.date
time = date_time.dt.time    

pressure_diff = pressure_psi.diff()
temp_diff = temp.diff()
humidity_diff = humidity.diff()



def rem_NaN(*args):
    return [arg.fillna(0) for arg in args]

temp, pressure_psi, humidity, temp_diff, pressure_diff, humidity_diff = rem_NaN(temp, pressure_psi, humidity, temp_diff, pressure_diff, humidity_diff)



weather_telemetry = pd.DataFrame({
    "Date": date,
    "Time": time, 
    "Temperature (F)": temp, 
    "Temperature Change (F)": temp_diff,
    "Pressure (psi)": pressure_psi,
    "Pressure Change (psi)": pressure_diff,
    "Humidity (%)": humidity,
    "Humidity Change (%)": humidity_diff
})


coordinates = pd.DataFrame({
    "Latitude": data["latitude"],
    "Longitude": data["longitude"]
})

coords = coordinates.to_numpy()


first_position = coords[0]
final_position = coords[-1]


average_latitude = np.mean(coords[:, 0])
average_longitude = np.mean(coords[:, 1])

average_position = np.array([average_latitude, average_longitude])


#Haversine formula to calculate distance between two coordinates
def find_distance(coors):

    """
    Calculate the distance between consecutive coordinates using the Haversine formula.

    Parameters:
    coors (np.ndarray): An array of coordinates (latitude, longitude).

    Returns:
    np.ndarray: An array of distances between consecutive coordinates.
    """

    coords_rad = np.radians(coors)
    lats = coords_rad[:, 0]
    lons = coords_rad[:, 1]

    radius_miles = 3959

    lat_dif = np.diff(lats)
    lon_dif = np.diff(lons)

    a = np.sin(lat_dif / 2) ** 2 + np.cos(lats[:-1]) * np.cos(lats[1:]) * np.sin(lon_dif / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    distances = radius_miles * c

    lat_dif_disp = lats[-1] - lats[0]
    lon_dif_disp = lons[-1] - lons[0]

    a_disp = np.sin(lat_dif_disp / 2) ** 2 + np.cos(lats[0]) * np.cos(lats[-1]) * np.sin(lon_dif_disp / 2) ** 2
    c_disp = 2 * np.arctan2(np.sqrt(a_disp), np.sqrt(1 - a_disp))

    displacement = radius_miles * c_disp

    return distances, displacement


distances, displacement = find_distance(coords)

#adding 0 at index 0 to represent the starting point of the journey
distances = np.insert(distances, 0, 0)

cons_distances = np.cumsum(distances)


#speed calculation
dt = date_time.diff().dt.total_seconds().fillna(0).to_numpy()
dt = dt / 3600  # Convert seconds to hours

#velocity = distances / dt
velocity = np.divide(distances, dt, out=np.zeros_like(distances), where=dt!=0)

total_distance = np.sum(distances)
path_ratio = displacement / total_distance

average_velocity = np.mean(velocity)

#direction
heading = data["heading_deg"]


#Quadrant bearing
def find_quadrant_bearing(heading):

    results = []

    cardinal = {
        90: "E",
        180: "S",
        270: "W",
        360: "N",
        0: "N"
    }

    for h in heading:

        if h < 0 or h > 360:
            result = "Not valid"

        elif h in [90, 180, 270, 360, 0]:
            result = cardinal[h]

        else:

            if h < 90 or h > 270:
                point_1 = "N"
                if(h < 90):
                   point_2 = "E"
                   degree = h
                elif h > 270:
                   point_2 = "W"
                   degree = 360 - h
                else:
                   print("NaN")

            elif 270 > h > 90:
                point_1 = "S"
                if 180 > h > 90:
                    point_2 = "E"
                    degree = 180 - h
                elif 180 < h < 270:
                    point_2 = "W"
                    degree = h - 180
                else: 
                    print("NaN")
            else:
                print("NaN")

            degree = round(degree, 4)
            result = point_1 + str(degree) + point_2

        results.append(result)

    return results


bearing = find_quadrant_bearing(heading)        


direction_telemetry = pd.DataFrame({
    "Time": time,
    "Consecutive distance (meters)": cons_distances * 1609.34,
    "Heading (degrees)": heading,
    "Bearing": bearing
})


direction_telemetry["Heading Changes"] = rem_NaN(direction_telemetry["Heading (degrees)"].diff())[0]
#direction["Heading Changes"] = rem_NaN(direction["Heading Changes"])[0]

#FInding the average heading using scipy
average_heading = circmean(
    direction_telemetry["Heading (degrees)"], 
    high=360,
    low=0
)


trun_treshold = 25  # Example threshold, adjust as needed

direction_telemetry["Turn"] = direction_telemetry["Heading Changes"].apply(lambda x:
                                "Turn" if abs(x) > trun_treshold 
                                        else "Straight")

#overall_direction = 
most_common_direction = direction_telemetry["Bearing"].mode()[0]
start_bearing = bearing[0]
final_bearing = bearing[-1]

max_heading_change = direction_telemetry["Heading Changes"].abs().max()

movement_telemetry = pd.DataFrame({
    "Date": date,
    "Time": time,
    "Latitude": coords[:, 0],
    "Longitude": coords[:, 1],
    "Distance per steps (miles)": distances,
    "Consecutive Distance (miles)": cons_distances,
    "Velocity (mile/hour)": velocity

})


mo_telemetry = pd.DataFrame({
    "total_distance (miles)": [total_distance],
    "average_velocity (mile/hour)": [average_velocity],
    "displacement (miles)": [displacement],
    "Path Ratio": [path_ratio],
    #"Overall Direction": [overall_direction],
    "Most Common Direction": [most_common_direction],
    "Start": [start_bearing],
    "End": [final_bearing]
})


weather_telemetry.index = pd.RangeIndex(start=1, stop=len(weather_telemetry) + 1, name='Index')



"""

output_files = {
    "weather_telemetry.csv": weather_telemetry,
    "movement_telemetry.csv": movement_telemetry,
    "Movement_Overview_telemerty.csv": mo_telemetry,
    "Direction_telemetry.csv": direction
}


for filename, df in output_files.items():
    df.to_csv(filename, index=True)

"""



print("Weather Telemetry DataFrame:")
print(weather_telemetry.head(10).to_string())
print("\nMovement Telemetry DataFrame:")
print(movement_telemetry.head(10).to_string())
print("\n Movement Overview Telemetry DataFrame:")
print(mo_telemetry.to_string(index=False))
print("\n Direction Telemetry DataFrame:")
print(direction_telemetry.head(10).to_string())



"""
figure, axes = plt.subplots(
    3, 2,
    figsize=(10, 10),
    gridspec_kw={"wspace": 0.20, "hspace": 0.30})

figure.suptitle( 
    "RUNING VISUALISATION",
    fontweight = "bold",
    fontsize = 22,
    color = "#805cca",
    y = 0.98
)

figure.text(
    0.05, 0.925,
    "GPS * IMU * ROUTING * WEATHER",
    fontweight = "bold",
    fontsize = 12,
    color = "#bea0fa",
    ha = "left"
)

figure.text(
    0.95, 0.945,
    "* LIVE",
    fontsize = 11,
    fontweight = "bold",
    color = "#ff3471",
    ha = "right"
)

figure.patch.set_facecolor("#b4f7f3")

for ax in axes.flat:
    ax.set_facecolor("#f3deaf")

    for spine in ax.spines.values():
        spine.set_color("#0aefff")
        spine.set_linewidth(1)

axes[0, 0].plot(coords[:, 1], coords[:, 0], color="#ff640a", linewidth=2)
axes[0, 0].scatter(coords[:1, 1], coords[:1, 0], s=50, color="blue")
axes[0, 0].scatter(coords[-1:, 1], coords[-1:, 0], s=50, color="red")
axes[0, 0].grid(True, which="both", linestyle="--", color="#e070e4", linewidth=1)
axes[0, 0].set_title("PATH", color="#da9d1a", fontweight="bold", fontsize=16)
axes[0, 0].set_xlabel("LONGITUDE", fontsize=13, fontweight="bold", color="#da9d1a")
axes[0, 0].set_ylabel("LATITUDE", fontsize=13, fontweight="bold", color="#da9d1a")
axes[0, 0].text(0, total_distance, f"{total_distance:.2f} miles", ha="left", va="top")


axes[0, 1].plot(velocity, color="#ff640a", linewidth=2)
axes[0, 1].axhline(y=np.mean(velocity), color="#5b2fd3", linewidth=2, linestyle="dotted")
#axes[0, 1].scatter(np.max(velocity), np.argmax(velocity), marker="o", s=60, color="#20da1a")
axes[0, 1].set_title("SPEED", fontsize=16, fontweight="bold", color="#da9d1a")
axes[0, 1].grid(True, which="both", linestyle="--", color="#e070e4", linewidth=1)




plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
"""
#/////////////////////////////////////////////////////////////
#Plotting








