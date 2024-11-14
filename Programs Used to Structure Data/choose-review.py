import pandas as pd

# Change the file name with your actual file name
file = "processed_reviews_with_sentiment.csv"

df = pd.read_csv(file)

def return_reviews_and_sentiment(bot_name):
    # Check if 'bot_name', 'text', and 'sentiment' columns exist
    if 'bot_name' not in df.columns or 'text' not in df.columns or 'sentiment' not in df.columns:
        return "Required columns are missing from the CSV file"
    
    # Find the row with the given bot-name
    row = df[df['bot_name'] == bot_name]
    
    if row.empty:
        return f"No entries found for bot-name: {bot_name}"
    
    # Get the review and sentiment from the row
    review = row['text'].values[0]
    sentiment = row['sentiment'].values[0]
    
    return review, sentiment

def get_positive_reviews(data):
    # Check if 'sentiment' and 'text' columns exist
    if 'sentiment' not in data.columns or 'text' not in data.columns or 'score' not in data.columns:
        return "Required columns are missing from the CSV file"

    # Filter reviews with positive sentiment
    positive_reviews = data[data['sentiment'] == 'positive']

    if positive_reviews.empty:
        return "No positive reviews found"

    # Get positive review texts and scores
    positive_texts = positive_reviews['text'].tolist()
    positive_scores = positive_reviews['score'].tolist()

    return list(zip(positive_texts, positive_scores))

# Example usage
unique_bot_names = df['bot_name'].unique()
for bot_name in unique_bot_names:
    result = return_reviews_and_sentiment(bot_name)
    print(f"Bot Name: {bot_name}, Review and Sentiment: {result}")

positive_reviews = get_positive_reviews(df)
print("Positive Reviews:")
for review, score in positive_reviews:
    print(f"Review: {review}, Score: {score}")
