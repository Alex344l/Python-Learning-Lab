import pandas as pd
import numpy as np

data = pd.read_csv("p1.csv")

coords = pd.DataFrame({
    "latitude": data["latitude"],
    "longitude": data["longitude"]
})

coord_arr = coords.to_numpy()

#Direction
def find_heading(start, end):

    start = np.radians(start)
    end = np.radians(end)
    
    delta_lon = end[:, 1] - start[:, 1]

    x = np.cos(end[:, 0]) * np.sin(delta_lon)
    y = np.cos(start[:, 0]) * np.sin(end[:, 0]) - np.sin(start[:, 0]) * np.cos(end[:, 0]) * np.cos(delta_lon)

    bearing = np.arctan2(x, y)
    return np.degrees(bearing) % 360

position_1 = coord_arr[:-1]
position_end = coord_arr[1:]
    
bearing = find_heading(position_1, position_end)


def find_bearing(heading):

    results = []

    cardinals = {
        0: "N",
        360: "N",
        90: "E",
        180: "S",
        270: "W"
    }

    for h in heading:

        if h < 0 or h > 360:
            result = "Not Valid"
        elif h in [0, 90, 180, 270, 360]:
            result = cardinals[h]
        else:
            if h < 90 or h > 270:
                point1 = "N"

                if h < 90:
                    point2 = "E"
                    degree = h
                else: 
                    point2 = "W"
                    degree = 360 - h
                    
            elif 270 > h > 90:
                point1 = "S"

                if 180 > h > 90:
                    point2 = "E"
                    degree = 180 - h
                elif 270 > h > 180:
                    point2 = "W"
                    degree = h - 180

            degree = round(degree, 3)
            result = point1 + str(degree) + point2

        results.append(result)

    return results

quadrant_bearing = find_bearing(bearing)

#distance
def find_distance(coordinates):

    radius = 6371000

    coords_rad = np.radians(coordinates)

    lats = coords_rad[:, 0]
    lons = coords_rad[:, 1]

    lat_diff = np.diff(lats)
    lons_diff = np.diff(lons)

    a = np.sin(lat_diff / 2) ** 2 + np.cos(lats[:-1]) * np.cos(lats[1:]) * np.sin(lons_diff / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    distance = c * radius
    return distance

distances = find_distance(coord_arr)




heading = pd.DataFrame({
    "heading": bearing.round(3),
    "bearing": quadrant_bearing,
    "Distance": distances
})

heading.index = pd.RangeIndex(start=1, stop=len(heading) + 1, name="Index")

print(heading.head(10))
