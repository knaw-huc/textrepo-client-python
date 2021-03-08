# textrepo_client.DocumentsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](DocumentsApi.md#delete) | **DELETE** /rest/documents/{docId}/metadata/{key} | Delete document metadata entry
[**delete1**](DocumentsApi.md#delete1) | **DELETE** /rest/documents/{id} | Delete document
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /task/delete/documents/{externalId} | Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.
[**get1**](DocumentsApi.md#get1) | **GET** /rest/documents/{docId}/files | Retrieve document files
[**get2**](DocumentsApi.md#get2) | **GET** /rest/documents/{docId}/metadata | Retrieve document metadata
[**get3**](DocumentsApi.md#get3) | **GET** /rest/documents/{id} | Retrieve document
[**get4**](DocumentsApi.md#get4) | **GET** /rest/documents | Retrieve documents, newest first
[**post**](DocumentsApi.md#post) | **POST** /rest/documents/{docId}/metadata | Not allowed to post metadata: use put instead
[**post1**](DocumentsApi.md#post1) | **POST** /rest/documents | Create document
[**put**](DocumentsApi.md#put) | **PUT** /rest/documents/{id} | Create or update document
[**update**](DocumentsApi.md#update) | **PUT** /rest/documents/{docId}/metadata/{key} | Create or update document metadata entry

# **delete**
> delete(doc_id, key)

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
    api_instance.delete(doc_id, key)
except ApiException as e:
    print("Exception when calling DocumentsApi->delete: %s\n" % e)
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

# **delete1**
> delete1(id)

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
    api_instance.delete1(id)
except ApiException as e:
    print("Exception when calling DocumentsApi->delete1: %s\n" % e)
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

# **delete_document**
> delete_document(external_id)

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
    api_instance.delete_document(external_id)
except ApiException as e:
    print("Exception when calling DocumentsApi->delete_document: %s\n" % e)
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

# **get1**
> ResultDocument get1(doc_id, limit=limit, offset=offset)

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
    api_response = api_instance.get1(doc_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | [**str**](.md)|  | 
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

# **get2**
> dict(str, str) get2(doc_id)

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
    api_response = api_instance.get2(doc_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get2: %s\n" % e)
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

# **get3**
> ResultDocument get3(id)

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
    api_response = api_instance.get3(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get3: %s\n" % e)
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

# **get4**
> ResultDocument get4(external_id=external_id, created_after=created_after, limit=limit, offset=offset)

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
    api_response = api_instance.get4(external_id=external_id, created_after=created_after, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | [optional] 
 **created_after** | **datetime**|  | [optional] 
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

# **post**
> post()

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
    api_instance.post()
except ApiException as e:
    print("Exception when calling DocumentsApi->post: %s\n" % e)
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

# **post1**
> ResultDocument post1(body=body)

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
    api_response = api_instance.post1(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->post1: %s\n" % e)
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

# **put**
> ResultDocument put(id, body=body)

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
    api_response = api_instance.put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->put: %s\n" % e)
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

# **update**
> update(doc_id, key, body=body)

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
    api_instance.update(doc_id, key, body=body)
except ApiException as e:
    print("Exception when calling DocumentsApi->update: %s\n" % e)
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

