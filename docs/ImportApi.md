# textrepo_client.ImportApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_document_contents_for_file_with_type**](ImportApi.md#import_document_contents_for_file_with_type) | **POST** /task/import/documents/{externalId}/{typeName} | Import file as the current version for {typeName} of document referenced by {externalId} without indexing


# **import_document_contents_for_file_with_type**
> import_document_contents_for_file_with_type(external_id, type_name, contents)

Import file as the current version for {typeName} of document referenced by {externalId} without indexing

### Example

```python
import time
import textrepo_client
from textrepo_client.api import import_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = import_api.ImportApi(api_client)
    external_id = "externalId_example" # str | 
    type_name = "typeName_example" # str | 
    contents = open('/path/to/file', 'rb') # file_type | 
    allow_new_document = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Import file as the current version for {typeName} of document referenced by {externalId} without indexing
        api_instance.import_document_contents_for_file_with_type(external_id, type_name, contents)
    except textrepo_client.ApiException as e:
        print("Exception when calling ImportApi->import_document_contents_for_file_with_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import file as the current version for {typeName} of document referenced by {externalId} without indexing
        api_instance.import_document_contents_for_file_with_type(external_id, type_name, contents, allow_new_document=allow_new_document)
    except textrepo_client.ApiException as e:
        print("Exception when calling ImportApi->import_document_contents_for_file_with_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  |
 **type_name** | **str**|  |
 **contents** | **file_type**|  |
 **allow_new_document** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

