# textrepo_client.ContentsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete5**](ContentsApi.md#delete5) | **DELETE** /rest/versions/{versionId}/contents | Not allowed to delete contents of version: delete version instead
[**get**](ContentsApi.md#get) | **GET** /rest/contents/{sha} | Retrieve contents
[**get8**](ContentsApi.md#get8) | **GET** /rest/versions/{versionId}/contents | Retrieve version contents
[**post5**](ContentsApi.md#post5) | **POST** /rest/versions/{versionId}/contents | Not allowed to post contents: post new version instead
[**put4**](ContentsApi.md#put4) | **PUT** /rest/versions/{versionId}/contents | Not allowed to put contents of version: post new version instead

# **delete5**
> delete5()

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
    api_instance.delete5()
except ApiException as e:
    print("Exception when calling ContentsApi->delete5: %s\n" % e)
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

# **get**
> list[str] get(sha, accept_encoding=accept_encoding)

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
accept_encoding = 'accept_encoding_example' # str |  (optional)

try:
    # Retrieve contents
    api_response = api_instance.get(sha, accept_encoding=accept_encoding)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentsApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sha** | **str**|  | 
 **accept_encoding** | **str**|  | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get8**
> ResultVersion get8(version_id, accept_encoding=accept_encoding)

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
accept_encoding = 'accept_encoding_example' # str |  (optional)

try:
    # Retrieve version contents
    api_response = api_instance.get8(version_id, accept_encoding=accept_encoding)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentsApi->get8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**str**](.md)|  | 
 **accept_encoding** | **str**|  | [optional] 

### Return type

[**ResultVersion**](ResultVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post5**
> post5()

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
    api_instance.post5()
except ApiException as e:
    print("Exception when calling ContentsApi->post5: %s\n" % e)
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

# **put4**
> put4()

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
    api_instance.put4()
except ApiException as e:
    print("Exception when calling ContentsApi->put4: %s\n" % e)
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

