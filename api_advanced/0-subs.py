#!/usr/bin/python3
"""Query the Reddit API for a subreddit's subscriber count."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a subreddit, or 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python:alu-scripting:v1.0 (by /u/vchina-star)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    return data.get("subscribers")
