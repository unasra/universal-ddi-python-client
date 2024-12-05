# coding: utf-8

"""
    Discovery Configuration API V2

    The Discovery configuration service is a BloxOne Service that provides configuration for accessing and syncing the Cloud assets   Base Paths:  1. provider: **/api/cloud_discovery/v2/**  

    The version of the OpenAPI document: v2
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
from cloud_discovery.models.additional_config import AdditionalConfig
from cloud_discovery.models.credential_preference import CredentialPreference
from cloud_discovery.models.destination import Destination
from cloud_discovery.models.source_config import SourceConfig
from typing import Optional, Set
from typing_extensions import Self


class DiscoveryConfig(BaseModel):
    """
    Discovery configuration
    """

  # noqa: E501
    account_preference: StrictStr = Field(
        description=
        "Account preference. For ex.: single, multiple, auto-discover-multiple."
    )
    additional_config: Optional[AdditionalConfig] = Field(
        default=None,
        description=
        "Additional configuration. Ex.: '{    \"excluded_object_types\": [],    \"exclusion_account_list\": [],    \"zone_forwarding\": \"true\" or \"false\" }'."
    )
    created_at: Optional[datetime] = Field(
        default=None,
        description="Timestamp when the object has been created.")
    credential_preference: Optional[CredentialPreference] = Field(
        default=None,
        description=
        "Credential preference. Ex.: '{    \"type\": \"static\" or \"delegated\",    \"access_identifier_type\": \"role_arn\" or \"tenant_id\" or \"project_id\"  }'."
    )
    deleted_at: Optional[datetime] = Field(
        default=None,
        description="Timestamp when the object has been deleted.")
    description: Optional[StrictStr] = Field(
        default=None,
        description="Description of the discovery config. Optional.")
    desired_state: Optional[StrictStr] = Field(
        default=None, description="Desired state. Default is \"enabled\".")
    destination_types_enabled: Optional[List[StrictStr]] = Field(
        default=None,
        description="Destinations types enabled: Ex.: DNS, IPAM and ACCOUNT.")
    destinations: Optional[List[Destination]] = Field(
        default=None, description="Destinations.")
    id: Optional[StrictStr] = Field(
        default=None,
        description="Auto-generated unique discovery config ID. Format BloxID."
    )
    last_sync: Optional[datetime] = Field(default=None,
                                          description="Last sync timestamp.")
    name: StrictStr = Field(description="Name of the discovery config.")
    provider_type: StrictStr = Field(
        description=
        "Provider type. Ex.: Amazon Web Services, Google Cloud Platform, Microsoft Azure."
    )
    source_configs: Optional[List[SourceConfig]] = Field(
        default=None, description="Source configs.")
    status: Optional[StrictStr] = Field(
        default=None,
        description=
        "Status of the sync operation. In single account case, Its the combined status of account & all the destinations statuses In auto discover case, Its the status of the account discovery only."
    )
    status_message: Optional[StrictStr] = Field(
        default=None,
        description="Aggregate status message of the sync operation.")
    sync_interval: Optional[StrictStr] = None
    tags: Optional[Dict[str, Any]] = Field(default=None,
                                           description="Tagging specifics.")
    updated_at: Optional[datetime] = Field(
        default=None,
        description="Timestamp when the object has been updated.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "account_preference", "additional_config", "created_at",
        "credential_preference", "deleted_at", "description", "desired_state",
        "destination_types_enabled", "destinations", "id", "last_sync", "name",
        "provider_type", "source_configs", "status", "status_message",
        "sync_interval", "tags", "updated_at"
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
        """Create an instance of DiscoveryConfig from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "deleted_at",
            "id",
            "last_sync",
            "status",
            "status_message",
            "updated_at",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of additional_config
        if self.additional_config:
            _dict['additional_config'] = self.additional_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credential_preference
        if self.credential_preference:
            _dict[
                'credential_preference'] = self.credential_preference.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of each item in destinations (list)
        _items = []
        if self.destinations:
            for _item in self.destinations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['destinations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in source_configs (list)
        _items = []
        if self.source_configs:
            for _item in self.source_configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['source_configs'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DiscoveryConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account_preference":
            obj.get("account_preference"),
            "additional_config":
            AdditionalConfig.from_dict(obj["additional_config"])
            if obj.get("additional_config") is not None else None,
            "created_at":
            obj.get("created_at"),
            "credential_preference":
            CredentialPreference.from_dict(obj["credential_preference"])
            if obj.get("credential_preference") is not None else None,
            "deleted_at":
            obj.get("deleted_at"),
            "description":
            obj.get("description"),
            "desired_state":
            obj.get("desired_state"),
            "destination_types_enabled":
            obj.get("destination_types_enabled"),
            "destinations":
            [Destination.from_dict(_item) for _item in obj["destinations"]]
            if obj.get("destinations") is not None else None,
            "id":
            obj.get("id"),
            "last_sync":
            obj.get("last_sync"),
            "name":
            obj.get("name"),
            "provider_type":
            obj.get("provider_type"),
            "source_configs":
            [SourceConfig.from_dict(_item) for _item in obj["source_configs"]]
            if obj.get("source_configs") is not None else None,
            "status":
            obj.get("status"),
            "status_message":
            obj.get("status_message"),
            "sync_interval":
            obj.get("sync_interval"),
            "tags":
            obj.get("tags"),
            "updated_at":
            obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
