# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional, List
from dataclasses import dataclass, field as _field

Type = Literal[
    "cellular",
    "ethernet",
    "globalSettings",
    "networkProtocol",
    "securityPolicy",
    "wifi",
]


@dataclass
class Variable:
    json_path: str = _field(metadata={"alias": "jsonPath"})
    var_name: str = _field(metadata={"alias": "varName"})


@dataclass
class PolicyRule:
    action: Optional[str] = _field(default=None)
    dest_ip: Optional[str] = _field(default=None, metadata={"alias": "destIp"})
    dest_port: Optional[int] = _field(default=None, metadata={"alias": "destPort"})
    protocol_type: Optional[List[str]] = _field(
        default=None, metadata={"alias": "protocolType"}
    )
    source_ip: Optional[str] = _field(default=None, metadata={"alias": "sourceIp"})
    source_port: Optional[int] = _field(default=None, metadata={"alias": "sourcePort"})


@dataclass
class CreateSecurityPolicyProfileParcelForMobilityPostRequest:
    # Name of the Profile Parcel. Must be unique.
    name: str
    type_: Type = _field(metadata={"alias": "type"})
    # User who last created this.
    created_by: Optional[str] = _field(default=None, metadata={"alias": "createdBy"})
    # Timestamp of creation
    created_on: Optional[int] = _field(default=None, metadata={"alias": "createdOn"})
    default_action: Optional[str] = _field(
        default=None, metadata={"alias": "defaultAction"}
    )
    # Description of the Profile Parcel.
    description: Optional[str] = _field(default=None)
    # System generated unique identifier of the Profile Parcel in UUID format.
    id: Optional[str] = _field(default=None)
    # User who last updated this.
    last_updated_by: Optional[str] = _field(
        default=None, metadata={"alias": "lastUpdatedBy"}
    )
    # Timestamp of last update
    last_updated_on: Optional[int] = _field(
        default=None, metadata={"alias": "lastUpdatedOn"}
    )
    policy_name: Optional[str] = _field(default=None, metadata={"alias": "policyName"})
    policy_rules: Optional[List[PolicyRule]] = _field(
        default=None, metadata={"alias": "policyRules"}
    )
    variables: Optional[List[Variable]] = _field(default=None)
