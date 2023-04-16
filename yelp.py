import requests

limit = 50
payload = {'location' : 'New York City', 'radius' : 40000, 'sort_by':'review_count', 'offset' : 1, 'limit': limit}

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer TODO_API_TOKEN"
}

filename = 'yelpBusinesses.json'
print('Calling the API')

max_results = 3000
i = 1
while i < max_results:

    payload['offset'] = i
    response = requests.get(url, headers=headers, params=payload, stream= True)

    with open(filename, 'ab') as fd:
        for chunk in response.iter_content(chunk_size=128):
            fd.write(chunk)
    
    i += limit


print('Saved to file.')