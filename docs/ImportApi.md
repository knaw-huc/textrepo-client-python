# textrepo_client.ImportApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_document_contents_for_file_with_type**](ImportApi.md#import_document_contents_for_file_with_type) | **POST** /task/import/documents/{externalId}/{typeName} | Import file as the current version for {typeName} of document referenced by {externalId} without indexing

# **import_document_contents_for_file_with_type**
> import_document_contents_for_file_with_type(contents, external_id, type_name, allow_new_document=allow_new_document)

Import file as the current version for {typeName} of document referenced by {externalId} without indexing

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.ImportApi()
contents = 'contents_example' # str | 
external_id = 'external_id_example' # str | 
type_name = 'type_name_example' # str | 
allow_new_document = false # bool |  (optional) (default to false)

try:
    # Import file as the current version for {typeName} of document referenced by {externalId} without indexing
    api_instance.import_document_contents_for_file_with_type(contents, external_id, type_name, allow_new_document=allow_new_document)
except ApiException as e:
    print("Exception when calling ImportApi->import_document_contents_for_file_with_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contents** | **str**|  | 
 **external_id** | **str**|  | 
 **type_name** | **str**|  | 
 **allow_new_document** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

