import unittest
import uuid
from datetime import datetime
from io import StringIO
from multiprocessing import Pool

from icecream import ic

from textrepo.client import TextRepoClient

TR = TextRepoClient(base_uri='http://localhost:8080/textrepo/', verbose=True,
                    api_key='YWFwOm5vb3QwLW1pZXMxLXNlY3JldC1rZXktaXMtZ2Vlbi11dWlk')


class TextRepoTestCase(unittest.TestCase):

    def test_textrepo_base_url(self):
        tr1 = TextRepoClient('http://localhost:8080/textrepo/')
        self.assertEqual('http://localhost:8080/textrepo', tr1.base_uri)
        tr2 = TextRepoClient('http://localhost:8080/textrepo')
        self.assertEqual('http://localhost:8080/textrepo', tr2.base_uri)

    def test_about(self):
        ic(TR)
        about = TR.get_about()
        ic(about)
        self.assertIsNotNone(about)

    def test_read_documents(self):
        documents_page = TR.read_documents()
        ic(documents_page)
        self.assertIsNotNone(documents_page)
        self.assertEqual(10, documents_page.page_limit)
        self.assertEqual(0, documents_page.page_offset)

    def test_read_documents_with_limit_and_offset(self):
        documents_page = TR.read_documents(limit=100, offset=201)
        ic(documents_page)
        self.assertIsNotNone(documents_page)
        self.assertEqual(100, documents_page.page_limit)
        self.assertEqual(201, documents_page.page_offset)

    def test_read_documents_with_externalId(self):
        documents_page = TR.read_documents(external_id='ga:xyz')
        ic(documents_page)
        self.assertIsNotNone(documents_page)

    def test_read_documents_created_after(self):
        documents_page = TR.read_documents(created_after=datetime.today())
        ic(documents_page)
        self.assertIsNotNone(documents_page)
        self.assertEqual(0, documents_page.total)

    def test_file_type_crud(self):
        purge_file_types()

        ftype = TR.create_file_type("httml", "application/text+html")
        ic(ftype)
        self.assertEqual("httml", ftype.name)
        self.assertEqual("application/text+html", ftype.mimetype)

        updated_type = TR.update_file_type(ftype.id, "html", "text/html")
        self.assertEqual("html", updated_type.name)
        self.assertEqual("text/html", updated_type.mimetype)
        self.assertEqual(ftype.id, updated_type.id)

        types = TR.read_file_types()
        self.assertEqual(1, len(types))
        self.assertEqual(updated_type, types[0])

        ok = TR.delete_file_type(ftype.id)
        assert ok

        types = TR.read_file_types()
        self.assertEqual(0, len(types))

    def test_document_crud(self):
        purge_all_documents()
        purge_file_types()

        external_id = f'ga:annotationId:{uuid.uuid4()}'
        document_id = TR.create_document(external_id)
        ic(document_id)
        self.assertIsNotNone(document_id)

        read_id = TR.read_document(document_id)
        ic(read_id)
        self.assertEqual(document_id, read_id)

        files = TR.read_document_files(document_id)
        ic(files)

        result = TR.set_document_metadata(document_id.id, "field", "value")
        ic(result)

        metadata = TR.read_document_metadata(document_id)
        ic(metadata)
        self.assertEqual({"field": "value"}, metadata)

        xml_type = TR.create_file_type("xml", "text/xml")
        ic(xml_type)

        file_id = TR.create_document_file(document_id, xml_type.id)
        ic(file_id)

        ok = TR.set_file_metadata(file_id.id, "creator", "ga-ner-tool")
        assert ok

        metadata = TR.read_file_metadata(file_id.id)
        ic(metadata)
        self.assertEqual("ga-ner-tool", metadata["creator"])

        versions = TR.read_file_versions(file_id.id)
        ic(versions)

        file = StringIO('<xml>the contents of this version<</xml>')
        ic(type(file))
        version_id = TR.create_version(file_id.id, file)
        ic(version_id)

        ok = TR.delete_file(file_id.id)
        assert ok

        ok = TR.delete_document_metadata(document_id, "field")
        assert ok

        ok = TR.delete_file_type(xml_type.id)
        assert ok

        doc_id = TR.update_document_external_id(document_id, "new_external_id")
        ic(doc_id)
        self.assertEqual("new_external_id", doc_id.external_id)

        ok = TR.delete_document(read_id)
        assert ok

    def test_document_purge(self):
        external_id = f'ga:annotationId:{uuid.uuid4()}'
        document_id = TR.create_document(external_id)
        ic(document_id)
        self.assertIsNotNone(document_id)

        ok = TR.purge_document(external_id)
        assert ok


def purge_file_types():
    if 'localhost' not in TR.base_uri:
        print("no purging on external textrepo's!!")
        exit(-1)
    else:
        for ftype in TR.read_file_types():
            TR.delete_file_type(ftype.id)


def purge_all_documents():
    if 'localhost' not in TR.base_uri:
        print("no purging on external textrepo's!!")
        exit(-1)
    else:
        doc_page = TR.read_documents()
        total = doc_page.total
        doc_page = TR.read_documents(limit=total)
        with Pool(5) as p:
            p.map(TR.purge_document, [document.external_id for document in doc_page.items])

        # for document in doc_page.items:
        #     try:
        #         TR.purge_document(document.externalId)
        #     except Exception:
        #         print(f"{TR.base_uri}/rest/documents/{document.id}")


if __name__ == '__main__':
    unittest.main()
