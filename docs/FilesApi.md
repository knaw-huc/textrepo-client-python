# textrepo_client.FilesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](FilesApi.md#create_file) | **POST** /rest/files | Create file
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /rest/files/{id} | Delete file
[**delete_file_metadata_entry**](FilesApi.md#delete_file_metadata_entry) | **DELETE** /rest/files/{fileId}/metadata/{key} | Delete file metadata entry
[**get_file**](FilesApi.md#get_file) | **GET** /rest/files/{id} | Retrieve file
[**get_file_metadata**](FilesApi.md#get_file_metadata) | **GET** /rest/files/{fileId}/metadata | Retrieve file metadata
[**get_file_versions**](FilesApi.md#get_file_versions) | **GET** /rest/files/{fileId}/versions | Retrieve file versions, newest first
[**post_file_metadata_is_not_allowed**](FilesApi.md#post_file_metadata_is_not_allowed) | **POST** /rest/files/{fileId}/metadata | Not allowed to post metadata: use put instead
[**put_file**](FilesApi.md#put_file) | **PUT** /rest/files/{id} | Create or update file
[**put_file_metadata_entry**](FilesApi.md#put_file_metadata_entry) | **PUT** /rest/files/{fileId}/metadata/{key} | Create or update file metadata entry


# **create_file**
> ResultTextRepoFile create_file()

Create file

### Example

```python
import time
import textrepo_client
from textrepo_client.api import files_api
from textrepo_client.model.result_text_repo_file import ResultTextRepoFile
from textrepo_client.model.form_text_repo_file import FormTextRepoFile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    body = FormTextRepoFile(
        doc_id="doc_id_example",
        type_id=1,
    ) # FormTextRepoFile |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create file
        api_response = api_instance.create_file(body=body)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling FilesApi->create_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FormTextRepoFile**](FormTextRepoFile.md)|  | [optional]

### Return type

[**ResultTextRepoFile**](ResultTextRepoFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(id)

Delete file

### Example

```python
import time
import textrepo_client
from textrepo_client.api import files_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete file
        api_instance.delete_file(id)
    except textrepo_client.ApiException as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file_metadata_entry**
> delete_file_metadata_entry(file_id, key)

Delete file metadata entry

### Example

```python
import time
import textrepo_client
from textrepo_client.api import files_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    file_id = "fileId_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete file metadata entry
        api_instance.delete_file_metadata_entry(file_id, key)
    except textrepo_client.ApiException as e:
        print("Exception when calling FilesApi->delete_file_metadata_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  |
 **key** | **str**|  |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> ResultTextRepoFile get_file(id)

Retrieve file

### Example

```python
import time
import textrepo_client
from textrepo_client.api import files_api
from textrepo_client.model.result_text_repo_file import ResultTextRepoFile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve file
        api_response = api_instance.get_file(id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ResultTextRepoFile**](ResultTextRepoFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_metadata**
> {str: (str,)} get_file_metadata(file_id)

Retrieve file metadata

### Example

```python
import time
import textrepo_client
from textrepo_client.api import files_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    file_id = "fileId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve file metadata
        api_response = api_instance.get_file_metadata(file_id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling FilesApi->get_file_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  |

### Return type

**{str: (str,)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_versions**
> ResultVersion get_file_versions(file_id)

Retrieve file versions, newest first

### Example

```python
import time
import textrepo_client
from textrepo_client.api import files_api
from textrepo_client.model.result_version import ResultVersion
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    file_id = "fileId_example" # str | 
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve file versions, newest first
        api_response = api_instance.get_file_versions(file_id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling FilesApi->get_file_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve file versions, newest first
        api_response = api_instance.get_file_versions(file_id, limit=limit, offset=offset, created_after=created_after)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling FilesApi->get_file_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  |
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **created_after** | **datetime**|  | [optional]

### Return type

[**ResultVersion**](ResultVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_file_metadata_is_not_allowed**
> post_file_metadata_is_not_allowed()

Not allowed to post metadata: use put instead

### Example

```python
import time
import textrepo_client
from textrepo_client.api import files_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Not allowed to post metadata: use put instead
        api_instance.post_file_metadata_is_not_allowed()
    except textrepo_client.ApiException as e:
        print("Exception when calling FilesApi->post_file_metadata_is_not_allowed: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**405** | Not allowed to post metadata: use put instead |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_file**
> ResultTextRepoFile put_file(id)

Create or update file

### Example

```python
import time
import textrepo_client
from textrepo_client.api import files_api
from textrepo_client.model.result_text_repo_file import ResultTextRepoFile
from textrepo_client.model.form_text_repo_file import FormTextRepoFile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    id = "id_example" # str | 
    body = FormTextRepoFile(
        doc_id="doc_id_example",
        type_id=1,
    ) # FormTextRepoFile |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update file
        api_response = api_instance.put_file(id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling FilesApi->put_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update file
        api_response = api_instance.put_file(id, body=body)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling FilesApi->put_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **body** | [**FormTextRepoFile**](FormTextRepoFile.md)|  | [optional]

### Return type

[**ResultTextRepoFile**](ResultTextRepoFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_file_metadata_entry**
> put_file_metadata_entry(file_id, key)

Create or update file metadata entry

### Example

```python
import time
import textrepo_client
from textrepo_client.api import files_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    file_id = "fileId_example" # str | 
    key = "key_example" # str | 
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update file metadata entry
        api_instance.put_file_metadata_entry(file_id, key)
    except textrepo_client.ApiException as e:
        print("Exception when calling FilesApi->put_file_metadata_entry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update file metadata entry
        api_instance.put_file_metadata_entry(file_id, key, body=body)
    except textrepo_client.ApiException as e:
        print("Exception when calling FilesApi->put_file_metadata_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  |
 **key** | **str**|  |
 **body** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

