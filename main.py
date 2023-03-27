from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Enter your custom search engine ID and API key here
SEARCH_ENGINE_ID = '05a0718899f664fda'
API_KEY = 'AIzaSyAe34tm9-Og0El5ISwScopDSlYspE-XwO0'


def search_and_store_first_url(query):
    """
    Searches a query on a custom Google search engine and stores the first URL.

    :param query: The query to search for.
    :return: A dictionary containing the search results, with the query as the key.
    """
    search = f'"{query}"'

    # Build the service object for the Custom Search JSON API
    service = build('customsearch', 'v1', developerKey=API_KEY)

    # Perform the search request and store the first URL in a dictionary with the query as the key
    try:
        response = service.cse().list(q=search, cx=SEARCH_ENGINE_ID, num=1).execute()
        if 'items' in response:
            first_url = response['items'][0]['link']
            result_dict = {query: first_url}
        else:
            result_dict = {query: None}
    except HttpError as error:
        print(f'An error occurred: {error}')
        result_dict = {query: None}

    # Return the first URL from the search results
    return result_dict

# Test the function with a sample query


query1 = 'In 2015, the University of Birmingham conducted a carbon dating analysis of a Quranic manuscript known as the "Birmingham Quran".'
query2 = 'machine learning'
result_dict = {}

result_dict.update(search_and_store_first_url(query1))
result_dict.update(search_and_store_first_url(query2))

filename = 'input.txt'
with open(filename, 'r', encoding='utf-8') as f:
    data = f.read()  # Read the entire file into a string variable

sentences = data.split('.')  # Split the string into sentences based on full stops

for sentence in sentences:
    result_dict.update(search_and_store_first_url(sentence))

print(result_dict)
