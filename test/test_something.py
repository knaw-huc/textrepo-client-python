import unittest
import uuid
from pprint import pprint
from unittest import TestCase

import textrepo_client
from textrepo_client import ApiException, ApiClient
from textrepo_client.api.documents_api import DocumentsApi
from textrepo_client.api.files_api import FilesApi
from textrepo_client.api.types_api import TypesApi
from textrepo_client.model.form_document import FormDocument
from textrepo_client.model.form_text_repo_file import FormTextRepoFile
from textrepo_client.model.form_type import FormType


class TestFileUpload(TestCase):
    config_portainer = textrepo_client.Configuration(
        host="http://n-195-169-89-124.diginfra.net:49226"
    )

    config_republic = textrepo_client.Configuration(
        host="https://textrepo.republic-caf.diginfra.org/api/"
    )

    def test_create_type(self):
        with ApiClient(self.config_portainer) as api_client:
            types_api_instance = TypesApi(api_client)
            body = FormType(
                name="plain_text",
                mimetype="text/plain",
            )
            type_id = None
            try:
                result_type = types_api_instance.create_type(body=body)

                pprint(result_type)
                type_id = result_type.id
            except ApiException as e:
                print("Exception when calling DocumentsApi->get_documents(): %s\n" % e)

            pprint(type_id)

    def test_create_document(self):

        external_id = str(uuid.uuid4())
        with ApiClient(self.config_portainer) as api_client:
            # Create an instance of the API class
            documents_api_instance = DocumentsApi(api_client)
            doc_id = None
            body = FormDocument(
                external_id=external_id
            )
            try:
                result_doc = documents_api_instance.create_document(body=body)
                pprint(result_doc)
                doc_id = result_doc.id
            except ApiException as e:
                print("Exception when calling DocumentsApi->get_documents(): %s\n" % e)

            files_api_instance = FilesApi(api_client)
            body = FormTextRepoFile(
                doc_id=doc_id,
                type_id=1
            )
            file_id = None
            try:
                result_file = files_api_instance.create_file(body=body)

                pprint(result_file)
                file_id = result_file.id

            except textrepo_client.ApiException as e:
                print("Exception when calling FilesApi->create_file: %s\n" % e)

            pprint(file_id)


if __name__ == '__main__':
    unittest.main()
