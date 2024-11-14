import pandas as pd
import re

def process_bot_reviews(input_csv, output_csv):
    # Read the input CSV file
    df = pd.read_csv(input_csv)

    # Create a list to store the processed data
    processed_data = []

    # Define a regular expression pattern to split at ', ' but not within quotes
    pattern = re.compile(r",\s*(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")

    # Iterate over each row in the dataframe
    for index, row in df.iterrows():
        botname = row['bot_name']
        review_str = row['text']

        # Remove brackets and split the string using regex
        review_str = review_str.strip('[]').replace("'", "").strip()
        reviews = pattern.split(review_str)

        # Remove any extra spaces or quotes around reviews
        reviews = [review.strip().strip('"') for review in reviews]

        label = row['label']

        # If there's more than one review, create a new row for each review
        if len(reviews) > 1:
            for i, review in enumerate(reviews):
                new_row = row.copy()
                new_row['text'] = review
                new_row['bot_name'] = f"{botname}_{i+1}"  # Append a suffix to create a new instance
                processed_data.append(new_row)
        else:
            row['text'] = reviews[0]
            processed_data.append(row)

    # Convert processed data back to DataFrame
    processed_df = pd.DataFrame(processed_data)

    # Write the processed data to the output CSV file
    processed_df.to_csv(output_csv, index=False)

# File paths
input_csv = 'processed_combined.csv'
output_csv = 'seperated.csv'

# Process the CSV file
process_bot_reviews(input_csv, output_csv)

print(f'Processed data has been saved to {output_csv}')
