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
from sys import argv


def top_ten(subreddit):
    """
    Prints the title of the firts 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    user = {'User-Agent': 'bot'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)

# if __name__ == "__main__":
#     top_ten(argv[1])
