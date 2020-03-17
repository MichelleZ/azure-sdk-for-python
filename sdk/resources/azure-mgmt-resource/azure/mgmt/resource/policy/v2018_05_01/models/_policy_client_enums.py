# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class ResourceIdentityType(str, Enum):
    """The identity type.
    """

    system_assigned = "SystemAssigned"
    none = "None"

class PolicyType(str, Enum):
    """The type of policy definition. Possible values are NotSpecified, BuiltIn, and Custom.
    """

    not_specified = "NotSpecified"
    built_in = "BuiltIn"
    custom = "Custom"

class PolicyMode(str, Enum):
    """The policy definition mode. Possible values are NotSpecified, Indexed, and All.
    """

    not_specified = "NotSpecified"
    indexed = "Indexed"
    all = "All"
