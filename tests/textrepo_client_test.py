import importlib
import unittest
from importlib.metadata import version

import pkg_resources
from icecream import ic

from textrepo.client import TextRepoClient


class TextRepoClientTestCase(unittest.TestCase):
    def test_init(self):
        client = TextRepoClient("http://example.org")
        self.assertIsNotNone(client)

    def test_init_with_custom_timeout(self):
        client = TextRepoClient("http://example.org", timeout_in_seconds=20)
        self.assertIsNotNone(client)

    def test_init_with_custom_api_key(self):
        # mock api key: 'aap:noot0-mies1-secret-key-is-geen-uuid' in base64
        client = TextRepoClient('http://example.org', api_key='YWFwOm5vb3QwLW1pZXMxLXNlY3JldC1rZXktaXMtZ2Vlbi11dWlk')
        self.assertIsNotNone(client)

    # def test_custom_headers(self):
    #     client = TextRepoClient("https://globalise.tt.di.huc.knaw.nl/textrepo/", timeout_in_seconds=20)
    #     ft = client.read_file_types()
    #     ic(ft)
    #     a = client.get_about()
    #     ic(a)
    #     v = version('textrepo')
    #     # v = pkg_resources.get_distribution('textrepo-client').version
    #     ic(v)


if __name__ == '__main__':
    unittest.main()
