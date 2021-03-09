# textrepo_client.IndexApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_all**](IndexApi.md#index_all) | **POST** /task/index/files/{type} | Index all files by type
[**index_document**](IndexApi.md#index_document) | **POST** /task/index/document/{externalId}/{type} | Index file of document by externalId and file type
[**index_single_index**](IndexApi.md#index_single_index) | **POST** /task/index/{name} | Index all files of a single index


# **index_all**
> index_all(type)

Index all files by type

### Example

```python
import time
import textrepo_client
from textrepo_client.api import index_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = index_api.IndexApi(api_client)
    type = "type_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Index all files by type
        api_instance.index_all(type)
    except textrepo_client.ApiException as e:
        print("Exception when calling IndexApi->index_all: %s\n" % e)
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
from textrepo_client.api import index_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = index_api.IndexApi(api_client)
    external_id = "externalId_example" # str | 
    type = "type_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Index file of document by externalId and file type
        api_instance.index_document(external_id, type)
    except textrepo_client.ApiException as e:
        print("Exception when calling IndexApi->index_document: %s\n" % e)
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

Index all files of a single index

### Example

```python
import time
import textrepo_client
from textrepo_client.api import index_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = index_api.IndexApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Index all files of a single index
        api_instance.index_single_index(name)
    except textrepo_client.ApiException as e:
        print("Exception when calling IndexApi->index_single_index: %s\n" % e)
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

