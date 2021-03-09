# textrepo_client.ContentsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_version_contents_is_not_allowed**](ContentsApi.md#delete_version_contents_is_not_allowed) | **DELETE** /rest/versions/{versionId}/contents | Not allowed to delete contents of version: delete version instead
[**get_contents**](ContentsApi.md#get_contents) | **GET** /rest/contents/{sha} | Retrieve contents
[**get_version_contents**](ContentsApi.md#get_version_contents) | **GET** /rest/versions/{versionId}/contents | Retrieve version contents
[**post_version_contents_is_not_allowed**](ContentsApi.md#post_version_contents_is_not_allowed) | **POST** /rest/versions/{versionId}/contents | Not allowed to post contents: post new version instead
[**put_version_contents_is_not_allowed**](ContentsApi.md#put_version_contents_is_not_allowed) | **PUT** /rest/versions/{versionId}/contents | Not allowed to put contents of version: post new version instead

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
api_instance = textrepo_client.ContentsApi()

try:
    # Not allowed to delete contents of version: delete version instead
    api_instance.delete_version_contents_is_not_allowed()
except ApiException as e:
    print("Exception when calling ContentsApi->delete_version_contents_is_not_allowed: %s\n" % e)
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

# **get_contents**
> list[str] get_contents(sha)

Retrieve contents

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.ContentsApi()
sha = 'sha_example' # str | 

try:
    # Retrieve contents
    api_response = api_instance.get_contents(sha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentsApi->get_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sha** | **str**|  | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

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
api_instance = textrepo_client.ContentsApi()
version_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve version contents
    api_response = api_instance.get_version_contents(version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentsApi->get_version_contents: %s\n" % e)
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
api_instance = textrepo_client.ContentsApi()

try:
    # Not allowed to post contents: post new version instead
    api_instance.post_version_contents_is_not_allowed()
except ApiException as e:
    print("Exception when calling ContentsApi->post_version_contents_is_not_allowed: %s\n" % e)
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
api_instance = textrepo_client.ContentsApi()

try:
    # Not allowed to put contents of version: post new version instead
    api_instance.put_version_contents_is_not_allowed()
except ApiException as e:
    print("Exception when calling ContentsApi->put_version_contents_is_not_allowed: %s\n" % e)
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

