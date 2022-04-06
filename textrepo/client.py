import http.client
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from http import HTTPStatus
from typing import List, Dict

import requests
from dataclasses_json import dataclass_json, config, LetterCase
from marshmallow import fields
from requests import Response

import textrepo


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class DocumentIdentifier:
    id: uuid
    external_id: str
    created_at: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso')
        ))


@dataclass
class DocumentsPage:
    items: List[DocumentIdentifier]
    page_limit: int
    page_offset: int
    total: int


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class FileLocator:
    id: uuid
    doc_id: uuid
    type_id: int
    url: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class FileIdentifier:
    id: uuid
    doc_id: uuid
    type_id: int


@dataclass
class FilesPage:
    items: List[FileIdentifier]
    page_limit: int
    page_offset: int
    total: int


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class VersionIdentifier:
    id: uuid
    file_id: uuid
    created_at: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso')
        ))
    contents_sha: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class VersionInfo:
    document_id: uuid
    file_id: uuid
    version_id: uuid
    contents_sha: str
    new_version: bool


@dataclass_json
@dataclass
class FileType:
    id: int
    name: str
    mimetype: str


class TextRepoClient:

    def __init__(self, base_uri: str, verbose: bool = False, timeout_in_seconds: int = None, api_key=None):
        self.api_key = api_key
        self.base_uri = base_uri.strip('/')
        self.raise_exception = True
        self.timeout = timeout_in_seconds
        self.verbose = verbose

    def __str__(self):
        return f'TextRepoClient({self.base_uri},api_key={self.api_key})'

    def __repr__(self):
        return self.__str__()

    def get_about(self) -> dict:
        url = f'{self.base_uri}/'
        response = self.__get(url=url)
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
        response = self.__get(url=url, params=params)
        return self.__handle_response(response, {HTTPStatus.OK: to_documents_page})

    def create_document(self, external_id: str) -> DocumentIdentifier:
        url = f'{self.base_uri}/rest/documents'
        response = self.__post(url=url, json={"externalId": external_id})
        return self.__handle_response(response, {HTTPStatus.CREATED: to_document_identifier})

    def update_document_external_id(self, document_id: DocumentIdentifier, external_id: str) -> DocumentIdentifier:
        url = f'{self.base_uri}/rest/documents/{document_id.id}'
        response = self.__put(url=url, json={"externalId": external_id})
        return self.__handle_response(response, {HTTPStatus.OK: to_document_identifier})

    def read_document(self, document_identifier: DocumentIdentifier) -> DocumentIdentifier:
        """Retrieve document"""
        url = f'{self.base_uri}/rest/documents/{document_identifier.id}'
        response = self.__get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: to_document_identifier})

    def delete_document(self, document_id: DocumentIdentifier) -> bool:
        """Delete document"""
        url = f'{self.base_uri}/rest/documents/{document_id.id}'
        response = self.__delete(url=url)
        return self.__handle_response(response, {HTTPStatus.NO_CONTENT: lambda r: True})

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
        response = self.__delete(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def set_document_metadata(self, document_id: uuid, key: str, value: str) -> dict:
        url = f'{self.base_uri}/rest/documents/{document_id}/metadata/{key}'
        response = self.__put(url=url, data=value)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def read_document_metadata(self, document_identifier: DocumentIdentifier) -> dict:
        url = f'{self.base_uri}/rest/documents/{document_identifier.id}/metadata'
        response = self.__get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def delete_document_metadata(self, document_identifier: DocumentIdentifier, key: str) -> bool:
        url = f'{self.base_uri}/rest/documents/{document_identifier.id}/metadata/{key}'
        response = self.__delete(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def create_document_file(self, document_identifier: DocumentIdentifier, type_id: int) -> FileLocator:
        url = f'{self.base_uri}/rest/files'
        response = self.__post(url=url, json={'docId': document_identifier.id, 'typeId': type_id})
        return self.__handle_response(response, {HTTPStatus.CREATED: to_file_identifier})

    def read_file(self, file_id: uuid) -> FileLocator:
        url = f'{self.base_uri}/rest/files/{file_id}'
        response = self.__get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: to_file_identifier})

    def update_document_file(self, document_identifier: DocumentIdentifier, type_id: int) -> FileLocator:
        url = f'{self.base_uri}/rest/files'
        response = self.__put(url=url, data={'docId': document_identifier.id, 'typeId': type_id})
        return self.__handle_response(response, {HTTPStatus.OK: to_file_identifier})

    def delete_file(self, file_id: uuid) -> bool:
        url = f'{self.base_uri}/rest/files/{file_id}'
        response = self.__delete(url=url)
        return self.__handle_response(response, {HTTPStatus.NO_CONTENT: lambda r: True})

    def read_document_files(self, document_identifier: DocumentIdentifier,
                            type_id: int = None,
                            limit: int = None,
                            offset: int = None) -> FilesPage:
        url = f'{self.base_uri}/rest/documents/{document_identifier.id}/files'
        params = {}
        if type_id:
            params['typeId'] = type_id
        if limit:
            params['limit'] = limit
        if offset:
            params['offset'] = offset
        response = self.__get(url=url, params=params)
        return self.__handle_response(response, {HTTPStatus.OK: to_files_page})

    def resolve_file_location(self, file: FileIdentifier) -> FileLocator:
        return FileLocator(id=file.id,
                           doc_id=file.doc_id,
                           type_id=file.type_id,
                           url=f'{self.base_uri}/rest/files/{file.id}')

    def read_file_metadata(self, file_id: uuid) -> dict:
        url = f'{self.base_uri}/rest/files/{file_id}/metadata'
        response = self.__get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def set_file_metadata(self, file_id: uuid, key: str, value: str) -> bool:
        """Create or update file metadata entry"""
        url = f'{self.base_uri}/rest/files/{file_id}/metadata/{key}'
        response = self.__put(url=url, data=value)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def delete_file_metadata(self, file_id: uuid, key: str) -> bool:
        """Delete file metadata entry"""
        url = f'{self.base_uri}/rest/files/{file_id}/metadata/{key}'
        response = self.__delete(url=url)
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
        response = self.__get(url=url, params=params)
        return self.__handle_response(response,
                                      {HTTPStatus.OK: lambda r: [VersionIdentifier.from_dict(d) for d in
                                                                 r.json()['items']]})

    def create_version(self, file_id: uuid, file) -> VersionIdentifier:
        url = f'{self.base_uri}/rest/versions'
        files = {'contents': file}
        data = {'fileId': file_id}
        response = self.__post(url=url, files=files, data=data)
        return self.__handle_response(response, {HTTPStatus.CREATED: to_version_identifier})

    def set_version_metadata(self, version_id: uuid, key: str, value: str) -> bool:
        """Create or update version metadata entry"""
        url = f'{self.base_uri}/rest/versions/{version_id}/metadata/{key}'
        response = self.__put(url=url, data=value)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def read_file_types(self) -> List[FileType]:
        url = f'{self.base_uri}/rest/types'
        response = self.__get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: [FileType.from_dict(d) for d in r.json()]})

    def create_file_type(self, name: str, mimetype: str) -> FileType:
        url = f'{self.base_uri}/rest/types'
        response = self.__post(url=url, json={"name": name, "mimetype": mimetype})
        return self.__handle_response(response, {HTTPStatus.CREATED: to_file_type})

    def read_file_type(self, type_id: int) -> FileType:
        url = f'{self.base_uri}/rest/types/{type_id}'
        response = self.__get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: to_file_type})

    def update_file_type(self, type_id: int, name: str, mimetype: str) -> FileType:
        url = f'{self.base_uri}/rest/types/{type_id}'
        response = self.__put(url=url, json={"name": name, "mimetype": mimetype})
        return self.__handle_response(response, {HTTPStatus.OK: to_file_type})

    def delete_file_type(self, type_id: int) -> bool:
        url = f'{self.base_uri}/rest/types/{type_id}'
        response = self.__delete(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def import_version(self, external_id: str, type_name: str, contents, allow_new_document: bool = False,
                       as_latest_version: bool = False) -> VersionInfo:
        url = f'{self.base_uri}/task/import/documents/{external_id}/{type_name}'
        params = {'allowNewDocument': allow_new_document, 'asLatestVersion': as_latest_version}
        files = {'contents': contents}
        response = self.__post(url=url, params=params, files=files)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: VersionInfo.from_dict(r.json()),
                                                 HTTPStatus.CREATED: lambda r: VersionInfo.from_dict(r.json())})

    def index_file(self, external_id: str, type_name: str) -> bool:
        url = f'{self.base_uri}/task/index/file/{external_id}/{type_name}'
        response = self.__post(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def index_indexer(self, indexer_name: str) -> bool:
        url = f'{self.base_uri}/task/index/indexer/{indexer_name}'
        response = self.__post(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def index_type(self, type_name: str) -> bool:
        url = f'{self.base_uri}/task/index/type/{type_name}'
        response = self.__post(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: True})

    def find_document_metadata(self, external_id: str) -> Dict[str, str]:
        url = f'{self.base_uri}/task/find/{external_id}/document/metadata'
        response = self.__get(url=url)
        # ic(response.links)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def find_latest_file_contents(self, external_id: str, type_name: str) -> any:
        url = f'{self.base_uri}/task/find/{external_id}/file/contents'
        params = {'type': type_name}
        response = self.__get(url=url, params=params)
        # ic(response.links)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.content})

    def find_file_metadata(self, external_id: str, type_name: str) -> Dict[str, str]:
        url = f'{self.base_uri}/task/find/{external_id}/file/metadata'
        params = {'type': type_name}
        response = self.__get(url=url, params=params)
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
        file = self.read_document_files(doc, type_id).items[0]
        return self.read_file_versions(file.id)[0]

    def view_version_segments_by_index(self, version_id: uuid, start_index: str, end_index: str) -> List[str]:
        """
        Get fragment of version addressed by index anchors

        Gets the fragment of a segmented text between indices start_index and end_index (inclusive)

        :param version_id: UUID of version of a file of type compatible with segmented text view
        :param start_index: integer >= 0 or 'full' (implying index 0)
        :param end_index: integer <= total number of segments or 'full' (implying max index)
        :return: list of strings comprising the requested fragment
        """

        url = f'{self.base_uri}/view/versions/{version_id}/segments/index/{start_index}/{end_index}'
        response = self.__get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def view_version_segments_substring_by_index(self, version_id: uuid,
                                                 start_index: str, start_char_offset: str,
                                                 end_index: str, end_char_offset: str) -> List[str]:
        """
        Get substring of fragment of version addressed by index anchors and character offsets

        Gets the 'substring' fragment of a segmented text between indices start_index and end_index (inclusive)
        The first element of the fragment is reduced to the substring starting at start_char_offset and
        the last element of the fragment is reduced to the substring ending at end_char_offset

        :param version_id: UUID of version of a file of type compatible with segmented text view
        :param start_index: integer >= 0 or 'full' (implying index 0)
        :param start_char_offset: integer <= number of characters in first element or 'full' (implying offset 0)
        :param end_index: integer <= total number of segments or 'full' (implying max index)
        :param end_char_offset: integer <= number of characters in last element or 'full' (implying last character)
        :return: list of strings comprising the requested fragment substrings
        """

        url = f'{self.base_uri}/view/versions/{version_id}/segments/index' \
              f'/{start_index}/{start_char_offset}' \
              f'/{end_index}/{end_char_offset}'
        response = self.__get(url=url)
        return self.__handle_response(response, {HTTPStatus.OK: lambda r: r.json()})

    def __get(self, url, params=None, **kwargs):
        args = self.__set_defaults(kwargs)
        return requests.get(url, params=params, **args)

    def __post(self, url, data=None, json=None, **kwargs):
        args = self.__set_defaults(kwargs)
        return requests.post(url, data=data, json=json, **args)

    def __put(self, url, data=None, **kwargs):
        args = self.__set_defaults(kwargs)
        return requests.put(url, data=data, **args)

    def __delete(self, url, **kwargs):
        args = self.__set_defaults(kwargs)
        return requests.delete(url, **args)

    def __set_defaults(self, args: dict):
        if 'headers' not in args:
            args['headers'] = {}
        args['headers']['User-Agent'] = f'textrepo-python-client/{textrepo.__version__}'
        if self.api_key:
            args['headers']['Authorization'] = f'Basic: {self.api_key}'
        if self.timeout:
            args['timeout'] = self.timeout
        return args

    def __handle_response(self, response: Response, result_producers: dict):
        status_code = response.status_code
        status_message = http.client.responses[status_code]
        # ic(response.request.headers)
        if self.verbose:
            print(f'-> {response.request.method} {response.request.url}')
            print(f'<- {status_code} {status_message}')
        if status_code in result_producers:
            # if (self.raise_exceptions):
            return result_producers[response.status_code](response)
            # else:
            #     return Success(response, result)
        else:
            # if (self.raise_exceptions):
            raise Exception(
                f'{response.request.method} {response.request.url} returned {status_code} {status_message}'
                + f': "{response.text}"')


def to_document_identifier(response: Response) -> DocumentIdentifier:
    return DocumentIdentifier.from_dict(response.json())


def to_file_identifier(response: Response) -> FileLocator:
    json = response.json()
    json['url'] = response.headers['location']
    return FileLocator.from_dict(json)


def to_version_identifier(response: Response) -> VersionIdentifier:
    return VersionIdentifier.from_dict(response.json())


def to_documents_page(response: Response) -> DocumentsPage:
    json = response.json()
    items = [DocumentIdentifier.from_dict(j) for j in json['items']]
    page = json['page']
    return DocumentsPage(items=items,
                         page_limit=page['limit'],
                         page_offset=page['offset'],
                         total=json['total'])


def to_files_page(response: Response) -> FilesPage:
    json = response.json()
    items = [FileIdentifier.from_dict(j) for j in json['items']]
    page = json['page']
    return FilesPage(items=items,
                     page_limit=page['limit'],
                     page_offset=page['offset'],
                     total=json['total'])


def to_file_type(response: Response) -> FileType:
    return FileType.from_dict(response.json())
