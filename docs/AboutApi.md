# textrepo_client.AboutApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_about**](AboutApi.md#get_about) | **GET** / | Get info about application version and configuration

# **get_about**
> ResultAbout get_about()

Get info about application version and configuration

### Example
```python
from __future__ import print_function
import time
import textrepo_client
from textrepo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = textrepo_client.AboutApi()

try:
    # Get info about application version and configuration
    api_response = api_instance.get_about()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->get_about: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResultAbout**](ResultAbout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

