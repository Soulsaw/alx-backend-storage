#!/usr/bin/env python3
"""Doc module"""
import requests
import redis
import time
"""Doc import"""


def get_page(url: str) -> str:
    """# Initialize Redis client"""
    redis_client = redis.Redis()

    # Increment count for the URL accessed
    redis_key = f"count:{url}"
    redis_client.incr(redis_key)

    # Check if the page content is cached
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    # If not cached, fetch page content
    response = requests.get(url)
    content = response.text

    # Cache page content with expiration time of 10 seconds
    redis_client.setex(url, 10, content)

    return content

# Example Usage
url = "http://slowwly.robertomurray.co.uk"
start_time = time.time()
page_content = get_page(url)
end_time = time.time()
print("Page content:", page_content)
print("Time taken:", end_time - start_time, "seconds")
