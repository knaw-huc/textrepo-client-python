import unittest
import uuid
from datetime import datetime
from io import StringIO
from multiprocessing import Pool

from icecream import ic

from textrepo.client import TextRepoClient

TR = TextRepoClient(base_uri='http://localhost:8080/textrepo/', verbose=True)


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
        documentsPage = TR.read_documents()
        ic(documentsPage)
        self.assertIsNotNone(documentsPage)
        self.assertEqual(10, documentsPage.page_limit)
        self.assertEqual(0, documentsPage.page_offset)

    def test_read_documents_with_limit_and_offset(self):
        documentsPage = TR.read_documents(limit=100, offset=201)
        ic(documentsPage)
        self.assertIsNotNone(documentsPage)
        self.assertEqual(100, documentsPage.page_limit)
        self.assertEqual(201, documentsPage.page_offset)

    def test_read_documents_with_externalId(self):
        documentsPage = TR.read_documents(external_id='ga:xyz')
        ic(documentsPage)
        self.assertIsNotNone(documentsPage)

    def test_read_documents_created_after(self):
        documentsPage = TR.read_documents(created_after=datetime.today())
        ic(documentsPage)
        self.assertIsNotNone(documentsPage)
        self.assertEqual(0, documentsPage.total)

    def test_file_type_crud(self):
        purge_file_types()

        type = TR.create_file_type("httml", "application/text+html")
        ic(type)
        self.assertEqual("httml", type.name)
        self.assertEqual("application/text+html", type.mimetype)

        updated_type = TR.update_file_type(type.id, "html", "text/html")
        self.assertEqual("html", updated_type.name)
        self.assertEqual("text/html", updated_type.mimetype)
        self.assertEqual(type.id, updated_type.id)

        types = TR.read_file_types()
        self.assertEqual(1, len(types))
        self.assertEqual(updated_type, types[0])

        ok = TR.delete_file_type(type.id)
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

        readId = TR.read_document(document_id)
        ic(readId)
        self.assertEqual(document_id, readId)

        files = TR.read_document_files(document_id)
        ic(files)

        result = TR.set_document_metadata(document_id.id, "field", "value")
        ic(result)

        metadata = TR.read_document_metadata(document_id)
        ic(metadata)
        self.assertEqual({"field": "value"}, metadata)

        xmlType = TR.create_file_type("xml", "text/xml")
        ic(xmlType)

        fileId = TR.create_document_file(document_id, xmlType.id)
        ic(fileId)

        ok = TR.set_file_metadata(fileId.id, "creator", "ga-ner-tool")
        assert ok

        metadata = TR.read_file_metadata(fileId.id)
        ic(metadata)
        self.assertEqual("ga-ner-tool", metadata["creator"])

        versions = TR.read_file_versions(fileId.id)
        ic(versions)

        file = StringIO('<xml>the contents of this version<</xml>')
        ic(type(file))
        versionId = TR.create_version(fileId.id, file)
        ic(versionId)

        ok = TR.delete_file(fileId.id)
        assert ok

        ok = TR.delete_document_metadata(document_id, "field")
        assert ok

        ok = TR.delete_file_type(xmlType.id)
        assert ok

        docId = TR.update_document_externalId(document_id, "new_external_id")
        ic(docId)
        self.assertEqual("new_external_id", docId.externalId)

        ok = TR.delete_document(readId)
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
        for type in TR.read_file_types():
            TR.delete_file_type(type.id)


def purge_all_documents():
    if 'localhost' not in TR.base_uri:
        print("no purging on external textrepo's!!")
        exit(-1)
    else:
        docPage = TR.read_documents()
        total = docPage.total
        docPage = TR.read_documents(limit=total)
        with Pool(5) as p:
            p.map(TR.purge_document, [document.externalId for document in docPage.items])

        # for document in docPage.items:
        #     try:
        #         TR.purge_document(document.externalId)
        #     except Exception:
        #         print(f"{TR.base_uri}/rest/documents/{document.id}")


if __name__ == '__main__':
    unittest.main()
