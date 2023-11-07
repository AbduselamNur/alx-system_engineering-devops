#!/usr/bin/python3
"""Module prints the titles of the first 10 hot posts listed"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    A function that queries the Reddit API
    and prints the titles of the first 10 hot posts listed
    for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    params = {'after': after, 'limit': 100}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        res = data['data']['children']
        for title in res:
            post = title['data']['title']
            hot_list.append(post)
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
