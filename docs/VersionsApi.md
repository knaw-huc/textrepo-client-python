# textrepo_client.VersionsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete5**](VersionsApi.md#delete5) | **DELETE** /rest/versions/{versionId}/contents | Not allowed to delete contents of version: delete version instead
[**delete6**](VersionsApi.md#delete6) | **DELETE** /rest/versions/{versionId}/metadata/{key} | Delete document metadata entry
[**delete7**](VersionsApi.md#delete7) | **DELETE** /rest/versions/{id} | Delete version
[**get10**](VersionsApi.md#get10) | **GET** /rest/versions/{id} | Retrieve version
[**get8**](VersionsApi.md#get8) | **GET** /rest/versions/{versionId}/contents | Retrieve version contents
[**get9**](VersionsApi.md#get9) | **GET** /rest/versions/{versionId}/metadata | Retrieve version metadata
[**get_versions**](VersionsApi.md#get_versions) | **GET** /rest/files/{fileId}/versions | Retrieve file versions, newest first
[**post5**](VersionsApi.md#post5) | **POST** /rest/versions/{versionId}/contents | Not allowed to post contents: post new version instead
[**post6**](VersionsApi.md#post6) | **POST** /rest/versions/{versionId}/metadata | Not allowed to post metadata: use put instead
[**post7**](VersionsApi.md#post7) | **POST** /rest/versions | Create version
[**put4**](VersionsApi.md#put4) | **PUT** /rest/versions/{versionId}/contents | Not allowed to put contents of version: post new version instead
[**put5**](VersionsApi.md#put5) | **PUT** /rest/versions/{versionId}/metadata/{key} | Create or update version metadata entry
[**put6**](VersionsApi.md#put6) | **PUT** /rest/versions/{id} | Not allowed to update a version: create a new version using POST

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
api_instance = textrepo_client.VersionsApi()

try:
    # Not allowed to delete contents of version: delete version instead
    api_instance.delete5()
except ApiException as e:
    print("Exception when calling VersionsApi->delete5: %s\n" % e)
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

# **delete6**
> delete6(version_id, key)

Delete document metadata entry

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
key = 'key_example' # str | 

try:
    # Delete document metadata entry
    api_instance.delete6(version_id, key)
except ApiException as e:
    print("Exception when calling VersionsApi->delete6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**str**](.md)|  | 
 **key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete7**
> delete7(id)

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
    api_instance.delete7(id)
except ApiException as e:
    print("Exception when calling VersionsApi->delete7: %s\n" % e)
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

# **get10**
> ResultVersion get10(id)

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
    api_response = api_instance.get10(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->get10: %s\n" % e)
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
api_instance = textrepo_client.VersionsApi()
version_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
accept_encoding = 'accept_encoding_example' # str |  (optional)

try:
    # Retrieve version contents
    api_response = api_instance.get8(version_id, accept_encoding=accept_encoding)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->get8: %s\n" % e)
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

# **get9**
> dict(str, str) get9(version_id)

Retrieve version metadata

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
    # Retrieve version metadata
    api_response = api_instance.get9(version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->get9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**str**](.md)|  | 

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
api_instance = textrepo_client.VersionsApi()

try:
    # Not allowed to post contents: post new version instead
    api_instance.post5()
except ApiException as e:
    print("Exception when calling VersionsApi->post5: %s\n" % e)
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

# **post6**
> post6()

Not allowed to post metadata: use put instead

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
    # Not allowed to post metadata: use put instead
    api_instance.post6()
except ApiException as e:
    print("Exception when calling VersionsApi->post6: %s\n" % e)
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

# **post7**
> ResultVersion post7(file_id=file_id, contents=contents)

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
    api_response = api_instance.post7(file_id=file_id, contents=contents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->post7: %s\n" % e)
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
api_instance = textrepo_client.VersionsApi()

try:
    # Not allowed to put contents of version: post new version instead
    api_instance.put4()
except ApiException as e:
    print("Exception when calling VersionsApi->put4: %s\n" % e)
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

# **put5**
> put5(version_id, key, body=body)

Create or update version metadata entry

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
key = 'key_example' # str | 
body = 'body_example' # str |  (optional)

try:
    # Create or update version metadata entry
    api_instance.put5(version_id, key, body=body)
except ApiException as e:
    print("Exception when calling VersionsApi->put5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**str**](.md)|  | 
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

# **put6**
> put6(id, body=body)

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
    api_instance.put6(id, body=body)
except ApiException as e:
    print("Exception when calling VersionsApi->put6: %s\n" % e)
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

