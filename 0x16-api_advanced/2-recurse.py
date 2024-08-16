#!/usr/bin/python3
"""
Uses recursion to query a Reddit API and return  list of titles of all hot
articles for a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursiely queries the reddit API and returns a list of all articles for a
    given subreddit.

    - subreddit: subreddit to query
    - hot_list: list to store titles for hot articles (used for recursion)
    - after: ID of th last post n the current page (used for pagination)

    Returns:
    - List of titles of hot articles, or None if the subreddit is invalid. 
    """
    # Define the URL subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json" 

    # Define a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': "myRedditBot/0.0.1"}

    # Parameters to handle pagination
    params = {'limit': 100, 'after': after}

    try:
        # Send a get request to the Reddit API
        response = requests.get(
            url=url,
            headers=headers,
            params=params,
            allow_redirects=False
            )

        # Check if the status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']

            # Append titles of hot posts to hot_list
            hot_list.extend([post['data']['title'] for post in posts])

            # If 'after' is None, the end of the pagination has been reached
            if after is None:
                return hot_list
            else:
                # Recursively call the function to get the next page
                return recurse(subreddit, hot_list, after)
        else:
            # Return None if the subreddit is invalid
            return None
    except requests.RequestException:
        # Return None in case of any request exceptions
        return None
