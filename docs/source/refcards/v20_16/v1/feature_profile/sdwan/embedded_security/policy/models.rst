======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    GlobalOptionTypeDef = Literal["global"]

    ZoneValueStringDef = Literal["default", "self", "untrusted"]

    OnStringValueDef = Literal["on"]

    SettingsFailureModeDef = Literal["close", "open"]

    NetworkSettingsOptionTypeDef = Literal["network-settings"]

    Name = Literal["server1", "server2", "server3", "server4"]

    VariableOptionTypeDef = Literal["variable"]

    ResourceProfileValueDef = Literal["high", "low", "medium"]


    class CreateEmbeddedSecurityProfileParcelPostResponse:
        parcel_id: Optional[str]


    class RefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef:
        ref_id: RefIdDef


    class ZoneDef1:
        ref_id: RefIdDef


    class ZoneDef2:
        option_type: GlobalOptionTypeDef
        value: (
            ZoneValueStringDef  # pytype: disable=annotation-type-mismatch
        )


    class Entries:
        dst_zone: Union[ZoneDef1, ZoneDef2]
        src_zone: Union[ZoneDef1, ZoneDef2]


    class NgFirewallDef:
        entries: List[Entries]
        ref_id: RefIdDef


    class Assembly1:
        ssl_decryption: ReferenceDef
        advanced_inspection_profile: Optional[ReferenceDef]
        ngfirewall: Optional[NgFirewallDef]


    class Assembly2:
        ngfirewall: NgFirewallDef
        advanced_inspection_profile: Optional[ReferenceDef]
        ssl_decryption: Optional[ReferenceDef]


    class Assembly3:
        advanced_inspection_profile: ReferenceDef
        ngfirewall: Optional[NgFirewallDef]
        ssl_decryption: Optional[ReferenceDef]


    class OneOfSettingsTcpSynFloodLimitOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSettingsMaxIncompleteTcpLimitOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSettingsMaxIncompleteUdpLimitOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSettingsMaxIncompleteIcmpLimitOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OnStringDef:
        option_type: GlobalOptionTypeDef
        value: (
            OnStringValueDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfSettingsFailureModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SettingsFailureModeDef  # pytype: disable=annotation-type-mismatch


    class NetworkSettingsOptionTypeObjectDef:
        option_type: NetworkSettingsOptionTypeDef
        value: bool


    class OneOfSourceInterfaceOptionsWithoutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSourceInterfaceOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: str


    class HighSpeedLogging:
        name: Name  # pytype: disable=annotation-type-mismatch
        source_interface: Union[
            OneOfSourceInterfaceOptionsWithoutDefault1,
            OneOfSourceInterfaceOptionsWithoutDefault2,
        ]


    class Settings:
        audit_trail: Optional[OnStringDef]
        failure_mode: Optional[OneOfSettingsFailureModeOptionsDef]
        # High Speed Logging
        high_speed_logging: Optional[List[HighSpeedLogging]]
        icmp_unreachable_allow: Optional[OnStringDef]
        max_incomplete_icmp_limit: Optional[
            OneOfSettingsMaxIncompleteIcmpLimitOptionsDef
        ]
        max_incomplete_tcp_limit: Optional[
            OneOfSettingsMaxIncompleteTcpLimitOptionsDef
        ]
        max_incomplete_udp_limit: Optional[
            OneOfSettingsMaxIncompleteUdpLimitOptionsDef
        ]
        security_logging: Optional[NetworkSettingsOptionTypeObjectDef]
        session_reclassify_allow: Optional[OnStringDef]
        sys_log_server_source_interface: Optional[
            Union[
                OneOfSourceInterfaceOptionsWithoutDefault1,
                OneOfSourceInterfaceOptionsWithoutDefault2,
            ]
        ]
        tcp_syn_flood_limit: Optional[
            OneOfSettingsTcpSynFloodLimitOptionsDef
        ]
        unified_logging: Optional[OnStringDef]


    class OneOfAppHostingNatOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAppHostingResourceProfileOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ResourceProfileValueDef  # pytype: disable=annotation-type-mismatch


    class AppHosting:
        database_url: Union[
            OneOfAppHostingNatOptionsDef1,
            OneOfSourceInterfaceOptionsWithoutDefault1,
        ]
        nat: Union[
            OneOfAppHostingNatOptionsDef1,
            OneOfSourceInterfaceOptionsWithoutDefault1,
        ]
        resource_profile: Union[
            OneOfAppHostingResourceProfileOptionsDef1,
            OneOfSourceInterfaceOptionsWithoutDefault1,
        ]


    class Data:
        assembly: List[Union[Assembly1, Assembly2, Assembly3]]
        app_hosting: Optional[AppHosting]
        settings: Optional[Settings]


    class CreateEmbeddedSecurityProfileParcelPostRequest:
        """
        Policy profile Feature schema for POST request
        """

        data: Data
        description: str
        name: str
        # This is the documentation for POST request schema for Policy profile Feature
        documentation: Optional[Any]
        metadata: Optional[Any]


