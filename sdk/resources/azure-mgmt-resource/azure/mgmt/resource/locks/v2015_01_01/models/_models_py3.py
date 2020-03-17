# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional, Union

import msrest.serialization


class ManagementLockListResult(msrest.serialization.Model):
    """List of management locks.

    :param value: The list of locks.
    :type value: list[~azure.mgmt.resource.locks.v2015_01_01.models.ManagementLockObject]
    :param next_link: The URL to get the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ManagementLockObject]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ManagementLockObject"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ManagementLockListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ManagementLockObject(msrest.serialization.Model):
    """Management lock information.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The Id of the lock.
    :vartype id: str
    :ivar type: The type of the lock.
    :vartype type: str
    :param name: The name of the lock.
    :type name: str
    :param level: The lock level of the management lock. Possible values include: 'NotSpecified',
     'CanNotDelete', 'ReadOnly'.
    :type level: str or ~azure.mgmt.resource.locks.v2015_01_01.models.LockLevel
    :param notes: The notes of the management lock.
    :type notes: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'level': {'key': 'properties.level', 'type': 'str'},
        'notes': {'key': 'properties.notes', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        level: Optional[Union[str, "LockLevel"]] = None,
        notes: Optional[str] = None,
        **kwargs
    ):
        super(ManagementLockObject, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = name
        self.level = level
        self.notes = notes
