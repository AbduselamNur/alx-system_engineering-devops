#!/usr/bin/python3
"""
A module parses the title of all hot articles, and prints
A sorted count of given keywords"""
from collections import Counter
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords for a given subreddit.
    """
    headers = {'User-Agent': 'My-User-Agent'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)
        after = data['data']['after']
        if after is not None:
            return count_words(subreddit, word_list, hot_list, after)
        else:
            word_list = [word.lower() for word in word_list]
            word_count = Counter()
            for title in hot_list:
                words = title.lower().split()
                for word in word_list:
                    word_count[word] += words.count(word)
            word_count = sorted(word_count.items(),
                                key=lambda x: (-x[1], x[0]))
            for word, count in word_count:
                if count > 0:
                    print("{}: {}".format(word, count))
                return hot_list
    else:
        return None
