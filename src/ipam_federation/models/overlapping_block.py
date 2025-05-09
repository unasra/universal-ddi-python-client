# coding: utf-8

"""
    IPAM Federation API

    The DDI IPAM Federation application enables a SaaS administrator to manage multiple IPAM systems from one central control point CSP.    

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self


class OverlappingBlock(BaseModel):
    """
    An __OverlappingBlock__ object (_federation/overlapping_block_) is a set of contiguous IP addresses with no gap, expressed as a CIDR block. It is explicitly associated with a Federated Realm, and implicitly with a Federated Block Parent. An __OverlappingBlock__ in a given realm is said to be the child of the closest enclosing parent. An __OverlappingBlock__ indicates an address range that may be managed independently by all participating IPAM services.
    """ # noqa: E501
    address: StrictStr = Field(
        description=
        "The address field in form “a.b.c.d/n” where the “/n” may be omitted. In this case, the CIDR value must be defined in the _cidr_ field. When reading, the _address_ field is always in the form “a.b.c.d”."
    )
    cidr: Optional[Annotated[int, Field(le=128, strict=True, ge=1)]] = Field(
        default=None,
        description=
        "The CIDR of the overlapping block. This is required, if _address_ does not specify it in its input."
    )
    comment: Optional[StrictStr] = Field(
        default=None,
        description=
        "The description for the overlapping block. May contain 0 to 1024 characters. Can include UTF-8."
    )
    created_at: Optional[datetime] = Field(
        default=None, description="Time when the object has been created.")
    federated_realm: StrictStr = Field(description="The resource identifier.")
    id: Optional[StrictStr] = Field(default=None,
                                    description="The resource identifier.")
    name: Optional[StrictStr] = Field(
        default=None,
        description=
        "The name of the overlapping block. May contain 1 to 256 characters. Can include UTF-8."
    )
    parent: Optional[StrictStr] = Field(default=None,
                                        description="The resource identifier.")
    protocol: Optional[StrictStr] = Field(
        default=None,
        description=
        "The type of protocol of overlapping block (_ip4_ or _ip6_).")
    tags: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The tags for the overlapping block in JSON format.")
    updated_at: Optional[datetime] = Field(
        default=None,
        description=
        "Time when the object has been updated. Equals to _created_at_ if not updated after creation."
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "address", "cidr", "comment", "created_at", "federated_realm", "id",
        "name", "parent", "protocol", "tags", "updated_at"
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OverlappingBlock from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "id",
            "protocol",
            "updated_at",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OverlappingBlock from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "cidr": obj.get("cidr"),
            "comment": obj.get("comment"),
            "created_at": obj.get("created_at"),
            "federated_realm": obj.get("federated_realm"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "parent": obj.get("parent"),
            "protocol": obj.get("protocol"),
            "tags": obj.get("tags"),
            "updated_at": obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
