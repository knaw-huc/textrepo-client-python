# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from textrepo_client.api_client import ApiClient


class FindApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_document_metadata(self, external_id, **kwargs):  # noqa: E501
        """Find metadata of document by external ID, with header links to original and parent resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_metadata(external_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str external_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_document_metadata_with_http_info(external_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_document_metadata_with_http_info(external_id, **kwargs)  # noqa: E501
            return data

    def get_document_metadata_with_http_info(self, external_id, **kwargs):  # noqa: E501
        """Find metadata of document by external ID, with header links to original and parent resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_metadata_with_http_info(external_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str external_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['external_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'external_id' is set
        if ('external_id' not in params or
                params['external_id'] is None):
            raise ValueError("Missing the required parameter `external_id` when calling `get_document_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'external_id' in params:
            path_params['externalId'] = params['external_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/task/find/{externalId}/document/metadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_file_metadata(self, external_id, type, **kwargs):  # noqa: E501
        """Find metadata of file by external ID and file type, with header links to original, parent and type resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_file_metadata(external_id, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str external_id: (required)
        :param str type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_file_metadata_with_http_info(external_id, type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_file_metadata_with_http_info(external_id, type, **kwargs)  # noqa: E501
            return data

    def get_file_metadata_with_http_info(self, external_id, type, **kwargs):  # noqa: E501
        """Find metadata of file by external ID and file type, with header links to original, parent and type resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_file_metadata_with_http_info(external_id, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str external_id: (required)
        :param str type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['external_id', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'external_id' is set
        if ('external_id' not in params or
                params['external_id'] is None):
            raise ValueError("Missing the required parameter `external_id` when calling `get_file_metadata`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `get_file_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'external_id' in params:
            path_params['externalId'] = params['external_id']  # noqa: E501

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/task/find/{externalId}/file/metadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_latest_file_version_content(self, external_id, type, **kwargs):  # noqa: E501
        """Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_latest_file_version_content(external_id, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str external_id: (required)
        :param str type: (required)
        :param str accept_encoding:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_latest_file_version_content_with_http_info(external_id, type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_latest_file_version_content_with_http_info(external_id, type, **kwargs)  # noqa: E501
            return data

    def get_latest_file_version_content_with_http_info(self, external_id, type, **kwargs):  # noqa: E501
        """Find contents of latest file version by external ID and file type, with header links to version history, parent and type resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_latest_file_version_content_with_http_info(external_id, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str external_id: (required)
        :param str type: (required)
        :param str accept_encoding:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['external_id', 'type', 'accept_encoding']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_latest_file_version_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'external_id' is set
        if ('external_id' not in params or
                params['external_id'] is None):
            raise ValueError("Missing the required parameter `external_id` when calling `get_latest_file_version_content`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `get_latest_file_version_content`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'external_id' in params:
            path_params['externalId'] = params['external_id']  # noqa: E501

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}
        if 'accept_encoding' in params:
            header_params['Accept-Encoding'] = params['accept_encoding']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/task/find/{externalId}/file/contents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)