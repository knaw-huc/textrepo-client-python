# textrepo_client.TypesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_type**](TypesApi.md#create_type) | **POST** /rest/types | Create type
[**delete_type**](TypesApi.md#delete_type) | **DELETE** /rest/types/{id} | Delete type
[**get_type**](TypesApi.md#get_type) | **GET** /rest/types/{id} | Retrieve types
[**get_types**](TypesApi.md#get_types) | **GET** /rest/types | Retrieve types
[**put_type**](TypesApi.md#put_type) | **PUT** /rest/types/{id} | Create or update type

# **create_type**
> create_type(body=body)

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
    api_instance.create_type(body=body)
except ApiException as e:
    print("Exception when calling TypesApi->create_type: %s\n" % e)
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

# **delete_type**
> delete_type(id)

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
    api_instance.delete_type(id)
except ApiException as e:
    print("Exception when calling TypesApi->delete_type: %s\n" % e)
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

# **get_type**
> get_type(id)

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
    api_instance.get_type(id)
except ApiException as e:
    print("Exception when calling TypesApi->get_type: %s\n" % e)
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

# **get_types**
> get_types()

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
    api_instance.get_types()
except ApiException as e:
    print("Exception when calling TypesApi->get_types: %s\n" % e)
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

# **put_type**
> put_type(id, body=body)

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
    api_instance.put_type(id, body=body)
except ApiException as e:
    print("Exception when calling TypesApi->put_type: %s\n" % e)
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

