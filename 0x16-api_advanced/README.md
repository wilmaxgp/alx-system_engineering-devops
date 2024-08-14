
# Reddit API Project

## Overview

This project contains Python scripts that interact with the Reddit API to perform various tasks such as fetching subscriber counts, listing top posts, and counting keywords in post titles.

## Tasks

### 0. Number of Subscribers

**File:** `0-subs.py`

**Description:**
Fetches the number of subscribers for a given subreddit. Returns `0` if the subreddit is invalid.

**Usage:**

```bash
python3 0-main.py <subreddit>
```

**Example:**

```bash
python3 0-main.py programming
# Output: 756024

python3 0-main.py this_is_a_fake_subreddit
# Output: 0
```

### 1. Top Ten

**File:** `1-top_ten.py`

**Description:**
Prints the titles of the top 10 hot posts for a given subreddit. Prints `None` if the subreddit is invalid.

**Usage:**

```bash
python3 1-main.py <subreddit>
```

**Example:**

```bash
python3 1-main.py programming
# Output:
# Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
# How a 64k intro is made
# ...

python3 1-main.py this_is_a_fake_subreddit
# Output: None
```

### 2. Recurse It

**File:** `2-recurse.py`

**Description:**
Recursively fetches all hot post titles for a given subreddit. Returns `None` if the subreddit is invalid or if no posts are found.

**Usage:**

```bash
python3 2-main.py <subreddit>
```

**Example:**

```bash
python3 2-main.py programming
# Output: List of titles

python3 2-main.py this_is_a_fake_subreddit
# Output: None
```

### 3. Count It

**File:** `100-count.py`

**Description:**
Counts and sorts occurrences of specified keywords in hot post titles for a given subreddit. Results are printed in descending order by count.

**Usage:**

```bash
python3 100-main.py <subreddit> '<keywords>'
```

**Example:**

```bash
python3 100-main.py programming 'react python java javascript'
# Output:
# java: 27
# python: 17
# ...

python3 100-main.py not_a_valid_subreddit 'python java'
# Output: (no output)
```
