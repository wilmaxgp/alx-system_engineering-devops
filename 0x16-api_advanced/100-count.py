#!/usr/bin/python3
import requests
import re
from collections import defaultdict

def clean_word(word):
    """
    Clean the word to ensure it matches the keyword list format.
    """
    return re.sub(r'\W+', '', word).lower()

def count_words(subreddit, word_list, counts=None, after=None):
    """
    Recursively fetches all hot articles and counts occurrences of given keywords.
    
    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        counts (dict): Accumulator for keyword counts.
        after (str): Parameter for pagination.
        
    Returns:
        dict or None: A dictionary of keyword counts or None if subreddit is invalid.
    """
    if counts is None:
        counts = defaultdict(int)
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    
    headers = {"User-Agent": "my-user-agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Debugging output
    print(f"Fetching: {url}")
    print(f"Status Code: {response.status_code}")
    
    if response.status_code != 200:
        print("Invalid subreddit or API error.")
        return None
    
    data = response.json().get('data', {})
    posts = data.get('children', [])
    next_page = data.get('after', None)
    
    if not posts:
        return counts if counts else None
    
    for post in posts:
        title = post['data']['title'].lower()
        print(f"Title: {title}")  # Debugging output
        for word in word_list:
            clean_word = re.sub(r'\W+', '', word).lower()
            count = len(re.findall(r'\b' + re.escape(clean_word) + r'\b', title))
            counts[clean_word] += count
    
    if next_page:
        return count_words(subreddit, word_list, counts, next_page)
    
    # Sorting and printing results
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")

    return counts
