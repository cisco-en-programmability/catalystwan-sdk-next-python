# Copyright 2024 Cisco Systems, Inc. and its affiliates
from dataclasses import dataclass
from dataclasses import field as _field
from typing import Any, List, Literal, Optional, Union

GlobalOptionTypeDef = Literal["global"]

ZoneValueStringDef = Literal["default", "self", "untrusted"]

OnStringValueDef = Literal["on"]

SettingsFailureModeDef = Literal["close", "open"]

NetworkSettingsOptionTypeDef = Literal["network-settings"]

Name = Literal["server1", "server2", "server3", "server4"]

VariableOptionTypeDef = Literal["variable"]

ResourceProfileValueDef = Literal["high", "low", "medium"]


@dataclass
class CreateEmbeddedSecurityProfileParcelPostResponse:
    parcel_id: Optional[str] = _field(default=None, metadata={"alias": "parcelId"})


@dataclass
class RefIdDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str


@dataclass
class ReferenceDef:
    ref_id: RefIdDef = _field(metadata={"alias": "refId"})


@dataclass
class ZoneDef1:
    ref_id: RefIdDef = _field(metadata={"alias": "refId"})


@dataclass
class ZoneDef2:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: ZoneValueStringDef  # pytype: disable=annotation-type-mismatch


@dataclass
class Entries:
    dst_zone: Union[ZoneDef1, ZoneDef2] = _field(metadata={"alias": "dstZone"})
    src_zone: Union[ZoneDef1, ZoneDef2] = _field(metadata={"alias": "srcZone"})


@dataclass
class NgFirewallDef:
    entries: List[Entries]
    ref_id: RefIdDef = _field(metadata={"alias": "refId"})


@dataclass
class Assembly1:
    ssl_decryption: ReferenceDef = _field(metadata={"alias": "sslDecryption"})
    advanced_inspection_profile: Optional[ReferenceDef] = _field(
        default=None, metadata={"alias": "advancedInspectionProfile"}
    )
    ngfirewall: Optional[NgFirewallDef] = _field(default=None)


@dataclass
class Assembly2:
    ngfirewall: NgFirewallDef
    advanced_inspection_profile: Optional[ReferenceDef] = _field(
        default=None, metadata={"alias": "advancedInspectionProfile"}
    )
    ssl_decryption: Optional[ReferenceDef] = _field(
        default=None, metadata={"alias": "sslDecryption"}
    )


@dataclass
class Assembly3:
    advanced_inspection_profile: ReferenceDef = _field(
        metadata={"alias": "advancedInspectionProfile"}
    )
    ngfirewall: Optional[NgFirewallDef] = _field(default=None)
    ssl_decryption: Optional[ReferenceDef] = _field(
        default=None, metadata={"alias": "sslDecryption"}
    )


@dataclass
class OneOfSettingsTcpSynFloodLimitOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str


@dataclass
class OneOfSettingsMaxIncompleteTcpLimitOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str


@dataclass
class OneOfSettingsMaxIncompleteUdpLimitOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str


@dataclass
class OneOfSettingsMaxIncompleteIcmpLimitOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str


@dataclass
class OnStringDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: OnStringValueDef  # pytype: disable=annotation-type-mismatch


@dataclass
class OneOfSettingsFailureModeOptionsDef:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: SettingsFailureModeDef  # pytype: disable=annotation-type-mismatch


@dataclass
class NetworkSettingsOptionTypeObjectDef:
    option_type: NetworkSettingsOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: bool


@dataclass
class OneOfSourceInterfaceOptionsWithoutDefault1:
    option_type: VariableOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str
    default: Optional[str] = _field(default=None)
    description: Optional[str] = _field(default=None)


@dataclass
class OneOfSourceInterfaceOptionsWithoutDefault2:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: str


@dataclass
class HighSpeedLogging:
    name: Name  # pytype: disable=annotation-type-mismatch
    source_interface: Union[
        OneOfSourceInterfaceOptionsWithoutDefault1, OneOfSourceInterfaceOptionsWithoutDefault2
    ] = _field(metadata={"alias": "sourceInterface"})


@dataclass
class Settings:
    audit_trail: Optional[OnStringDef] = _field(default=None, metadata={"alias": "auditTrail"})
    failure_mode: Optional[OneOfSettingsFailureModeOptionsDef] = _field(
        default=None, metadata={"alias": "failureMode"}
    )
    # High Speed Logging
    high_speed_logging: Optional[List[HighSpeedLogging]] = _field(
        default=None, metadata={"alias": "highSpeedLogging"}
    )
    icmp_unreachable_allow: Optional[OnStringDef] = _field(
        default=None, metadata={"alias": "icmpUnreachableAllow"}
    )
    max_incomplete_icmp_limit: Optional[OneOfSettingsMaxIncompleteIcmpLimitOptionsDef] = _field(
        default=None, metadata={"alias": "maxIncompleteIcmpLimit"}
    )
    max_incomplete_tcp_limit: Optional[OneOfSettingsMaxIncompleteTcpLimitOptionsDef] = _field(
        default=None, metadata={"alias": "maxIncompleteTcpLimit"}
    )
    max_incomplete_udp_limit: Optional[OneOfSettingsMaxIncompleteUdpLimitOptionsDef] = _field(
        default=None, metadata={"alias": "maxIncompleteUdpLimit"}
    )
    security_logging: Optional[NetworkSettingsOptionTypeObjectDef] = _field(
        default=None, metadata={"alias": "securityLogging"}
    )
    session_reclassify_allow: Optional[OnStringDef] = _field(
        default=None, metadata={"alias": "sessionReclassifyAllow"}
    )
    sys_log_server_source_interface: Optional[
        Union[
            OneOfSourceInterfaceOptionsWithoutDefault1, OneOfSourceInterfaceOptionsWithoutDefault2
        ]
    ] = _field(default=None, metadata={"alias": "sysLogServerSourceInterface"})
    tcp_syn_flood_limit: Optional[OneOfSettingsTcpSynFloodLimitOptionsDef] = _field(
        default=None, metadata={"alias": "tcpSynFloodLimit"}
    )
    unified_logging: Optional[OnStringDef] = _field(
        default=None, metadata={"alias": "unifiedLogging"}
    )


@dataclass
class OneOfAppHostingNatOptionsDef1:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: bool


@dataclass
class OneOfAppHostingResourceProfileOptionsDef1:
    option_type: GlobalOptionTypeDef = _field(
        metadata={"alias": "optionType"}
    )  # pytype: disable=annotation-type-mismatch
    value: ResourceProfileValueDef  # pytype: disable=annotation-type-mismatch


@dataclass
class AppHosting:
    database_url: Union[
        OneOfAppHostingNatOptionsDef1, OneOfSourceInterfaceOptionsWithoutDefault1
    ] = _field(metadata={"alias": "databaseUrl"})
    nat: Union[OneOfAppHostingNatOptionsDef1, OneOfSourceInterfaceOptionsWithoutDefault1]
    resource_profile: Union[
        OneOfAppHostingResourceProfileOptionsDef1, OneOfSourceInterfaceOptionsWithoutDefault1
    ] = _field(metadata={"alias": "resourceProfile"})


@dataclass
class Data:
    assembly: List[Union[Assembly1, Assembly2, Assembly3]]
    app_hosting: Optional[AppHosting] = _field(default=None, metadata={"alias": "appHosting"})
    settings: Optional[Settings] = _field(default=None)


@dataclass
class CreateEmbeddedSecurityProfileParcelPostRequest:
    """
    Policy profile Feature schema for POST request
    """

    data: Data
    description: str
    name: str
    # This is the documentation for POST request schema for Policy profile Feature
    documentation: Optional[Any] = _field(default=None)
    metadata: Optional[Any] = _field(default=None)
