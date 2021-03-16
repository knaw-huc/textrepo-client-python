# textrepo_client.MetadataApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document_metadata_entry**](MetadataApi.md#delete_document_metadata_entry) | **DELETE** /rest/documents/{docId}/metadata/{key} | Delete document metadata entry
[**delete_file_metadata_entry**](MetadataApi.md#delete_file_metadata_entry) | **DELETE** /rest/files/{fileId}/metadata/{key} | Delete file metadata entry
[**delete_version_metadata_entry**](MetadataApi.md#delete_version_metadata_entry) | **DELETE** /rest/versions/{versionId}/metadata/{key} | Delete version metadata entry
[**get_document_metadata**](MetadataApi.md#get_document_metadata) | **GET** /rest/documents/{docId}/metadata | Retrieve document metadata
[**get_documents_given_metadata_key**](MetadataApi.md#get_documents_given_metadata_key) | **GET** /rest/metadata/{key}/documents | Find which documents have a given metadata key
[**get_file_metadata**](MetadataApi.md#get_file_metadata) | **GET** /rest/files/{fileId}/metadata | Retrieve file metadata
[**get_version_metadata**](MetadataApi.md#get_version_metadata) | **GET** /rest/versions/{versionId}/metadata | Retrieve version metadata
[**post_document_metadata_is_not_allowed**](MetadataApi.md#post_document_metadata_is_not_allowed) | **POST** /rest/documents/{docId}/metadata | Not allowed to post metadata: use put instead
[**post_file_metadata_is_not_allowed**](MetadataApi.md#post_file_metadata_is_not_allowed) | **POST** /rest/files/{fileId}/metadata | Not allowed to post metadata: use put instead
[**post_version_metadata_is_not_allowed**](MetadataApi.md#post_version_metadata_is_not_allowed) | **POST** /rest/versions/{versionId}/metadata | Not allowed to post metadata: use put instead
[**put_document_metadata_entry**](MetadataApi.md#put_document_metadata_entry) | **PUT** /rest/documents/{docId}/metadata/{key} | Create or update document metadata entry
[**put_file_metadata_entry**](MetadataApi.md#put_file_metadata_entry) | **PUT** /rest/files/{fileId}/metadata/{key} | Create or update file metadata entry
[**put_version_metadata_entry**](MetadataApi.md#put_version_metadata_entry) | **PUT** /rest/versions/{versionId}/metadata/{key} | Create or update version metadata entry


# **delete_document_metadata_entry**
> delete_document_metadata_entry(doc_id, key)

Delete document metadata entry

### Example

```python
import time
import textrepo_client
from textrepo_client.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    doc_id = "docId_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete document metadata entry
        api_instance.delete_document_metadata_entry(doc_id, key)
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->delete_document_metadata_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **str**|  |
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

# **delete_file_metadata_entry**
> delete_file_metadata_entry(file_id, key)

Delete file metadata entry

### Example

```python
import time
import textrepo_client
from textrepo_client.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    file_id = "fileId_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete file metadata entry
        api_instance.delete_file_metadata_entry(file_id, key)
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->delete_file_metadata_entry: %s\n" % e)
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

# **delete_version_metadata_entry**
> delete_version_metadata_entry(version_id, key)

Delete version metadata entry

### Example

```python
import time
import textrepo_client
from textrepo_client.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    version_id = "versionId_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete version metadata entry
        api_instance.delete_version_metadata_entry(version_id, key)
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->delete_version_metadata_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**|  |
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

# **get_document_metadata**
> {str: (str,)} get_document_metadata(doc_id)

Retrieve document metadata

### Example

```python
import time
import textrepo_client
from textrepo_client.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    doc_id = "docId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve document metadata
        api_response = api_instance.get_document_metadata(doc_id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->get_document_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **str**|  |

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
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents_given_metadata_key**
> [str] get_documents_given_metadata_key(key)

Find which documents have a given metadata key

### Example

```python
import time
import textrepo_client
from textrepo_client.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Find which documents have a given metadata key
        api_response = api_instance.get_documents_given_metadata_key(key)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->get_documents_given_metadata_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  |

### Return type

**[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_metadata**
> {str: (str,)} get_file_metadata(file_id)

Retrieve file metadata

### Example

```python
import time
import textrepo_client
from textrepo_client.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    file_id = "fileId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve file metadata
        api_response = api_instance.get_file_metadata(file_id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->get_file_metadata: %s\n" % e)
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

# **get_version_metadata**
> {str: (str,)} get_version_metadata(version_id)

Retrieve version metadata

### Example

```python
import time
import textrepo_client
from textrepo_client.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    version_id = "versionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve version metadata
        api_response = api_instance.get_version_metadata(version_id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->get_version_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**|  |

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

# **post_document_metadata_is_not_allowed**
> post_document_metadata_is_not_allowed()

Not allowed to post metadata: use put instead

### Example

```python
import time
import textrepo_client
from textrepo_client.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Not allowed to post metadata: use put instead
        api_instance.post_document_metadata_is_not_allowed()
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->post_document_metadata_is_not_allowed: %s\n" % e)
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

# **post_file_metadata_is_not_allowed**
> post_file_metadata_is_not_allowed()

Not allowed to post metadata: use put instead

### Example

```python
import time
import textrepo_client
from textrepo_client.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Not allowed to post metadata: use put instead
        api_instance.post_file_metadata_is_not_allowed()
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->post_file_metadata_is_not_allowed: %s\n" % e)
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

# **post_version_metadata_is_not_allowed**
> post_version_metadata_is_not_allowed()

Not allowed to post metadata: use put instead

### Example

```python
import time
import textrepo_client
from textrepo_client.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Not allowed to post metadata: use put instead
        api_instance.post_version_metadata_is_not_allowed()
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->post_version_metadata_is_not_allowed: %s\n" % e)
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

# **put_document_metadata_entry**
> put_document_metadata_entry(doc_id, key)

Create or update document metadata entry

### Example

```python
import time
import textrepo_client
from textrepo_client.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    doc_id = "docId_example" # str | 
    key = "key_example" # str | 
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update document metadata entry
        api_instance.put_document_metadata_entry(doc_id, key)
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->put_document_metadata_entry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update document metadata entry
        api_instance.put_document_metadata_entry(doc_id, key, body=body)
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->put_document_metadata_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **str**|  |
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

# **put_file_metadata_entry**
> put_file_metadata_entry(file_id, key)

Create or update file metadata entry

### Example

```python
import time
import textrepo_client
from textrepo_client.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    file_id = "fileId_example" # str | 
    key = "key_example" # str | 
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update file metadata entry
        api_instance.put_file_metadata_entry(file_id, key)
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->put_file_metadata_entry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update file metadata entry
        api_instance.put_file_metadata_entry(file_id, key, body=body)
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->put_file_metadata_entry: %s\n" % e)
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

# **put_version_metadata_entry**
> put_version_metadata_entry(version_id, key)

Create or update version metadata entry

### Example

```python
import time
import textrepo_client
from textrepo_client.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    version_id = "versionId_example" # str | 
    key = "key_example" # str | 
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update version metadata entry
        api_instance.put_version_metadata_entry(version_id, key)
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->put_version_metadata_entry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update version metadata entry
        api_instance.put_version_metadata_entry(version_id, key, body=body)
    except textrepo_client.ApiException as e:
        print("Exception when calling MetadataApi->put_version_metadata_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**|  |
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

