======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    SseInstanceDef = Literal["Cisco-Secure-Access"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanFalseDef = Literal[False]

    CiscoGlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    SseCiscoGlobalOptionTypeDef = Literal["global"]

    CiscoVariableOptionTypeDef = Literal["variable"]

    SdRoutingSseCiscoGlobalOptionTypeDef = Literal["global"]

    SseCiscoVariableOptionTypeDef = Literal["variable"]

    CiscoDefaultOptionTypeDef = Literal["default"]

    FeatureProfileSdRoutingSseCiscoGlobalOptionTypeDef = Literal["global"]

    InterfaceTunnelDcPreferenceDef = Literal["primary-dc", "secondary-dc"]

    V1FeatureProfileSdRoutingSseCiscoGlobalOptionTypeDef = Literal[
        "global"
    ]

    SdRoutingSseCiscoVariableOptionTypeDef = Literal["variable"]

    SseCiscoDefaultOptionTypeDef = Literal["default"]

    GlobalOptionTypeDef1 = Literal["global"]

    FeatureProfileSdRoutingSseCiscoVariableOptionTypeDef = Literal[
        "variable"
    ]

    GlobalOptionTypeDef2 = Literal["global"]

    V1FeatureProfileSdRoutingSseCiscoVariableOptionTypeDef = Literal[
        "variable"
    ]

    SdRoutingSseCiscoDefaultOptionTypeDef = Literal["default"]

    GlobalOptionTypeDef3 = Literal["global"]

    VariableOptionTypeDef1 = Literal["variable"]

    FeatureProfileSdRoutingSseCiscoDefaultOptionTypeDef = Literal[
        "default"
    ]

    GlobalOptionTypeDef4 = Literal["global"]

    VariableOptionTypeDef2 = Literal["variable"]

    V1FeatureProfileSdRoutingSseCiscoDefaultOptionTypeDef = Literal[
        "default"
    ]

    GlobalOptionTypeDef5 = Literal["global"]

    VariableOptionTypeDef3 = Literal["variable"]

    DefaultOptionTypeDef1 = Literal["default"]

    GlobalOptionTypeDef6 = Literal["global"]

    InterfaceIkeCiphersuiteDef = Literal[
        "aes128-cbc-sha1",
        "aes128-cbc-sha2",
        "aes256-cbc-sha1",
        "aes256-cbc-sha2",
    ]

    VariableOptionTypeDef4 = Literal["variable"]

    DefaultOptionTypeDef2 = Literal["default"]

    DefaultInterfaceIkeCiphersuiteDef = Literal["aes256-cbc-sha1"]

    GlobalOptionTypeDef7 = Literal["global"]

    InterfaceIkeGroupDef = Literal[
        "14", "15", "16", "19", "2", "20", "21", "5"
    ]

    VariableOptionTypeDef5 = Literal["variable"]

    DefaultOptionTypeDef3 = Literal["default"]

    GlobalOptionTypeDef8 = Literal["global"]

    VariableOptionTypeDef6 = Literal["variable"]

    DefaultOptionTypeDef4 = Literal["default"]

    GlobalOptionTypeDef9 = Literal["global"]

    VariableOptionTypeDef7 = Literal["variable"]

    DefaultOptionTypeDef5 = Literal["default"]

    GlobalOptionTypeDef10 = Literal["global"]

    InterfaceIpsecCiphersuiteDef = Literal[
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-cbc-sha384",
        "aes256-cbc-sha512",
        "aes256-gcm",
    ]

    VariableOptionTypeDef8 = Literal["variable"]

    DefaultOptionTypeDef6 = Literal["default"]

    GlobalOptionTypeDef11 = Literal["global"]

    InterfacePerfectForwardSecrecyDef = Literal[
        "group-14",
        "group-15",
        "group-16",
        "group-19",
        "group-2",
        "group-20",
        "group-21",
        "group-5",
        "none",
    ]

    VariableOptionTypeDef9 = Literal["variable"]

    DefaultOptionTypeDef7 = Literal["default"]

    GlobalOptionTypeDef12 = Literal["global"]

    DefaultOptionTypeDef8 = Literal["default"]

    DefaultInterfaceTrackerDef = Literal["DefaultTracker"]

    BooleanTrueDef = Literal[True]

    GlobalOptionTypeDef13 = Literal["global"]

    GlobalOptionTypeDef14 = Literal["global"]

    GlobalOptionTypeDef15 = Literal["global"]

    GlobalOptionTypeDef16 = Literal["global"]

    DefaultRegionDef = Literal["auto"]

    GlobalOptionTypeDef17 = Literal["global"]

    GlobalOptionTypeDef18 = Literal["global"]

    VariableOptionTypeDef10 = Literal["variable"]

    GlobalOptionTypeDef19 = Literal["global"]

    VariableOptionTypeDef11 = Literal["variable"]

    DefaultOptionTypeDef9 = Literal["default"]

    GlobalOptionTypeDef20 = Literal["global"]

    VariableOptionTypeDef12 = Literal["variable"]

    DefaultOptionTypeDef10 = Literal["default"]

    GlobalOptionTypeDef21 = Literal["global"]

    VariableOptionTypeDef13 = Literal["variable"]

    DefaultOptionTypeDef11 = Literal["default"]

    TrackerTrackerTypeDef = Literal["cisco-sse"]

    CiscoSseInstanceDef = Literal["Cisco-Secure-Access"]

    CiscoDefaultRegionDef = Literal["auto"]

    CiscoTrackerTrackerTypeDef = Literal["cisco-sse"]

    SseCiscoSseInstanceDef = Literal["Cisco-Secure-Access"]

    SseCiscoDefaultRegionDef = Literal["auto"]

    SseCiscoTrackerTrackerTypeDef = Literal["cisco-sse"]


    class OneOfSseInstanceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SseInstanceDef


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfInterfaceIfNameOptionsDef:
        option_type: CiscoGlobalOptionTypeDef
        value: str


    class OneOfOnBooleanDefaultFalseOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOnBooleanDefaultFalseOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultFalseOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfInterfaceTunnelSourceInterfaceOptionsDef1:
        option_type: SseCiscoGlobalOptionTypeDef
        value: str


    class OneOfInterfaceTunnelSourceInterfaceOptionsDef2:
        option_type: CiscoVariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceTunnelRouteViaOptionsDef1:
        option_type: SdRoutingSseCiscoGlobalOptionTypeDef
        value: str


    class OneOfInterfaceTunnelRouteViaOptionsDef2:
        option_type: SseCiscoVariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceTunnelRouteViaOptionsDef3:
        option_type: Optional[CiscoDefaultOptionTypeDef]
        value: Optional[str]


    class OneOfInterfaceTunnelDcPreferenceOptionsDef:
        option_type: FeatureProfileSdRoutingSseCiscoGlobalOptionTypeDef
        value: InterfaceTunnelDcPreferenceDef


    class OneOfInterfaceTcpMssAdjustOptionsDef1:
        option_type: V1FeatureProfileSdRoutingSseCiscoGlobalOptionTypeDef
        value: int


    class OneOfInterfaceTcpMssAdjustOptionsDef2:
        option_type: SdRoutingSseCiscoVariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceTcpMssAdjustOptionsDef3:
        option_type: SseCiscoDefaultOptionTypeDef


    class OneOfInterfaceMtuOptionsDef1:
        option_type: GlobalOptionTypeDef1
        value: int


    class OneOfInterfaceMtuOptionsDef2:
        option_type: FeatureProfileSdRoutingSseCiscoVariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceDpdIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef2
        value: int


    class OneOfInterfaceDpdIntervalOptionsDef2:
        option_type: (
            V1FeatureProfileSdRoutingSseCiscoVariableOptionTypeDef
        )
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceDpdIntervalOptionsDef3:
        option_type: Optional[SdRoutingSseCiscoDefaultOptionTypeDef]
        value: Optional[int]


    class OneOfInterfaceDpdRetriesOptionsDef1:
        option_type: GlobalOptionTypeDef3
        value: int


    class OneOfInterfaceDpdRetriesOptionsDef2:
        option_type: VariableOptionTypeDef1
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceDpdRetriesOptionsDef3:
        option_type: Optional[
            FeatureProfileSdRoutingSseCiscoDefaultOptionTypeDef
        ]
        value: Optional[int]


    class OneOfInterfaceIkeVersionOptionsDef1:
        option_type: GlobalOptionTypeDef4
        value: int


    class OneOfInterfaceIkeVersionOptionsDef2:
        option_type: VariableOptionTypeDef2
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIkeVersionOptionsDef3:
        option_type: Optional[
            V1FeatureProfileSdRoutingSseCiscoDefaultOptionTypeDef
        ]
        value: Optional[int]


    class OneOfInterfaceIkeRekeyIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef5
        value: int


    class OneOfInterfaceIkeRekeyIntervalOptionsDef2:
        option_type: VariableOptionTypeDef3
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIkeRekeyIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef1]
        value: Optional[int]


    class OneOfInterfaceIkeCiphersuiteOptionsDef1:
        option_type: GlobalOptionTypeDef6
        value: InterfaceIkeCiphersuiteDef


    class OneOfInterfaceIkeCiphersuiteOptionsDef2:
        option_type: VariableOptionTypeDef4
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIkeCiphersuiteOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef2]
        value: Optional[DefaultInterfaceIkeCiphersuiteDef]


    class OneOfInterfaceIkeGroupOptionsDef1:
        option_type: GlobalOptionTypeDef7
        value: InterfaceIkeGroupDef


    class OneOfInterfaceIkeGroupOptionsDef2:
        option_type: VariableOptionTypeDef5
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIkeGroupOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef3]
        value: Optional[InterfaceIkeGroupDef]


    class OneOfInterfaceIpsecRekeyIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef8
        value: int


    class OneOfInterfaceIpsecRekeyIntervalOptionsDef2:
        option_type: VariableOptionTypeDef6
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIpsecRekeyIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef4]
        value: Optional[int]


    class OneOfInterfaceIpsecReplayWindowOptionsDef1:
        option_type: GlobalOptionTypeDef9
        value: int


    class OneOfInterfaceIpsecReplayWindowOptionsDef2:
        option_type: VariableOptionTypeDef7
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIpsecReplayWindowOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef5]
        value: Optional[int]


    class OneOfInterfaceIpsecCiphersuiteOptionsDef1:
        option_type: GlobalOptionTypeDef10
        value: InterfaceIpsecCiphersuiteDef


    class OneOfInterfaceIpsecCiphersuiteOptionsDef2:
        option_type: VariableOptionTypeDef8
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIpsecCiphersuiteOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef6]
        value: Optional[InterfaceIpsecCiphersuiteDef]


    class OneOfInterfacePerfectForwardSecrecyOptionsDef1:
        option_type: GlobalOptionTypeDef11
        value: InterfacePerfectForwardSecrecyDef


    class OneOfInterfacePerfectForwardSecrecyOptionsDef2:
        option_type: VariableOptionTypeDef9
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfacePerfectForwardSecrecyOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef7]
        value: Optional[InterfacePerfectForwardSecrecyDef]


    class OneOfInterfaceTrackerOptionsDef1:
        option_type: GlobalOptionTypeDef12
        value: str


    class OneOfInterfaceTrackerOptionsDef2:
        option_type: DefaultOptionTypeDef8
        value: DefaultInterfaceTrackerDef  # pytype: disable=annotation-type-mismatch


    class OneOfOnBooleanDefaultTrueOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOnBooleanDefaultTrueOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultTrueOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class Interface:
        if_name: OneOfInterfaceIfNameOptionsDef
        dpd_interval: Optional[
            Union[
                OneOfInterfaceDpdIntervalOptionsDef1,
                OneOfInterfaceDpdIntervalOptionsDef2,
                OneOfInterfaceDpdIntervalOptionsDef3,
            ]
        ]
        dpd_retries: Optional[
            Union[
                OneOfInterfaceDpdRetriesOptionsDef1,
                OneOfInterfaceDpdRetriesOptionsDef2,
                OneOfInterfaceDpdRetriesOptionsDef3,
            ]
        ]
        ike_ciphersuite: Optional[
            Union[
                OneOfInterfaceIkeCiphersuiteOptionsDef1,
                OneOfInterfaceIkeCiphersuiteOptionsDef2,
                OneOfInterfaceIkeCiphersuiteOptionsDef3,
            ]
        ]
        ike_group: Optional[
            Union[
                OneOfInterfaceIkeGroupOptionsDef1,
                OneOfInterfaceIkeGroupOptionsDef2,
                OneOfInterfaceIkeGroupOptionsDef3,
            ]
        ]
        ike_rekey_interval: Optional[
            Union[
                OneOfInterfaceIkeRekeyIntervalOptionsDef1,
                OneOfInterfaceIkeRekeyIntervalOptionsDef2,
                OneOfInterfaceIkeRekeyIntervalOptionsDef3,
            ]
        ]
        ike_version: Optional[
            Union[
                OneOfInterfaceIkeVersionOptionsDef1,
                OneOfInterfaceIkeVersionOptionsDef2,
                OneOfInterfaceIkeVersionOptionsDef3,
            ]
        ]
        ipsec_ciphersuite: Optional[
            Union[
                OneOfInterfaceIpsecCiphersuiteOptionsDef1,
                OneOfInterfaceIpsecCiphersuiteOptionsDef2,
                OneOfInterfaceIpsecCiphersuiteOptionsDef3,
            ]
        ]
        ipsec_rekey_interval: Optional[
            Union[
                OneOfInterfaceIpsecRekeyIntervalOptionsDef1,
                OneOfInterfaceIpsecRekeyIntervalOptionsDef2,
                OneOfInterfaceIpsecRekeyIntervalOptionsDef3,
            ]
        ]
        ipsec_replay_window: Optional[
            Union[
                OneOfInterfaceIpsecReplayWindowOptionsDef1,
                OneOfInterfaceIpsecReplayWindowOptionsDef2,
                OneOfInterfaceIpsecReplayWindowOptionsDef3,
            ]
        ]
        mtu: Optional[
            Union[
                OneOfInterfaceMtuOptionsDef1, OneOfInterfaceMtuOptionsDef2
            ]
        ]
        perfect_forward_secrecy: Optional[
            Union[
                OneOfInterfacePerfectForwardSecrecyOptionsDef1,
                OneOfInterfacePerfectForwardSecrecyOptionsDef2,
                OneOfInterfacePerfectForwardSecrecyOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        tcp_mss_adjust: Optional[
            Union[
                OneOfInterfaceTcpMssAdjustOptionsDef1,
                OneOfInterfaceTcpMssAdjustOptionsDef2,
                OneOfInterfaceTcpMssAdjustOptionsDef3,
            ]
        ]
        track_enable: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        tracker: Optional[
            Union[
                OneOfInterfaceTrackerOptionsDef1,
                OneOfInterfaceTrackerOptionsDef2,
            ]
        ]
        tunnel_dc_preference: Optional[
            OneOfInterfaceTunnelDcPreferenceOptionsDef
        ]
        tunnel_route_via: Optional[
            Union[
                OneOfInterfaceTunnelRouteViaOptionsDef1,
                OneOfInterfaceTunnelRouteViaOptionsDef2,
                OneOfInterfaceTunnelRouteViaOptionsDef3,
            ]
        ]
        tunnel_source_interface: Optional[
            Union[
                OneOfInterfaceTunnelSourceInterfaceOptionsDef1,
                OneOfInterfaceTunnelSourceInterfaceOptionsDef2,
            ]
        ]


    class OneOfServiceInterfacePairActiveInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef13
        value: str


    class OneOfServiceInterfacePairActiveInterfaceWeightOptionsDef:
        option_type: GlobalOptionTypeDef14
        value: int


    class OneOfServiceInterfacePairBackupInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef15
        value: str


    class OneOfServiceInterfacePairBackupInterfaceWeightOptionsDef:
        option_type: GlobalOptionTypeDef16
        value: int


    class InterfacePair:
        active_interface: (
            OneOfServiceInterfacePairActiveInterfaceOptionsDef
        )
        backup_interface: (
            OneOfServiceInterfacePairBackupInterfaceOptionsDef
        )
        active_interface_weight: Optional[
            OneOfServiceInterfacePairActiveInterfaceWeightOptionsDef
        ]
        backup_interface_weight: Optional[
            OneOfServiceInterfacePairBackupInterfaceWeightOptionsDef
        ]


    class OneOfRegionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRegionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRegionOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[DefaultRegionDef]


    class OneOfIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfTrackerNameOptionsDef:
        option_type: GlobalOptionTypeDef17
        value: str


    class OneOfTrackerEndpointApiUrlOptionsDef1:
        option_type: GlobalOptionTypeDef18
        value: str


    class OneOfTrackerEndpointApiUrlOptionsDef2:
        option_type: VariableOptionTypeDef10
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef19
        value: int


    class OneOfTrackerThresholdOptionsDef2:
        option_type: VariableOptionTypeDef11
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerThresholdOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef9]
        value: Optional[int]


    class OneOfTrackerIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef20
        value: int


    class OneOfTrackerIntervalOptionsDef2:
        option_type: VariableOptionTypeDef12
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef10]
        value: Optional[int]


    class OneOfTrackerMultiplierOptionsDef1:
        option_type: GlobalOptionTypeDef21
        value: int


    class OneOfTrackerMultiplierOptionsDef2:
        option_type: VariableOptionTypeDef13
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerMultiplierOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef11]
        value: Optional[int]


    class OneOfTrackerTrackerTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: TrackerTrackerTypeDef


    class Tracker:
        endpoint_api_url: Union[
            OneOfTrackerEndpointApiUrlOptionsDef1,
            OneOfTrackerEndpointApiUrlOptionsDef2,
        ]
        name: OneOfTrackerNameOptionsDef
        tracker_type: OneOfTrackerTrackerTypeOptionsDef
        interval: Optional[
            Union[
                OneOfTrackerIntervalOptionsDef1,
                OneOfTrackerIntervalOptionsDef2,
                OneOfTrackerIntervalOptionsDef3,
            ]
        ]
        multiplier: Optional[
            Union[
                OneOfTrackerMultiplierOptionsDef1,
                OneOfTrackerMultiplierOptionsDef2,
                OneOfTrackerMultiplierOptionsDef3,
            ]
        ]
        threshold: Optional[
            Union[
                OneOfTrackerThresholdOptionsDef1,
                OneOfTrackerThresholdOptionsDef2,
                OneOfTrackerThresholdOptionsDef3,
            ]
        ]


    class CiscoData:
        # Interface name: IPsec when present
        interface: List[Interface]
        # Interface Pair for active and backup
        interface_pair: List[InterfacePair]
        region: Union[
            OneOfRegionOptionsDef1,
            OneOfRegionOptionsDef2,
            OneOfRegionOptionsDef3,
        ]
        sse_instance: OneOfSseInstanceOptionsDef
        tracker_src_ip: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        context_sharing_for_sgt: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        context_sharing_for_vpn: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        # Tracker configuration
        tracker: Optional[List[Tracker]]


    class Payload:
        """
        Cisco-SSE schema for POST request
        """

        data: CiscoData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


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
        # Cisco-SSE schema for POST request
        payload: Optional[Payload]


    class GetListSdRoutingSseCiscoSsePayload:
        data: Optional[List[Data]]


    class CreateCiscoSseFeatureForSsePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SseCiscoData:
        # Interface name: IPsec when present
        interface: List[Interface]
        # Interface Pair for active and backup
        interface_pair: List[InterfacePair]
        region: Union[
            OneOfRegionOptionsDef1,
            OneOfRegionOptionsDef2,
            OneOfRegionOptionsDef3,
        ]
        sse_instance: OneOfSseInstanceOptionsDef
        tracker_src_ip: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        context_sharing_for_sgt: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        context_sharing_for_vpn: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        # Tracker configuration
        tracker: Optional[List[Tracker]]


    class CreateCiscoSseFeatureForSsePostRequest:
        """
        Cisco-SSE schema for POST request
        """

        data: SseCiscoData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class CiscoOneOfSseInstanceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: CiscoSseInstanceDef


    class CiscoOneOfRegionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CiscoOneOfRegionOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[CiscoDefaultRegionDef]


    class CiscoOneOfTrackerTrackerTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: CiscoTrackerTrackerTypeDef


    class CiscoTracker:
        endpoint_api_url: Union[
            OneOfTrackerEndpointApiUrlOptionsDef1,
            OneOfTrackerEndpointApiUrlOptionsDef2,
        ]
        name: OneOfTrackerNameOptionsDef
        tracker_type: CiscoOneOfTrackerTrackerTypeOptionsDef
        interval: Optional[
            Union[
                OneOfTrackerIntervalOptionsDef1,
                OneOfTrackerIntervalOptionsDef2,
                OneOfTrackerIntervalOptionsDef3,
            ]
        ]
        multiplier: Optional[
            Union[
                OneOfTrackerMultiplierOptionsDef1,
                OneOfTrackerMultiplierOptionsDef2,
                OneOfTrackerMultiplierOptionsDef3,
            ]
        ]
        threshold: Optional[
            Union[
                OneOfTrackerThresholdOptionsDef1,
                OneOfTrackerThresholdOptionsDef2,
                OneOfTrackerThresholdOptionsDef3,
            ]
        ]


    class SdRoutingSseCiscoData:
        # Interface name: IPsec when present
        interface: List[Interface]
        # Interface Pair for active and backup
        interface_pair: List[InterfacePair]
        region: Union[
            CiscoOneOfRegionOptionsDef1,
            OneOfRegionOptionsDef2,
            CiscoOneOfRegionOptionsDef3,
        ]
        sse_instance: CiscoOneOfSseInstanceOptionsDef
        tracker_src_ip: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        context_sharing_for_sgt: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        context_sharing_for_vpn: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        # Tracker configuration
        tracker: Optional[List[CiscoTracker]]


    class CiscoPayload:
        """
        Cisco-SSE schema for PUT request
        """

        data: SdRoutingSseCiscoData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdRoutingSseCiscoSsePayload:
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
        # Cisco-SSE schema for PUT request
        payload: Optional[CiscoPayload]


    class EditCiscoSseFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SseCiscoOneOfSseInstanceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SseCiscoSseInstanceDef


    class SseCiscoOneOfRegionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SseCiscoOneOfRegionOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SseCiscoDefaultRegionDef]


    class SseCiscoOneOfTrackerTrackerTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SseCiscoTrackerTrackerTypeDef


    class SseCiscoTracker:
        endpoint_api_url: Union[
            OneOfTrackerEndpointApiUrlOptionsDef1,
            OneOfTrackerEndpointApiUrlOptionsDef2,
        ]
        name: OneOfTrackerNameOptionsDef
        tracker_type: SseCiscoOneOfTrackerTrackerTypeOptionsDef
        interval: Optional[
            Union[
                OneOfTrackerIntervalOptionsDef1,
                OneOfTrackerIntervalOptionsDef2,
                OneOfTrackerIntervalOptionsDef3,
            ]
        ]
        multiplier: Optional[
            Union[
                OneOfTrackerMultiplierOptionsDef1,
                OneOfTrackerMultiplierOptionsDef2,
                OneOfTrackerMultiplierOptionsDef3,
            ]
        ]
        threshold: Optional[
            Union[
                OneOfTrackerThresholdOptionsDef1,
                OneOfTrackerThresholdOptionsDef2,
                OneOfTrackerThresholdOptionsDef3,
            ]
        ]


    class FeatureProfileSdRoutingSseCiscoData:
        # Interface name: IPsec when present
        interface: List[Interface]
        # Interface Pair for active and backup
        interface_pair: List[InterfacePair]
        region: Union[
            SseCiscoOneOfRegionOptionsDef1,
            OneOfRegionOptionsDef2,
            SseCiscoOneOfRegionOptionsDef3,
        ]
        sse_instance: SseCiscoOneOfSseInstanceOptionsDef
        tracker_src_ip: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        context_sharing_for_sgt: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        context_sharing_for_vpn: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        # Tracker configuration
        tracker: Optional[List[SseCiscoTracker]]


    class EditCiscoSseFeaturePutRequest:
        """
        Cisco-SSE schema for PUT request
        """

        data: FeatureProfileSdRoutingSseCiscoData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


