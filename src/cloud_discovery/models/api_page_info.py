# coding: utf-8

"""
    Discovery Configuration API V2

    The Discovery configuration service is a Universal DDI Service that provides configuration for accessing and syncing the Cloud assets   Base Paths:  1. provider: **/api/cloud_discovery/v2/**  

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class ApiPageInfo(BaseModel):
    """
    PageInfo represents both server-driven and client-driven pagination response. Server-driven pagination is a model in which the server returns some amount of data along with an token indicating there is more data and where subsequent queries can get the next page of data. Client-driven pagination is a model in which rows are addressable by offset and page size (limit).
    """ # noqa: E501
    offset: Optional[StrictInt] = Field(
        default=None,
        description=
        "The service may optionally include the offset of the next page of resources. A null value indicates no more pages."
    )
    page_token: Optional[StrictStr] = Field(
        default=None,
        description=
        "The service response should contain a string to indicate the next page of resources. A null value indicates no more pages."
    )
    size: Optional[StrictInt] = Field(
        default=None,
        description=
        "The service may optionally include the total number of resources being paged."
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["offset", "page_token", "size"]

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
        """Create an instance of ApiPageInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
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
        """Create an instance of ApiPageInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "offset": obj.get("offset"),
            "page_token": obj.get("page_token"),
            "size": obj.get("size")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
