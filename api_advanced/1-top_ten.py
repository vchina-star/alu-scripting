#!/usr/bin/python3
"""Print titles of the first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Print the 10 hot post titles, or None if subreddit is invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:alu-scripting:v1.0 (by /u/vchina-star)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    results = response.json().get("data")
    for post in results.get("children"):
        print(post.get("data").get("title"))
