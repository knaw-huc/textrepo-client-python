# textrepo_client.TaskApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document_recursively**](TaskApi.md#delete_document_recursively) | **DELETE** /task/delete/documents/{externalId} | Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.
[**get_document_metadata_for_external_id**](TaskApi.md#get_document_metadata_for_external_id) | **GET** /task/find/{externalId}/document/metadata | Find metadata of document by external ID, with header links to original and parent resource
[**get_file_metadata_for_external_id**](TaskApi.md#get_file_metadata_for_external_id) | **GET** /task/find/{externalId}/file/metadata | Find metadata of file by external ID and file type, with header links to original, parent and type resource
[**get_latest_file_version_content**](TaskApi.md#get_latest_file_version_content) | **GET** /task/find/{externalId}/file/contents | Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource
[**import_document_contents_for_file_with_type**](TaskApi.md#import_document_contents_for_file_with_type) | **POST** /task/import/documents/{externalId}/{typeName} | Import file as the current version for {typeName} of document referenced by {externalId} without indexing
[**index_all**](TaskApi.md#index_all) | **POST** /task/index/files/{type} | Index all files by type
[**index_document**](TaskApi.md#index_document) | **POST** /task/index/document/{externalId}/{type} | Index file of document by externalId and file type
[**index_single_index**](TaskApi.md#index_single_index) | **POST** /task/index/{name} | Index or reindex single index with all relevant files, including those without versions


# **delete_document_recursively**
> delete_document_recursively(external_id)

Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.

### Example

```python
import time
import textrepo_client
from textrepo_client.api import task_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)
    external_id = "externalId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.
        api_instance.delete_document_recursively(external_id)
    except textrepo_client.ApiException as e:
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


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_metadata_for_external_id**
> {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)} get_document_metadata_for_external_id(external_id)

Find metadata of document by external ID, with header links to original and parent resource

### Example

```python
import time
import textrepo_client
from textrepo_client.api import task_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)
    external_id = "externalId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Find metadata of document by external ID, with header links to original and parent resource
        api_response = api_instance.get_document_metadata_for_external_id(external_id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling TaskApi->get_document_metadata_for_external_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  |

### Return type

**{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Given document could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_metadata_for_external_id**
> {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)} get_file_metadata_for_external_id(external_id)

Find metadata of file by external ID and file type, with header links to original, parent and type resource

### Example

```python
import time
import textrepo_client
from textrepo_client.api import task_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)
    external_id = "externalId_example" # str | 
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Find metadata of file by external ID and file type, with header links to original, parent and type resource
        api_response = api_instance.get_file_metadata_for_external_id(external_id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling TaskApi->get_file_metadata_for_external_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find metadata of file by external ID and file type, with header links to original, parent and type resource
        api_response = api_instance.get_file_metadata_for_external_id(external_id, type=type)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling TaskApi->get_file_metadata_for_external_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  |
 **type** | **str**|  | [optional]

### Return type

**{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Given file could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_file_version_content**
> {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)} get_latest_file_version_content(external_id)

Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource

### Example

```python
import time
import textrepo_client
from textrepo_client.api import task_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)
    external_id = "externalId_example" # str | 
    accept_encoding = "Accept-Encoding_example" # str |  (optional)
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource
        api_response = api_instance.get_latest_file_version_content(external_id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling TaskApi->get_latest_file_version_content: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource
        api_response = api_instance.get_latest_file_version_content(external_id, accept_encoding=accept_encoding, type=type)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling TaskApi->get_latest_file_version_content: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  |
 **accept_encoding** | **str**|  | [optional]
 **type** | **str**|  | [optional]

### Return type

**{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Given type, document or supposed contents could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_document_contents_for_file_with_type**
> import_document_contents_for_file_with_type(external_id, type_name)

Import file as the current version for {typeName} of document referenced by {externalId} without indexing

### Example

```python
import time
import textrepo_client
from textrepo_client.api import task_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)
    external_id = "externalId_example" # str | 
    type_name = "typeName_example" # str | 
    allow_new_document = False # bool |  (optional) if omitted the server will use the default value of False
    type = "type_example" # str |  (optional)
    file_name = "file_name_example" # str |  (optional)
    creation_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    modification_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    read_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    size = 1 # int |  (optional)
    name = "name_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import file as the current version for {typeName} of document referenced by {externalId} without indexing
        api_instance.import_document_contents_for_file_with_type(external_id, type_name)
    except textrepo_client.ApiException as e:
        print("Exception when calling TaskApi->import_document_contents_for_file_with_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import file as the current version for {typeName} of document referenced by {externalId} without indexing
        api_instance.import_document_contents_for_file_with_type(external_id, type_name, allow_new_document=allow_new_document, type=type, file_name=file_name, creation_date=creation_date, modification_date=modification_date, read_date=read_date, size=size, name=name)
    except textrepo_client.ApiException as e:
        print("Exception when calling TaskApi->import_document_contents_for_file_with_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  |
 **type_name** | **str**|  |
 **allow_new_document** | **bool**|  | [optional] if omitted the server will use the default value of False
 **type** | **str**|  | [optional]
 **file_name** | **str**|  | [optional]
 **creation_date** | **datetime**|  | [optional]
 **modification_date** | **datetime**|  | [optional]
 **read_date** | **datetime**|  | [optional]
 **size** | **int**|  | [optional]
 **name** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_all**
> index_all(type)

Index all files by type

### Example

```python
import time
import textrepo_client
from textrepo_client.api import task_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)
    type = "type_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Index all files by type
        api_instance.index_all(type)
    except textrepo_client.ApiException as e:
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


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_document**
> index_document(external_id, type)

Index file of document by externalId and file type

### Example

```python
import time
import textrepo_client
from textrepo_client.api import task_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)
    external_id = "externalId_example" # str | 
    type = "type_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Index file of document by externalId and file type
        api_instance.index_document(external_id, type)
    except textrepo_client.ApiException as e:
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


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_single_index**
> index_single_index(name)

Index or reindex single index with all relevant files, including those without versions

### Example

```python
import time
import textrepo_client
from textrepo_client.api import task_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Index or reindex single index with all relevant files, including those without versions
        api_instance.index_single_index(name)
    except textrepo_client.ApiException as e:
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


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

