"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import textrepo_client
from textrepo_client.api.metadata_api import MetadataApi  # noqa: E501


class TestMetadataApi(unittest.TestCase):
    """MetadataApi unit test stubs"""

    def setUp(self):
        self.api = MetadataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_document_metadata_entry(self):
        """Test case for delete_document_metadata_entry

        Delete document metadata entry  # noqa: E501
        """
        pass

    def test_delete_file_metadata_entry(self):
        """Test case for delete_file_metadata_entry

        Delete file metadata entry  # noqa: E501
        """
        pass

    def test_get_document_metadata(self):
        """Test case for get_document_metadata

        Retrieve document metadata  # noqa: E501
        """
        pass

    def test_get_documents_given_metadata_key(self):
        """Test case for get_documents_given_metadata_key

        Find which documents have a given metadata key  # noqa: E501
        """
        pass

    def test_get_file_metadata(self):
        """Test case for get_file_metadata

        Retrieve file metadata  # noqa: E501
        """
        pass

    def test_post_document_metadata_is_not_allowed(self):
        """Test case for post_document_metadata_is_not_allowed

        Not allowed to post metadata: use put instead  # noqa: E501
        """
        pass

    def test_post_metadata_is_not_allowed(self):
        """Test case for post_metadata_is_not_allowed

        Not allowed to post metadata: use put instead  # noqa: E501
        """
        pass

    def test_put_document_metadata_entry(self):
        """Test case for put_document_metadata_entry

        Create or update document metadata entry  # noqa: E501
        """
        pass

    def test_put_file_metadata_entry(self):
        """Test case for put_file_metadata_entry

        Create or update file metadata entry  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
