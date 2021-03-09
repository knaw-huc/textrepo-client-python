# textrepo_client.DashboardApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_documents_by_metadata_key**](DashboardApi.md#count_documents_by_metadata_key) | **GET** /dashboard/metadata | Get document count breakdown by metadata key (yields Map: key -&gt; count)
[**count_documents_by_metadata_value**](DashboardApi.md#count_documents_by_metadata_value) | **GET** /dashboard/metadata/{key} | Get document count breakdown by metadata value for given metadata key
[**find_orphans**](DashboardApi.md#find_orphans) | **GET** /dashboard/orphans | Find orphans: documents with neither metadata nor any associated files
[**get_stats**](DashboardApi.md#get_stats) | **GET** /dashboard | Get document count overview


# **count_documents_by_metadata_key**
> count_documents_by_metadata_key()

Get document count breakdown by metadata key (yields Map: key -> count)

### Example

```python
import time
import textrepo_client
from textrepo_client.api import dashboard_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dashboard_api.DashboardApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get document count breakdown by metadata key (yields Map: key -> count)
        api_instance.count_documents_by_metadata_key()
    except textrepo_client.ApiException as e:
        print("Exception when calling DashboardApi->count_documents_by_metadata_key: %s\n" % e)
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
**200** | OK. Body contains Map: String key -&gt; int count |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_documents_by_metadata_value**
> count_documents_by_metadata_value(key)

Get document count breakdown by metadata value for given metadata key

### Example

```python
import time
import textrepo_client
from textrepo_client.api import dashboard_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dashboard_api.DashboardApi(api_client)
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get document count breakdown by metadata value for given metadata key
        api_instance.count_documents_by_metadata_value(key)
    except textrepo_client.ApiException as e:
        print("Exception when calling DashboardApi->count_documents_by_metadata_value: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | OK. Body contains Map: String value -&gt; int count. Link rel&#x3D;&#39;collection&#39; to relevant documents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_orphans**
> ResultDocument find_orphans()

Find orphans: documents with neither metadata nor any associated files

### Example

```python
import time
import textrepo_client
from textrepo_client.api import dashboard_api
from textrepo_client.model.result_document import ResultDocument
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dashboard_api.DashboardApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find orphans: documents with neither metadata nor any associated files
        api_response = api_instance.find_orphans(limit=limit, offset=offset)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling DashboardApi->find_orphans: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]

### Return type

[**ResultDocument**](ResultDocument.md)

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

# **get_stats**
> ResultDocumentsOverview get_stats()

Get document count overview

### Example

```python
import time
import textrepo_client
from textrepo_client.api import dashboard_api
from textrepo_client.model.result_documents_overview import ResultDocumentsOverview
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dashboard_api.DashboardApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get document count overview
        api_response = api_instance.get_stats()
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling DashboardApi->get_stats: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ResultDocumentsOverview**](ResultDocumentsOverview.md)

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

