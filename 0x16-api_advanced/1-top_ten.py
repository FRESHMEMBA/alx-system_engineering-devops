#!/usr/bin/python3
"""
Queries the Reddit API and prints the title of the first 10 hot posts listed
for a given subreddit.

Requirements:
    Prototype: def top_ten(subreddit)
    If not a valid subreddit, print None
    NOTE: Invalid subreddits may return a redirect to search results.
        Ensure that you are not following redirects.
"""

import requests

def top_ten(subreddit):
    """
    Prints the title of the firts 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    # Define the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Define a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditBot/0.1.1'}

    try:
        # Send a get request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            # Extract the posts
            posts =  response.json()['data']['children']

            # Print the title of each post
            for post in posts:
                print(post['data']['title'])
        else:
            # Print None if the subreddit is invalid
            print(None)
    
    except requests.RequestException:
        # Print None in case of any request exception
        print(None)
