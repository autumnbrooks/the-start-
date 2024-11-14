import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv('processed_reviews_labeled.csv')

def convert_to_document(csvfile):
    
    if 'text' in csvfile:
        with open('text_document.txt', 'w') as f:
            for item in csvfile['text']:
                f.write(item + '\n')
    return "Document Created"


def perform_tfidf(input_file, output_file):
    # Read the text file
    with open(input_file, 'r') as file:
        documents = file.readlines()
    
    # Initialize the TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the documents
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Convert TF-IDF matrix to DataFrame
    df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
    
    # Save the DataFrame to a CSV file
    df_tfidf.to_csv(output_file, index=False)
    
    return "TF-IDF processing complete. Results saved to " + output_file

# Usage
input_file = 'text_document.txt'  # The input file containing text data
output_file = 'tfidf_results.csv'  # The output file to save the TF-IDF results

print(perform_tfidf(input_file, output_file))