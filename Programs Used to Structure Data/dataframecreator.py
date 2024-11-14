import pandas as pd
import json

filename = 'combine.json'

# Read the JSON file into a Python object (list of dictionaries or dictionary)
with open(filename, 'r') as file:
    data = json.load(file)

print(data)
# Convert the Python object into a DataFrame
# newframe = pd.DataFrame(data)

# Print the DataFrame
# print(newframe)