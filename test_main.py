import unittest
from main import test_endpoint

class TestEndpoints(unittest.TestCase):
    def test_valid_url(self):
        status_code, _ = test_endpoint("https://jsonplaceholder.typicode.com/posts/1")
        self.assertEqual(status_code, 200)

    def test_invalid_url(self):
        status_code, error = test_endpoint("https://invalid.url.abc")
        self.assertIsNone(status_code)
        self.assertTrue(
            "getaddrinfo failed" in error or
            "NameResolutionError" in error or
            "Failed to resolve" in error
        )

if __name__ == '__main__':
    unittest.main()
