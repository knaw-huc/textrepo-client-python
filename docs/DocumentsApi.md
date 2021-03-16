# textrepo_client.DocumentsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document**](DocumentsApi.md#create_document) | **POST** /rest/documents | Create document
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /rest/documents/{id} | Delete document
[**delete_document_metadata_entry**](DocumentsApi.md#delete_document_metadata_entry) | **DELETE** /rest/documents/{docId}/metadata/{key} | Delete document metadata entry
[**delete_document_recursively**](DocumentsApi.md#delete_document_recursively) | **DELETE** /task/delete/documents/{externalId} | Delete a document including its metadata, files, versions and contents. Contents are only deleted when not referenced by any other versions.
[**get_document**](DocumentsApi.md#get_document) | **GET** /rest/documents/{id} | Retrieve document
[**get_document_files**](DocumentsApi.md#get_document_files) | **GET** /rest/documents/{docId}/files | Retrieve document files
[**get_document_metadata**](DocumentsApi.md#get_document_metadata) | **GET** /rest/documents/{docId}/metadata | Retrieve document metadata
[**get_documents**](DocumentsApi.md#get_documents) | **GET** /rest/documents | Retrieve documents, newest first
[**post_document_metadata_is_not_allowed**](DocumentsApi.md#post_document_metadata_is_not_allowed) | **POST** /rest/documents/{docId}/metadata | Not allowed to post metadata: use put instead
[**put_document**](DocumentsApi.md#put_document) | **PUT** /rest/documents/{id} | Create or update document
[**put_document_metadata_entry**](DocumentsApi.md#put_document_metadata_entry) | **PUT** /rest/documents/{docId}/metadata/{key} | Create or update document metadata entry


# **create_document**
> ResultDocument create_document()

Create document

### Example

```python
import time
import textrepo_client
from textrepo_client.api import documents_api
from textrepo_client.model.result_document import ResultDocument
from textrepo_client.model.form_document import FormDocument
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    body = FormDocument(
        external_id="external_id_example",
    ) # FormDocument |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create document
        api_response = api_instance.create_document(body=body)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling DocumentsApi->create_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FormDocument**](FormDocument.md)|  | [optional]

### Return type

[**ResultDocument**](ResultDocument.md)

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

# **delete_document**
> delete_document(id)

Delete document

### Example

```python
import time
import textrepo_client
from textrepo_client.api import documents_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete document
        api_instance.delete_document(id)
    except textrepo_client.ApiException as e:
        print("Exception when calling DocumentsApi->delete_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **delete_document_metadata_entry**
> delete_document_metadata_entry(doc_id, key)

Delete document metadata entry

### Example

```python
import time
import textrepo_client
from textrepo_client.api import documents_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    doc_id = "docId_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete document metadata entry
        api_instance.delete_document_metadata_entry(doc_id, key)
    except textrepo_client.ApiException as e:
        print("Exception when calling DocumentsApi->delete_document_metadata_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **str**|  |
 **key** | **str**|  |

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

# **delete_document_recursively**
> delete_document_recursively(external_id)

Delete a document including its metadata, files, versions and contents. Contents are only deleted when not referenced by any other versions.

### Example

```python
import time
import textrepo_client
from textrepo_client.api import documents_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    external_id = "externalId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a document including its metadata, files, versions and contents. Contents are only deleted when not referenced by any other versions.
        api_instance.delete_document_recursively(external_id)
    except textrepo_client.ApiException as e:
        print("Exception when calling DocumentsApi->delete_document_recursively: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  |

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
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> ResultDocument get_document(id)

Retrieve document

### Example

```python
import time
import textrepo_client
from textrepo_client.api import documents_api
from textrepo_client.model.result_document import ResultDocument
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve document
        api_response = api_instance.get_document(id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling DocumentsApi->get_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ResultDocument**](ResultDocument.md)

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

# **get_document_files**
> ResultPage get_document_files(doc_id)

Retrieve document files

### Example

```python
import time
import textrepo_client
from textrepo_client.api import documents_api
from textrepo_client.model.result_page import ResultPage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    doc_id = "docId_example" # str | 
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve document files
        api_response = api_instance.get_document_files(doc_id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling DocumentsApi->get_document_files: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve document files
        api_response = api_instance.get_document_files(doc_id, limit=limit, offset=offset)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling DocumentsApi->get_document_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **str**|  |
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]

### Return type

[**ResultPage**](ResultPage.md)

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

# **get_document_metadata**
> {str: (str,)} get_document_metadata(doc_id)

Retrieve document metadata

### Example

```python
import time
import textrepo_client
from textrepo_client.api import documents_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    doc_id = "docId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve document metadata
        api_response = api_instance.get_document_metadata(doc_id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling DocumentsApi->get_document_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **str**|  |

### Return type

**{str: (str,)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents**
> ResultPage get_documents()

Retrieve documents, newest first

### Example

```python
import time
import textrepo_client
from textrepo_client.api import documents_api
from textrepo_client.model.result_page import ResultPage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    external_id = "externalId_example" # str |  (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve documents, newest first
        api_response = api_instance.get_documents(external_id=external_id, created_after=created_after, limit=limit, offset=offset)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling DocumentsApi->get_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | [optional]
 **created_after** | **datetime**|  | [optional]
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]

### Return type

[**ResultPage**](ResultPage.md)

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

# **post_document_metadata_is_not_allowed**
> post_document_metadata_is_not_allowed()

Not allowed to post metadata: use put instead

### Example

```python
import time
import textrepo_client
from textrepo_client.api import documents_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Not allowed to post metadata: use put instead
        api_instance.post_document_metadata_is_not_allowed()
    except textrepo_client.ApiException as e:
        print("Exception when calling DocumentsApi->post_document_metadata_is_not_allowed: %s\n" % e)
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


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**405** | Not allowed to post metadata: use put instead |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_document**
> ResultDocument put_document(id)

Create or update document

### Example

```python
import time
import textrepo_client
from textrepo_client.api import documents_api
from textrepo_client.model.result_document import ResultDocument
from textrepo_client.model.form_document import FormDocument
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    id = "id_example" # str | 
    body = FormDocument(
        external_id="external_id_example",
    ) # FormDocument |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update document
        api_response = api_instance.put_document(id)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling DocumentsApi->put_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update document
        api_response = api_instance.put_document(id, body=body)
        pprint(api_response)
    except textrepo_client.ApiException as e:
        print("Exception when calling DocumentsApi->put_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **body** | [**FormDocument**](FormDocument.md)|  | [optional]

### Return type

[**ResultDocument**](ResultDocument.md)

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

# **put_document_metadata_entry**
> put_document_metadata_entry(doc_id, key)

Create or update document metadata entry

### Example

```python
import time
import textrepo_client
from textrepo_client.api import documents_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = textrepo_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with textrepo_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    doc_id = "docId_example" # str | 
    key = "key_example" # str | 
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update document metadata entry
        api_instance.put_document_metadata_entry(doc_id, key)
    except textrepo_client.ApiException as e:
        print("Exception when calling DocumentsApi->put_document_metadata_entry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update document metadata entry
        api_instance.put_document_metadata_entry(doc_id, key, body=body)
    except textrepo_client.ApiException as e:
        print("Exception when calling DocumentsApi->put_document_metadata_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **str**|  |
 **key** | **str**|  |
 **body** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

