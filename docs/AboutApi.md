# textrepo_client.AboutApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_about**](AboutApi.md#get_about) | **GET** / | Get info about application version and configuration


# **get_about**
> ResultAbout get_about()

Get info about application version and configuration

### Example

```python
import time
import textrepo_client
from textrepo_client.api import about_api
from textrepo_client.model.result_about import ResultAbout
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = about_api.AboutApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get info about application version and configuration
        api_response = api_instance.get_about()
        pprint(api_response)
    except textrepo_client.ApiException as e:
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


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

