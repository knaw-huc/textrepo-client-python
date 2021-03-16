# textrepo_client.FindApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_document_metadata_for_external_id**](FindApi.md#get_document_metadata_for_external_id) | **GET** /task/find/{externalId}/document/metadata | Find metadata of document by external ID, with header links to original and parent resource
[**get_file_metadata_for_external_id**](FindApi.md#get_file_metadata_for_external_id) | **GET** /task/find/{externalId}/file/metadata | Find metadata of file by external ID and file type, with header links to original, parent and type resource
[**get_latest_file_version_content**](FindApi.md#get_latest_file_version_content) | **GET** /task/find/{externalId}/file/contents | Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource


# **get_document_metadata_for_external_id**
> get_document_metadata_for_external_id(external_id)

Find metadata of document by external ID, with header links to original and parent resource

### Example

```python
import time
import textrepo_client
from textrepo_client.api import find_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = find_api.FindApi(api_client)
    external_id = "externalId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Find metadata of document by external ID, with header links to original and parent resource
        api_instance.get_document_metadata_for_external_id(external_id)
    except textrepo_client.ApiException as e:
        print("Exception when calling FindApi->get_document_metadata_for_external_id: %s\n" % e)
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
**200** | OK |  -  |
**404** | Given document could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_metadata_for_external_id**
> get_file_metadata_for_external_id(external_id, type)

Find metadata of file by external ID and file type, with header links to original, parent and type resource

### Example

```python
import time
import textrepo_client
from textrepo_client.api import find_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = find_api.FindApi(api_client)
    external_id = "externalId_example" # str | 
    type = "type_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Find metadata of file by external ID and file type, with header links to original, parent and type resource
        api_instance.get_file_metadata_for_external_id(external_id, type)
    except textrepo_client.ApiException as e:
        print("Exception when calling FindApi->get_file_metadata_for_external_id: %s\n" % e)
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
**200** | OK |  -  |
**404** | Given file could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_file_version_content**
> get_latest_file_version_content(external_id, type)

Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource

### Example

```python
import time
import textrepo_client
from textrepo_client.api import find_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = find_api.FindApi(api_client)
    external_id = "externalId_example" # str | 
    type = "type_example" # str | 
    accept_encoding = "Accept-Encoding_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource
        api_instance.get_latest_file_version_content(external_id, type)
    except textrepo_client.ApiException as e:
        print("Exception when calling FindApi->get_latest_file_version_content: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource
        api_instance.get_latest_file_version_content(external_id, type, accept_encoding=accept_encoding)
    except textrepo_client.ApiException as e:
        print("Exception when calling FindApi->get_latest_file_version_content: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  |
 **type** | **str**|  |
 **accept_encoding** | **str**|  | [optional]

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
**404** | Given type, document or supposed contents could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

