import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "MyRedditClient/0.1 by yourusername"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        return 0

    try:
        results = response.json().get("data")
        if results:
            return results.get("subscribers", 0)
        else:
            return 0
    except requests.exceptions.JSONDecodeError:
        return 0

