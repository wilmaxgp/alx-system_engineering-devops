# Reddit API - Subscriber Count

This project includes a function that queries the Reddit API to return the number of subscribers for a given subreddit.

## Function

- **Prototype:** `def number_of_subscribers(subreddit)`
- **Description:** 
  - Queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit.
  - If the subreddit is invalid, the function returns `0`.

## Example

```bash
$ ./0-main.py programming
756024

$ ./0-main.py this_is_a_fake_subreddit
0
