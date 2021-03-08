# textrepo_client.DashboardApi

All URIs are relative to */api*

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
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.DashboardApi()

try:
    # Get document count breakdown by metadata key (yields Map: key -> count)
    api_instance.count_documents_by_metadata_key()
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_documents_by_metadata_value**
> count_documents_by_metadata_value(key)

Get document count breakdown by metadata value for given metadata key

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.DashboardApi()
key = 'key_example' # str | 

try:
    # Get document count breakdown by metadata value for given metadata key
    api_instance.count_documents_by_metadata_value(key)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_orphans**
> ResultDocument find_orphans(limit=limit, offset=offset)

Find orphans: documents with neither metadata nor any associated files

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.DashboardApi()
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)

try:
    # Find orphans: documents with neither metadata nor any associated files
    api_response = api_instance.find_orphans(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats**
> ResultDocumentsOverview get_stats()

Get document count overview

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.DashboardApi()

try:
    # Get document count overview
    api_response = api_instance.get_stats()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

