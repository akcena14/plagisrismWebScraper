import googlesearch
import requests
from bs4 import BeautifulSoup

# Read text file
with open('input.txt', 'r') as file:
    text = file.read()

# Tokenize text based on full stops
sentences = text.split('.')

# Set up Google Search API parameters
params = {
    "num": 1,  # Number of search results to retrieve (in this case, only the first result)
    "start": 0,  # Starting point of search results (default is 0)
}

# Use the Google Search API to retrieve search results for each sentence
results_dict = {}  # Dictionary to store URLs for each query
for sentence in sentences:
    sentence = sentence.strip()  # Remove any leading/trailing whitespace
    if sentence:  # Ignore empty sentences
        query = f'"{sentence}"'  # Set query parameter for current sentence in quotes
        params['q'] = query
        search_results = list(googlesearch.search(query, num_results=1))  # Retrieve search results
        if search_results:  # If results were found, retrieve the HTML soup for the first result
            url = search_results[0]
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            if sentence.lower() in soup.text.lower():  # Check if query is in soup
                results_dict[query] = url  # Store URL for query
            else:
                results_dict[query] = None  # Store None for query if not found
        else:  # If no results were found, store None for query
            results_dict[query] = None

# Print results
for query, url in results_dict.items():
    if url:
        print(f"Query '{query}' found in soup for URL: {url}\n")
    else:
        print(f"Query '{query}' not found in any soup\n")
