import pandas as pd

data = pd.read_csv("p1.csv")
heading = data["heading_deg"]


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

bearing_calc = pd.DataFrame({
    "Heading": heading,
    "Bearing": bearing
})
bearing_calc.index = pd.RangeIndex(start=1, stop=len(bearing_calc) + 1, name="Index")

print(bearing_calc.head(10))

