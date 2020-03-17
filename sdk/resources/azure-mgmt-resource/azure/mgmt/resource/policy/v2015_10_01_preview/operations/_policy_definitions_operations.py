# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class PolicyDefinitionsOperations(object):
    """PolicyDefinitionsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.policy.v2015_10_01_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def create_or_update(
        self,
        policy_definition_name,  # type: str
        parameters,  # type: "models.PolicyDefinition"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.PolicyDefinition"
        """Creates or updates a policy definition.

        :param policy_definition_name: The name of the policy definition to create.
        :type policy_definition_name: str
        :param parameters: The policy definition properties.
        :type parameters: ~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyDefinition
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyDefinition or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PolicyDefinition"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2015-10-01-preview"

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'policyDefinitionName': self._serialize.url("policy_definition_name", policy_definition_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'PolicyDefinition')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyDefinition', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policydefinitions/{policyDefinitionName}'}

    def delete(
        self,
        policy_definition_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes a policy definition.

        :param policy_definition_name: The name of the policy definition to delete.
        :type policy_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2015-10-01-preview"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'policyDefinitionName': self._serialize.url("policy_definition_name", policy_definition_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policydefinitions/{policyDefinitionName}'}

    def get(
        self,
        policy_definition_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.PolicyDefinition"
        """Gets the policy definition.

        :param policy_definition_name: The name of the policy definition to get.
        :type policy_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyDefinition or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PolicyDefinition"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2015-10-01-preview"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'policyDefinitionName': self._serialize.url("policy_definition_name", policy_definition_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyDefinition', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policydefinitions/{policyDefinitionName}'}

    def list(
        self,
        filter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.PolicyDefinitionListResult"
        """Gets all the policy definitions for a subscription.

        :param filter: The filter to apply on the operation.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyDefinitionListResult or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyDefinitionListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PolicyDefinitionListResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2015-10-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            if filter is not None:
                query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('PolicyDefinitionListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policydefinitions'}
