# textrepo_client.TypesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete4**](TypesApi.md#delete4) | **DELETE** /rest/types/{id} | Delete type
[**get7**](TypesApi.md#get7) | **GET** /rest/types/{id} | Retrieve types
[**get_all**](TypesApi.md#get_all) | **GET** /rest/types | Retrieve types
[**post4**](TypesApi.md#post4) | **POST** /rest/types | Create type
[**put3**](TypesApi.md#put3) | **PUT** /rest/types/{id} | Create or update type

# **delete4**
> delete4(id)

Delete type

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TypesApi()
id = 56 # int | 

try:
    # Delete type
    api_instance.delete4(id)
except ApiException as e:
    print("Exception when calling TypesApi->delete4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get7**
> get7(id)

Retrieve types

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TypesApi()
id = 56 # int | 

try:
    # Retrieve types
    api_instance.get7(id)
except ApiException as e:
    print("Exception when calling TypesApi->get7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> get_all()

Retrieve types

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TypesApi()

try:
    # Retrieve types
    api_instance.get_all()
except ApiException as e:
    print("Exception when calling TypesApi->get_all: %s\n" % e)
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

# **post4**
> post4(body=body)

Create type

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TypesApi()
body = textrepo_client.FormType() # FormType |  (optional)

try:
    # Create type
    api_instance.post4(body=body)
except ApiException as e:
    print("Exception when calling TypesApi->post4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FormType**](FormType.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put3**
> put3(id, body=body)

Create or update type

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.TypesApi()
id = 56 # int | 
body = textrepo_client.FormType() # FormType |  (optional)

try:
    # Create or update type
    api_instance.put3(id, body=body)
except ApiException as e:
    print("Exception when calling TypesApi->put3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**FormType**](FormType.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

