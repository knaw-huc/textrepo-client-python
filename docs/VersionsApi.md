# textrepo_client.VersionsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_version**](VersionsApi.md#create_version) | **POST** /rest/versions | Create version
[**delete_version**](VersionsApi.md#delete_version) | **DELETE** /rest/versions/{id} | Delete version
[**delete_version_contents_is_not_allowed**](VersionsApi.md#delete_version_contents_is_not_allowed) | **DELETE** /rest/versions/{versionId}/contents | Not allowed to delete contents of version: delete version instead
[**delete_version_metadata_entry**](VersionsApi.md#delete_version_metadata_entry) | **DELETE** /rest/versions/{versionId}/metadata/{key} | Delete version metadata entry
[**get_file_versions**](VersionsApi.md#get_file_versions) | **GET** /rest/files/{fileId}/versions | Retrieve file versions, newest first
[**get_version**](VersionsApi.md#get_version) | **GET** /rest/versions/{id} | Retrieve version
[**get_version_contents**](VersionsApi.md#get_version_contents) | **GET** /rest/versions/{versionId}/contents | Retrieve version contents
[**get_version_metadata**](VersionsApi.md#get_version_metadata) | **GET** /rest/versions/{versionId}/metadata | Retrieve version metadata
[**post_version_contents_is_not_allowed**](VersionsApi.md#post_version_contents_is_not_allowed) | **POST** /rest/versions/{versionId}/contents | Not allowed to post contents: post new version instead
[**post_version_metadata_is_not_allowed**](VersionsApi.md#post_version_metadata_is_not_allowed) | **POST** /rest/versions/{versionId}/metadata | Not allowed to post metadata: use put instead
[**put_version_contents_is_not_allowed**](VersionsApi.md#put_version_contents_is_not_allowed) | **PUT** /rest/versions/{versionId}/contents | Not allowed to put contents of version: post new version instead
[**put_version_is_not_allowed**](VersionsApi.md#put_version_is_not_allowed) | **PUT** /rest/versions/{id} | Not allowed to update a version: create a new version using POST
[**put_version_metadata_entry**](VersionsApi.md#put_version_metadata_entry) | **PUT** /rest/versions/{versionId}/metadata/{key} | Create or update version metadata entry


# **create_version**
> ResultVersion create_version()

Create version

### Example

```python
import time
import textrepo_client
from textrepo_client.api import versions_api
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
    api_instance = versions_api.VersionsApi(api_client)
    file_id = "file_id_example" # str |  (optional)
    contents = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create version
        api_response = api_instance.create_version(file_id=file_id, contents=contents)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->create_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | [optional]
 **contents** | **file_type**|  | [optional]

### Return type

[**ResultVersion**](ResultVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version**
> delete_version(id)

Delete version

### Example

```python
import time
import textrepo_client
from textrepo_client.api import versions_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete version
        api_instance.delete_version(id)
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->delete_version: %s\n" % e)
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

# **delete_version_contents_is_not_allowed**
> delete_version_contents_is_not_allowed()

Not allowed to delete contents of version: delete version instead

### Example

```python
import time
import textrepo_client
from textrepo_client.api import versions_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Not allowed to delete contents of version: delete version instead
        api_instance.delete_version_contents_is_not_allowed()
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->delete_version_contents_is_not_allowed: %s\n" % e)
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
**405** | Not allowed to delete contents of version: delete version instead |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version_metadata_entry**
> delete_version_metadata_entry(version_id, key)

Delete version metadata entry

### Example

```python
import time
import textrepo_client
from textrepo_client.api import versions_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)
    version_id = "versionId_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete version metadata entry
        api_instance.delete_version_metadata_entry(version_id, key)
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->delete_version_metadata_entry: %s\n" % e)
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

# **get_file_versions**
> ResultVersion get_file_versions(file_id)

Retrieve file versions, newest first

### Example

```python
import time
import textrepo_client
from textrepo_client.api import versions_api
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
    api_instance = versions_api.VersionsApi(api_client)
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
        print("Exception when calling VersionsApi->get_file_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve file versions, newest first
        api_response = api_instance.get_file_versions(file_id, limit=limit, offset=offset, created_after=created_after)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->get_file_versions: %s\n" % e)
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

# **get_version**
> ResultVersion get_version(id)

Retrieve version

### Example

```python
import time
import textrepo_client
from textrepo_client.api import versions_api
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
    api_instance = versions_api.VersionsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve version
        api_response = api_instance.get_version(id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->get_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get_version_contents**
> ResultVersion get_version_contents(version_id)

Retrieve version contents

### Example

```python
import time
import textrepo_client
from textrepo_client.api import versions_api
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
    api_instance = versions_api.VersionsApi(api_client)
    version_id = "versionId_example" # str | 
    accept_encoding = "Accept-Encoding_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve version contents
        api_response = api_instance.get_version_contents(version_id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->get_version_contents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve version contents
        api_response = api_instance.get_version_contents(version_id, accept_encoding=accept_encoding)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->get_version_contents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**|  |
 **accept_encoding** | **str**|  | [optional]

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

# **get_version_metadata**
> {str: (str,)} get_version_metadata(version_id)

Retrieve version metadata

### Example

```python
import time
import textrepo_client
from textrepo_client.api import versions_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)
    version_id = "versionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve version metadata
        api_response = api_instance.get_version_metadata(version_id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->get_version_metadata: %s\n" % e)
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

# **post_version_contents_is_not_allowed**
> post_version_contents_is_not_allowed()

Not allowed to post contents: post new version instead

### Example

```python
import time
import textrepo_client
from textrepo_client.api import versions_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Not allowed to post contents: post new version instead
        api_instance.post_version_contents_is_not_allowed()
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->post_version_contents_is_not_allowed: %s\n" % e)
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
**405** | Not allowed to post contents: post new version instead |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_version_metadata_is_not_allowed**
> post_version_metadata_is_not_allowed()

Not allowed to post metadata: use put instead

### Example

```python
import time
import textrepo_client
from textrepo_client.api import versions_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Not allowed to post metadata: use put instead
        api_instance.post_version_metadata_is_not_allowed()
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->post_version_metadata_is_not_allowed: %s\n" % e)
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

# **put_version_contents_is_not_allowed**
> put_version_contents_is_not_allowed()

Not allowed to put contents of version: post new version instead

### Example

```python
import time
import textrepo_client
from textrepo_client.api import versions_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Not allowed to put contents of version: post new version instead
        api_instance.put_version_contents_is_not_allowed()
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->put_version_contents_is_not_allowed: %s\n" % e)
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
**405** | Not allowed to put contents of version: post new version instead |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_version_is_not_allowed**
> put_version_is_not_allowed(id)

Not allowed to update a version: create a new version using POST

### Example

```python
import time
import textrepo_client
from textrepo_client.api import versions_api
from textrepo_client.model.form_version import FormVersion
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)
    id = "id_example" # str | 
    body = FormVersion(
        external_id="external_id_example",
    ) # FormVersion |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Not allowed to update a version: create a new version using POST
        api_instance.put_version_is_not_allowed(id)
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->put_version_is_not_allowed: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Not allowed to update a version: create a new version using POST
        api_instance.put_version_is_not_allowed(id, body=body)
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->put_version_is_not_allowed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **body** | [**FormVersion**](FormVersion.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**405** | Not allowed to update a version: create a new version using POST |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_version_metadata_entry**
> put_version_metadata_entry(version_id, key)

Create or update version metadata entry

### Example

```python
import time
import textrepo_client
from textrepo_client.api import versions_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)
    version_id = "versionId_example" # str | 
    key = "key_example" # str | 
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update version metadata entry
        api_instance.put_version_metadata_entry(version_id, key)
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->put_version_metadata_entry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update version metadata entry
        api_instance.put_version_metadata_entry(version_id, key, body=body)
    except textrepo_client.ApiException as e:
        print("Exception when calling VersionsApi->put_version_metadata_entry: %s\n" % e)
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

