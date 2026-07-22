#!/usr/bin/python3
"""Print titles of the first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Print the 10 hot post titles, or None if subreddit is invalid."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data").get("children")
    for post in posts:
        print(post.get("data").get("title"))
