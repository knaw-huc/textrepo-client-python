# textrepo_client.TaskApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document_recursively**](TaskApi.md#delete_document_recursively) | **DELETE** /task/delete/documents/{externalId} | Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.
[**get_document_metadata**](TaskApi.md#get_document_metadata) | **GET** /task/find/{externalId}/document/metadata | Find metadata of document by external ID, with header links to original and parent resource
[**get_file_metadata**](TaskApi.md#get_file_metadata) | **GET** /task/find/{externalId}/file/metadata | Find metadata of file by external ID and file type, with header links to original, parent and type resource
[**get_latest_file_version_content**](TaskApi.md#get_latest_file_version_content) | **GET** /task/find/{externalId}/file/contents | Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource
[**import_document_contents_for_file_with_type**](TaskApi.md#import_document_contents_for_file_with_type) | **POST** /task/import/documents/{externalId}/{typeName} | Import file as the current version for {typeName} of document referenced by {externalId} without indexing
[**index_all**](TaskApi.md#index_all) | **POST** /task/index/files/{type} | Index all files by type
[**index_document**](TaskApi.md#index_document) | **POST** /task/index/document/{externalId}/{type} | Index file of document by externalId and file type
[**index_single_index**](TaskApi.md#index_single_index) | **POST** /task/index/{name} | Index all files of a single index
[**post_identifiers**](TaskApi.md#post_identifiers) | **POST** /task/register | 
[**put_identifiers**](TaskApi.md#put_identifiers) | **PUT** /task/register | 

# **delete_document_recursively**
> delete_document_recursively(external_id)

Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TaskApi()
external_id = 'external_id_example' # str | 

try:
    # Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.
    api_instance.delete_document_recursively(external_id)
except ApiException as e:
    print("Exception when calling TaskApi->delete_document_recursively: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_metadata**
> get_document_metadata(external_id)

Find metadata of document by external ID, with header links to original and parent resource

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TaskApi()
external_id = 'external_id_example' # str | 

try:
    # Find metadata of document by external ID, with header links to original and parent resource
    api_instance.get_document_metadata(external_id)
except ApiException as e:
    print("Exception when calling TaskApi->get_document_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_metadata**
> get_file_metadata(external_id, type)

Find metadata of file by external ID and file type, with header links to original, parent and type resource

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TaskApi()
external_id = 'external_id_example' # str | 
type = 'type_example' # str | 

try:
    # Find metadata of file by external ID and file type, with header links to original, parent and type resource
    api_instance.get_file_metadata(external_id, type)
except ApiException as e:
    print("Exception when calling TaskApi->get_file_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | 
 **type** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_file_version_content**
> get_latest_file_version_content(external_id, type)

Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TaskApi()
external_id = 'external_id_example' # str | 
type = 'type_example' # str | 

try:
    # Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource
    api_instance.get_latest_file_version_content(external_id, type)
except ApiException as e:
    print("Exception when calling TaskApi->get_latest_file_version_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | 
 **type** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_document_contents_for_file_with_type**
> import_document_contents_for_file_with_type(contents, external_id, type_name, allow_new_document=allow_new_document)

Import file as the current version for {typeName} of document referenced by {externalId} without indexing

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TaskApi()
contents = 'contents_example' # str | 
external_id = 'external_id_example' # str | 
type_name = 'type_name_example' # str | 
allow_new_document = false # bool |  (optional) (default to false)

try:
    # Import file as the current version for {typeName} of document referenced by {externalId} without indexing
    api_instance.import_document_contents_for_file_with_type(contents, external_id, type_name, allow_new_document=allow_new_document)
except ApiException as e:
    print("Exception when calling TaskApi->import_document_contents_for_file_with_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contents** | **str**|  | 
 **external_id** | **str**|  | 
 **type_name** | **str**|  | 
 **allow_new_document** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_all**
> index_all(type)

Index all files by type

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TaskApi()
type = 'type_example' # str | 

try:
    # Index all files by type
    api_instance.index_all(type)
except ApiException as e:
    print("Exception when calling TaskApi->index_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_document**
> index_document(external_id, type)

Index file of document by externalId and file type

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TaskApi()
external_id = 'external_id_example' # str | 
type = 'type_example' # str | 

try:
    # Index file of document by externalId and file type
    api_instance.index_document(external_id, type)
except ApiException as e:
    print("Exception when calling TaskApi->index_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | 
 **type** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_single_index**
> index_single_index(name)

Index all files of a single index

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TaskApi()
name = 'name_example' # str | 

try:
    # Index all files of a single index
    api_instance.index_single_index(name)
except ApiException as e:
    print("Exception when calling TaskApi->index_single_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identifiers**
> list[Document] post_identifiers(body=body)



### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TaskApi()
body = textrepo_client.InputStream() # InputStream |  (optional)

try:
    api_response = api_instance.post_identifiers(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->post_identifiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputStream**](InputStream.md)|  | [optional] 

### Return type

[**list[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_identifiers**
> list[Document] put_identifiers(body=body)



### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TaskApi()
body = textrepo_client.InputStream() # InputStream |  (optional)

try:
    api_response = api_instance.put_identifiers(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->put_identifiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputStream**](InputStream.md)|  | [optional] 

### Return type

[**list[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

