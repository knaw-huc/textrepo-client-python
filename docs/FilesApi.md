# textrepo_client.FilesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](FilesApi.md#create_file) | **POST** /rest/files | Create file
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /rest/files/{id} | Delete file
[**delete_file_metadata_entry**](FilesApi.md#delete_file_metadata_entry) | **DELETE** /rest/files/{fileId}/metadata/{key} | Delete file metadata entry
[**get_file**](FilesApi.md#get_file) | **GET** /rest/files/{id} | Retrieve file
[**get_file_metadata**](FilesApi.md#get_file_metadata) | **GET** /rest/files/{fileId}/metadata | Retrieve file metadata
[**get_versions**](FilesApi.md#get_versions) | **GET** /rest/files/{fileId}/versions | Retrieve file versions, newest first
[**post_metadata_is_not_allowed**](FilesApi.md#post_metadata_is_not_allowed) | **POST** /rest/files/{fileId}/metadata | Not allowed to post metadata: use put instead
[**put_file**](FilesApi.md#put_file) | **PUT** /rest/files/{id} | Create or update file
[**put_file_metadata_entry**](FilesApi.md#put_file_metadata_entry) | **PUT** /rest/files/{fileId}/metadata/{key} | Create or update file metadata entry

# **create_file**
> ResultTextRepoFile create_file(body=body)

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
    api_response = api_instance.create_file(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->create_file: %s\n" % e)
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

# **delete_file**
> delete_file(id)

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
    api_instance.delete_file(id)
except ApiException as e:
    print("Exception when calling FilesApi->delete_file: %s\n" % e)
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
api_instance = textrepo_client.FilesApi()
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
key = 'key_example' # str | 

try:
    # Delete file metadata entry
    api_instance.delete_file_metadata_entry(file_id, key)
except ApiException as e:
    print("Exception when calling FilesApi->delete_file_metadata_entry: %s\n" % e)
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

# **get_file**
> ResultTextRepoFile get_file(id)

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
    api_response = api_instance.get_file(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->get_file: %s\n" % e)
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
api_instance = textrepo_client.FilesApi()
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve file metadata
    api_response = api_instance.get_file_metadata(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->get_file_metadata: %s\n" % e)
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
api_instance = textrepo_client.FilesApi()

try:
    # Not allowed to post metadata: use put instead
    api_instance.post_metadata_is_not_allowed()
except ApiException as e:
    print("Exception when calling FilesApi->post_metadata_is_not_allowed: %s\n" % e)
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

# **put_file**
> ResultTextRepoFile put_file(id, body=body)

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
    api_response = api_instance.put_file(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->put_file: %s\n" % e)
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
api_instance = textrepo_client.FilesApi()
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
key = 'key_example' # str | 
body = 'body_example' # str |  (optional)

try:
    # Create or update file metadata entry
    api_instance.put_file_metadata_entry(file_id, key, body=body)
except ApiException as e:
    print("Exception when calling FilesApi->put_file_metadata_entry: %s\n" % e)
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

