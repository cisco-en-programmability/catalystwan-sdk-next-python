======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    ZoneValueStringDef = Literal["default", "self", "untrusted"]

    OnStringValueDef = Literal["on"]

    SettingsFailureModeDef = Literal["close", "open"]

    NetworkSettingsOptionTypeDef = Literal["network-settings"]

    Name = Literal["server1", "server2", "server3", "server4"]

    VariableOptionTypeDef = Literal["variable"]

    ResourceProfileValueDef = Literal["high", "low", "medium"]

    PolicyZoneValueStringDef = Literal["default", "self", "untrusted"]

    EmbeddedSecurityPolicyZoneValueStringDef = Literal[
        "default", "self", "untrusted"
    ]

    SdRoutingEmbeddedSecurityPolicyZoneValueStringDef = Literal[
        "default", "self", "untrusted"
    ]

    FeatureProfileSdRoutingEmbeddedSecurityPolicyZoneValueStringDef = (
        Literal["default", "self", "untrusted"]
    )

    V1FeatureProfileSdRoutingEmbeddedSecurityPolicyZoneValueStringDef = (
        Literal["default", "self", "untrusted"]
    )

    ZoneValueStringDef1 = Literal["default", "self", "untrusted"]

    PolicyOnStringValueDef = Literal["on"]

    EmbeddedSecurityPolicyOnStringValueDef = Literal["on"]

    SdRoutingEmbeddedSecurityPolicyOnStringValueDef = Literal["on"]

    FeatureProfileSdRoutingEmbeddedSecurityPolicyOnStringValueDef = (
        Literal["on"]
    )

    PolicySettingsFailureModeDef = Literal["close", "open"]

    PolicyResourceProfileValueDef = Literal["high", "low", "medium"]

    ZoneValueStringDef2 = Literal["default", "self", "untrusted"]

    ZoneValueStringDef3 = Literal["default", "self", "untrusted"]

    ZoneValueStringDef4 = Literal["default", "self", "untrusted"]

    ZoneValueStringDef5 = Literal["default", "self", "untrusted"]

    ZoneValueStringDef6 = Literal["default", "self", "untrusted"]

    ZoneValueStringDef7 = Literal["default", "self", "untrusted"]

    V1FeatureProfileSdRoutingEmbeddedSecurityPolicyOnStringValueDef = (
        Literal["on"]
    )

    OnStringValueDef1 = Literal["on"]

    OnStringValueDef2 = Literal["on"]

    OnStringValueDef3 = Literal["on"]

    EmbeddedSecurityPolicySettingsFailureModeDef = Literal[
        "close", "open"
    ]

    EmbeddedSecurityPolicyResourceProfileValueDef = Literal[
        "high", "low", "medium"
    ]


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


    class OneOfAppHostingNatOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAppHostingDataBaseUrlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAppHostingDataBaseUrlOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAppHostingResourceProfileOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ResourceProfileValueDef  # pytype: disable=annotation-type-mismatch


    class OneOfAppHostingResourceProfileOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class AppHosting:
        database_url: Union[
            OneOfAppHostingDataBaseUrlOptionsDef1,
            OneOfAppHostingDataBaseUrlOptionsDef2,
        ]
        nat: Union[
            OneOfAppHostingNatOptionsDef1, OneOfAppHostingNatOptionsDef2
        ]
        resource_profile: Union[
            OneOfAppHostingResourceProfileOptionsDef1,
            OneOfAppHostingResourceProfileOptionsDef2,
        ]


    class PolicyData:
        assembly: List[Union[Assembly1, Assembly2, Assembly3]]
        app_hosting: Optional[AppHosting]
        settings: Optional[Settings]


    class Payload:
        """
        Policy profile Feature schema for POST request
        """

        data: PolicyData
        description: str
        name: str
        metadata: Optional[Any]


    class Data:
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # Policy profile Feature schema for POST request
        payload: Optional[Payload]


    class GetListSdRoutingEmbeddedSecurityPolicyPayload:
        data: Optional[List[Data]]


    class CreateEmbeddedSecurityFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class EmbeddedSecurityPolicyData:
        assembly: List[Union[Assembly1, Assembly2, Assembly3]]
        app_hosting: Optional[AppHosting]
        settings: Optional[Settings]


    class CreateEmbeddedSecurityFeaturePostRequest:
        """
        Policy profile Feature schema for POST request
        """

        data: EmbeddedSecurityPolicyData
        description: str
        name: str
        metadata: Optional[Any]


    class PolicyRefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyReferenceDef:
        ref_id: PolicyRefIdDef


    class EmbeddedSecurityPolicyRefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class EmbeddedSecurityPolicyReferenceDef:
        ref_id: EmbeddedSecurityPolicyRefIdDef


    class SdRoutingEmbeddedSecurityPolicyRefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdRoutingEmbeddedSecurityPolicyRefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyZoneDef1:
        ref_id: FeatureProfileSdRoutingEmbeddedSecurityPolicyRefIdDef


    class PolicyZoneDef2:
        option_type: GlobalOptionTypeDef
        value: PolicyZoneValueStringDef  # pytype: disable=annotation-type-mismatch


    class V1FeatureProfileSdRoutingEmbeddedSecurityPolicyRefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class EmbeddedSecurityPolicyZoneDef1:
        ref_id: V1FeatureProfileSdRoutingEmbeddedSecurityPolicyRefIdDef


    class EmbeddedSecurityPolicyZoneDef2:
        option_type: GlobalOptionTypeDef
        value: EmbeddedSecurityPolicyZoneValueStringDef  # pytype: disable=annotation-type-mismatch


    class PolicyEntries:
        dst_zone: Union[
            EmbeddedSecurityPolicyZoneDef1, EmbeddedSecurityPolicyZoneDef2
        ]
        src_zone: Union[PolicyZoneDef1, PolicyZoneDef2]


    class PolicyNgFirewallDef:
        entries: List[PolicyEntries]
        ref_id: SdRoutingEmbeddedSecurityPolicyRefIdDef


    class PolicyAssembly1:
        ssl_decryption: EmbeddedSecurityPolicyReferenceDef
        advanced_inspection_profile: Optional[PolicyReferenceDef]
        ngfirewall: Optional[PolicyNgFirewallDef]


    class RefIdDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingEmbeddedSecurityPolicyReferenceDef:
        ref_id: RefIdDef1


    class RefIdDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdRoutingEmbeddedSecurityPolicyReferenceDef:
        ref_id: RefIdDef2


    class RefIdDef3:
        option_type: GlobalOptionTypeDef
        value: str


    class RefIdDef4:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingEmbeddedSecurityPolicyZoneDef1:
        ref_id: RefIdDef4


    class SdRoutingEmbeddedSecurityPolicyZoneDef2:
        option_type: GlobalOptionTypeDef
        value: SdRoutingEmbeddedSecurityPolicyZoneValueStringDef  # pytype: disable=annotation-type-mismatch


    class RefIdDef5:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdRoutingEmbeddedSecurityPolicyZoneDef1:
        ref_id: RefIdDef5


    class FeatureProfileSdRoutingEmbeddedSecurityPolicyZoneDef2:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdRoutingEmbeddedSecurityPolicyZoneValueStringDef  # pytype: disable=annotation-type-mismatch


    class EmbeddedSecurityPolicyEntries:
        dst_zone: Union[
            FeatureProfileSdRoutingEmbeddedSecurityPolicyZoneDef1,
            FeatureProfileSdRoutingEmbeddedSecurityPolicyZoneDef2,
        ]
        src_zone: Union[
            SdRoutingEmbeddedSecurityPolicyZoneDef1,
            SdRoutingEmbeddedSecurityPolicyZoneDef2,
        ]


    class EmbeddedSecurityPolicyNgFirewallDef:
        entries: List[EmbeddedSecurityPolicyEntries]
        ref_id: RefIdDef3


    class PolicyAssembly2:
        ngfirewall: EmbeddedSecurityPolicyNgFirewallDef
        advanced_inspection_profile: Optional[
            SdRoutingEmbeddedSecurityPolicyReferenceDef
        ]
        ssl_decryption: Optional[
            FeatureProfileSdRoutingEmbeddedSecurityPolicyReferenceDef
        ]


    class RefIdDef6:
        option_type: GlobalOptionTypeDef
        value: str


    class V1FeatureProfileSdRoutingEmbeddedSecurityPolicyReferenceDef:
        ref_id: RefIdDef6


    class RefIdDef7:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef1:
        ref_id: RefIdDef7


    class RefIdDef8:
        option_type: GlobalOptionTypeDef
        value: str


    class RefIdDef9:
        option_type: GlobalOptionTypeDef
        value: str


    class V1FeatureProfileSdRoutingEmbeddedSecurityPolicyZoneDef1:
        ref_id: RefIdDef9


    class V1FeatureProfileSdRoutingEmbeddedSecurityPolicyZoneDef2:
        option_type: GlobalOptionTypeDef
        value: V1FeatureProfileSdRoutingEmbeddedSecurityPolicyZoneValueStringDef  # pytype: disable=annotation-type-mismatch


    class RefIdDef10:
        option_type: GlobalOptionTypeDef
        value: str


    class ZoneDef11:
        ref_id: RefIdDef10


    class ZoneDef21:
        option_type: GlobalOptionTypeDef
        value: ZoneValueStringDef1  # pytype: disable=annotation-type-mismatch


    class SdRoutingEmbeddedSecurityPolicyEntries:
        dst_zone: Union[ZoneDef11, ZoneDef21]
        src_zone: Union[
            V1FeatureProfileSdRoutingEmbeddedSecurityPolicyZoneDef1,
            V1FeatureProfileSdRoutingEmbeddedSecurityPolicyZoneDef2,
        ]


    class SdRoutingEmbeddedSecurityPolicyNgFirewallDef:
        entries: List[SdRoutingEmbeddedSecurityPolicyEntries]
        ref_id: RefIdDef8


    class PolicyAssembly3:
        advanced_inspection_profile: (
            V1FeatureProfileSdRoutingEmbeddedSecurityPolicyReferenceDef
        )
        ngfirewall: Optional[SdRoutingEmbeddedSecurityPolicyNgFirewallDef]
        ssl_decryption: Optional[ReferenceDef1]


    class PolicyOneOfSettingsTcpSynFloodLimitOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyOneOfSettingsMaxIncompleteTcpLimitOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyOneOfSettingsMaxIncompleteUdpLimitOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyOneOfSettingsMaxIncompleteIcmpLimitOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyOnStringDef:
        option_type: GlobalOptionTypeDef
        value: PolicyOnStringValueDef  # pytype: disable=annotation-type-mismatch


    class EmbeddedSecurityPolicyOnStringDef:
        option_type: GlobalOptionTypeDef
        value: EmbeddedSecurityPolicyOnStringValueDef  # pytype: disable=annotation-type-mismatch


    class SdRoutingEmbeddedSecurityPolicyOnStringDef:
        option_type: GlobalOptionTypeDef
        value: SdRoutingEmbeddedSecurityPolicyOnStringValueDef  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdRoutingEmbeddedSecurityPolicyOnStringDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdRoutingEmbeddedSecurityPolicyOnStringValueDef  # pytype: disable=annotation-type-mismatch


    class PolicyOneOfSettingsFailureModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicySettingsFailureModeDef  # pytype: disable=annotation-type-mismatch


    class PolicyOneOfSourceInterfaceOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyHighSpeedLogging:
        name: Name  # pytype: disable=annotation-type-mismatch
        source_interface: Union[
            OneOfSourceInterfaceOptionsWithoutDefault1,
            PolicyOneOfSourceInterfaceOptionsWithoutDefault2,
        ]


    class EmbeddedSecurityPolicyOneOfSourceInterfaceOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicySettings:
        audit_trail: Optional[PolicyOnStringDef]
        failure_mode: Optional[PolicyOneOfSettingsFailureModeOptionsDef]
        # High Speed Logging
        high_speed_logging: Optional[List[PolicyHighSpeedLogging]]
        icmp_unreachable_allow: Optional[
            FeatureProfileSdRoutingEmbeddedSecurityPolicyOnStringDef
        ]
        max_incomplete_icmp_limit: Optional[
            PolicyOneOfSettingsMaxIncompleteIcmpLimitOptionsDef
        ]
        max_incomplete_tcp_limit: Optional[
            PolicyOneOfSettingsMaxIncompleteTcpLimitOptionsDef
        ]
        max_incomplete_udp_limit: Optional[
            PolicyOneOfSettingsMaxIncompleteUdpLimitOptionsDef
        ]
        security_logging: Optional[NetworkSettingsOptionTypeObjectDef]
        session_reclassify_allow: Optional[
            SdRoutingEmbeddedSecurityPolicyOnStringDef
        ]
        sys_log_server_source_interface: Optional[
            Union[
                OneOfSourceInterfaceOptionsWithoutDefault1,
                EmbeddedSecurityPolicyOneOfSourceInterfaceOptionsWithoutDefault2,
            ]
        ]
        tcp_syn_flood_limit: Optional[
            PolicyOneOfSettingsTcpSynFloodLimitOptionsDef
        ]
        unified_logging: Optional[EmbeddedSecurityPolicyOnStringDef]


    class PolicyOneOfAppHostingResourceProfileOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: PolicyResourceProfileValueDef  # pytype: disable=annotation-type-mismatch


    class PolicyAppHosting:
        database_url: Union[
            OneOfAppHostingDataBaseUrlOptionsDef1,
            OneOfAppHostingDataBaseUrlOptionsDef2,
        ]
        nat: Union[
            OneOfAppHostingNatOptionsDef1, OneOfAppHostingNatOptionsDef2
        ]
        resource_profile: Union[
            PolicyOneOfAppHostingResourceProfileOptionsDef1,
            OneOfAppHostingResourceProfileOptionsDef2,
        ]


    class SdRoutingEmbeddedSecurityPolicyData:
        assembly: List[
            Union[PolicyAssembly1, PolicyAssembly2, PolicyAssembly3]
        ]
        app_hosting: Optional[PolicyAppHosting]
        settings: Optional[PolicySettings]


    class PolicyPayload:
        """
        Policy profile Feature schema for PUT request
        """

        data: SdRoutingEmbeddedSecurityPolicyData
        description: str
        name: str
        metadata: Optional[Any]


    class GetSingleSdRoutingEmbeddedSecurityPolicyPayload:
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # Policy profile Feature schema for PUT request
        payload: Optional[PolicyPayload]


    class EditSecurityFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class RefIdDef11:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef2:
        ref_id: RefIdDef11


    class RefIdDef12:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef3:
        ref_id: RefIdDef12


    class RefIdDef13:
        option_type: GlobalOptionTypeDef
        value: str


    class RefIdDef14:
        option_type: GlobalOptionTypeDef
        value: str


    class ZoneDef12:
        ref_id: RefIdDef14


    class ZoneDef22:
        option_type: GlobalOptionTypeDef
        value: ZoneValueStringDef2  # pytype: disable=annotation-type-mismatch


    class RefIdDef15:
        option_type: GlobalOptionTypeDef
        value: str


    class ZoneDef13:
        ref_id: RefIdDef15


    class ZoneDef23:
        option_type: GlobalOptionTypeDef
        value: ZoneValueStringDef3  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdRoutingEmbeddedSecurityPolicyEntries:
        dst_zone: Union[ZoneDef13, ZoneDef23]
        src_zone: Union[ZoneDef12, ZoneDef22]


    class FeatureProfileSdRoutingEmbeddedSecurityPolicyNgFirewallDef:
        entries: List[
            FeatureProfileSdRoutingEmbeddedSecurityPolicyEntries
        ]
        ref_id: RefIdDef13


    class EmbeddedSecurityPolicyAssembly1:
        ssl_decryption: ReferenceDef3
        advanced_inspection_profile: Optional[ReferenceDef2]
        ngfirewall: Optional[
            FeatureProfileSdRoutingEmbeddedSecurityPolicyNgFirewallDef
        ]


    class RefIdDef16:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef4:
        ref_id: RefIdDef16


    class RefIdDef17:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef5:
        ref_id: RefIdDef17


    class RefIdDef18:
        option_type: GlobalOptionTypeDef
        value: str


    class RefIdDef19:
        option_type: GlobalOptionTypeDef
        value: str


    class ZoneDef14:
        ref_id: RefIdDef19


    class ZoneDef24:
        option_type: GlobalOptionTypeDef
        value: ZoneValueStringDef4  # pytype: disable=annotation-type-mismatch


    class RefIdDef20:
        option_type: GlobalOptionTypeDef
        value: str


    class ZoneDef15:
        ref_id: RefIdDef20


    class ZoneDef25:
        option_type: GlobalOptionTypeDef
        value: ZoneValueStringDef5  # pytype: disable=annotation-type-mismatch


    class V1FeatureProfileSdRoutingEmbeddedSecurityPolicyEntries:
        dst_zone: Union[ZoneDef15, ZoneDef25]
        src_zone: Union[ZoneDef14, ZoneDef24]


    class V1FeatureProfileSdRoutingEmbeddedSecurityPolicyNgFirewallDef:
        entries: List[
            V1FeatureProfileSdRoutingEmbeddedSecurityPolicyEntries
        ]
        ref_id: RefIdDef18


    class EmbeddedSecurityPolicyAssembly2:
        ngfirewall: (
            V1FeatureProfileSdRoutingEmbeddedSecurityPolicyNgFirewallDef
        )
        advanced_inspection_profile: Optional[ReferenceDef4]
        ssl_decryption: Optional[ReferenceDef5]


    class RefIdDef21:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef6:
        ref_id: RefIdDef21


    class RefIdDef22:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef7:
        ref_id: RefIdDef22


    class RefIdDef23:
        option_type: GlobalOptionTypeDef
        value: str


    class RefIdDef24:
        option_type: GlobalOptionTypeDef
        value: str


    class ZoneDef16:
        ref_id: RefIdDef24


    class ZoneDef26:
        option_type: GlobalOptionTypeDef
        value: ZoneValueStringDef6  # pytype: disable=annotation-type-mismatch


    class RefIdDef25:
        option_type: GlobalOptionTypeDef
        value: str


    class ZoneDef17:
        ref_id: RefIdDef25


    class ZoneDef27:
        option_type: GlobalOptionTypeDef
        value: ZoneValueStringDef7  # pytype: disable=annotation-type-mismatch


    class Entries1:
        dst_zone: Union[ZoneDef17, ZoneDef27]
        src_zone: Union[ZoneDef16, ZoneDef26]


    class NgFirewallDef1:
        entries: List[Entries1]
        ref_id: RefIdDef23


    class EmbeddedSecurityPolicyAssembly3:
        advanced_inspection_profile: ReferenceDef6
        ngfirewall: Optional[NgFirewallDef1]
        ssl_decryption: Optional[ReferenceDef7]


    class EmbeddedSecurityPolicyOneOfSettingsTcpSynFloodLimitOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class EmbeddedSecurityPolicyOneOfSettingsMaxIncompleteTcpLimitOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class EmbeddedSecurityPolicyOneOfSettingsMaxIncompleteUdpLimitOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class EmbeddedSecurityPolicyOneOfSettingsMaxIncompleteIcmpLimitOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class V1FeatureProfileSdRoutingEmbeddedSecurityPolicyOnStringDef:
        option_type: GlobalOptionTypeDef
        value: V1FeatureProfileSdRoutingEmbeddedSecurityPolicyOnStringValueDef  # pytype: disable=annotation-type-mismatch


    class OnStringDef1:
        option_type: GlobalOptionTypeDef
        value: (
            OnStringValueDef1  # pytype: disable=annotation-type-mismatch
        )


    class OnStringDef2:
        option_type: GlobalOptionTypeDef
        value: (
            OnStringValueDef2  # pytype: disable=annotation-type-mismatch
        )


    class OnStringDef3:
        option_type: GlobalOptionTypeDef
        value: (
            OnStringValueDef3  # pytype: disable=annotation-type-mismatch
        )


    class EmbeddedSecurityPolicyOneOfSettingsFailureModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EmbeddedSecurityPolicySettingsFailureModeDef  # pytype: disable=annotation-type-mismatch


    class SdRoutingEmbeddedSecurityPolicyOneOfSourceInterfaceOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: str


    class EmbeddedSecurityPolicyHighSpeedLogging:
        name: Name  # pytype: disable=annotation-type-mismatch
        source_interface: Union[
            OneOfSourceInterfaceOptionsWithoutDefault1,
            SdRoutingEmbeddedSecurityPolicyOneOfSourceInterfaceOptionsWithoutDefault2,
        ]


    class FeatureProfileSdRoutingEmbeddedSecurityPolicyOneOfSourceInterfaceOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: str


    class EmbeddedSecurityPolicySettings:
        audit_trail: Optional[
            V1FeatureProfileSdRoutingEmbeddedSecurityPolicyOnStringDef
        ]
        failure_mode: Optional[
            EmbeddedSecurityPolicyOneOfSettingsFailureModeOptionsDef
        ]
        # High Speed Logging
        high_speed_logging: Optional[
            List[EmbeddedSecurityPolicyHighSpeedLogging]
        ]
        icmp_unreachable_allow: Optional[OnStringDef3]
        max_incomplete_icmp_limit: Optional[
            EmbeddedSecurityPolicyOneOfSettingsMaxIncompleteIcmpLimitOptionsDef
        ]
        max_incomplete_tcp_limit: Optional[
            EmbeddedSecurityPolicyOneOfSettingsMaxIncompleteTcpLimitOptionsDef
        ]
        max_incomplete_udp_limit: Optional[
            EmbeddedSecurityPolicyOneOfSettingsMaxIncompleteUdpLimitOptionsDef
        ]
        security_logging: Optional[NetworkSettingsOptionTypeObjectDef]
        session_reclassify_allow: Optional[OnStringDef2]
        sys_log_server_source_interface: Optional[
            Union[
                OneOfSourceInterfaceOptionsWithoutDefault1,
                FeatureProfileSdRoutingEmbeddedSecurityPolicyOneOfSourceInterfaceOptionsWithoutDefault2,
            ]
        ]
        tcp_syn_flood_limit: Optional[
            EmbeddedSecurityPolicyOneOfSettingsTcpSynFloodLimitOptionsDef
        ]
        unified_logging: Optional[OnStringDef1]


    class EmbeddedSecurityPolicyOneOfAppHostingResourceProfileOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EmbeddedSecurityPolicyResourceProfileValueDef  # pytype: disable=annotation-type-mismatch


    class EmbeddedSecurityPolicyAppHosting:
        database_url: Union[
            OneOfAppHostingDataBaseUrlOptionsDef1,
            OneOfAppHostingDataBaseUrlOptionsDef2,
        ]
        nat: Union[
            OneOfAppHostingNatOptionsDef1, OneOfAppHostingNatOptionsDef2
        ]
        resource_profile: Union[
            EmbeddedSecurityPolicyOneOfAppHostingResourceProfileOptionsDef1,
            OneOfAppHostingResourceProfileOptionsDef2,
        ]


    class FeatureProfileSdRoutingEmbeddedSecurityPolicyData:
        assembly: List[
            Union[
                EmbeddedSecurityPolicyAssembly1,
                EmbeddedSecurityPolicyAssembly2,
                EmbeddedSecurityPolicyAssembly3,
            ]
        ]
        app_hosting: Optional[EmbeddedSecurityPolicyAppHosting]
        settings: Optional[EmbeddedSecurityPolicySettings]


    class EditSecurityFeaturePutRequest:
        """
        Policy profile Feature schema for PUT request
        """

        data: FeatureProfileSdRoutingEmbeddedSecurityPolicyData
        description: str
        name: str
        metadata: Optional[Any]


