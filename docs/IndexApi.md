# textrepo_client.IndexApi

All URIs are relative to */api*

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
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.IndexApi()
type = 'type_example' # str | 

try:
    # Index all files by type
    api_instance.index_all(type)
except ApiException as e:
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
api_instance = textrepo_client.IndexApi()
external_id = 'external_id_example' # str | 
type = 'type_example' # str | 

try:
    # Index file of document by externalId and file type
    api_instance.index_document(external_id, type)
except ApiException as e:
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
api_instance = textrepo_client.IndexApi()
name = 'name_example' # str | 

try:
    # Index all files of a single index
    api_instance.index_single_index(name)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

