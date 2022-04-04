import unittest

from icecream import ic

from textrepo.client import TextRepoClient


class TextRepoClientTestCase(unittest.TestCase):
    def test_init(self):
        client = TextRepoClient("http://example.org")
        self.assertIsNotNone(client)

    def test_init_with_custom_timeout(self):
        client = TextRepoClient("http://example.org", timeout_in_seconds=20)
        self.assertIsNotNone(client)

    def test_custom_headers(self):
        client = TextRepoClient("https://globalise.tt.di.huc.knaw.nl/textrepo/", timeout_in_seconds=20)
        ft = client.read_file_types()
        ic(ft)


if __name__ == '__main__':
    unittest.main()
