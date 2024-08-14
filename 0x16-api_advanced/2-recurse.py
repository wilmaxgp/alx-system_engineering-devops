#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[]):

    """
    Recursively fetches all hot articles from a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): Accumulates the titles of hot articles.
        
    Returns:
        list or None: A list of hot article titles or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "my-user-agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    posts = data.get('children', [])
    next_page = data.get('after', None)
    
    if not posts:
        return hot_list if hot_list else None

    for post in posts:
        hot_list.append(post['data']['title'])

    if next_page:
        next_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={next_page}"
        recurse(subreddit, hot_list)

    return hot_list
