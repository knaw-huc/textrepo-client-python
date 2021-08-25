import http.client
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from http import HTTPStatus
from typing import List, Dict

import requests
from dataclasses_json import dataclass_json, config
from dateutil.parser import isoparse
from marshmallow import fields
from requests import Response


@dataclass
class DocumentIdentifier:
    id: uuid
    externalId: str
    createdAt: datetime


@dataclass
class DocumentsPage:
    items: list
    page_limit: int
    page_offset: int
    total: int


@dataclass
class FileIdentifier:
    id: uuid
    docId: uuid
    typeId: int
    url: str


@dataclass_json
@dataclass
class VersionIdentifier:
    id: uuid
    fileId: uuid
    createdAt: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso')
        ))
    contentsSha: str


@dataclass_json
@dataclass
class VersionInfo:
    documentId: uuid
    fileId: uuid
    versionId: uuid
    contentsSha: str
    newVersion: bool


@dataclass_json
@dataclass
class FileType:
    id: int
    name: str
    mimetype: str


class TextRepoClient:

    def __init__(self, base_uri: str, verbose: bool = False):
        self.base_uri = base_uri.strip('/')
        self.raise_exception = True
        self.verbose = verbose

    def __str__(self):
        return f"TextRepoClient({self.base_uri})"

    def __repr__(self):
        return self.__str__()

    def get_about(self) -> dict:
        url = f'{self.base_uri}/'
        response = requests.get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def read_documents(self,
                       external_id: str = None,
                       created_after: datetime = None,
                       limit: int = None,
                       offset: int = None
                       ) -> DocumentsPage:
        url = f'{self.base_uri}/rest/documents'
        params = {}
        if external_id:
            params['externalId'] = external_id
        if created_after:
            params['createdAfter'] = created_after.isoformat(timespec='seconds')
        if limit:
            params['limit'] = limit
        if offset:
            params['offset'] = offset
        response = requests.get(url=url, params=params)
        return self.__handle_response(response, {HTTPStatus.OK: to_documents_page})

    def create_document(self, external_id: str) -> DocumentIdentifier:
        url = f'{self.base_uri}/rest/documents'
        response = requests.post(url=url, json={"externalId": external_id})
        return self.__handle_response(response, {HTTPStatus.CREATED: to_document_identifier})

    def update_document_external_id(self, document_id: DocumentIdentifier, external_id: str) -> DocumentIdentifier:
        url = f'{self.base_uri}/rest/documents/{document_id.id}'
        response = requests.put(url=url, json={"externalId": external_id})
        return self.__handle_response(response, {HTTPStatus.OK: to_document_identifier})

    def read_document(self, document_identifier: DocumentIdentifier) -> DocumentIdentifier:
        """Retrieve document"""
        url = f'{self.base_uri}/rest/documents/{document_identifier.id}'
        response = requests.get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: to_document_identifier})

    def delete_document(self, document_id: DocumentIdentifier) -> bool:
        """Delete document"""
        url = f'{self.base_uri}/rest/documents/{document_id.id}'
        response = requests.delete(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def purge_document(self, external_id: str) -> bool:
        """
        Delete a document including its metadata, files, versions and contents.
        Contents are only deleted when not referenced by any other versions.

        :param external_id: the external Id
        :type external_id: str
        :return: whether the purge succeeded
        :rtype: bool
        """
        url = f'{self.base_uri}/task/delete/documents/{external_id}'
        response = requests.delete(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def set_document_metadata(self, document_id: uuid, key: str, value: str) -> dict:
        url = f'{self.base_uri}/rest/documents/{document_id}/metadata/{key}'
        response = requests.put(url=url, data=value)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def read_document_metadata(self, document_identifier: DocumentIdentifier) -> dict:
        url = f'{self.base_uri}/rest/documents/{document_identifier.id}/metadata'
        response = requests.get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def delete_document_metadata(self, document_identifier: DocumentIdentifier, key: str) -> bool:
        url = f'{self.base_uri}/rest/documents/{document_identifier.id}/metadata/{key}'
        response = requests.delete(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def create_document_file(self, document_identifier: DocumentIdentifier, type_id: int) -> FileIdentifier:
        url = f'{self.base_uri}/rest/files'
        response = requests.post(url=url, json={'docId': document_identifier.id, 'typeId': type_id})
        return self.__handle_response(response, {HTTPStatus.CREATED: to_file_identifier})

    def read_file(self, file_id: uuid) -> FileIdentifier:
        url = f'{self.base_uri}/rest/files/{file_id}'
        response = requests.get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: to_file_identifier})

    def update_document_file(self, document_identifier: DocumentIdentifier, type_id: int) -> FileIdentifier:
        url = f'{self.base_uri}/rest/files'
        response = requests.put(url=url, data={'docId': document_identifier.id, 'typeId': type_id})
        return self.__handle_response(response, {HTTPStatus.OK: to_file_identifier})

    def delete_file(self, file_id: uuid) -> bool:
        url = f'{self.base_uri}/rest/files/{file_id}'
        response = requests.delete(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def read_document_files(self, document_identifier: DocumentIdentifier,
                            type_id: int = None,
                            limit: int = None,
                            offset: int = None) -> dict:
        url = f'{self.base_uri}/rest/documents/{document_identifier.id}/files'
        params = {}
        if type_id:
            params['typeId'] = type_id
        if limit:
            params['limit'] = limit
        if offset:
            params['offset'] = offset
        response = requests.get(url=url, params=params)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def read_file_metadata(self, file_id: uuid) -> dict:
        url = f'{self.base_uri}/rest/files/{file_id}/metadata'
        response = requests.get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def set_file_metadata(self, file_id: uuid, key: str, value: str) -> bool:
        """Create or update file metadata entry"""
        url = f'{self.base_uri}/rest/files/{file_id}/metadata/{key}'
        response = requests.put(url=url, data=value)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def delete_file_metadata(self, file_id: uuid, key: str) -> bool:
        """Delete file metadata entry"""
        url = f'{self.base_uri}/rest/files/{file_id}/metadata/{key}'
        response = requests.delete(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def read_file_versions(self,
                           file_id: uuid,
                           limit: int = None,
                           offset: int = None,
                           created_after: datetime = None
                           ) -> List[VersionIdentifier]:
        url = f'{self.base_uri}/rest/files/{file_id}/versions'
        params = {}
        if created_after:
            params['createdAfter'] = created_after.isoformat(timespec='seconds')
        if limit:
            params['limit'] = limit
        if offset:
            params['offset'] = offset
        response = requests.get(url=url, params=params)
        return self.__handle_response(response,
                                      {HTTPStatus.OK: lambda r: [VersionIdentifier.from_dict(d) for d in
                                                                 r.json()["items"]]})

    def create_version(self, file_id: uuid, file) -> VersionIdentifier:
        url = f'{self.base_uri}/rest/versions'
        files = {'contents': file}
        data = {'fileId': file_id}
        response = requests.post(url=url, files=files, data=data)
        return self.__handle_response(response, {HTTPStatus.CREATED: to_version_identifier})

    def set_version_metadata(self, version_id: uuid, key: str, value: str) -> bool:
        """Create or update version metadata entry"""
        url = f'{self.base_uri}/rest/versions/{version_id}/metadata/{key}'
        response = requests.put(url=url, data=value)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def read_file_types(self) -> List[FileType]:
        url = f'{self.base_uri}/rest/types'
        response = requests.get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: [FileType.from_dict(d) for d in r.json()]})

    def create_file_type(self, name: str, mimetype: str) -> FileType:
        url = f'{self.base_uri}/rest/types'
        response = requests.post(url=url, json={"name": name, "mimetype": mimetype})
        return self.__handle_response(response, {HTTPStatus.CREATED: to_file_type})

    def read_file_type(self, type_id: int) -> FileType:
        url = f'{self.base_uri}/rest/types/{type_id}'
        response = requests.get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: to_file_type})

    def update_file_type(self, type_id: int, name: str, mimetype: str) -> FileType:
        url = f'{self.base_uri}/rest/types/{type_id}'
        response = requests.put(url=url, json={"name": name, "mimetype": mimetype})
        return self.__handle_response(response, {HTTPStatus.OK: to_file_type})

    def delete_file_type(self, type_id: int) -> bool:
        url = f'{self.base_uri}/rest/types/{type_id}'
        response = requests.delete(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def import_version(self, external_id: str, type_name: str, contents, allow_new_document: bool = False,
                       as_latest_version: bool = False) -> VersionInfo:
        url = f'{self.base_uri}/task/import/documents/{external_id}/{type_name}'
        params = {'allowNewDocument': allow_new_document, 'asLatestVersion': as_latest_version}
        files = {'contents': contents}
        response = requests.post(url=url, params=params, files=files)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: VersionInfo.from_dict(r.json()),
                                                 HTTPStatus.CREATED: lambda r: VersionInfo.from_dict(r.json())})

    def index_file(self, external_id: str, type_name: str) -> bool:
        url = f'{self.base_uri}/task/index/file/{external_id}/{type_name}'
        response = requests.post(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def index_indexer(self, indexer_name: str) -> bool:
        url = f'{self.base_uri}/task/index/indexer/{indexer_name}'
        response = requests.post(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def index_type(self, type_name: str) -> bool:
        url = f'{self.base_uri}/task/index/type/{type_name}'
        response = requests.post(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def find_document_metadata(self, external_id: str) -> Dict[str, str]:
        url = f'{self.base_uri}/task/find/{external_id}/document/metadata'
        response = requests.get(url=url)
        # ic(response.links)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def find_latest_file_contents(self, external_id: str, type_name: str) -> any:
        url = f'{self.base_uri}/task/find/{external_id}/file/contents'
        params = {'type': type_name}
        response = requests.get(url=url, params=params)
        # ic(response.links)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.content})

    def find_file_metadata(self, external_id: str, type_name: str) -> Dict[str, str]:
        url = f'{self.base_uri}/task/find/{external_id}/file/metadata'
        params = {'type': type_name}
        response = requests.get(url=url, params=params)
        # ic(response.links)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def find_file_type(self, type_name: str) -> FileType:
        for t in self.read_file_types():
            if t.name == type_name:
                return t
        raise Exception(f'FileType "{type_name}" not found')

    def find_latest_version(self, external_id: str, type_name: str) -> VersionIdentifier:
        type_id = self.find_file_type(type_name).id
        doc = self.read_documents(external_id).items[0]
        file = self.read_document_files(doc, type_id)['items'][0]
        ver = self.read_file_versions(file['id'])[0]
        return ver

    def view_version_segments_by_index(self, version_id: str, start_index: str, end_index: str) -> List[str]:
        """
        Get fragment of version addressed by index anchors

        Gets the fragment of a segmented text between indices start_index and end_index (inclusive)

        :param version_id: UUID of version of a file of type compatible with segmented text view
        :param start_index: integer >= 0 or 'full' (implying index 0)
        :param end_index: integer >= 0, <= total number of segments or 'full' (implying max index)
        :return: list of strings comprising the requested fragment
        """

        url = f'{self.base_uri}/view/versions/{version_id}/segments/index/{start_index}/{end_index}'
        response = requests.get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def view_version_segments_substring_by_index(self, version_id: str,
                                                 start_index: str, start_char_offset: str,
                                                 end_index: str, end_char_offset: str) -> List[str]:
        url = f'{self.base_uri}/view/versions/{version_id}/segments/index' \
              f'/{start_index}/{start_char_offset}' \
              f'/{end_index}/{end_char_offset}'
        response = requests.get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def __handle_response(self, response: Response, result_producers: dict):
        status_code = response.status_code
        status_message = http.client.responses[status_code]
        if self.verbose:
            print(f'-> {response.request.method} {response.request.url}')
            print(f'<- {status_code} {status_message}')
        if status_code in result_producers.keys():
            result = result_producers[response.status_code](response)
            # if (self.raise_exceptions):
            return result
            # else:
            #     return Success(response, result)
        else:
            # if (self.raise_exceptions):
            raise Exception(
                f'{response.request.method} {response.request.url} returned {status_code} {status_message}'
                + ': "{response.text}"')
            # else:
            #     return Failure(response)


# else:
#     return Failure(response)

def to_document_identifier(response: Response) -> DocumentIdentifier:
    json = response.json()
    return DocumentIdentifier(id=json['id'],
                              externalId=json['externalId'],
                              createdAt=isoparse(json['createdAt']))


def to_file_identifier(response: Response) -> FileIdentifier:
    json = response.json()
    return FileIdentifier(id=json['id'],
                          docId=json['docId'],
                          typeId=json['typeId'],
                          url=response.headers['location'])


def to_version_identifier(response: Response) -> VersionIdentifier:
    return VersionIdentifier.from_dict(response.json())


def to_documents_page(response: Response) -> DocumentsPage:
    json = response.json()
    items = [DocumentIdentifier(id=j['id'],
                                externalId=j['externalId'],
                                createdAt=isoparse(j['createdAt']))
             for j in json['items']]
    return DocumentsPage(items=items,
                         page_limit=json['page']['limit'],
                         page_offset=json['page']['offset'],
                         total=json['total'])


def to_file_type(response: Response) -> FileType:
    return FileType.from_dict(response.json())
