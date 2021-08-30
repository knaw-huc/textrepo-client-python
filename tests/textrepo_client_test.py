import unittest

from textrepo.client import TextRepoClient


class TextRepoClientTestCase(unittest.TestCase):
    def test_init(self):
        client = TextRepoClient("http://example.org")
        self.assertIsNotNone(client)


if __name__ == '__main__':
    unittest.main()
