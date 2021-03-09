# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import textrepo_client
from textrepo_client.api.files_api import FilesApi  # noqa: E501
from textrepo_client.rest import ApiException


class TestFilesApi(unittest.TestCase):
    """FilesApi unit test stubs"""

    def setUp(self):
        self.api = FilesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_file(self):
        """Test case for create_file

        Create file  # noqa: E501
        """
        pass

    def test_delete_file(self):
        """Test case for delete_file

        Delete file  # noqa: E501
        """
        pass

    def test_delete_file_metadata_entry(self):
        """Test case for delete_file_metadata_entry

        Delete file metadata entry  # noqa: E501
        """
        pass

    def test_get_file(self):
        """Test case for get_file

        Retrieve file  # noqa: E501
        """
        pass

    def test_get_file_metadata(self):
        """Test case for get_file_metadata

        Retrieve file metadata  # noqa: E501
        """
        pass

    def test_get_versions(self):
        """Test case for get_versions

        Retrieve file versions, newest first  # noqa: E501
        """
        pass

    def test_post_metadata_is_not_allowed(self):
        """Test case for post_metadata_is_not_allowed

        Not allowed to post metadata: use put instead  # noqa: E501
        """
        pass

    def test_put_file(self):
        """Test case for put_file

        Create or update file  # noqa: E501
        """
        pass

    def test_put_file_metadata_entry(self):
        """Test case for put_file_metadata_entry

        Create or update file metadata entry  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
