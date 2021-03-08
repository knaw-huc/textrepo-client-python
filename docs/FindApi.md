# textrepo_client.FindApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_document_metadata**](FindApi.md#get_document_metadata) | **GET** /task/find/{externalId}/document/metadata | Find metadata of document by external ID, with header links to original and parent resource
[**get_file_metadata**](FindApi.md#get_file_metadata) | **GET** /task/find/{externalId}/file/metadata | Find metadata of file by external ID and file type, with header links to original, parent and type resource
[**get_latest_file_version_content**](FindApi.md#get_latest_file_version_content) | **GET** /task/find/{externalId}/file/contents | Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource

# **get_document_metadata**
> get_document_metadata(external_id)

Find metadata of document by external ID, with header links to original and parent resource

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.FindApi()
external_id = 'external_id_example' # str | 

try:
    # Find metadata of document by external ID, with header links to original and parent resource
    api_instance.get_document_metadata(external_id)
except ApiException as e:
    print("Exception when calling FindApi->get_document_metadata: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_metadata**
> get_file_metadata(external_id, type)

Find metadata of file by external ID and file type, with header links to original, parent and type resource

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.FindApi()
external_id = 'external_id_example' # str | 
type = 'type_example' # str | 

try:
    # Find metadata of file by external ID and file type, with header links to original, parent and type resource
    api_instance.get_file_metadata(external_id, type)
except ApiException as e:
    print("Exception when calling FindApi->get_file_metadata: %s\n" % e)
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

# **get_latest_file_version_content**
> get_latest_file_version_content(external_id, type, accept_encoding=accept_encoding)

Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.FindApi()
external_id = 'external_id_example' # str | 
type = 'type_example' # str | 
accept_encoding = 'accept_encoding_example' # str |  (optional)

try:
    # Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource
    api_instance.get_latest_file_version_content(external_id, type, accept_encoding=accept_encoding)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

