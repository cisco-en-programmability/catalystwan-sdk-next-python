======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    SseInstanceDef = Literal["Cisco-Secure-Access"]

    DefaultOptionTypeDef = Literal["default"]

    VariableOptionTypeDef = Literal["variable"]

    InterfaceTunnelDcPreferenceDef = Literal["primary-dc", "secondary-dc"]

    InterfaceIkeCiphersuiteDef = Literal[
        "aes128-cbc-sha1",
        "aes128-cbc-sha2",
        "aes256-cbc-sha1",
        "aes256-cbc-sha2",
    ]

    DefaultInterfaceIkeCiphersuiteDef = Literal["aes256-cbc-sha1"]

    InterfaceIkeGroupDef = Literal[
        "14", "15", "16", "19", "2", "20", "21", "5"
    ]

    InterfaceIpsecCiphersuiteDef = Literal[
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-cbc-sha384",
        "aes256-cbc-sha512",
        "aes256-gcm",
    ]

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

    DefaultInterfaceTrackerDef = Literal["DefaultTracker"]

    DefaultRegionDef = Literal["auto"]

    TrackerTrackerTypeDef = Literal["cisco-sse"]

    CiscoSseInstanceDef = Literal["Cisco-Secure-Access"]

    CiscoInterfaceTunnelDcPreferenceDef = Literal[
        "primary-dc", "secondary-dc"
    ]

    CiscoInterfaceIkeCiphersuiteDef = Literal[
        "aes128-cbc-sha1",
        "aes128-cbc-sha2",
        "aes256-cbc-sha1",
        "aes256-cbc-sha2",
    ]

    CiscoDefaultInterfaceIkeCiphersuiteDef = Literal["aes256-cbc-sha1"]

    CiscoInterfaceIkeGroupDef = Literal[
        "14", "15", "16", "19", "2", "20", "21", "5"
    ]

    SseCiscoInterfaceIkeGroupDef = Literal[
        "14", "15", "16", "19", "2", "20", "21", "5"
    ]

    CiscoInterfaceIpsecCiphersuiteDef = Literal[
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-cbc-sha384",
        "aes256-cbc-sha512",
        "aes256-gcm",
    ]

    SseCiscoInterfaceIpsecCiphersuiteDef = Literal[
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-cbc-sha384",
        "aes256-cbc-sha512",
        "aes256-gcm",
    ]

    CiscoInterfacePerfectForwardSecrecyDef = Literal[
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

    SseCiscoInterfacePerfectForwardSecrecyDef = Literal[
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

    CiscoDefaultInterfaceTrackerDef = Literal["DefaultTracker"]

    CiscoDefaultRegionDef = Literal["auto"]

    CiscoTrackerTrackerTypeDef = Literal["cisco-sse"]

    SseCiscoSseInstanceDef = Literal["Cisco-Secure-Access"]

    SseCiscoInterfaceTunnelDcPreferenceDef = Literal[
        "primary-dc", "secondary-dc"
    ]

    SseCiscoInterfaceIkeCiphersuiteDef = Literal[
        "aes128-cbc-sha1",
        "aes128-cbc-sha2",
        "aes256-cbc-sha1",
        "aes256-cbc-sha2",
    ]

    SseCiscoDefaultInterfaceIkeCiphersuiteDef = Literal["aes256-cbc-sha1"]

    SdRoutingSseCiscoInterfaceIkeGroupDef = Literal[
        "14", "15", "16", "19", "2", "20", "21", "5"
    ]

    FeatureProfileSdRoutingSseCiscoInterfaceIkeGroupDef = Literal[
        "14", "15", "16", "19", "2", "20", "21", "5"
    ]

    SdRoutingSseCiscoInterfaceIpsecCiphersuiteDef = Literal[
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-cbc-sha384",
        "aes256-cbc-sha512",
        "aes256-gcm",
    ]

    FeatureProfileSdRoutingSseCiscoInterfaceIpsecCiphersuiteDef = Literal[
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-cbc-sha384",
        "aes256-cbc-sha512",
        "aes256-gcm",
    ]

    SdRoutingSseCiscoInterfacePerfectForwardSecrecyDef = Literal[
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

    FeatureProfileSdRoutingSseCiscoInterfacePerfectForwardSecrecyDef = (
        Literal[
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
    )

    SseCiscoDefaultInterfaceTrackerDef = Literal["DefaultTracker"]

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
        value: bool


    class OneOfInterfaceIfNameOptionsDef:
        option_type: GlobalOptionTypeDef
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
        value: bool


    class OneOfInterfaceTunnelSourceInterfaceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceTunnelSourceInterfaceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceTunnelRouteViaOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceTunnelRouteViaOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceTunnelDcPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: InterfaceTunnelDcPreferenceDef


    class OneOfInterfaceTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceTcpMssAdjustOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceTcpMssAdjustOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceMtuOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceDpdIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceDpdIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceDpdIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class OneOfInterfaceDpdRetriesOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceDpdRetriesOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceDpdRetriesOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class OneOfInterfaceIkeVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceIkeVersionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIkeVersionOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class OneOfInterfaceIkeRekeyIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceIkeRekeyIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIkeRekeyIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class OneOfInterfaceIkeCiphersuiteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceIkeCiphersuiteDef


    class OneOfInterfaceIkeCiphersuiteOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIkeCiphersuiteOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[DefaultInterfaceIkeCiphersuiteDef]


    class OneOfInterfaceIkeGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceIkeGroupDef


    class OneOfInterfaceIkeGroupOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIkeGroupOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[InterfaceIkeGroupDef]


    class OneOfInterfaceIpsecRekeyIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceIpsecRekeyIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIpsecRekeyIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class OneOfInterfaceIpsecReplayWindowOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceIpsecReplayWindowOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIpsecReplayWindowOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class OneOfInterfaceIpsecCiphersuiteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceIpsecCiphersuiteDef


    class OneOfInterfaceIpsecCiphersuiteOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIpsecCiphersuiteOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[InterfaceIpsecCiphersuiteDef]


    class OneOfInterfacePerfectForwardSecrecyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfacePerfectForwardSecrecyDef


    class OneOfInterfacePerfectForwardSecrecyOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfacePerfectForwardSecrecyOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[InterfacePerfectForwardSecrecyDef]


    class OneOfInterfaceTrackerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceTrackerOptionsDef2:
        option_type: DefaultOptionTypeDef
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
        value: bool


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
            ]
        ]
        tunnel_source_interface: Optional[
            Union[
                OneOfInterfaceTunnelSourceInterfaceOptionsDef1,
                OneOfInterfaceTunnelSourceInterfaceOptionsDef2,
            ]
        ]


    class OneOfServiceInterfacePairActiveInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfServiceInterfacePairActiveInterfaceWeightOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfServiceInterfacePairBackupInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfServiceInterfacePairBackupInterfaceWeightOptionsDef:
        option_type: GlobalOptionTypeDef
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
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTrackerEndpointApiUrlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTrackerEndpointApiUrlOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTrackerThresholdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerThresholdOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class OneOfTrackerIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTrackerIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class OneOfTrackerMultiplierOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTrackerMultiplierOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerMultiplierOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
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


    class CiscoOneOfInterfaceIfNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class CiscoOneOfInterfaceTunnelRouteViaOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CiscoOneOfInterfaceTunnelDcPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: CiscoInterfaceTunnelDcPreferenceDef


    class CiscoOneOfInterfaceTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CiscoOneOfInterfaceMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CiscoOneOfInterfaceDpdIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CiscoOneOfInterfaceDpdIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class CiscoOneOfInterfaceDpdRetriesOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CiscoOneOfInterfaceDpdRetriesOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class CiscoOneOfInterfaceIkeVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CiscoOneOfInterfaceIkeVersionOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class CiscoOneOfInterfaceIkeRekeyIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CiscoOneOfInterfaceIkeRekeyIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class CiscoOneOfInterfaceIkeCiphersuiteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: CiscoInterfaceIkeCiphersuiteDef


    class CiscoOneOfInterfaceIkeCiphersuiteOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[CiscoDefaultInterfaceIkeCiphersuiteDef]


    class CiscoOneOfInterfaceIkeGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: CiscoInterfaceIkeGroupDef


    class CiscoOneOfInterfaceIkeGroupOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SseCiscoInterfaceIkeGroupDef]


    class CiscoOneOfInterfaceIpsecRekeyIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CiscoOneOfInterfaceIpsecRekeyIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class CiscoOneOfInterfaceIpsecReplayWindowOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CiscoOneOfInterfaceIpsecReplayWindowOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class CiscoOneOfInterfaceIpsecCiphersuiteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: CiscoInterfaceIpsecCiphersuiteDef


    class CiscoOneOfInterfaceIpsecCiphersuiteOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SseCiscoInterfaceIpsecCiphersuiteDef]


    class CiscoOneOfInterfacePerfectForwardSecrecyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: CiscoInterfacePerfectForwardSecrecyDef


    class CiscoOneOfInterfacePerfectForwardSecrecyOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SseCiscoInterfacePerfectForwardSecrecyDef]


    class CiscoOneOfInterfaceTrackerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CiscoOneOfInterfaceTrackerOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: CiscoDefaultInterfaceTrackerDef  # pytype: disable=annotation-type-mismatch


    class CiscoInterface:
        if_name: CiscoOneOfInterfaceIfNameOptionsDef
        dpd_interval: Optional[
            Union[
                CiscoOneOfInterfaceDpdIntervalOptionsDef1,
                OneOfInterfaceDpdIntervalOptionsDef2,
                CiscoOneOfInterfaceDpdIntervalOptionsDef3,
            ]
        ]
        dpd_retries: Optional[
            Union[
                CiscoOneOfInterfaceDpdRetriesOptionsDef1,
                OneOfInterfaceDpdRetriesOptionsDef2,
                CiscoOneOfInterfaceDpdRetriesOptionsDef3,
            ]
        ]
        ike_ciphersuite: Optional[
            Union[
                CiscoOneOfInterfaceIkeCiphersuiteOptionsDef1,
                OneOfInterfaceIkeCiphersuiteOptionsDef2,
                CiscoOneOfInterfaceIkeCiphersuiteOptionsDef3,
            ]
        ]
        ike_group: Optional[
            Union[
                CiscoOneOfInterfaceIkeGroupOptionsDef1,
                OneOfInterfaceIkeGroupOptionsDef2,
                CiscoOneOfInterfaceIkeGroupOptionsDef3,
            ]
        ]
        ike_rekey_interval: Optional[
            Union[
                CiscoOneOfInterfaceIkeRekeyIntervalOptionsDef1,
                OneOfInterfaceIkeRekeyIntervalOptionsDef2,
                CiscoOneOfInterfaceIkeRekeyIntervalOptionsDef3,
            ]
        ]
        ike_version: Optional[
            Union[
                CiscoOneOfInterfaceIkeVersionOptionsDef1,
                OneOfInterfaceIkeVersionOptionsDef2,
                CiscoOneOfInterfaceIkeVersionOptionsDef3,
            ]
        ]
        ipsec_ciphersuite: Optional[
            Union[
                CiscoOneOfInterfaceIpsecCiphersuiteOptionsDef1,
                OneOfInterfaceIpsecCiphersuiteOptionsDef2,
                CiscoOneOfInterfaceIpsecCiphersuiteOptionsDef3,
            ]
        ]
        ipsec_rekey_interval: Optional[
            Union[
                CiscoOneOfInterfaceIpsecRekeyIntervalOptionsDef1,
                OneOfInterfaceIpsecRekeyIntervalOptionsDef2,
                CiscoOneOfInterfaceIpsecRekeyIntervalOptionsDef3,
            ]
        ]
        ipsec_replay_window: Optional[
            Union[
                CiscoOneOfInterfaceIpsecReplayWindowOptionsDef1,
                OneOfInterfaceIpsecReplayWindowOptionsDef2,
                CiscoOneOfInterfaceIpsecReplayWindowOptionsDef3,
            ]
        ]
        mtu: Optional[
            Union[
                CiscoOneOfInterfaceMtuOptionsDef1,
                OneOfInterfaceMtuOptionsDef2,
            ]
        ]
        perfect_forward_secrecy: Optional[
            Union[
                CiscoOneOfInterfacePerfectForwardSecrecyOptionsDef1,
                OneOfInterfacePerfectForwardSecrecyOptionsDef2,
                CiscoOneOfInterfacePerfectForwardSecrecyOptionsDef3,
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
                CiscoOneOfInterfaceTcpMssAdjustOptionsDef1,
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
                CiscoOneOfInterfaceTrackerOptionsDef1,
                CiscoOneOfInterfaceTrackerOptionsDef2,
            ]
        ]
        tunnel_dc_preference: Optional[
            CiscoOneOfInterfaceTunnelDcPreferenceOptionsDef
        ]
        tunnel_route_via: Optional[
            Union[
                CiscoOneOfInterfaceTunnelRouteViaOptionsDef1,
                OneOfInterfaceTunnelRouteViaOptionsDef2,
            ]
        ]
        tunnel_source_interface: Optional[
            Union[
                OneOfInterfaceTunnelSourceInterfaceOptionsDef1,
                OneOfInterfaceTunnelSourceInterfaceOptionsDef2,
            ]
        ]


    class CiscoOneOfServiceInterfacePairActiveInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class CiscoOneOfServiceInterfacePairActiveInterfaceWeightOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class CiscoOneOfServiceInterfacePairBackupInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class CiscoOneOfServiceInterfacePairBackupInterfaceWeightOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class CiscoInterfacePair:
        active_interface: (
            CiscoOneOfServiceInterfacePairActiveInterfaceOptionsDef
        )
        backup_interface: (
            CiscoOneOfServiceInterfacePairBackupInterfaceOptionsDef
        )
        active_interface_weight: Optional[
            CiscoOneOfServiceInterfacePairActiveInterfaceWeightOptionsDef
        ]
        backup_interface_weight: Optional[
            CiscoOneOfServiceInterfacePairBackupInterfaceWeightOptionsDef
        ]


    class CiscoOneOfRegionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CiscoOneOfRegionOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[CiscoDefaultRegionDef]


    class CiscoOneOfTrackerNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class CiscoOneOfTrackerEndpointApiUrlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CiscoOneOfTrackerThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CiscoOneOfTrackerThresholdOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class CiscoOneOfTrackerIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CiscoOneOfTrackerIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class CiscoOneOfTrackerMultiplierOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CiscoOneOfTrackerMultiplierOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class CiscoOneOfTrackerTrackerTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: CiscoTrackerTrackerTypeDef


    class CiscoTracker:
        endpoint_api_url: Union[
            CiscoOneOfTrackerEndpointApiUrlOptionsDef1,
            OneOfTrackerEndpointApiUrlOptionsDef2,
        ]
        name: CiscoOneOfTrackerNameOptionsDef
        tracker_type: CiscoOneOfTrackerTrackerTypeOptionsDef
        interval: Optional[
            Union[
                CiscoOneOfTrackerIntervalOptionsDef1,
                OneOfTrackerIntervalOptionsDef2,
                CiscoOneOfTrackerIntervalOptionsDef3,
            ]
        ]
        multiplier: Optional[
            Union[
                CiscoOneOfTrackerMultiplierOptionsDef1,
                OneOfTrackerMultiplierOptionsDef2,
                CiscoOneOfTrackerMultiplierOptionsDef3,
            ]
        ]
        threshold: Optional[
            Union[
                CiscoOneOfTrackerThresholdOptionsDef1,
                OneOfTrackerThresholdOptionsDef2,
                CiscoOneOfTrackerThresholdOptionsDef3,
            ]
        ]


    class SdRoutingSseCiscoData:
        # Interface name: IPsec when present
        interface: List[CiscoInterface]
        # Interface Pair for active and backup
        interface_pair: List[CiscoInterfacePair]
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


    class SseCiscoOneOfInterfaceIfNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SseCiscoOneOfInterfaceTunnelRouteViaOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SseCiscoOneOfInterfaceTunnelDcPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SseCiscoInterfaceTunnelDcPreferenceDef


    class SseCiscoOneOfInterfaceTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SseCiscoOneOfInterfaceMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SseCiscoOneOfInterfaceDpdIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SseCiscoOneOfInterfaceDpdIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SseCiscoOneOfInterfaceDpdRetriesOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SseCiscoOneOfInterfaceDpdRetriesOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SseCiscoOneOfInterfaceIkeVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SseCiscoOneOfInterfaceIkeVersionOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SseCiscoOneOfInterfaceIkeRekeyIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SseCiscoOneOfInterfaceIkeRekeyIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SseCiscoOneOfInterfaceIkeCiphersuiteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SseCiscoInterfaceIkeCiphersuiteDef


    class SseCiscoOneOfInterfaceIkeCiphersuiteOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SseCiscoDefaultInterfaceIkeCiphersuiteDef]


    class SseCiscoOneOfInterfaceIkeGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SdRoutingSseCiscoInterfaceIkeGroupDef


    class SseCiscoOneOfInterfaceIkeGroupOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[
            FeatureProfileSdRoutingSseCiscoInterfaceIkeGroupDef
        ]


    class SseCiscoOneOfInterfaceIpsecRekeyIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SseCiscoOneOfInterfaceIpsecRekeyIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SseCiscoOneOfInterfaceIpsecReplayWindowOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SseCiscoOneOfInterfaceIpsecReplayWindowOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SseCiscoOneOfInterfaceIpsecCiphersuiteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SdRoutingSseCiscoInterfaceIpsecCiphersuiteDef


    class SseCiscoOneOfInterfaceIpsecCiphersuiteOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[
            FeatureProfileSdRoutingSseCiscoInterfaceIpsecCiphersuiteDef
        ]


    class SseCiscoOneOfInterfacePerfectForwardSecrecyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SdRoutingSseCiscoInterfacePerfectForwardSecrecyDef


    class SseCiscoOneOfInterfacePerfectForwardSecrecyOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[
            FeatureProfileSdRoutingSseCiscoInterfacePerfectForwardSecrecyDef
        ]


    class SseCiscoOneOfInterfaceTrackerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SseCiscoOneOfInterfaceTrackerOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: SseCiscoDefaultInterfaceTrackerDef  # pytype: disable=annotation-type-mismatch


    class SseCiscoInterface:
        if_name: SseCiscoOneOfInterfaceIfNameOptionsDef
        dpd_interval: Optional[
            Union[
                SseCiscoOneOfInterfaceDpdIntervalOptionsDef1,
                OneOfInterfaceDpdIntervalOptionsDef2,
                SseCiscoOneOfInterfaceDpdIntervalOptionsDef3,
            ]
        ]
        dpd_retries: Optional[
            Union[
                SseCiscoOneOfInterfaceDpdRetriesOptionsDef1,
                OneOfInterfaceDpdRetriesOptionsDef2,
                SseCiscoOneOfInterfaceDpdRetriesOptionsDef3,
            ]
        ]
        ike_ciphersuite: Optional[
            Union[
                SseCiscoOneOfInterfaceIkeCiphersuiteOptionsDef1,
                OneOfInterfaceIkeCiphersuiteOptionsDef2,
                SseCiscoOneOfInterfaceIkeCiphersuiteOptionsDef3,
            ]
        ]
        ike_group: Optional[
            Union[
                SseCiscoOneOfInterfaceIkeGroupOptionsDef1,
                OneOfInterfaceIkeGroupOptionsDef2,
                SseCiscoOneOfInterfaceIkeGroupOptionsDef3,
            ]
        ]
        ike_rekey_interval: Optional[
            Union[
                SseCiscoOneOfInterfaceIkeRekeyIntervalOptionsDef1,
                OneOfInterfaceIkeRekeyIntervalOptionsDef2,
                SseCiscoOneOfInterfaceIkeRekeyIntervalOptionsDef3,
            ]
        ]
        ike_version: Optional[
            Union[
                SseCiscoOneOfInterfaceIkeVersionOptionsDef1,
                OneOfInterfaceIkeVersionOptionsDef2,
                SseCiscoOneOfInterfaceIkeVersionOptionsDef3,
            ]
        ]
        ipsec_ciphersuite: Optional[
            Union[
                SseCiscoOneOfInterfaceIpsecCiphersuiteOptionsDef1,
                OneOfInterfaceIpsecCiphersuiteOptionsDef2,
                SseCiscoOneOfInterfaceIpsecCiphersuiteOptionsDef3,
            ]
        ]
        ipsec_rekey_interval: Optional[
            Union[
                SseCiscoOneOfInterfaceIpsecRekeyIntervalOptionsDef1,
                OneOfInterfaceIpsecRekeyIntervalOptionsDef2,
                SseCiscoOneOfInterfaceIpsecRekeyIntervalOptionsDef3,
            ]
        ]
        ipsec_replay_window: Optional[
            Union[
                SseCiscoOneOfInterfaceIpsecReplayWindowOptionsDef1,
                OneOfInterfaceIpsecReplayWindowOptionsDef2,
                SseCiscoOneOfInterfaceIpsecReplayWindowOptionsDef3,
            ]
        ]
        mtu: Optional[
            Union[
                SseCiscoOneOfInterfaceMtuOptionsDef1,
                OneOfInterfaceMtuOptionsDef2,
            ]
        ]
        perfect_forward_secrecy: Optional[
            Union[
                SseCiscoOneOfInterfacePerfectForwardSecrecyOptionsDef1,
                OneOfInterfacePerfectForwardSecrecyOptionsDef2,
                SseCiscoOneOfInterfacePerfectForwardSecrecyOptionsDef3,
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
                SseCiscoOneOfInterfaceTcpMssAdjustOptionsDef1,
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
                SseCiscoOneOfInterfaceTrackerOptionsDef1,
                SseCiscoOneOfInterfaceTrackerOptionsDef2,
            ]
        ]
        tunnel_dc_preference: Optional[
            SseCiscoOneOfInterfaceTunnelDcPreferenceOptionsDef
        ]
        tunnel_route_via: Optional[
            Union[
                SseCiscoOneOfInterfaceTunnelRouteViaOptionsDef1,
                OneOfInterfaceTunnelRouteViaOptionsDef2,
            ]
        ]
        tunnel_source_interface: Optional[
            Union[
                OneOfInterfaceTunnelSourceInterfaceOptionsDef1,
                OneOfInterfaceTunnelSourceInterfaceOptionsDef2,
            ]
        ]


    class SseCiscoOneOfServiceInterfacePairActiveInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SseCiscoOneOfServiceInterfacePairActiveInterfaceWeightOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SseCiscoOneOfServiceInterfacePairBackupInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SseCiscoOneOfServiceInterfacePairBackupInterfaceWeightOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SseCiscoInterfacePair:
        active_interface: (
            SseCiscoOneOfServiceInterfacePairActiveInterfaceOptionsDef
        )
        backup_interface: (
            SseCiscoOneOfServiceInterfacePairBackupInterfaceOptionsDef
        )
        active_interface_weight: Optional[
            SseCiscoOneOfServiceInterfacePairActiveInterfaceWeightOptionsDef
        ]
        backup_interface_weight: Optional[
            SseCiscoOneOfServiceInterfacePairBackupInterfaceWeightOptionsDef
        ]


    class SseCiscoOneOfRegionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SseCiscoOneOfRegionOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SseCiscoDefaultRegionDef]


    class SseCiscoOneOfTrackerNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SseCiscoOneOfTrackerEndpointApiUrlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SseCiscoOneOfTrackerThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SseCiscoOneOfTrackerThresholdOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SseCiscoOneOfTrackerIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SseCiscoOneOfTrackerIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SseCiscoOneOfTrackerMultiplierOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SseCiscoOneOfTrackerMultiplierOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SseCiscoOneOfTrackerTrackerTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SseCiscoTrackerTrackerTypeDef


    class SseCiscoTracker:
        endpoint_api_url: Union[
            SseCiscoOneOfTrackerEndpointApiUrlOptionsDef1,
            OneOfTrackerEndpointApiUrlOptionsDef2,
        ]
        name: SseCiscoOneOfTrackerNameOptionsDef
        tracker_type: SseCiscoOneOfTrackerTrackerTypeOptionsDef
        interval: Optional[
            Union[
                SseCiscoOneOfTrackerIntervalOptionsDef1,
                OneOfTrackerIntervalOptionsDef2,
                SseCiscoOneOfTrackerIntervalOptionsDef3,
            ]
        ]
        multiplier: Optional[
            Union[
                SseCiscoOneOfTrackerMultiplierOptionsDef1,
                OneOfTrackerMultiplierOptionsDef2,
                SseCiscoOneOfTrackerMultiplierOptionsDef3,
            ]
        ]
        threshold: Optional[
            Union[
                SseCiscoOneOfTrackerThresholdOptionsDef1,
                OneOfTrackerThresholdOptionsDef2,
                SseCiscoOneOfTrackerThresholdOptionsDef3,
            ]
        ]


    class FeatureProfileSdRoutingSseCiscoData:
        # Interface name: IPsec when present
        interface: List[SseCiscoInterface]
        # Interface Pair for active and backup
        interface_pair: List[SseCiscoInterfacePair]
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


