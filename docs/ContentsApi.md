# textrepo_client.ContentsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_version_contents_is_not_allowed**](ContentsApi.md#delete_version_contents_is_not_allowed) | **DELETE** /rest/versions/{versionId}/contents | Not allowed to delete contents of version: delete version instead
[**get_contents**](ContentsApi.md#get_contents) | **GET** /rest/contents/{sha} | Retrieve contents
[**get_version_contents**](ContentsApi.md#get_version_contents) | **GET** /rest/versions/{versionId}/contents | Retrieve version contents
[**post_version_contents_is_not_allowed**](ContentsApi.md#post_version_contents_is_not_allowed) | **POST** /rest/versions/{versionId}/contents | Not allowed to post contents: post new version instead
[**put_version_contents_is_not_allowed**](ContentsApi.md#put_version_contents_is_not_allowed) | **PUT** /rest/versions/{versionId}/contents | Not allowed to put contents of version: post new version instead


# **delete_version_contents_is_not_allowed**
> delete_version_contents_is_not_allowed()

Not allowed to delete contents of version: delete version instead

### Example

```python
import time
import textrepo_client
from textrepo_client.api import contents_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = contents_api.ContentsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Not allowed to delete contents of version: delete version instead
        api_instance.delete_version_contents_is_not_allowed()
    except textrepo_client.ApiException as e:
        print("Exception when calling ContentsApi->delete_version_contents_is_not_allowed: %s\n" % e)
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

# **get_contents**
> [str] get_contents(sha)

Retrieve contents

### Example

```python
import time
import textrepo_client
from textrepo_client.api import contents_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = contents_api.ContentsApi(api_client)
    sha = "sha_example" # str | 
    accept_encoding = "Accept-Encoding_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve contents
        api_response = api_instance.get_contents(sha)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling ContentsApi->get_contents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve contents
        api_response = api_instance.get_contents(sha, accept_encoding=accept_encoding)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling ContentsApi->get_contents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sha** | **str**|  |
 **accept_encoding** | **str**|  | [optional]

### Return type

**[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json


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
from textrepo_client.api import contents_api
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
    api_instance = contents_api.ContentsApi(api_client)
    version_id = "versionId_example" # str | 
    accept_encoding = "Accept-Encoding_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve version contents
        api_response = api_instance.get_version_contents(version_id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling ContentsApi->get_version_contents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve version contents
        api_response = api_instance.get_version_contents(version_id, accept_encoding=accept_encoding)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling ContentsApi->get_version_contents: %s\n" % e)
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

# **post_version_contents_is_not_allowed**
> post_version_contents_is_not_allowed()

Not allowed to post contents: post new version instead

### Example

```python
import time
import textrepo_client
from textrepo_client.api import contents_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = contents_api.ContentsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Not allowed to post contents: post new version instead
        api_instance.post_version_contents_is_not_allowed()
    except textrepo_client.ApiException as e:
        print("Exception when calling ContentsApi->post_version_contents_is_not_allowed: %s\n" % e)
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

# **put_version_contents_is_not_allowed**
> put_version_contents_is_not_allowed()

Not allowed to put contents of version: post new version instead

### Example

```python
import time
import textrepo_client
from textrepo_client.api import contents_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = contents_api.ContentsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Not allowed to put contents of version: post new version instead
        api_instance.put_version_contents_is_not_allowed()
    except textrepo_client.ApiException as e:
        print("Exception when calling ContentsApi->put_version_contents_is_not_allowed: %s\n" % e)
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

