import pandas as pd

def word_frequencies(text):
    # Tokenize the text into words
    words = text.split()
    
    # Create a DataFrame with words
    df = pd.DataFrame(words, columns=['word'])
    
    # Count the frequency of each word
    word_counts = df['word'].value_counts().reset_index()
    word_counts.columns = ['word', 'frequency']
    
    return word_counts

# Example usage
with open('text_document.txt', 'r') as file:
    text = file.read()

word_counts_df = word_frequencies(text)

print("Word Frequencies DataFrame:")
word_counts_df.to_csv('word_frequencies.csv', index=False)
