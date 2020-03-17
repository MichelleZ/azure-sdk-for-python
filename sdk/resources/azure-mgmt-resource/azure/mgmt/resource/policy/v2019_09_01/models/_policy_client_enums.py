# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class ResourceIdentityType(str, Enum):
    """The identity type. This is the only required field when adding a system assigned identity to a
    resource.
    """

    system_assigned = "SystemAssigned"  #: Indicates that a system assigned identity is associated with the resource.
    none = "None"  #: Indicates that no identity is associated with the resource or that the existing identity should be removed.

class EnforcementMode(str, Enum):
    """The policy assignment enforcement mode. Possible values are Default and DoNotEnforce.
    """

    default = "Default"  #: The policy effect is enforced during resource creation or update.
    do_not_enforce = "DoNotEnforce"  #: The policy effect is not enforced during resource creation or update.

class PolicyType(str, Enum):
    """The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static.
    """

    not_specified = "NotSpecified"
    built_in = "BuiltIn"
    custom = "Custom"
    static = "Static"

class ParameterType(str, Enum):
    """The data type of the parameter.
    """

    string = "String"
    array = "Array"
    object = "Object"
    boolean = "Boolean"
    integer = "Integer"
    float = "Float"
    date_time = "DateTime"
