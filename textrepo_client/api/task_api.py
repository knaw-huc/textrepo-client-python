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


class TaskApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_document(self, external_id, **kwargs):  # noqa: E501
        """Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_document(external_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str external_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_document_with_http_info(external_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_document_with_http_info(external_id, **kwargs)  # noqa: E501
            return data

    def delete_document_with_http_info(self, external_id, **kwargs):  # noqa: E501
        """Delete a document including its metadata, files, versions and contents. Contents are only only deleted when not referenced by any other versions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_document_with_http_info(external_id, async_req=True)
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
                    " to method delete_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'external_id' is set
        if ('external_id' not in params or
                params['external_id'] is None):
            raise ValueError("Missing the required parameter `external_id` when calling `delete_document`")  # noqa: E501

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
            '/task/delete/documents/{externalId}', 'DELETE',
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

    def import_document_contents_for_file_with_type(self, contents, external_id, type_name, **kwargs):  # noqa: E501
        """Import file as the current version for {typeName} of document referenced by {externalId} without indexing  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_document_contents_for_file_with_type(contents, external_id, type_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str contents: (required)
        :param str external_id: (required)
        :param str type_name: (required)
        :param bool allow_new_document:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.import_document_contents_for_file_with_type_with_http_info(contents, external_id, type_name, **kwargs)  # noqa: E501
        else:
            (data) = self.import_document_contents_for_file_with_type_with_http_info(contents, external_id, type_name, **kwargs)  # noqa: E501
            return data

    def import_document_contents_for_file_with_type_with_http_info(self, contents, external_id, type_name, **kwargs):  # noqa: E501
        """Import file as the current version for {typeName} of document referenced by {externalId} without indexing  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_document_contents_for_file_with_type_with_http_info(contents, external_id, type_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str contents: (required)
        :param str external_id: (required)
        :param str type_name: (required)
        :param bool allow_new_document:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contents', 'external_id', 'type_name', 'allow_new_document']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_document_contents_for_file_with_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'contents' is set
        if ('contents' not in params or
                params['contents'] is None):
            raise ValueError("Missing the required parameter `contents` when calling `import_document_contents_for_file_with_type`")  # noqa: E501
        # verify the required parameter 'external_id' is set
        if ('external_id' not in params or
                params['external_id'] is None):
            raise ValueError("Missing the required parameter `external_id` when calling `import_document_contents_for_file_with_type`")  # noqa: E501
        # verify the required parameter 'type_name' is set
        if ('type_name' not in params or
                params['type_name'] is None):
            raise ValueError("Missing the required parameter `type_name` when calling `import_document_contents_for_file_with_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'external_id' in params:
            path_params['externalId'] = params['external_id']  # noqa: E501
        if 'type_name' in params:
            path_params['typeName'] = params['type_name']  # noqa: E501

        query_params = []
        if 'allow_new_document' in params:
            query_params.append(('allowNewDocument', params['allow_new_document']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'contents' in params:
            local_var_files['contents'] = params['contents']  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/task/import/documents/{externalId}/{typeName}', 'POST',
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

    def index_all(self, type, **kwargs):  # noqa: E501
        """Index all files by type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_all(type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.index_all_with_http_info(type, **kwargs)  # noqa: E501
        else:
            (data) = self.index_all_with_http_info(type, **kwargs)  # noqa: E501
            return data

    def index_all_with_http_info(self, type, **kwargs):  # noqa: E501
        """Index all files by type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_all_with_http_info(type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method index_all" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `index_all`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'type' in params:
            path_params['type'] = params['type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/task/index/files/{type}', 'POST',
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

    def index_document(self, external_id, type, **kwargs):  # noqa: E501
        """Index file of document by externalId and file type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_document(external_id, type, async_req=True)
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
            return self.index_document_with_http_info(external_id, type, **kwargs)  # noqa: E501
        else:
            (data) = self.index_document_with_http_info(external_id, type, **kwargs)  # noqa: E501
            return data

    def index_document_with_http_info(self, external_id, type, **kwargs):  # noqa: E501
        """Index file of document by externalId and file type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_document_with_http_info(external_id, type, async_req=True)
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
                    " to method index_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'external_id' is set
        if ('external_id' not in params or
                params['external_id'] is None):
            raise ValueError("Missing the required parameter `external_id` when calling `index_document`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `index_document`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'external_id' in params:
            path_params['externalId'] = params['external_id']  # noqa: E501
        if 'type' in params:
            path_params['type'] = params['type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/task/index/document/{externalId}/{type}', 'POST',
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

    def index_single_index(self, name, **kwargs):  # noqa: E501
        """Index or reindex single index with all relevant files, including those without versions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_single_index(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.index_single_index_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.index_single_index_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def index_single_index_with_http_info(self, name, **kwargs):  # noqa: E501
        """Index or reindex single index with all relevant files, including those without versions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_single_index_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method index_single_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `index_single_index`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/task/index/{name}', 'POST',
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

    def post_identifiers(self, **kwargs):  # noqa: E501
        """post_identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_identifiers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InputStream body:
        :return: list[Document]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_identifiers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_identifiers_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_identifiers_with_http_info(self, **kwargs):  # noqa: E501
        """post_identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_identifiers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InputStream body:
        :return: list[Document]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_identifiers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/task/register', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Document]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_identifiers(self, **kwargs):  # noqa: E501
        """put_identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_identifiers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InputStream body:
        :return: list[Document]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_identifiers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.put_identifiers_with_http_info(**kwargs)  # noqa: E501
            return data

    def put_identifiers_with_http_info(self, **kwargs):  # noqa: E501
        """put_identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_identifiers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InputStream body:
        :return: list[Document]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_identifiers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/task/register', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Document]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
