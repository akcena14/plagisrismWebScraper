from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Enter your custom search engine ID and API key here
SEARCH_ENGINE_ID = '05a0718899f664fda'
API_KEY = 'AIzaSyAe34tm9-Og0El5ISwScopDSlYspE-XwO0'


def search_and_store_first_url(queries):
    """
    Searches a list of queries on a custom Google search engine and stores the first URL for each query.

    :param queries: A list of queries to search for.
    :return: A dictionary containing the search results, with the queries as the keys.
    """

    # Build the service object for the Custom Search JSON API
    service = build('customsearch', 'v1', developerKey=API_KEY)

    # Initialize an empty dictionary to store the search results
    result_dict = {}

    # Perform the search request for each query and store the first URL in the dictionary with the query as the key
    for query in queries:
        #  adding qoutes to query for searching
        search = f'"{query}"'
        try:
            response = service.cse().list(q=search, cx=SEARCH_ENGINE_ID, num=1).execute()
            if 'items' in response:
                first_url = response['items'][0]['link']
                result_dict[query] = first_url
            else:
                print(f"No search results found for '{query}'")
                result_dict[query] = None
        except HttpError as error:
            print(f'An error occurred: {error}')
            result_dict[query] = None

    # Return the dictionary with the search results
    return result_dict

# Test the function with a sample query


filename = 'input.txt'
with open(filename, 'r', encoding='utf-8') as f:
    data = f.read()  # Read the entire file into a string variable

sentences = data.split('.')  # Split the string into sentences based on full stops
sentences.pop()
print(sentences)

result_dict = (search_and_store_first_url(sentences))  # call function and constantly update dictionary

print(result_dict)
