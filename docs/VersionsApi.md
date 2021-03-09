# textrepo_client.VersionsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_version**](VersionsApi.md#create_version) | **POST** /rest/versions | Create version
[**delete_version**](VersionsApi.md#delete_version) | **DELETE** /rest/versions/{id} | Delete version
[**delete_version_contents_is_not_allowed**](VersionsApi.md#delete_version_contents_is_not_allowed) | **DELETE** /rest/versions/{versionId}/contents | Not allowed to delete contents of version: delete version instead
[**get_version**](VersionsApi.md#get_version) | **GET** /rest/versions/{id} | Retrieve version
[**get_version_contents**](VersionsApi.md#get_version_contents) | **GET** /rest/versions/{versionId}/contents | Retrieve version contents
[**get_versions**](VersionsApi.md#get_versions) | **GET** /rest/files/{fileId}/versions | Retrieve file versions, newest first
[**post_version_contents_is_not_allowed**](VersionsApi.md#post_version_contents_is_not_allowed) | **POST** /rest/versions/{versionId}/contents | Not allowed to post contents: post new version instead
[**put_version_contents_is_not_allowed**](VersionsApi.md#put_version_contents_is_not_allowed) | **PUT** /rest/versions/{versionId}/contents | Not allowed to put contents of version: post new version instead
[**put_version_is_not_allowed**](VersionsApi.md#put_version_is_not_allowed) | **PUT** /rest/versions/{id} | Not allowed to update a version: create a new version using POST

# **create_version**
> ResultVersion create_version(file_id=file_id, contents=contents)

Create version

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.VersionsApi()
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
contents = 'contents_example' # str |  (optional)

try:
    # Create version
    api_response = api_instance.create_version(file_id=file_id, contents=contents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->create_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | [**str**](.md)|  | [optional] 
 **contents** | **str**|  | [optional] 

### Return type

[**ResultVersion**](ResultVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version**
> delete_version(id)

Delete version

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.VersionsApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete version
    api_instance.delete_version(id)
except ApiException as e:
    print("Exception when calling VersionsApi->delete_version: %s\n" % e)
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

# **delete_version_contents_is_not_allowed**
> delete_version_contents_is_not_allowed()

Not allowed to delete contents of version: delete version instead

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.VersionsApi()

try:
    # Not allowed to delete contents of version: delete version instead
    api_instance.delete_version_contents_is_not_allowed()
except ApiException as e:
    print("Exception when calling VersionsApi->delete_version_contents_is_not_allowed: %s\n" % e)
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

# **get_version**
> ResultVersion get_version(id)

Retrieve version

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.VersionsApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve version
    api_response = api_instance.get_version(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->get_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**ResultVersion**](ResultVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_contents**
> ResultVersion get_version_contents(version_id)

Retrieve version contents

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.VersionsApi()
version_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve version contents
    api_response = api_instance.get_version_contents(version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->get_version_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**str**](.md)|  | 

### Return type

[**ResultVersion**](ResultVersion.md)

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
api_instance = textrepo_client.VersionsApi()
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    # Retrieve file versions, newest first
    api_response = api_instance.get_versions(file_id, limit=limit, offset=offset, created_after=created_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->get_versions: %s\n" % e)
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

# **post_version_contents_is_not_allowed**
> post_version_contents_is_not_allowed()

Not allowed to post contents: post new version instead

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.VersionsApi()

try:
    # Not allowed to post contents: post new version instead
    api_instance.post_version_contents_is_not_allowed()
except ApiException as e:
    print("Exception when calling VersionsApi->post_version_contents_is_not_allowed: %s\n" % e)
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

# **put_version_contents_is_not_allowed**
> put_version_contents_is_not_allowed()

Not allowed to put contents of version: post new version instead

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.VersionsApi()

try:
    # Not allowed to put contents of version: post new version instead
    api_instance.put_version_contents_is_not_allowed()
except ApiException as e:
    print("Exception when calling VersionsApi->put_version_contents_is_not_allowed: %s\n" % e)
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

# **put_version_is_not_allowed**
> put_version_is_not_allowed(id, body=body)

Not allowed to update a version: create a new version using POST

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.VersionsApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = textrepo_client.FormVersion() # FormVersion |  (optional)

try:
    # Not allowed to update a version: create a new version using POST
    api_instance.put_version_is_not_allowed(id, body=body)
except ApiException as e:
    print("Exception when calling VersionsApi->put_version_is_not_allowed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **body** | [**FormVersion**](FormVersion.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

