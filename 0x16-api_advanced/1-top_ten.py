import requests

def top_ten(subreddit):
    '''
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    '''
    user = {'User-Agent': 'MyRedditClient/0.1 by yourusername'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    
    try:
        response = requests.get(url, headers=user, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code != 200:
            print(None)
            return
        
        data = response.json()
        
        # Check if the necessary keys are in the JSON response
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print(None)
    
    except requests.exceptions.RequestException:
        print(None)
    except ValueError:
        # Catch JSON decoding errors
        print(None)
