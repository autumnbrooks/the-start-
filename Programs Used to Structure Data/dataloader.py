import pandas as pd
import json

# File paths
filename = 'combined.json'
csvfile = 'combined.csv'

# Read the JSON file into a Python object (list of dictionaries or dictionary)
with open(filename, 'r') as file:
    data = json.load(file)

# Convert the Python object into a DataFrame
newframe = pd.DataFrame(data)

newframe['labelByHuman'] = newframe['labelByHuman'].astype("string").str.lower().fillna('none')

# Check unique values after conversion
print(newframe['labelByHuman'].unique())

# Define the conversion function to handle lowercase values
def convert_label(label):
    if label == 'true':
        return 1
    elif label == 'false' or label == 'none':
        return 0
    else:
        return None

# Apply the conversion function to create the 'label' column
newframe['label'] = newframe['labelByHuman'].apply(convert_label)


# Save the DataFrame to a CSV file
newframe.to_csv(csvfile, index=False)

# Read the CSV file into a DataFrame
df = pd.read_csv(csvfile)


# Keep 'reviews', 'bot_name', and the new 'label' column
df = df[['reviews', 'bot_name', 'label']]

# Rename columns to match the desired output format
df.columns = ['text', 'bot_name', 'label']

# Save the processed DataFrame to a new CSV file
df.to_csv('processed_combined.csv', index=False)

print(df.head())

