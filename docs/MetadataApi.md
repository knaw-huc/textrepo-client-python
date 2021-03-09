# textrepo_client.MetadataApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document_metadata_entry**](MetadataApi.md#delete_document_metadata_entry) | **DELETE** /rest/documents/{docId}/metadata/{key} | Delete document metadata entry
[**delete_file_metadata_entry**](MetadataApi.md#delete_file_metadata_entry) | **DELETE** /rest/files/{fileId}/metadata/{key} | Delete file metadata entry
[**get_document_metadata**](MetadataApi.md#get_document_metadata) | **GET** /rest/documents/{docId}/metadata | Retrieve document metadata
[**get_documents_given_metadata_key**](MetadataApi.md#get_documents_given_metadata_key) | **GET** /rest/metadata/{key}/documents | Find which documents have a given metadata key
[**get_file_metadata**](MetadataApi.md#get_file_metadata) | **GET** /rest/files/{fileId}/metadata | Retrieve file metadata
[**post_document_metadata_is_not_allowed**](MetadataApi.md#post_document_metadata_is_not_allowed) | **POST** /rest/documents/{docId}/metadata | Not allowed to post metadata: use put instead
[**post_metadata_is_not_allowed**](MetadataApi.md#post_metadata_is_not_allowed) | **POST** /rest/files/{fileId}/metadata | Not allowed to post metadata: use put instead
[**put_document_metadata_entry**](MetadataApi.md#put_document_metadata_entry) | **PUT** /rest/documents/{docId}/metadata/{key} | Create or update document metadata entry
[**put_file_metadata_entry**](MetadataApi.md#put_file_metadata_entry) | **PUT** /rest/files/{fileId}/metadata/{key} | Create or update file metadata entry

# **delete_document_metadata_entry**
> delete_document_metadata_entry(doc_id, key)

Delete document metadata entry

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.MetadataApi()
doc_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
key = 'key_example' # str | 

try:
    # Delete document metadata entry
    api_instance.delete_document_metadata_entry(doc_id, key)
except ApiException as e:
    print("Exception when calling MetadataApi->delete_document_metadata_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | [**str**](.md)|  | 
 **key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file_metadata_entry**
> delete_file_metadata_entry(file_id, key)

Delete file metadata entry

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.MetadataApi()
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
key = 'key_example' # str | 

try:
    # Delete file metadata entry
    api_instance.delete_file_metadata_entry(file_id, key)
except ApiException as e:
    print("Exception when calling MetadataApi->delete_file_metadata_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | [**str**](.md)|  | 
 **key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_metadata**
> dict(str, str) get_document_metadata(doc_id)

Retrieve document metadata

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.MetadataApi()
doc_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve document metadata
    api_response = api_instance.get_document_metadata(doc_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_document_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | [**str**](.md)|  | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents_given_metadata_key**
> list[str] get_documents_given_metadata_key(key)

Find which documents have a given metadata key

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.MetadataApi()
key = 'key_example' # str | 

try:
    # Find which documents have a given metadata key
    api_response = api_instance.get_documents_given_metadata_key(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_documents_given_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_metadata**
> dict(str, str) get_file_metadata(file_id)

Retrieve file metadata

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.MetadataApi()
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve file metadata
    api_response = api_instance.get_file_metadata(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_file_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | [**str**](.md)|  | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_metadata_is_not_allowed**
> post_document_metadata_is_not_allowed()

Not allowed to post metadata: use put instead

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.MetadataApi()

try:
    # Not allowed to post metadata: use put instead
    api_instance.post_document_metadata_is_not_allowed()
except ApiException as e:
    print("Exception when calling MetadataApi->post_document_metadata_is_not_allowed: %s\n" % e)
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

# **post_metadata_is_not_allowed**
> post_metadata_is_not_allowed()

Not allowed to post metadata: use put instead

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.MetadataApi()

try:
    # Not allowed to post metadata: use put instead
    api_instance.post_metadata_is_not_allowed()
except ApiException as e:
    print("Exception when calling MetadataApi->post_metadata_is_not_allowed: %s\n" % e)
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

# **put_document_metadata_entry**
> put_document_metadata_entry(doc_id, key, body=body)

Create or update document metadata entry

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.MetadataApi()
doc_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
key = 'key_example' # str | 
body = 'body_example' # str |  (optional)

try:
    # Create or update document metadata entry
    api_instance.put_document_metadata_entry(doc_id, key, body=body)
except ApiException as e:
    print("Exception when calling MetadataApi->put_document_metadata_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | [**str**](.md)|  | 
 **key** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_file_metadata_entry**
> put_file_metadata_entry(file_id, key, body=body)

Create or update file metadata entry

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.MetadataApi()
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
key = 'key_example' # str | 
body = 'body_example' # str |  (optional)

try:
    # Create or update file metadata entry
    api_instance.put_file_metadata_entry(file_id, key, body=body)
except ApiException as e:
    print("Exception when calling MetadataApi->put_file_metadata_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | [**str**](.md)|  | 
 **key** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

