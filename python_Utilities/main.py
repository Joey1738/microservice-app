import requests
import logging
from log_config import setup_logger

logger = setup_logger()

def test_endpoint(url):
    try:
        response = requests.get(url)
        logger.info(f"Requested URL: {url} | Status: {response.status_code}")
        return response.status_code, response.text
    except requests.RequestException as e:
        logger.error(f"Request to {url} failed: {e}")
        return None, str(e)

# Example usage
if __name__ == "__main__":
    test_endpoint("https://jsonplaceholder.typicode.com/posts/1")
