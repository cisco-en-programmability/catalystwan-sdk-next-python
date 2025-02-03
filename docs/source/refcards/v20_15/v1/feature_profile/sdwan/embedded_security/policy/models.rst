======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    GlobalOptionTypeDef = Literal["global"]

    ZoneValueStringDef = Literal["default", "self", "untrusted"]

    OnStringValueDef = Literal["on"]

    SettingsFailureModeDef = Literal["close", "open"]

    NetworkSettingsOptionTypeDef = Literal["network-settings"]

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


    class Settings:
        audit_trail: Optional[OnStringDef]
        failure_mode: Optional[OneOfSettingsFailureModeOptionsDef]
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
        tcp_syn_flood_limit: Optional[
            OneOfSettingsTcpSynFloodLimitOptionsDef
        ]
        unified_logging: Optional[OnStringDef]


    class OneOfAppHostingNatOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAppHostingNatOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAppHostingResourceProfileOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ResourceProfileValueDef  # pytype: disable=annotation-type-mismatch


    class AppHosting:
        database_url: Union[
            OneOfAppHostingNatOptionsDef1, OneOfAppHostingNatOptionsDef2
        ]
        nat: Union[
            OneOfAppHostingNatOptionsDef1, OneOfAppHostingNatOptionsDef2
        ]
        resource_profile: Union[
            OneOfAppHostingResourceProfileOptionsDef1,
            OneOfAppHostingNatOptionsDef2,
        ]


    class Data:
        assembly: List[Union[Assembly1, Assembly2, Assembly3]]
        app_hosting: Optional[AppHosting]
        settings: Optional[Settings]


    class CreateEmbeddedSecurityProfileParcelPostRequest:
        """
        Policy profile parcel schema for POST request
        """

        data: Data
        description: str
        name: str
        # This is the documentation for POST request schema for Policy profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


