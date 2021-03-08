# textrepo_client.RegisterApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_identifiers**](RegisterApi.md#post_identifiers) | **POST** /task/register | 
[**put_identifiers**](RegisterApi.md#put_identifiers) | **PUT** /task/register | 

# **post_identifiers**
> list[Document] post_identifiers(body=body)



### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.RegisterApi()
body = textrepo_client.InputStream() # InputStream |  (optional)

try:
    api_response = api_instance.post_identifiers(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisterApi->post_identifiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputStream**](InputStream.md)|  | [optional] 

### Return type

[**list[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_identifiers**
> list[Document] put_identifiers(body=body)



### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.RegisterApi()
body = textrepo_client.InputStream() # InputStream |  (optional)

try:
    api_response = api_instance.put_identifiers(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisterApi->put_identifiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputStream**](InputStream.md)|  | [optional] 

### Return type

[**list[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

