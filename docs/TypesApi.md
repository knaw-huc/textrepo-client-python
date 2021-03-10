# textrepo_client.TypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_type**](TypesApi.md#create_type) | **POST** /rest/types | Create type
[**delete_type**](TypesApi.md#delete_type) | **DELETE** /rest/types/{id} | Delete type
[**get_type**](TypesApi.md#get_type) | **GET** /rest/types/{id} | Retrieve type
[**get_types**](TypesApi.md#get_types) | **GET** /rest/types | Retrieve types
[**put_type**](TypesApi.md#put_type) | **PUT** /rest/types/{id} | Create or update type


# **create_type**
> ResultType create_type()

Create type

### Example

```python
import time
import textrepo_client
from textrepo_client.api import types_api
from textrepo_client.model.result_type import ResultType
from textrepo_client.model.form_type import FormType
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types_api.TypesApi(api_client)
    body = FormType(
        name="name_example",
        mimetype="mimetype_example",
    ) # FormType |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create type
        api_response = api_instance.create_type(body=body)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling TypesApi->create_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FormType**](FormType.md)|  | [optional]

### Return type

[**ResultType**](ResultType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_type**
> delete_type(id)

Delete type

### Example

```python
import time
import textrepo_client
from textrepo_client.api import types_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types_api.TypesApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete type
        api_instance.delete_type(id)
    except textrepo_client.ApiException as e:
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


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_type**
> ResultType get_type(id)

Retrieve type

### Example

```python
import time
import textrepo_client
from textrepo_client.api import types_api
from textrepo_client.model.result_type import ResultType
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types_api.TypesApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve type
        api_response = api_instance.get_type(id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling TypesApi->get_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ResultType**](ResultType.md)

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

# **get_types**
> ResultType get_types()

Retrieve types

### Example

```python
import time
import textrepo_client
from textrepo_client.api import types_api
from textrepo_client.model.result_type import ResultType
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types_api.TypesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve types
        api_response = api_instance.get_types()
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling TypesApi->get_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ResultType**](ResultType.md)

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

# **put_type**
> ResultType put_type(id)

Create or update type

### Example

```python
import time
import textrepo_client
from textrepo_client.api import types_api
from textrepo_client.model.result_type import ResultType
from textrepo_client.model.form_type import FormType
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = types_api.TypesApi(api_client)
    id = 1 # int | 
    body = FormType(
        name="name_example",
        mimetype="mimetype_example",
    ) # FormType |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update type
        api_response = api_instance.put_type(id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling TypesApi->put_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update type
        api_response = api_instance.put_type(id, body=body)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling TypesApi->put_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **body** | [**FormType**](FormType.md)|  | [optional]

### Return type

[**ResultType**](ResultType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

