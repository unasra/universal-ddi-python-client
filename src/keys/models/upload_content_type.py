# coding: utf-8

"""
    DDI Keys API

    The DDI Keys application is a Universal DDI service for managing TSIG keys and GSS-TSIG (Kerberos) keys which are used by other Universal DDI applications. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UploadContentType(str, Enum):
    """
     - UNKNOWN: Unknown type.  - KEYTAB: Keytab file containing Kerberos keys.
    """
    """
    allowed enum values
    """
    UNKNOWN = 'UNKNOWN'
    KEYTAB = 'KEYTAB'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UploadContentType from a JSON string"""
        return cls(json.loads(json_str))
