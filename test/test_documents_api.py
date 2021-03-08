# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import textrepo_client
from textrepo_client.api.documents_api import DocumentsApi  # noqa: E501
from textrepo_client.rest import ApiException


class TestDocumentsApi(unittest.TestCase):
    """DocumentsApi unit test stubs"""

    def setUp(self):
        self.api = DocumentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete(self):
        """Test case for delete

        Delete document metadata entry  # noqa: E501
        """
        pass

    def test_delete1(self):
        """Test case for delete1

        Delete document  # noqa: E501
        """
        pass

    def test_delete_document(self):
        """Test case for delete_document

        Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.  # noqa: E501
        """
        pass

    def test_get1(self):
        """Test case for get1

        Retrieve document files  # noqa: E501
        """
        pass

    def test_get2(self):
        """Test case for get2

        Retrieve document metadata  # noqa: E501
        """
        pass

    def test_get3(self):
        """Test case for get3

        Retrieve document  # noqa: E501
        """
        pass

    def test_get4(self):
        """Test case for get4

        Retrieve documents, newest first  # noqa: E501
        """
        pass

    def test_post(self):
        """Test case for post

        Not allowed to post metadata: use put instead  # noqa: E501
        """
        pass

    def test_post1(self):
        """Test case for post1

        Create document  # noqa: E501
        """
        pass

    def test_put(self):
        """Test case for put

        Create or update document  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Create or update document metadata entry  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
