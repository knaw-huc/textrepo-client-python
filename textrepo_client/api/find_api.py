"""
    TextRepo API

    The API for TextRepo  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from textrepo_client.api_client import ApiClient, Endpoint as _Endpoint
from textrepo_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)


class FindApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_document_metadata_for_external_id(
            self,
            external_id,
            **kwargs
        ):
            """Find metadata of document by external ID, with header links to original and parent resource  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_document_metadata_for_external_id(external_id, async_req=True)
            >>> result = thread.get()

            Args:
                external_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['external_id'] = \
                external_id
            return self.call_with_http_info(**kwargs)

        self.get_document_metadata_for_external_id = _Endpoint(
            settings={
                'response_type': ({str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)},),
                'auth': [],
                'endpoint_path': '/task/find/{externalId}/document/metadata',
                'operation_id': 'get_document_metadata_for_external_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'external_id',
                ],
                'required': [
                    'external_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'external_id':
                        (str,),
                },
                'attribute_map': {
                    'external_id': 'externalId',
                },
                'location_map': {
                    'external_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_document_metadata_for_external_id
        )

        def __get_file_metadata_for_external_id(
            self,
            external_id,
            **kwargs
        ):
            """Find metadata of file by external ID and file type, with header links to original, parent and type resource  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_file_metadata_for_external_id(external_id, async_req=True)
            >>> result = thread.get()

            Args:
                external_id (str):

            Keyword Args:
                type (str): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['external_id'] = \
                external_id
            return self.call_with_http_info(**kwargs)

        self.get_file_metadata_for_external_id = _Endpoint(
            settings={
                'response_type': ({str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)},),
                'auth': [],
                'endpoint_path': '/task/find/{externalId}/file/metadata',
                'operation_id': 'get_file_metadata_for_external_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'external_id',
                    'type',
                ],
                'required': [
                    'external_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'external_id':
                        (str,),
                    'type':
                        (str,),
                },
                'attribute_map': {
                    'external_id': 'externalId',
                    'type': 'type',
                },
                'location_map': {
                    'external_id': 'path',
                    'type': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_file_metadata_for_external_id
        )

        def __get_latest_file_version_content(
            self,
            external_id,
            **kwargs
        ):
            """Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_latest_file_version_content(external_id, async_req=True)
            >>> result = thread.get()

            Args:
                external_id (str):

            Keyword Args:
                accept_encoding (str): [optional]
                type (str): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['external_id'] = \
                external_id
            return self.call_with_http_info(**kwargs)

        self.get_latest_file_version_content = _Endpoint(
            settings={
                'response_type': ({str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)},),
                'auth': [],
                'endpoint_path': '/task/find/{externalId}/file/contents',
                'operation_id': 'get_latest_file_version_content',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'external_id',
                    'accept_encoding',
                    'type',
                ],
                'required': [
                    'external_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'external_id':
                        (str,),
                    'accept_encoding':
                        (str,),
                    'type':
                        (str,),
                },
                'attribute_map': {
                    'external_id': 'externalId',
                    'accept_encoding': 'Accept-Encoding',
                    'type': 'type',
                },
                'location_map': {
                    'external_id': 'path',
                    'accept_encoding': 'header',
                    'type': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/octet-stream'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_latest_file_version_content
        )
