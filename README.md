# textrepo-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import textrepo_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import textrepo_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import textrepo_client
from pprint import pprint
from textrepo_client.api import contents_api
from textrepo_client.model.result_version import ResultVersion
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)



# Enter a context with an instance of the API client
with textrepo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contents_api.ContentsApi(api_client)
    
    try:
        # Not allowed to delete contents of version: delete version instead
        api_instance.delete_version_contents_is_not_allowed()
    except textrepo_client.ApiException as e:
        print("Exception when calling ContentsApi->delete_version_contents_is_not_allowed: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContentsApi* | [**delete_version_contents_is_not_allowed**](docs/ContentsApi.md#delete_version_contents_is_not_allowed) | **DELETE** /rest/versions/{versionId}/contents | Not allowed to delete contents of version: delete version instead
*ContentsApi* | [**get_contents**](docs/ContentsApi.md#get_contents) | **GET** /rest/contents/{sha} | Retrieve contents
*ContentsApi* | [**get_version_contents**](docs/ContentsApi.md#get_version_contents) | **GET** /rest/versions/{versionId}/contents | Retrieve version contents
*ContentsApi* | [**post_version_contents_is_not_allowed**](docs/ContentsApi.md#post_version_contents_is_not_allowed) | **POST** /rest/versions/{versionId}/contents | Not allowed to post contents: post new version instead
*ContentsApi* | [**put_version_contents_is_not_allowed**](docs/ContentsApi.md#put_version_contents_is_not_allowed) | **PUT** /rest/versions/{versionId}/contents | Not allowed to put contents of version: post new version instead
*DashboardApi* | [**count_documents_by_metadata_key**](docs/DashboardApi.md#count_documents_by_metadata_key) | **GET** /dashboard/metadata | Get document count breakdown by metadata key (yields Map: key -&gt; count)
*DashboardApi* | [**count_documents_by_metadata_value**](docs/DashboardApi.md#count_documents_by_metadata_value) | **GET** /dashboard/metadata/{key} | Get document count breakdown by metadata value for given metadata key
*DashboardApi* | [**find_orphans**](docs/DashboardApi.md#find_orphans) | **GET** /dashboard/orphans | Find orphans: documents with neither metadata nor any associated files
*DashboardApi* | [**get_stats**](docs/DashboardApi.md#get_stats) | **GET** /dashboard | Get document count overview
*DocumentsApi* | [**create_document**](docs/DocumentsApi.md#create_document) | **POST** /rest/documents | Create document
*DocumentsApi* | [**delete_document**](docs/DocumentsApi.md#delete_document) | **DELETE** /rest/documents/{id} | Delete document
*DocumentsApi* | [**delete_document_metadata_entry**](docs/DocumentsApi.md#delete_document_metadata_entry) | **DELETE** /rest/documents/{docId}/metadata/{key} | Delete document metadata entry
*DocumentsApi* | [**delete_document_recursively**](docs/DocumentsApi.md#delete_document_recursively) | **DELETE** /task/delete/documents/{externalId} | Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.
*DocumentsApi* | [**get_document**](docs/DocumentsApi.md#get_document) | **GET** /rest/documents/{id} | Retrieve document
*DocumentsApi* | [**get_document_files**](docs/DocumentsApi.md#get_document_files) | **GET** /rest/documents/{docId}/files | Retrieve document files
*DocumentsApi* | [**get_document_metadata**](docs/DocumentsApi.md#get_document_metadata) | **GET** /rest/documents/{docId}/metadata | Retrieve document metadata
*DocumentsApi* | [**get_documents**](docs/DocumentsApi.md#get_documents) | **GET** /rest/documents | Retrieve documents, newest first
*DocumentsApi* | [**post_document_metadata_is_not_allowed**](docs/DocumentsApi.md#post_document_metadata_is_not_allowed) | **POST** /rest/documents/{docId}/metadata | Not allowed to post metadata: use put instead
*DocumentsApi* | [**put_document**](docs/DocumentsApi.md#put_document) | **PUT** /rest/documents/{id} | Create or update document
*DocumentsApi* | [**put_document_metadata_entry**](docs/DocumentsApi.md#put_document_metadata_entry) | **PUT** /rest/documents/{docId}/metadata/{key} | Create or update document metadata entry
*FilesApi* | [**create_file**](docs/FilesApi.md#create_file) | **POST** /rest/files | Create file
*FilesApi* | [**delete_file**](docs/FilesApi.md#delete_file) | **DELETE** /rest/files/{id} | Delete file
*FilesApi* | [**delete_file_metadata_entry**](docs/FilesApi.md#delete_file_metadata_entry) | **DELETE** /rest/files/{fileId}/metadata/{key} | Delete file metadata entry
*FilesApi* | [**get_file**](docs/FilesApi.md#get_file) | **GET** /rest/files/{id} | Retrieve file
*FilesApi* | [**get_file_metadata**](docs/FilesApi.md#get_file_metadata) | **GET** /rest/files/{fileId}/metadata | Retrieve file metadata
*FilesApi* | [**get_versions**](docs/FilesApi.md#get_versions) | **GET** /rest/files/{fileId}/versions | Retrieve file versions, newest first
*FilesApi* | [**post_metadata_is_not_allowed**](docs/FilesApi.md#post_metadata_is_not_allowed) | **POST** /rest/files/{fileId}/metadata | Not allowed to post metadata: use put instead
*FilesApi* | [**put_file**](docs/FilesApi.md#put_file) | **PUT** /rest/files/{id} | Create or update file
*FilesApi* | [**put_file_metadata_entry**](docs/FilesApi.md#put_file_metadata_entry) | **PUT** /rest/files/{fileId}/metadata/{key} | Create or update file metadata entry
*FindApi* | [**get_document_metadata**](docs/FindApi.md#get_document_metadata) | **GET** /task/find/{externalId}/document/metadata | Find metadata of document by external ID, with header links to original and parent resource
*FindApi* | [**get_file_metadata**](docs/FindApi.md#get_file_metadata) | **GET** /task/find/{externalId}/file/metadata | Find metadata of file by external ID and file type, with header links to original, parent and type resource
*FindApi* | [**get_latest_file_version_content**](docs/FindApi.md#get_latest_file_version_content) | **GET** /task/find/{externalId}/file/contents | Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource
*ImportApi* | [**import_document_contents_for_file_with_type**](docs/ImportApi.md#import_document_contents_for_file_with_type) | **POST** /task/import/documents/{externalId}/{typeName} | Import file as the current version for {typeName} of document referenced by {externalId} without indexing
*IndexApi* | [**index_all**](docs/IndexApi.md#index_all) | **POST** /task/index/files/{type} | Index all files by type
*IndexApi* | [**index_document**](docs/IndexApi.md#index_document) | **POST** /task/index/document/{externalId}/{type} | Index file of document by externalId and file type
*IndexApi* | [**index_single_index**](docs/IndexApi.md#index_single_index) | **POST** /task/index/{name} | Index all files of a single index
*MetadataApi* | [**delete_document_metadata_entry**](docs/MetadataApi.md#delete_document_metadata_entry) | **DELETE** /rest/documents/{docId}/metadata/{key} | Delete document metadata entry
*MetadataApi* | [**delete_file_metadata_entry**](docs/MetadataApi.md#delete_file_metadata_entry) | **DELETE** /rest/files/{fileId}/metadata/{key} | Delete file metadata entry
*MetadataApi* | [**get_document_metadata**](docs/MetadataApi.md#get_document_metadata) | **GET** /rest/documents/{docId}/metadata | Retrieve document metadata
*MetadataApi* | [**get_documents_given_metadata_key**](docs/MetadataApi.md#get_documents_given_metadata_key) | **GET** /rest/metadata/{key}/documents | Find which documents have a given metadata key
*MetadataApi* | [**get_file_metadata**](docs/MetadataApi.md#get_file_metadata) | **GET** /rest/files/{fileId}/metadata | Retrieve file metadata
*MetadataApi* | [**post_document_metadata_is_not_allowed**](docs/MetadataApi.md#post_document_metadata_is_not_allowed) | **POST** /rest/documents/{docId}/metadata | Not allowed to post metadata: use put instead
*MetadataApi* | [**post_metadata_is_not_allowed**](docs/MetadataApi.md#post_metadata_is_not_allowed) | **POST** /rest/files/{fileId}/metadata | Not allowed to post metadata: use put instead
*MetadataApi* | [**put_document_metadata_entry**](docs/MetadataApi.md#put_document_metadata_entry) | **PUT** /rest/documents/{docId}/metadata/{key} | Create or update document metadata entry
*MetadataApi* | [**put_file_metadata_entry**](docs/MetadataApi.md#put_file_metadata_entry) | **PUT** /rest/files/{fileId}/metadata/{key} | Create or update file metadata entry
*RegisterApi* | [**post_identifiers**](docs/RegisterApi.md#post_identifiers) | **POST** /task/register | 
*RegisterApi* | [**put_identifiers**](docs/RegisterApi.md#put_identifiers) | **PUT** /task/register | 
*TaskApi* | [**delete_document_recursively**](docs/TaskApi.md#delete_document_recursively) | **DELETE** /task/delete/documents/{externalId} | Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.
*TaskApi* | [**get_document_metadata**](docs/TaskApi.md#get_document_metadata) | **GET** /task/find/{externalId}/document/metadata | Find metadata of document by external ID, with header links to original and parent resource
*TaskApi* | [**get_file_metadata**](docs/TaskApi.md#get_file_metadata) | **GET** /task/find/{externalId}/file/metadata | Find metadata of file by external ID and file type, with header links to original, parent and type resource
*TaskApi* | [**get_latest_file_version_content**](docs/TaskApi.md#get_latest_file_version_content) | **GET** /task/find/{externalId}/file/contents | Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource
*TaskApi* | [**import_document_contents_for_file_with_type**](docs/TaskApi.md#import_document_contents_for_file_with_type) | **POST** /task/import/documents/{externalId}/{typeName} | Import file as the current version for {typeName} of document referenced by {externalId} without indexing
*TaskApi* | [**index_all**](docs/TaskApi.md#index_all) | **POST** /task/index/files/{type} | Index all files by type
*TaskApi* | [**index_document**](docs/TaskApi.md#index_document) | **POST** /task/index/document/{externalId}/{type} | Index file of document by externalId and file type
*TaskApi* | [**index_single_index**](docs/TaskApi.md#index_single_index) | **POST** /task/index/{name} | Index all files of a single index
*TaskApi* | [**post_identifiers**](docs/TaskApi.md#post_identifiers) | **POST** /task/register | 
*TaskApi* | [**put_identifiers**](docs/TaskApi.md#put_identifiers) | **PUT** /task/register | 
*TypesApi* | [**create_type**](docs/TypesApi.md#create_type) | **POST** /rest/types | Create type
*TypesApi* | [**delete_type**](docs/TypesApi.md#delete_type) | **DELETE** /rest/types/{id} | Delete type
*TypesApi* | [**get_type**](docs/TypesApi.md#get_type) | **GET** /rest/types/{id} | Retrieve types
*TypesApi* | [**get_types**](docs/TypesApi.md#get_types) | **GET** /rest/types | Retrieve types
*TypesApi* | [**put_type**](docs/TypesApi.md#put_type) | **PUT** /rest/types/{id} | Create or update type
*VersionsApi* | [**create_version**](docs/VersionsApi.md#create_version) | **POST** /rest/versions | Create version
*VersionsApi* | [**delete_version**](docs/VersionsApi.md#delete_version) | **DELETE** /rest/versions/{id} | Delete version
*VersionsApi* | [**delete_version_contents_is_not_allowed**](docs/VersionsApi.md#delete_version_contents_is_not_allowed) | **DELETE** /rest/versions/{versionId}/contents | Not allowed to delete contents of version: delete version instead
*VersionsApi* | [**get_version**](docs/VersionsApi.md#get_version) | **GET** /rest/versions/{id} | Retrieve version
*VersionsApi* | [**get_version_contents**](docs/VersionsApi.md#get_version_contents) | **GET** /rest/versions/{versionId}/contents | Retrieve version contents
*VersionsApi* | [**get_versions**](docs/VersionsApi.md#get_versions) | **GET** /rest/files/{fileId}/versions | Retrieve file versions, newest first
*VersionsApi* | [**post_version_contents_is_not_allowed**](docs/VersionsApi.md#post_version_contents_is_not_allowed) | **POST** /rest/versions/{versionId}/contents | Not allowed to post contents: post new version instead
*VersionsApi* | [**put_version_contents_is_not_allowed**](docs/VersionsApi.md#put_version_contents_is_not_allowed) | **PUT** /rest/versions/{versionId}/contents | Not allowed to put contents of version: post new version instead
*VersionsApi* | [**put_version_is_not_allowed**](docs/VersionsApi.md#put_version_is_not_allowed) | **PUT** /rest/versions/{id} | Not allowed to update a version: create a new version using POST


## Documentation For Models

 - [Document](docs/Document.md)
 - [FormDocument](docs/FormDocument.md)
 - [FormTextRepoFile](docs/FormTextRepoFile.md)
 - [FormType](docs/FormType.md)
 - [FormVersion](docs/FormVersion.md)
 - [ResultDocument](docs/ResultDocument.md)
 - [ResultDocumentsOverview](docs/ResultDocumentsOverview.md)
 - [ResultPage](docs/ResultPage.md)
 - [ResultPageParams](docs/ResultPageParams.md)
 - [ResultPageResultDocument](docs/ResultPageResultDocument.md)
 - [ResultTextRepoFile](docs/ResultTextRepoFile.md)
 - [ResultVersion](docs/ResultVersion.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in textrepo_client.apis and textrepo_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from textrepo_client.api.default_api import DefaultApi`
- `from textrepo_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import textrepo_client
from textrepo_client.apis import *
from textrepo_client.models import *
```

