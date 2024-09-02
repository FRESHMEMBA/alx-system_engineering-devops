#!/usr/bin/python3
"""
Defines a recursive function that queries the Reddit API,
and parses the title of all hot posts, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces)
"""


import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the /Reddit API, parses the titles of all hot articles,
    and counts the occurenece of specified keywords (case-insensitive)

    - subreddit: The subreddit to be queried.
    - word_list: A listof of keywords to count in the titles.
    - after: The 'after' paramter for pagination.
    -word_count: A dictionary to store counts of each keyword.

    The function prints the sorted count of keywords in descending order.
    followed by alphabetical order of ties.
    """
    # Set the base URL for the Reddit API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'myRedditBot/0.0.1'}
    params = {'limit': 100, 'after': after}

    try:
        # Send a get request to Reddit
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        # Check if the request is succesful
        if response.status_code != 200:
            return
        
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']

        # Normalize word_list to lowercase
        word_list = [word.lower() for word in word_list]

        # Count the occurences of each keyword in the titles
        for post in posts:
            title = post['data']['title'].lower().split()
            for word in word_list:
                word_count[word] = word_count.get(word, 0) + title.count(word)

        # If 'after' is None, we have reached the end of pagination
        if after is None:
            # Filter out words with a count of 0
            word_count = {k: v for k, v in word_count.items() if v > 0}

            # Sort by count (desc) and alphabetically (asc)
            sorted_word_count = sorted(
                word_count.items(),
                key=lambda item: (-item[1], item[0])
                )

            # Print the results
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
            return
        else:
            # continue to the next page
            return count_words(subreddit, word_list, after, word_count)
    except requests.RequestException:
        return
