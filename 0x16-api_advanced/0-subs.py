#!/usr/bin/python3
"""Module That Return The Total subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    a function that queries the Reddit API
    and returns the number of subscribers
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    else:
        data = res.json()
        sub = data['data']['subscribers']
        return sub
