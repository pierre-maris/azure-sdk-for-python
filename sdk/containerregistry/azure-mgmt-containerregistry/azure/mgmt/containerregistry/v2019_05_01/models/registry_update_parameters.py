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


class RegistryUpdateParameters(Model):
    """The parameters for updating a container registry.

    :param tags: The tags for the container registry.
    :type tags: dict[str, str]
    :param sku: The SKU of the container registry.
    :type sku: ~azure.mgmt.containerregistry.v2019_05_01.models.Sku
    :param admin_user_enabled: The value that indicates whether the admin user
     is enabled.
    :type admin_user_enabled: bool
    :param network_rule_set: The network rule set for a container registry.
    :type network_rule_set:
     ~azure.mgmt.containerregistry.v2019_05_01.models.NetworkRuleSet
    :param policies: The policies for a container registry.
    :type policies: ~azure.mgmt.containerregistry.v2019_05_01.models.Policies
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'admin_user_enabled': {'key': 'properties.adminUserEnabled', 'type': 'bool'},
        'network_rule_set': {'key': 'properties.networkRuleSet', 'type': 'NetworkRuleSet'},
        'policies': {'key': 'properties.policies', 'type': 'Policies'},
    }

    def __init__(self, **kwargs):
        super(RegistryUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.sku = kwargs.get('sku', None)
        self.admin_user_enabled = kwargs.get('admin_user_enabled', None)
        self.network_rule_set = kwargs.get('network_rule_set', None)
        self.policies = kwargs.get('policies', None)