#!/usr/bin/python3
"""Recursively count keyword occurrences in hot post titles."""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """Print a sorted count of keywords found in hot post titles."""
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced:v1.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "").lower()
        for word in title.split():
            if word in counts:
                counts[word] += 1

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, counts, after)

    lowered = [word.lower() for word in word_list]
    results = []
    for word in set(lowered):
        total = counts.get(word, 0) * lowered.count(word)
        if total > 0:
            results.append((word, total))

    results.sort(key=lambda pair: (-pair[1], pair[0]))
    for word, total in results:
        print("{}: {}".format(word, total))
