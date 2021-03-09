# textrepo_client.DocumentsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document**](DocumentsApi.md#create_document) | **POST** /rest/documents | Create document
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /rest/documents/{id} | Delete document
[**delete_document_metadata_entry**](DocumentsApi.md#delete_document_metadata_entry) | **DELETE** /rest/documents/{docId}/metadata/{key} | Delete document metadata entry
[**delete_document_recursively**](DocumentsApi.md#delete_document_recursively) | **DELETE** /task/delete/documents/{externalId} | Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.
[**get_document**](DocumentsApi.md#get_document) | **GET** /rest/documents/{id} | Retrieve document
[**get_document_files**](DocumentsApi.md#get_document_files) | **GET** /rest/documents/{docId}/files | Retrieve document files
[**get_document_metadata**](DocumentsApi.md#get_document_metadata) | **GET** /rest/documents/{docId}/metadata | Retrieve document metadata
[**get_documents**](DocumentsApi.md#get_documents) | **GET** /rest/documents | Retrieve documents, newest first
[**post_document_metadata_is_not_allowed**](DocumentsApi.md#post_document_metadata_is_not_allowed) | **POST** /rest/documents/{docId}/metadata | Not allowed to post metadata: use put instead
[**put_document**](DocumentsApi.md#put_document) | **PUT** /rest/documents/{id} | Create or update document
[**put_document_metadata_entry**](DocumentsApi.md#put_document_metadata_entry) | **PUT** /rest/documents/{docId}/metadata/{key} | Create or update document metadata entry

# **create_document**
> ResultDocument create_document(body=body)

Create document

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.DocumentsApi()
body = textrepo_client.FormDocument() # FormDocument |  (optional)

try:
    # Create document
    api_response = api_instance.create_document(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FormDocument**](FormDocument.md)|  | [optional] 

### Return type

[**ResultDocument**](ResultDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> delete_document(id)

Delete document

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.DocumentsApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete document
    api_instance.delete_document(id)
except ApiException as e:
    print("Exception when calling DocumentsApi->delete_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = textrepo_client.DocumentsApi()
doc_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
key = 'key_example' # str | 

try:
    # Delete document metadata entry
    api_instance.delete_document_metadata_entry(doc_id, key)
except ApiException as e:
    print("Exception when calling DocumentsApi->delete_document_metadata_entry: %s\n" % e)
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

# **delete_document_recursively**
> delete_document_recursively(external_id)

Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.DocumentsApi()
external_id = 'external_id_example' # str | 

try:
    # Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.
    api_instance.delete_document_recursively(external_id)
except ApiException as e:
    print("Exception when calling DocumentsApi->delete_document_recursively: %s\n" % e)
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

# **get_document**
> ResultDocument get_document(id)

Retrieve document

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.DocumentsApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve document
    api_response = api_instance.get_document(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**ResultDocument**](ResultDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_files**
> ResultPage get_document_files(doc_id, limit=limit, offset=offset)

Retrieve document files

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.DocumentsApi()
doc_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)

try:
    # Retrieve document files
    api_response = api_instance.get_document_files(doc_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_document_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | [**str**](.md)|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**ResultPage**](ResultPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
api_instance = textrepo_client.DocumentsApi()
doc_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve document metadata
    api_response = api_instance.get_document_metadata(doc_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_document_metadata: %s\n" % e)
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

# **get_documents**
> ResultPage get_documents(external_id=external_id, created_after=created_after, limit=limit, offset=offset)

Retrieve documents, newest first

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.DocumentsApi()
external_id = 'external_id_example' # str |  (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)

try:
    # Retrieve documents, newest first
    api_response = api_instance.get_documents(external_id=external_id, created_after=created_after, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | [optional] 
 **created_after** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**ResultPage**](ResultPage.md)

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
api_instance = textrepo_client.DocumentsApi()

try:
    # Not allowed to post metadata: use put instead
    api_instance.post_document_metadata_is_not_allowed()
except ApiException as e:
    print("Exception when calling DocumentsApi->post_document_metadata_is_not_allowed: %s\n" % e)
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

# **put_document**
> ResultDocument put_document(id, body=body)

Create or update document

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.DocumentsApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = textrepo_client.FormDocument() # FormDocument |  (optional)

try:
    # Create or update document
    api_response = api_instance.put_document(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->put_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **body** | [**FormDocument**](FormDocument.md)|  | [optional] 

### Return type

[**ResultDocument**](ResultDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

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
api_instance = textrepo_client.DocumentsApi()
doc_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
key = 'key_example' # str | 
body = 'body_example' # str |  (optional)

try:
    # Create or update document metadata entry
    api_instance.put_document_metadata_entry(doc_id, key, body=body)
except ApiException as e:
    print("Exception when calling DocumentsApi->put_document_metadata_entry: %s\n" % e)
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

