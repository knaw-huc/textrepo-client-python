"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import textrepo_client
from textrepo_client.api.import_api import ImportApi  # noqa: E501


class TestImportApi(unittest.TestCase):
    """ImportApi unit test stubs"""

    def setUp(self):
        self.api = ImportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_import_document_contents_for_file_with_type(self):
        """Test case for import_document_contents_for_file_with_type

        Import file as the current version for {typeName} of document referenced by {externalId} without indexing  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
