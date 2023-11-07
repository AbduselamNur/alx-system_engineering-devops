#!/usr/bin/python3
"""Module prints the titles of the first 10 hot posts listed"""
import requests


def top_ten(subreddit):
    """
    A function that queries the Reddit API
    and prints the titles of the first 10 hot posts listed
    for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        print("None")
    else:
        data = res.json()
        res = data['data']['children']
        for title in res:
            print(title['data']['title'])
