import requests

def fetch_trending_hashtags(top):
    # Set up the API endpoint and query parameters
    endpoint = 'https://api.ritekit.com/v1/search/trending'
    params = {
        'green': 1,
        'limit': top
    }

    # Make a GET request to the RiteKit API to fetch the top ten trending hashtags
    response = requests.get(endpoint, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the trending hashtags from the response
        trending_hashtags = [tag for tag in response.json()['tags']]

        tag_list = []
        for tag in sort_by_retweets(trending_hashtags):
            if len(tag['tag']) < 6: 
                tag_list.append("#" + tag['tag'])

        unique_tags = list(set(tag_list))

        # Return the top ten trending hashtags
        return unique_tags
    else:
        # Handle the case where the request was unsuccessful
        print(f'Error fetching trending hashtags: {response.status_code}')
        return []

def sort_by_retweets(data):
    """
    Sorts a list of objects by their 'retweets' value in descending order.
    
    :param list_of_objects: A list of objects with a 'retweets' attribute.
    :return: A sorted list of objects.
    """
    sorted_data = sorted(data, key=lambda k: k['retweets'], reverse=True)
    return sorted_data
