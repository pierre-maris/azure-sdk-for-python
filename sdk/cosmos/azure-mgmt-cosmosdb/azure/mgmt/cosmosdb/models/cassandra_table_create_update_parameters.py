# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class CassandraTableCreateUpdateParameters(Resource):
    """Parameters to create and update Cosmos DB Cassandra table.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The unique resource identifier of the ARM resource.
    :vartype id: str
    :ivar name: The name of the ARM resource.
    :vartype name: str
    :ivar type: The type of Azure resource.
    :vartype type: str
    :param location: The location of the resource group to which the resource
     belongs.
    :type location: str
    :param tags:
    :type tags: dict[str, str]
    :param resource: Required. The standard JSON format of a Cassandra table
    :type resource: ~azure.mgmt.cosmosdb.models.CassandraTableResource
    :param options: Required. A key-value pair of options to be applied for
     the request. This corresponds to the headers sent with the request.
    :type options: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'resource': {'required': True},
        'options': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'resource': {'key': 'properties.resource', 'type': 'CassandraTableResource'},
        'options': {'key': 'properties.options', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(CassandraTableCreateUpdateParameters, self).__init__(**kwargs)
        self.resource = kwargs.get('resource', None)
        self.options = kwargs.get('options', None)
