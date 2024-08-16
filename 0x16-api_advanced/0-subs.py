#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests,
ensure you’re setting a custom User-Agent.

Requirements:

Prototype: def number_of_subscribers(subreddit)
If not a valid subreddit, return 0.
NOTE: Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.
"""


import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    # Define the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Define a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditBot/0.0.1'}

    try:
        # Send a get request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            # Extract and return the number of subscribers
            return response.json()['data']['subscribers']
        else:
            # Return 0 if the subreddit is invalid
            return 0
    
    except requests.RequestException:
        # Return 0 in case of any request exception
        return 0
