import json

# Function to read JSON data from a file
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from {file_path} - {e}")
        return None
    except FileNotFoundError:
        print(f"Error: File not found {file_path}")
        return None

# Function to combine reviews without duplicates, filtering out short or invalid reviews
def combine_reviews(existing_reviews, new_reviews):
    review_set = {review.strip() for review in existing_reviews if len(review.strip()) > 1}
    new_valid_reviews = {review.strip() for review in new_reviews if len(review.strip()) > 1}
    review_set.update(new_valid_reviews)
    return list(review_set)

# Function to update initial data with new data
def update_data(initial_data, new_data):
    bot_name_to_data = {entry['bot_name']: entry for entry in initial_data}
    
    for new_entry in new_data:
        bot_name = new_entry.get('bot_name')
        new_reviews = new_entry.get('reviews', [])
        
        if bot_name in bot_name_to_data:
            combined_reviews = combine_reviews(bot_name_to_data[bot_name].get('reviews', []), new_reviews)
            bot_name_to_data[bot_name]['reviews'] = combined_reviews
    else:
         bot_name_to_data[bot_name] = new_entry
    
    return list(bot_name_to_data.values())

# Load initial and new JSON data
initial_data = load_json_file('flowgpt-reviews-labeled.json')
new_data = load_json_file('updated_data.json')

if initial_data is not None and new_data is not None:
    # Update the initial data with new data
    updated_data = update_data(initial_data, new_data)

    # Save the updated JSON data back to a file
    with open('combined.json', 'w') as f:
        json.dump(updated_data, f, indent=4)  # Save the data with indentation
    print("Reviews updated and saved to combined.json")
else:
    print("Error: Failed to load initial or new data.")
