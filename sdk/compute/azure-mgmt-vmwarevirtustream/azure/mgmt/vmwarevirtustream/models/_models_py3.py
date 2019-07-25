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

from msrest.serialization import Model


class AddIdentitySourceRequest(Model):
    """AddIdentitySourceRequest.

    :param name:
    :type name: str
    :param alias:
    :type alias: str
    :param domain:
    :type domain: str
    :param base_user_dn:
    :type base_user_dn: str
    :param base_group_dn:
    :type base_group_dn: str
    :param primary_server:
    :type primary_server: str
    :param secondary_server:
    :type secondary_server: str
    :param use_ssl:
    :type use_ssl: bool
    :param username:
    :type username: str
    :param credential:
    :type credential: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'alias': {'key': 'alias', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'base_user_dn': {'key': 'baseUserDN', 'type': 'str'},
        'base_group_dn': {'key': 'baseGroupDN', 'type': 'str'},
        'primary_server': {'key': 'primaryServer', 'type': 'str'},
        'secondary_server': {'key': 'secondaryServer', 'type': 'str'},
        'use_ssl': {'key': 'useSsl', 'type': 'bool'},
        'username': {'key': 'username', 'type': 'str'},
        'credential': {'key': 'credential', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, alias: str=None, domain: str=None, base_user_dn: str=None, base_group_dn: str=None, primary_server: str=None, secondary_server: str=None, use_ssl: bool=None, username: str=None, credential: str=None, **kwargs) -> None:
        super(AddIdentitySourceRequest, self).__init__(**kwargs)
        self.name = name
        self.alias = alias
        self.domain = domain
        self.base_user_dn = base_user_dn
        self.base_group_dn = base_group_dn
        self.primary_server = primary_server
        self.secondary_server = secondary_server
        self.use_ssl = use_ssl
        self.username = username
        self.credential = credential


class Circuit(Model):
    """Circuit.

    :param primary_subnet: CIDR of primary subnet
    :type primary_subnet: str
    :param secondary_subnet: CIDR of secondary subnet
    :type secondary_subnet: str
    :param express_route_id: ID of privateCloud customer ER (Microsoft Colo
     only)
    :type express_route_id: str
    :param authorizations: authorizations on privateCloud customer ER
     (Microsoft Colo only)
    :type authorizations:
     list[~azure.mgmt.vmwarevirtustream.models.ExpressRouteAuthorization]
    """

    _attribute_map = {
        'primary_subnet': {'key': 'primarySubnet', 'type': 'str'},
        'secondary_subnet': {'key': 'secondarySubnet', 'type': 'str'},
        'express_route_id': {'key': 'expressRouteID', 'type': 'str'},
        'authorizations': {'key': 'authorizations', 'type': '[ExpressRouteAuthorization]'},
    }

    def __init__(self, *, primary_subnet: str=None, secondary_subnet: str=None, express_route_id: str=None, authorizations=None, **kwargs) -> None:
        super(Circuit, self).__init__(**kwargs)
        self.primary_subnet = primary_subnet
        self.secondary_subnet = secondary_subnet
        self.express_route_id = express_route_id
        self.authorizations = authorizations


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class Cluster(Model):
    """Cluster.

    :param cluster_id:
    :type cluster_id: int
    :param provisioning_state: Possible values include: 'Succeeded', 'Failed',
     'Cancelled', 'Updating'
    :type provisioning_state: str or ~azure.mgmt.vmwarevirtustream.models.enum
    :param cluster_size:
    :type cluster_size: int
    :param hosts:
    :type hosts: list[str]
    """

    _attribute_map = {
        'cluster_id': {'key': 'clusterId', 'type': 'int'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'cluster_size': {'key': 'clusterSize', 'type': 'int'},
        'hosts': {'key': 'hosts', 'type': '[str]'},
    }

    def __init__(self, *, cluster_id: int=None, provisioning_state=None, cluster_size: int=None, hosts=None, **kwargs) -> None:
        super(Cluster, self).__init__(**kwargs)
        self.cluster_id = cluster_id
        self.provisioning_state = provisioning_state
        self.cluster_size = cluster_size
        self.hosts = hosts


class ClusterDetail(Model):
    """ClusterDetail.

    :param cluster_size: number of hosts in PrivateCloud cluster
    :type cluster_size: int
    """

    _attribute_map = {
        'cluster_size': {'key': 'clusterSize', 'type': 'int'},
    }

    def __init__(self, *, cluster_size: int=None, **kwargs) -> None:
        super(ClusterDetail, self).__init__(**kwargs)
        self.cluster_size = cluster_size


class ClusterRequest(Model):
    """ClusterRequest.

    :param location:
    :type location: str
    :param properties:
    :type properties: ~azure.mgmt.vmwarevirtustream.models.ClusterDetail
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ClusterDetail'},
    }

    def __init__(self, *, location: str=None, properties=None, **kwargs) -> None:
        super(ClusterRequest, self).__init__(**kwargs)
        self.location = location
        self.properties = properties


class ClusterResponse(Model):
    """ClusterResponse.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id:
    :vartype id: str
    :param location:
    :type location: str
    :ivar name:
    :vartype name: str
    :param properties:
    :type properties: ~azure.mgmt.vmwarevirtustream.models.Cluster
    :ivar type:
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'Cluster'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, properties=None, **kwargs) -> None:
        super(ClusterResponse, self).__init__(**kwargs)
        self.id = None
        self.location = location
        self.name = None
        self.properties = properties
        self.type = None


class DeleteIdentitySourceRequest(Model):
    """DeleteIdentitySourceRequest.

    :param name:
    :type name: str
    :param alias:
    :type alias: str
    :param domain:
    :type domain: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'alias': {'key': 'alias', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, alias: str=None, domain: str=None, **kwargs) -> None:
        super(DeleteIdentitySourceRequest, self).__init__(**kwargs)
        self.name = name
        self.alias = alias
        self.domain = domain


class Endpoints(Model):
    """Endpoints.

    :param nsx_manager:
    :type nsx_manager: str
    :param vcsa:
    :type vcsa: str
    """

    _attribute_map = {
        'nsx_manager': {'key': 'nsxManager', 'type': 'str'},
        'vcsa': {'key': 'vcsa', 'type': 'str'},
    }

    def __init__(self, *, nsx_manager: str=None, vcsa: str=None, **kwargs) -> None:
        super(Endpoints, self).__init__(**kwargs)
        self.nsx_manager = nsx_manager
        self.vcsa = vcsa


class ExpressRouteAuthorization(Model):
    """ExpressRouteAuthorization.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param key:
    :type key: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, name: str=None, key: str=None, **kwargs) -> None:
        super(ExpressRouteAuthorization, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.key = key


class GetAdminCredentialsResponse(Model):
    """GetAdminCredentialsResponse.

    :param nsx_user:
    :type nsx_user: str
    :param nsx_password:
    :type nsx_password: str
    :param user:
    :type user: str
    :param password:
    :type password: str
    """

    _attribute_map = {
        'nsx_user': {'key': 'nsxUser', 'type': 'str'},
        'nsx_password': {'key': 'nsxPassword', 'type': 'str'},
        'user': {'key': 'user', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
    }

    def __init__(self, *, nsx_user: str=None, nsx_password: str=None, user: str=None, password: str=None, **kwargs) -> None:
        super(GetAdminCredentialsResponse, self).__init__(**kwargs)
        self.nsx_user = nsx_user
        self.nsx_password = nsx_password
        self.user = user
        self.password = password


class IdentitySource(Model):
    """IdentitySource.

    :param name:
    :type name: str
    :param alias:
    :type alias: str
    :param domain:
    :type domain: str
    :param base_user_dn:
    :type base_user_dn: str
    :param base_group_dn:
    :type base_group_dn: str
    :param primary_server:
    :type primary_server: str
    :param secondary_server:
    :type secondary_server: str
    :param use_ssl:
    :type use_ssl: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'alias': {'key': 'alias', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'base_user_dn': {'key': 'baseUserDN', 'type': 'str'},
        'base_group_dn': {'key': 'baseGroupDN', 'type': 'str'},
        'primary_server': {'key': 'primaryServer', 'type': 'str'},
        'secondary_server': {'key': 'secondaryServer', 'type': 'str'},
        'use_ssl': {'key': 'useSsl', 'type': 'bool'},
    }

    def __init__(self, *, name: str=None, alias: str=None, domain: str=None, base_user_dn: str=None, base_group_dn: str=None, primary_server: str=None, secondary_server: str=None, use_ssl: bool=None, **kwargs) -> None:
        super(IdentitySource, self).__init__(**kwargs)
        self.name = name
        self.alias = alias
        self.domain = domain
        self.base_user_dn = base_user_dn
        self.base_group_dn = base_group_dn
        self.primary_server = primary_server
        self.secondary_server = secondary_server
        self.use_ssl = use_ssl


class Operation(Model):
    """A REST API operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the operation being performed on this particular
     object.
    :vartype name: str
    :ivar display: Contains the localized display information for this
     particular operation / action.
    :vartype display: ~azure.mgmt.vmwarevirtustream.models.OperationDisplay
    """

    _validation = {
        'name': {'readonly': True},
        'display': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = None


class OperationDisplay(Model):
    """Contains the localized display information for this particular operation /
    action.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provider: The localized friendly form of the resource provider name.
    :vartype provider: str
    :ivar resource: The localized friendly form of the resource type related
     to this action/operation.
    :vartype resource: str
    :ivar operation: The localized friendly name for the operation.
    :vartype operation: str
    :ivar description: The localized friendly description for the operation.
    :vartype description: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None


class PrivateCloud(Model):
    """PrivateCloud.

    :param provisioning_state: Possible values include: 'Succeeded', 'Failed',
     'Cancelled', 'Pending', 'Building', 'Updating'
    :type provisioning_state: str or ~azure.mgmt.vmwarevirtustream.models.enum
    :param circuit:
    :type circuit: ~azure.mgmt.vmwarevirtustream.models.Circuit
    :param cluster:
    :type cluster: ~azure.mgmt.vmwarevirtustream.models.Cluster
    :param clusters:
    :type clusters: list[str]
    :param endpoints:
    :type endpoints: ~azure.mgmt.vmwarevirtustream.models.Endpoints
    :param internet_enabled:
    :type internet_enabled: bool
    :param identity_sources:
    :type identity_sources:
     list[~azure.mgmt.vmwarevirtustream.models.IdentitySource]
    :param vpc:
    :type vpc: str
    """

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'circuit': {'key': 'circuit', 'type': 'Circuit'},
        'cluster': {'key': 'cluster', 'type': 'Cluster'},
        'clusters': {'key': 'clusters', 'type': '[str]'},
        'endpoints': {'key': 'endpoints', 'type': 'Endpoints'},
        'internet_enabled': {'key': 'internetEnabled', 'type': 'bool'},
        'identity_sources': {'key': 'identitySources', 'type': '[IdentitySource]'},
        'vpc': {'key': 'vpc', 'type': 'str'},
    }

    def __init__(self, *, provisioning_state=None, circuit=None, cluster=None, clusters=None, endpoints=None, internet_enabled: bool=None, identity_sources=None, vpc: str=None, **kwargs) -> None:
        super(PrivateCloud, self).__init__(**kwargs)
        self.provisioning_state = provisioning_state
        self.circuit = circuit
        self.cluster = cluster
        self.clusters = clusters
        self.endpoints = endpoints
        self.internet_enabled = internet_enabled
        self.identity_sources = identity_sources
        self.vpc = vpc


class PrivateCloudRequest(Model):
    """PrivateCloudRequest.

    :param location:
    :type location: str
    :param properties:
    :type properties: ~azure.mgmt.vmwarevirtustream.models.PrivateCloud
    :param tags:
    :type tags: object
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'PrivateCloud'},
        'tags': {'key': 'tags', 'type': 'object'},
    }

    def __init__(self, *, location: str=None, properties=None, tags=None, **kwargs) -> None:
        super(PrivateCloudRequest, self).__init__(**kwargs)
        self.location = location
        self.properties = properties
        self.tags = tags


class PrivateCloudResponse(Model):
    """PrivateCloudResponse.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id:
    :vartype id: str
    :param location:
    :type location: str
    :ivar name:
    :vartype name: str
    :param properties:
    :type properties: ~azure.mgmt.vmwarevirtustream.models.PrivateCloud
    :ivar type:
    :vartype type: str
    :param tags:
    :type tags: object
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'PrivateCloud'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'object'},
    }

    def __init__(self, *, location: str=None, properties=None, tags=None, **kwargs) -> None:
        super(PrivateCloudResponse, self).__init__(**kwargs)
        self.id = None
        self.location = location
        self.name = None
        self.properties = properties
        self.type = None
        self.tags = tags


class PrivateCloudResponseList(Model):
    """PrivateCloudResponseList.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value:
    :vartype value: object
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'object'},
    }

    def __init__(self, **kwargs) -> None:
        super(PrivateCloudResponseList, self).__init__(**kwargs)
        self.value = None