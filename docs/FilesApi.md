# textrepo_client.FilesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete2**](FilesApi.md#delete2) | **DELETE** /rest/files/{fileId}/metadata/{key} | Delete document metadata entry
[**delete3**](FilesApi.md#delete3) | **DELETE** /rest/files/{id} | Delete file
[**get5**](FilesApi.md#get5) | **GET** /rest/files/{fileId}/metadata | Retrieve file metadata
[**get6**](FilesApi.md#get6) | **GET** /rest/files/{id} | Retrieve file
[**get_versions**](FilesApi.md#get_versions) | **GET** /rest/files/{fileId}/versions | Retrieve file versions, newest first
[**post2**](FilesApi.md#post2) | **POST** /rest/files/{fileId}/metadata | Not allowed to post metadata: use put instead
[**post3**](FilesApi.md#post3) | **POST** /rest/files | Create file
[**put1**](FilesApi.md#put1) | **PUT** /rest/files/{fileId}/metadata/{key} | Create or update file metadata entry
[**put2**](FilesApi.md#put2) | **PUT** /rest/files/{id} | Create or update file

# **delete2**
> delete2(file_id, key)

Delete document metadata entry

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.FilesApi()
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
key = 'key_example' # str | 

try:
    # Delete document metadata entry
    api_instance.delete2(file_id, key)
except ApiException as e:
    print("Exception when calling FilesApi->delete2: %s\n" % e)
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

# **delete3**
> delete3(id)

Delete file

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.FilesApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete file
    api_instance.delete3(id)
except ApiException as e:
    print("Exception when calling FilesApi->delete3: %s\n" % e)
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

# **get5**
> dict(str, str) get5(file_id)

Retrieve file metadata

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.FilesApi()
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve file metadata
    api_response = api_instance.get5(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->get5: %s\n" % e)
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

# **get6**
> ResultTextRepoFile get6(id)

Retrieve file

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.FilesApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve file
    api_response = api_instance.get6(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->get6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**ResultTextRepoFile**](ResultTextRepoFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions**
> ResultVersion get_versions(file_id, limit=limit, offset=offset, created_after=created_after)

Retrieve file versions, newest first

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.FilesApi()
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    # Retrieve file versions, newest first
    api_response = api_instance.get_versions(file_id, limit=limit, offset=offset, created_after=created_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->get_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | [**str**](.md)|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **created_after** | **datetime**|  | [optional] 

### Return type

[**ResultVersion**](ResultVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post2**
> post2()

Not allowed to post metadata: use put instead

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.FilesApi()

try:
    # Not allowed to post metadata: use put instead
    api_instance.post2()
except ApiException as e:
    print("Exception when calling FilesApi->post2: %s\n" % e)
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

# **post3**
> ResultTextRepoFile post3(body=body)

Create file

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.FilesApi()
body = textrepo_client.FormTextRepoFile() # FormTextRepoFile |  (optional)

try:
    # Create file
    api_response = api_instance.post3(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->post3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FormTextRepoFile**](FormTextRepoFile.md)|  | [optional] 

### Return type

[**ResultTextRepoFile**](ResultTextRepoFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put1**
> put1(file_id, key, body=body)

Create or update file metadata entry

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.FilesApi()
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
key = 'key_example' # str | 
body = 'body_example' # str |  (optional)

try:
    # Create or update file metadata entry
    api_instance.put1(file_id, key, body=body)
except ApiException as e:
    print("Exception when calling FilesApi->put1: %s\n" % e)
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

# **put2**
> ResultTextRepoFile put2(id, body=body)

Create or update file

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.FilesApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = textrepo_client.FormTextRepoFile() # FormTextRepoFile |  (optional)

try:
    # Create or update file
    api_response = api_instance.put2(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->put2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **body** | [**FormTextRepoFile**](FormTextRepoFile.md)|  | [optional] 

### Return type

[**ResultTextRepoFile**](ResultTextRepoFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

