import unittest
import textrepo_client
from textrepo_client import ApiClient, Configuration
from unittest import TestCase


class TestSomething(TestCase):
    config_portainer = Configuration()
    config_portainer.host = "http://n-195-169-89-124.diginfra.net:49226"

    config_republic = Configuration()
    config_republic.host = "https://textrepo.republic-caf.diginfra.org/api/"

    def test_1(self):
        api_instance = textrepo_client.AboutApi(
            api_client=ApiClient(configuration=self.config_republic))
        api_response = api_instance.get_about()
        print(api_response)
        print(api_response.version.tag)

    def test_2(self):
        api_instance = textrepo_client.DocumentsApi(
            api_client=ApiClient(configuration=self.config_portainer))
        api_response = api_instance.get4()
        print(api_response)


if __name__ == '__main__':
    unittest.main()
