import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




data = {
    "Name": ['John', 'Micheal', 'Axel', 'Alex', 'Nathan', 'Louis', 'denzel'],
    "Position": ['Cashier', 'Manager', 'Cook', 'Cleaner', 'Cook', 'Cashier', 'Cook'],
    "Wage": [17, 45, 25, 20, 25, 17, 25],
    "Workhours": [25, 40, 35, 40, 35, 20, 30],
    "Age": [17, 45, 30, 25, 27, 19, 32]
}

df = pd.DataFrame(data, index=[1, 2, 3, 4, 5, 6, 7])

df["Experience"] = ["N/A", 10, 3, 5, 20, 1, 2]


#New Row////////////////////////
new_row = pd.DataFrame([{"Name": 'Sandy', "Position": 'Cleaner', "Wage": 20, "Workhours": 30, "Age": 22, "Experience": 5}, 
                        {"Name": 'Sandra', "Position": 'Stocker', "Wage": 20, "Workhours": 20, "Age": 26, "Experience": 6}], 
                        index=[8, 9])

df = pd.concat([df, new_row])
print(df)