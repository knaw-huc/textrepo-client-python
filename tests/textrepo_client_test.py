import unittest

from textrepo.client import TextRepoClient


class TextRepoClientTestCase(unittest.TestCase):
    def test_init(self):
        client = TextRepoClient("http://example.org")
        assert client != None


if __name__ == '__main__':
    unittest.main()
