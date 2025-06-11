======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    SigProviderDef = Literal["Generic", "Umbrella", "Zscaler"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanFalseDef = Literal[False]

    VariableOptionTypeDef = Literal["variable"]

    InterfaceApplicationDef = Literal["sig"]

    InterfaceTunnelSetDef = Literal[
        "secure-internet-gateway-other",
        "secure-internet-gateway-umbrella",
        "secure-internet-gateway-zscaler",
    ]

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

    InterfaceIpsecReplayWindowDef = Literal[64, 128, 256, 512, 1024]

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

    BooleanTrueDef = Literal[True]

    ServiceDisplayTimeUnitDef = Literal["DAY", "HOUR", "MINUTE"]

    DefaultServiceDisplayTimeUnitDef = Literal["MINUTE"]

    ServiceRefreshTimeUnitDef = Literal["DAY", "HOUR", "MINUTE"]

    DefaultServiceRefreshTimeUnitDef = Literal["MINUTE"]

    TrackerTrackerTypeDef = Literal["SIG"]

    SigSigProviderDef = Literal["Generic", "Umbrella", "Zscaler"]

    SigInterfaceApplicationDef = Literal["sig"]

    SigInterfaceTunnelSetDef = Literal[
        "secure-internet-gateway-other",
        "secure-internet-gateway-umbrella",
        "secure-internet-gateway-zscaler",
    ]

    SigInterfaceTunnelDcPreferenceDef = Literal[
        "primary-dc", "secondary-dc"
    ]

    SigInterfaceIkeCiphersuiteDef = Literal[
        "aes128-cbc-sha1",
        "aes128-cbc-sha2",
        "aes256-cbc-sha1",
        "aes256-cbc-sha2",
    ]

    SigDefaultInterfaceIkeCiphersuiteDef = Literal["aes256-cbc-sha1"]

    SigInterfaceIkeGroupDef = Literal[
        "14", "15", "16", "19", "2", "20", "21", "5"
    ]

    SigSecuritySigInterfaceIkeGroupDef = Literal[
        "14", "15", "16", "19", "2", "20", "21", "5"
    ]

    SigInterfaceIpsecReplayWindowDef = Literal[64, 128, 256, 512, 1024]

    SigInterfaceIpsecCiphersuiteDef = Literal[
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-cbc-sha384",
        "aes256-cbc-sha512",
        "aes256-gcm",
    ]

    SigSecuritySigInterfaceIpsecCiphersuiteDef = Literal[
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-cbc-sha384",
        "aes256-cbc-sha512",
        "aes256-gcm",
    ]

    SigInterfacePerfectForwardSecrecyDef = Literal[
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

    SigSecuritySigInterfacePerfectForwardSecrecyDef = Literal[
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

    SigServiceDisplayTimeUnitDef = Literal["DAY", "HOUR", "MINUTE"]

    SigDefaultServiceDisplayTimeUnitDef = Literal["MINUTE"]

    SigServiceRefreshTimeUnitDef = Literal["DAY", "HOUR", "MINUTE"]

    SigDefaultServiceRefreshTimeUnitDef = Literal["MINUTE"]

    SigTrackerTrackerTypeDef = Literal["SIG"]

    SigSecuritySigSigProviderDef = Literal[
        "Generic", "Umbrella", "Zscaler"
    ]

    SigSecuritySigInterfaceApplicationDef = Literal["sig"]

    SigSecuritySigInterfaceTunnelSetDef = Literal[
        "secure-internet-gateway-other",
        "secure-internet-gateway-umbrella",
        "secure-internet-gateway-zscaler",
    ]

    SigSecuritySigInterfaceTunnelDcPreferenceDef = Literal[
        "primary-dc", "secondary-dc"
    ]

    SigSecuritySigInterfaceIkeCiphersuiteDef = Literal[
        "aes128-cbc-sha1",
        "aes128-cbc-sha2",
        "aes256-cbc-sha1",
        "aes256-cbc-sha2",
    ]

    SigSecuritySigDefaultInterfaceIkeCiphersuiteDef = Literal[
        "aes256-cbc-sha1"
    ]

    SdwanSigSecuritySigInterfaceIkeGroupDef = Literal[
        "14", "15", "16", "19", "2", "20", "21", "5"
    ]

    FeatureProfileSdwanSigSecuritySigInterfaceIkeGroupDef = Literal[
        "14", "15", "16", "19", "2", "20", "21", "5"
    ]

    SigSecuritySigInterfaceIpsecReplayWindowDef = Literal[
        64, 128, 256, 512, 1024
    ]

    SdwanSigSecuritySigInterfaceIpsecCiphersuiteDef = Literal[
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-cbc-sha384",
        "aes256-cbc-sha512",
        "aes256-gcm",
    ]

    FeatureProfileSdwanSigSecuritySigInterfaceIpsecCiphersuiteDef = (
        Literal[
            "aes256-cbc-sha1",
            "aes256-cbc-sha256",
            "aes256-cbc-sha384",
            "aes256-cbc-sha512",
            "aes256-gcm",
        ]
    )

    SdwanSigSecuritySigInterfacePerfectForwardSecrecyDef = Literal[
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

    FeatureProfileSdwanSigSecuritySigInterfacePerfectForwardSecrecyDef = (
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

    SigSecuritySigServiceDisplayTimeUnitDef = Literal[
        "DAY", "HOUR", "MINUTE"
    ]

    SigSecuritySigDefaultServiceDisplayTimeUnitDef = Literal["MINUTE"]

    SigSecuritySigServiceRefreshTimeUnitDef = Literal[
        "DAY", "HOUR", "MINUTE"
    ]

    SigSecuritySigDefaultServiceRefreshTimeUnitDef = Literal["MINUTE"]

    SigSecuritySigTrackerTrackerTypeDef = Literal["SIG"]


    class OneOfSigProviderOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SigProviderDef


    class OneOfSrcVpnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfSrcVpnOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanFalseDef]


    class InterfaceMetadataSharing:
        src_vpn: Optional[
            Union[OneOfSrcVpnOptionsDef1, OneOfSrcVpnOptionsDef2]
        ]


    class OneOfInterfaceIfNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceAutoOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfInterfaceShutdownOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfInterfaceShutdownOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanFalseDef]


    class OneOfInterfaceDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceDescriptionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceDescriptionOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceUnnumberedOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfInterfaceAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceAddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceAddressOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceTunnelSourceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceTunnelSourceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


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


    class OneOfInterfaceTunnelDestinationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceTunnelDestinationOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceApplicationOptionsDef:
        option_type: GlobalOptionTypeDef
        value: InterfaceApplicationDef


    class OneOfInterfaceTunnelSetOptionsDef:
        option_type: GlobalOptionTypeDef
        value: InterfaceTunnelSetDef


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


    class OneOfInterfacePreSharedSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfacePreSharedSecretOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfacePreSharedSecretOptionsDef3:
        option_type: DefaultOptionTypeDef


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


    class OneOfInterfacePreSharedKeyDynamicOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfInterfaceIkeLocalIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceIkeLocalIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIkeLocalIdOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfInterfaceIkeRemoteIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceIkeRemoteIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceIkeRemoteIdOptionsDef3:
        option_type: DefaultOptionTypeDef


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
        value: InterfaceIpsecReplayWindowDef


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


    class OneOfInterfaceTrackEnableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfInterfaceTrackEnableOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanTrueDef]


    class OneOfInterfaceTunnelPublicIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceTunnelPublicIpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceTunnelPublicIpOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class Interface:
        if_name: OneOfInterfaceIfNameOptionsDef
        tunnel_source_interface: Union[
            OneOfInterfaceTunnelSourceInterfaceOptionsDef1,
            OneOfInterfaceTunnelSourceInterfaceOptionsDef2,
        ]
        address: Optional[
            Union[
                OneOfInterfaceAddressOptionsDef1,
                OneOfInterfaceAddressOptionsDef2,
                OneOfInterfaceAddressOptionsDef3,
            ]
        ]
        application: Optional[OneOfInterfaceApplicationOptionsDef]
        auto: Optional[OneOfInterfaceAutoOptionsDef]
        description: Optional[
            Union[
                OneOfInterfaceDescriptionOptionsDef1,
                OneOfInterfaceDescriptionOptionsDef2,
                OneOfInterfaceDescriptionOptionsDef3,
            ]
        ]
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
        ike_local_id: Optional[
            Union[
                OneOfInterfaceIkeLocalIdOptionsDef1,
                OneOfInterfaceIkeLocalIdOptionsDef2,
                OneOfInterfaceIkeLocalIdOptionsDef3,
            ]
        ]
        ike_rekey_interval: Optional[
            Union[
                OneOfInterfaceIkeRekeyIntervalOptionsDef1,
                OneOfInterfaceIkeRekeyIntervalOptionsDef2,
                OneOfInterfaceIkeRekeyIntervalOptionsDef3,
            ]
        ]
        ike_remote_id: Optional[
            Union[
                OneOfInterfaceIkeRemoteIdOptionsDef1,
                OneOfInterfaceIkeRemoteIdOptionsDef2,
                OneOfInterfaceIkeRemoteIdOptionsDef3,
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
        pre_shared_key_dynamic: Optional[
            OneOfInterfacePreSharedKeyDynamicOptionsDef
        ]
        pre_shared_secret: Optional[
            Union[
                OneOfInterfacePreSharedSecretOptionsDef1,
                OneOfInterfacePreSharedSecretOptionsDef2,
                OneOfInterfacePreSharedSecretOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfInterfaceShutdownOptionsDef1,
                OneOfInterfaceShutdownOptionsDef2,
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
                OneOfInterfaceTrackEnableOptionsDef1,
                OneOfInterfaceTrackEnableOptionsDef2,
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
        tunnel_destination: Optional[
            Union[
                OneOfInterfaceTunnelDestinationOptionsDef1,
                OneOfInterfaceTunnelDestinationOptionsDef2,
            ]
        ]
        tunnel_public_ip: Optional[
            Union[
                OneOfInterfaceTunnelPublicIpOptionsDef1,
                OneOfInterfaceTunnelPublicIpOptionsDef2,
                OneOfInterfaceTunnelPublicIpOptionsDef3,
            ]
        ]
        tunnel_route_via: Optional[
            Union[
                OneOfInterfaceTunnelRouteViaOptionsDef1,
                OneOfInterfaceTunnelRouteViaOptionsDef2,
            ]
        ]
        tunnel_set: Optional[OneOfInterfaceTunnelSetOptionsDef]
        tunnel_source: Optional[
            Union[
                OneOfInterfaceTunnelSourceOptionsDef1,
                OneOfInterfaceTunnelSourceOptionsDef2,
            ]
        ]
        unnumbered: Optional[OneOfInterfaceUnnumberedOptionsDef]


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


    class OneOfServiceAuthRequiredOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfServiceAuthRequiredOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanFalseDef]


    class OneOfServiceXffForwardEnabledOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfServiceXffForwardEnabledOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanFalseDef]


    class OneOfServiceOfwEnabledOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfServiceOfwEnabledOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanFalseDef]


    class OneOfServiceIpsControlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfServiceIpsControlOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanFalseDef]


    class OneOfServiceCautionEnabledOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfServiceCautionEnabledOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanFalseDef]


    class OneOfServicePrimaryDataCenterOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfServicePrimaryDataCenterOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class OneOfServicePrimaryDataCenterOptionsDef3:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfServiceSecondaryDataCenterOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfServiceSecondaryDataCenterOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class OneOfServiceSecondaryDataCenterOptionsDef3:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfServiceIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfServiceIpOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanFalseDef]


    class OneOfServiceIdleTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfServiceIdleTimeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfServiceDisplayTimeUnitOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ServiceDisplayTimeUnitDef


    class OneOfServiceDisplayTimeUnitOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[DefaultServiceDisplayTimeUnitDef]


    class OneOfServiceIpEnforcedForKnownBrowsersOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfServiceIpEnforcedForKnownBrowsersOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanFalseDef]


    class OneOfServiceRefreshTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfServiceRefreshTimeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfServiceRefreshTimeUnitOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ServiceRefreshTimeUnitDef


    class OneOfServiceRefreshTimeUnitOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[DefaultServiceRefreshTimeUnitDef]


    class OneOfServiceEnabledOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfServiceEnabledOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanFalseDef]


    class OneOfServiceBlockInternetUntilAcceptedOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfServiceBlockInternetUntilAcceptedOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanFalseDef]


    class OneOfServiceForceSslInspectionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfServiceForceSslInspectionOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanFalseDef]


    class OneOfServiceTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfServiceTimeoutOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class OneOfServiceLocationNameOptionsDef1:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class OneOfServiceLocationNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfServiceDataCenterPrimaryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfServiceDataCenterPrimaryOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class OneOfServiceDataCenterPrimaryOptionsDef3:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfServiceDataCenterSecondaryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfServiceDataCenterSecondaryOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class OneOfServiceDataCenterSecondaryOptionsDef3:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Service:
        """
        Configure services
        """

        auth_required: Optional[
            Union[
                OneOfServiceAuthRequiredOptionsDef1,
                OneOfServiceAuthRequiredOptionsDef2,
            ]
        ]
        block_internet_until_accepted: Optional[
            Union[
                OneOfServiceBlockInternetUntilAcceptedOptionsDef1,
                OneOfServiceBlockInternetUntilAcceptedOptionsDef2,
            ]
        ]
        caution_enabled: Optional[
            Union[
                OneOfServiceCautionEnabledOptionsDef1,
                OneOfServiceCautionEnabledOptionsDef2,
            ]
        ]
        data_center_primary: Optional[
            Union[
                OneOfServiceDataCenterPrimaryOptionsDef1,
                OneOfServiceDataCenterPrimaryOptionsDef2,
                OneOfServiceDataCenterPrimaryOptionsDef3,
            ]
        ]
        data_center_secondary: Optional[
            Union[
                OneOfServiceDataCenterSecondaryOptionsDef1,
                OneOfServiceDataCenterSecondaryOptionsDef2,
                OneOfServiceDataCenterSecondaryOptionsDef3,
            ]
        ]
        display_time_unit: Optional[
            Union[
                OneOfServiceDisplayTimeUnitOptionsDef1,
                OneOfServiceDisplayTimeUnitOptionsDef2,
            ]
        ]
        enabled: Optional[
            Union[
                OneOfServiceEnabledOptionsDef1,
                OneOfServiceEnabledOptionsDef2,
            ]
        ]
        force_ssl_inspection: Optional[
            Union[
                OneOfServiceForceSslInspectionOptionsDef1,
                OneOfServiceForceSslInspectionOptionsDef2,
            ]
        ]
        idle_time: Optional[
            Union[
                OneOfServiceIdleTimeOptionsDef1,
                OneOfServiceIdleTimeOptionsDef2,
            ]
        ]
        # Interface Pair for active and backup
        interface_pair: Optional[List[InterfacePair]]
        ip: Optional[
            Union[OneOfServiceIpOptionsDef1, OneOfServiceIpOptionsDef2]
        ]
        ip_enforced_for_known_browsers: Optional[
            Union[
                OneOfServiceIpEnforcedForKnownBrowsersOptionsDef1,
                OneOfServiceIpEnforcedForKnownBrowsersOptionsDef2,
            ]
        ]
        ips_control: Optional[
            Union[
                OneOfServiceIpsControlOptionsDef1,
                OneOfServiceIpsControlOptionsDef2,
            ]
        ]
        location_name: Optional[
            Union[
                OneOfServiceLocationNameOptionsDef1,
                OneOfServiceLocationNameOptionsDef2,
            ]
        ]
        ofw_enabled: Optional[
            Union[
                OneOfServiceOfwEnabledOptionsDef1,
                OneOfServiceOfwEnabledOptionsDef2,
            ]
        ]
        primary_data_center: Optional[
            Union[
                OneOfServicePrimaryDataCenterOptionsDef1,
                OneOfServicePrimaryDataCenterOptionsDef2,
                OneOfServicePrimaryDataCenterOptionsDef3,
            ]
        ]
        refresh_time: Optional[
            Union[
                OneOfServiceRefreshTimeOptionsDef1,
                OneOfServiceRefreshTimeOptionsDef2,
            ]
        ]
        refresh_time_unit: Optional[
            Union[
                OneOfServiceRefreshTimeUnitOptionsDef1,
                OneOfServiceRefreshTimeUnitOptionsDef2,
            ]
        ]
        secondary_data_center: Optional[
            Union[
                OneOfServiceSecondaryDataCenterOptionsDef1,
                OneOfServiceSecondaryDataCenterOptionsDef2,
                OneOfServiceSecondaryDataCenterOptionsDef3,
            ]
        ]
        timeout: Optional[
            Union[
                OneOfServiceTimeoutOptionsDef1,
                OneOfServiceTimeoutOptionsDef2,
            ]
        ]
        xff_forward_enabled: Optional[
            Union[
                OneOfServiceXffForwardEnabledOptionsDef1,
                OneOfServiceXffForwardEnabledOptionsDef2,
            ]
        ]


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


    class SigData:
        tracker_src_ip: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        # Interface name: IPsec when present
        interface: Optional[List[Interface]]
        interface_metadata_sharing: Optional[InterfaceMetadataSharing]
        # Configure services
        service: Optional[Service]
        sig_provider: Optional[OneOfSigProviderOptionsDef]
        # Tracker configuration
        tracker: Optional[List[Tracker]]


    class Payload:
        """
        SIG schema for POST request
        """

        data: SigData
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
        # SIG schema for POST request
        payload: Optional[Payload]


    class GetListSdwanSigSecuritySigPayload:
        data: Optional[List[Data]]


    class CreateSigSecurityProfileParcel1PostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SigSecuritySigData:
        tracker_src_ip: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        # Interface name: IPsec when present
        interface: Optional[List[Interface]]
        interface_metadata_sharing: Optional[InterfaceMetadataSharing]
        # Configure services
        service: Optional[Service]
        sig_provider: Optional[OneOfSigProviderOptionsDef]
        # Tracker configuration
        tracker: Optional[List[Tracker]]


    class CreateSigSecurityProfileParcel1PostRequest:
        """
        SIG schema for POST request
        """

        data: SigSecuritySigData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class SigOneOfSigProviderOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SigSigProviderDef


    class SigInterfaceMetadataSharing:
        src_vpn: Optional[
            Union[OneOfSrcVpnOptionsDef1, OneOfSrcVpnOptionsDef2]
        ]


    class SigOneOfInterfaceIfNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfInterfaceDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfInterfaceAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfInterfaceTunnelSourceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfInterfaceTunnelRouteViaOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfInterfaceTunnelDestinationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfInterfaceApplicationOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SigInterfaceApplicationDef


    class SigOneOfInterfaceTunnelSetOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SigInterfaceTunnelSetDef


    class SigOneOfInterfaceTunnelDcPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SigInterfaceTunnelDcPreferenceDef


    class SigOneOfInterfaceTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigOneOfInterfaceMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigOneOfInterfaceDpdIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigOneOfInterfaceDpdIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigOneOfInterfaceDpdRetriesOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigOneOfInterfaceDpdRetriesOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigOneOfInterfaceIkeVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigOneOfInterfaceIkeVersionOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigOneOfInterfacePreSharedSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfInterfaceIkeRekeyIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigOneOfInterfaceIkeRekeyIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigOneOfInterfaceIkeCiphersuiteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SigInterfaceIkeCiphersuiteDef


    class SigOneOfInterfaceIkeCiphersuiteOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SigDefaultInterfaceIkeCiphersuiteDef]


    class SigOneOfInterfaceIkeGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SigInterfaceIkeGroupDef


    class SigOneOfInterfaceIkeGroupOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SigSecuritySigInterfaceIkeGroupDef]


    class SigOneOfInterfaceIkeLocalIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfInterfaceIkeRemoteIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfInterfaceIpsecRekeyIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigOneOfInterfaceIpsecRekeyIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigOneOfInterfaceIpsecReplayWindowOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SigInterfaceIpsecReplayWindowDef


    class SigOneOfInterfaceIpsecReplayWindowOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigOneOfInterfaceIpsecCiphersuiteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SigInterfaceIpsecCiphersuiteDef


    class SigOneOfInterfaceIpsecCiphersuiteOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SigSecuritySigInterfaceIpsecCiphersuiteDef]


    class SigOneOfInterfacePerfectForwardSecrecyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SigInterfacePerfectForwardSecrecyDef


    class SigOneOfInterfacePerfectForwardSecrecyOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SigSecuritySigInterfacePerfectForwardSecrecyDef]


    class SigOneOfInterfaceTrackerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfInterfaceTunnelPublicIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfInterfaceTunnelPublicIpOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class SigInterface:
        if_name: SigOneOfInterfaceIfNameOptionsDef
        tunnel_source_interface: Union[
            OneOfInterfaceTunnelSourceInterfaceOptionsDef1,
            OneOfInterfaceTunnelSourceInterfaceOptionsDef2,
        ]
        address: Optional[
            Union[
                SigOneOfInterfaceAddressOptionsDef1,
                OneOfInterfaceAddressOptionsDef2,
                OneOfInterfaceAddressOptionsDef3,
            ]
        ]
        application: Optional[SigOneOfInterfaceApplicationOptionsDef]
        auto: Optional[OneOfInterfaceAutoOptionsDef]
        description: Optional[
            Union[
                SigOneOfInterfaceDescriptionOptionsDef1,
                OneOfInterfaceDescriptionOptionsDef2,
                OneOfInterfaceDescriptionOptionsDef3,
            ]
        ]
        dpd_interval: Optional[
            Union[
                SigOneOfInterfaceDpdIntervalOptionsDef1,
                OneOfInterfaceDpdIntervalOptionsDef2,
                SigOneOfInterfaceDpdIntervalOptionsDef3,
            ]
        ]
        dpd_retries: Optional[
            Union[
                SigOneOfInterfaceDpdRetriesOptionsDef1,
                OneOfInterfaceDpdRetriesOptionsDef2,
                SigOneOfInterfaceDpdRetriesOptionsDef3,
            ]
        ]
        ike_ciphersuite: Optional[
            Union[
                SigOneOfInterfaceIkeCiphersuiteOptionsDef1,
                OneOfInterfaceIkeCiphersuiteOptionsDef2,
                SigOneOfInterfaceIkeCiphersuiteOptionsDef3,
            ]
        ]
        ike_group: Optional[
            Union[
                SigOneOfInterfaceIkeGroupOptionsDef1,
                OneOfInterfaceIkeGroupOptionsDef2,
                SigOneOfInterfaceIkeGroupOptionsDef3,
            ]
        ]
        ike_local_id: Optional[
            Union[
                SigOneOfInterfaceIkeLocalIdOptionsDef1,
                OneOfInterfaceIkeLocalIdOptionsDef2,
                OneOfInterfaceIkeLocalIdOptionsDef3,
            ]
        ]
        ike_rekey_interval: Optional[
            Union[
                SigOneOfInterfaceIkeRekeyIntervalOptionsDef1,
                OneOfInterfaceIkeRekeyIntervalOptionsDef2,
                SigOneOfInterfaceIkeRekeyIntervalOptionsDef3,
            ]
        ]
        ike_remote_id: Optional[
            Union[
                SigOneOfInterfaceIkeRemoteIdOptionsDef1,
                OneOfInterfaceIkeRemoteIdOptionsDef2,
                OneOfInterfaceIkeRemoteIdOptionsDef3,
            ]
        ]
        ike_version: Optional[
            Union[
                SigOneOfInterfaceIkeVersionOptionsDef1,
                OneOfInterfaceIkeVersionOptionsDef2,
                SigOneOfInterfaceIkeVersionOptionsDef3,
            ]
        ]
        ipsec_ciphersuite: Optional[
            Union[
                SigOneOfInterfaceIpsecCiphersuiteOptionsDef1,
                OneOfInterfaceIpsecCiphersuiteOptionsDef2,
                SigOneOfInterfaceIpsecCiphersuiteOptionsDef3,
            ]
        ]
        ipsec_rekey_interval: Optional[
            Union[
                SigOneOfInterfaceIpsecRekeyIntervalOptionsDef1,
                OneOfInterfaceIpsecRekeyIntervalOptionsDef2,
                SigOneOfInterfaceIpsecRekeyIntervalOptionsDef3,
            ]
        ]
        ipsec_replay_window: Optional[
            Union[
                SigOneOfInterfaceIpsecReplayWindowOptionsDef1,
                OneOfInterfaceIpsecReplayWindowOptionsDef2,
                SigOneOfInterfaceIpsecReplayWindowOptionsDef3,
            ]
        ]
        mtu: Optional[
            Union[
                SigOneOfInterfaceMtuOptionsDef1,
                OneOfInterfaceMtuOptionsDef2,
            ]
        ]
        perfect_forward_secrecy: Optional[
            Union[
                SigOneOfInterfacePerfectForwardSecrecyOptionsDef1,
                OneOfInterfacePerfectForwardSecrecyOptionsDef2,
                SigOneOfInterfacePerfectForwardSecrecyOptionsDef3,
            ]
        ]
        pre_shared_key_dynamic: Optional[
            OneOfInterfacePreSharedKeyDynamicOptionsDef
        ]
        pre_shared_secret: Optional[
            Union[
                SigOneOfInterfacePreSharedSecretOptionsDef1,
                OneOfInterfacePreSharedSecretOptionsDef2,
                OneOfInterfacePreSharedSecretOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfInterfaceShutdownOptionsDef1,
                OneOfInterfaceShutdownOptionsDef2,
            ]
        ]
        tcp_mss_adjust: Optional[
            Union[
                SigOneOfInterfaceTcpMssAdjustOptionsDef1,
                OneOfInterfaceTcpMssAdjustOptionsDef2,
                OneOfInterfaceTcpMssAdjustOptionsDef3,
            ]
        ]
        track_enable: Optional[
            Union[
                OneOfInterfaceTrackEnableOptionsDef1,
                OneOfInterfaceTrackEnableOptionsDef2,
            ]
        ]
        tracker: Optional[
            Union[
                SigOneOfInterfaceTrackerOptionsDef1,
                OneOfInterfaceTrackerOptionsDef2,
            ]
        ]
        tunnel_dc_preference: Optional[
            SigOneOfInterfaceTunnelDcPreferenceOptionsDef
        ]
        tunnel_destination: Optional[
            Union[
                SigOneOfInterfaceTunnelDestinationOptionsDef1,
                OneOfInterfaceTunnelDestinationOptionsDef2,
            ]
        ]
        tunnel_public_ip: Optional[
            Union[
                SigOneOfInterfaceTunnelPublicIpOptionsDef1,
                OneOfInterfaceTunnelPublicIpOptionsDef2,
                SigOneOfInterfaceTunnelPublicIpOptionsDef3,
            ]
        ]
        tunnel_route_via: Optional[
            Union[
                SigOneOfInterfaceTunnelRouteViaOptionsDef1,
                OneOfInterfaceTunnelRouteViaOptionsDef2,
            ]
        ]
        tunnel_set: Optional[SigOneOfInterfaceTunnelSetOptionsDef]
        tunnel_source: Optional[
            Union[
                SigOneOfInterfaceTunnelSourceOptionsDef1,
                OneOfInterfaceTunnelSourceOptionsDef2,
            ]
        ]
        unnumbered: Optional[OneOfInterfaceUnnumberedOptionsDef]


    class SigOneOfServiceInterfacePairActiveInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfServiceInterfacePairActiveInterfaceWeightOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SigOneOfServiceInterfacePairBackupInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfServiceInterfacePairBackupInterfaceWeightOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SigInterfacePair:
        active_interface: (
            SigOneOfServiceInterfacePairActiveInterfaceOptionsDef
        )
        backup_interface: (
            SigOneOfServiceInterfacePairBackupInterfaceOptionsDef
        )
        active_interface_weight: Optional[
            SigOneOfServiceInterfacePairActiveInterfaceWeightOptionsDef
        ]
        backup_interface_weight: Optional[
            SigOneOfServiceInterfacePairBackupInterfaceWeightOptionsDef
        ]


    class SigOneOfServicePrimaryDataCenterOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfServicePrimaryDataCenterOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class SigOneOfServiceSecondaryDataCenterOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfServiceSecondaryDataCenterOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class SigOneOfServiceIdleTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigOneOfServiceIdleTimeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class SigOneOfServiceDisplayTimeUnitOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SigServiceDisplayTimeUnitDef


    class SigOneOfServiceDisplayTimeUnitOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SigDefaultServiceDisplayTimeUnitDef]


    class SigOneOfServiceRefreshTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigOneOfServiceRefreshTimeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class SigOneOfServiceRefreshTimeUnitOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SigServiceRefreshTimeUnitDef


    class SigOneOfServiceRefreshTimeUnitOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SigDefaultServiceRefreshTimeUnitDef]


    class SigOneOfServiceTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigOneOfServiceTimeoutOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigOneOfServiceLocationNameOptionsDef1:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class SigOneOfServiceDataCenterPrimaryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfServiceDataCenterPrimaryOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class SigOneOfServiceDataCenterSecondaryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfServiceDataCenterSecondaryOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class SigService:
        """
        Configure services
        """

        auth_required: Optional[
            Union[
                OneOfServiceAuthRequiredOptionsDef1,
                OneOfServiceAuthRequiredOptionsDef2,
            ]
        ]
        block_internet_until_accepted: Optional[
            Union[
                OneOfServiceBlockInternetUntilAcceptedOptionsDef1,
                OneOfServiceBlockInternetUntilAcceptedOptionsDef2,
            ]
        ]
        caution_enabled: Optional[
            Union[
                OneOfServiceCautionEnabledOptionsDef1,
                OneOfServiceCautionEnabledOptionsDef2,
            ]
        ]
        data_center_primary: Optional[
            Union[
                SigOneOfServiceDataCenterPrimaryOptionsDef1,
                SigOneOfServiceDataCenterPrimaryOptionsDef2,
                OneOfServiceDataCenterPrimaryOptionsDef3,
            ]
        ]
        data_center_secondary: Optional[
            Union[
                SigOneOfServiceDataCenterSecondaryOptionsDef1,
                SigOneOfServiceDataCenterSecondaryOptionsDef2,
                OneOfServiceDataCenterSecondaryOptionsDef3,
            ]
        ]
        display_time_unit: Optional[
            Union[
                SigOneOfServiceDisplayTimeUnitOptionsDef1,
                SigOneOfServiceDisplayTimeUnitOptionsDef2,
            ]
        ]
        enabled: Optional[
            Union[
                OneOfServiceEnabledOptionsDef1,
                OneOfServiceEnabledOptionsDef2,
            ]
        ]
        force_ssl_inspection: Optional[
            Union[
                OneOfServiceForceSslInspectionOptionsDef1,
                OneOfServiceForceSslInspectionOptionsDef2,
            ]
        ]
        idle_time: Optional[
            Union[
                SigOneOfServiceIdleTimeOptionsDef1,
                SigOneOfServiceIdleTimeOptionsDef2,
            ]
        ]
        # Interface Pair for active and backup
        interface_pair: Optional[List[SigInterfacePair]]
        ip: Optional[
            Union[OneOfServiceIpOptionsDef1, OneOfServiceIpOptionsDef2]
        ]
        ip_enforced_for_known_browsers: Optional[
            Union[
                OneOfServiceIpEnforcedForKnownBrowsersOptionsDef1,
                OneOfServiceIpEnforcedForKnownBrowsersOptionsDef2,
            ]
        ]
        ips_control: Optional[
            Union[
                OneOfServiceIpsControlOptionsDef1,
                OneOfServiceIpsControlOptionsDef2,
            ]
        ]
        location_name: Optional[
            Union[
                SigOneOfServiceLocationNameOptionsDef1,
                OneOfServiceLocationNameOptionsDef2,
            ]
        ]
        ofw_enabled: Optional[
            Union[
                OneOfServiceOfwEnabledOptionsDef1,
                OneOfServiceOfwEnabledOptionsDef2,
            ]
        ]
        primary_data_center: Optional[
            Union[
                SigOneOfServicePrimaryDataCenterOptionsDef1,
                SigOneOfServicePrimaryDataCenterOptionsDef2,
                OneOfServicePrimaryDataCenterOptionsDef3,
            ]
        ]
        refresh_time: Optional[
            Union[
                SigOneOfServiceRefreshTimeOptionsDef1,
                SigOneOfServiceRefreshTimeOptionsDef2,
            ]
        ]
        refresh_time_unit: Optional[
            Union[
                SigOneOfServiceRefreshTimeUnitOptionsDef1,
                SigOneOfServiceRefreshTimeUnitOptionsDef2,
            ]
        ]
        secondary_data_center: Optional[
            Union[
                SigOneOfServiceSecondaryDataCenterOptionsDef1,
                SigOneOfServiceSecondaryDataCenterOptionsDef2,
                OneOfServiceSecondaryDataCenterOptionsDef3,
            ]
        ]
        timeout: Optional[
            Union[
                SigOneOfServiceTimeoutOptionsDef1,
                SigOneOfServiceTimeoutOptionsDef2,
            ]
        ]
        xff_forward_enabled: Optional[
            Union[
                OneOfServiceXffForwardEnabledOptionsDef1,
                OneOfServiceXffForwardEnabledOptionsDef2,
            ]
        ]


    class SigOneOfTrackerNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfTrackerEndpointApiUrlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigOneOfTrackerThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigOneOfTrackerThresholdOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigOneOfTrackerIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigOneOfTrackerIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigOneOfTrackerMultiplierOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigOneOfTrackerMultiplierOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigOneOfTrackerTrackerTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SigTrackerTrackerTypeDef


    class SigTracker:
        endpoint_api_url: Union[
            SigOneOfTrackerEndpointApiUrlOptionsDef1,
            OneOfTrackerEndpointApiUrlOptionsDef2,
        ]
        name: SigOneOfTrackerNameOptionsDef
        tracker_type: SigOneOfTrackerTrackerTypeOptionsDef
        interval: Optional[
            Union[
                SigOneOfTrackerIntervalOptionsDef1,
                OneOfTrackerIntervalOptionsDef2,
                SigOneOfTrackerIntervalOptionsDef3,
            ]
        ]
        multiplier: Optional[
            Union[
                SigOneOfTrackerMultiplierOptionsDef1,
                OneOfTrackerMultiplierOptionsDef2,
                SigOneOfTrackerMultiplierOptionsDef3,
            ]
        ]
        threshold: Optional[
            Union[
                SigOneOfTrackerThresholdOptionsDef1,
                OneOfTrackerThresholdOptionsDef2,
                SigOneOfTrackerThresholdOptionsDef3,
            ]
        ]


    class SdwanSigSecuritySigData:
        tracker_src_ip: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        # Interface name: IPsec when present
        interface: Optional[List[SigInterface]]
        interface_metadata_sharing: Optional[SigInterfaceMetadataSharing]
        # Configure services
        service: Optional[SigService]
        sig_provider: Optional[SigOneOfSigProviderOptionsDef]
        # Tracker configuration
        tracker: Optional[List[SigTracker]]


    class SigPayload:
        """
        SIG schema for PUT request
        """

        data: SdwanSigSecuritySigData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanSigSecuritySigPayload:
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
        # SIG schema for PUT request
        payload: Optional[SigPayload]


    class EditSigSecurityProfileParcel1PutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SigSecuritySigOneOfSigProviderOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SigSecuritySigSigProviderDef


    class SigSecuritySigInterfaceMetadataSharing:
        src_vpn: Optional[
            Union[OneOfSrcVpnOptionsDef1, OneOfSrcVpnOptionsDef2]
        ]


    class SigSecuritySigOneOfInterfaceIfNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfInterfaceDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfInterfaceAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfInterfaceTunnelSourceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfInterfaceTunnelRouteViaOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfInterfaceTunnelDestinationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfInterfaceApplicationOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SigSecuritySigInterfaceApplicationDef


    class SigSecuritySigOneOfInterfaceTunnelSetOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SigSecuritySigInterfaceTunnelSetDef


    class SigSecuritySigOneOfInterfaceTunnelDcPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SigSecuritySigInterfaceTunnelDcPreferenceDef


    class SigSecuritySigOneOfInterfaceTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigOneOfInterfaceMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigOneOfInterfaceDpdIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigOneOfInterfaceDpdIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigSecuritySigOneOfInterfaceDpdRetriesOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigOneOfInterfaceDpdRetriesOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigSecuritySigOneOfInterfaceIkeVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigOneOfInterfaceIkeVersionOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigSecuritySigOneOfInterfacePreSharedSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfInterfaceIkeRekeyIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigOneOfInterfaceIkeRekeyIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigSecuritySigOneOfInterfaceIkeCiphersuiteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SigSecuritySigInterfaceIkeCiphersuiteDef


    class SigSecuritySigOneOfInterfaceIkeCiphersuiteOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SigSecuritySigDefaultInterfaceIkeCiphersuiteDef]


    class SigSecuritySigOneOfInterfaceIkeGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SdwanSigSecuritySigInterfaceIkeGroupDef


    class SigSecuritySigOneOfInterfaceIkeGroupOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[
            FeatureProfileSdwanSigSecuritySigInterfaceIkeGroupDef
        ]


    class SigSecuritySigOneOfInterfaceIkeLocalIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfInterfaceIkeRemoteIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfInterfaceIpsecRekeyIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigOneOfInterfaceIpsecRekeyIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigSecuritySigOneOfInterfaceIpsecReplayWindowOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SigSecuritySigInterfaceIpsecReplayWindowDef


    class SigSecuritySigOneOfInterfaceIpsecReplayWindowOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigSecuritySigOneOfInterfaceIpsecCiphersuiteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SdwanSigSecuritySigInterfaceIpsecCiphersuiteDef


    class SigSecuritySigOneOfInterfaceIpsecCiphersuiteOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[
            FeatureProfileSdwanSigSecuritySigInterfaceIpsecCiphersuiteDef
        ]


    class SigSecuritySigOneOfInterfacePerfectForwardSecrecyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SdwanSigSecuritySigInterfacePerfectForwardSecrecyDef


    class SigSecuritySigOneOfInterfacePerfectForwardSecrecyOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[
            FeatureProfileSdwanSigSecuritySigInterfacePerfectForwardSecrecyDef
        ]


    class SigSecuritySigOneOfInterfaceTrackerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfInterfaceTunnelPublicIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfInterfaceTunnelPublicIpOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class SigSecuritySigInterface:
        if_name: SigSecuritySigOneOfInterfaceIfNameOptionsDef
        tunnel_source_interface: Union[
            OneOfInterfaceTunnelSourceInterfaceOptionsDef1,
            OneOfInterfaceTunnelSourceInterfaceOptionsDef2,
        ]
        address: Optional[
            Union[
                SigSecuritySigOneOfInterfaceAddressOptionsDef1,
                OneOfInterfaceAddressOptionsDef2,
                OneOfInterfaceAddressOptionsDef3,
            ]
        ]
        application: Optional[
            SigSecuritySigOneOfInterfaceApplicationOptionsDef
        ]
        auto: Optional[OneOfInterfaceAutoOptionsDef]
        description: Optional[
            Union[
                SigSecuritySigOneOfInterfaceDescriptionOptionsDef1,
                OneOfInterfaceDescriptionOptionsDef2,
                OneOfInterfaceDescriptionOptionsDef3,
            ]
        ]
        dpd_interval: Optional[
            Union[
                SigSecuritySigOneOfInterfaceDpdIntervalOptionsDef1,
                OneOfInterfaceDpdIntervalOptionsDef2,
                SigSecuritySigOneOfInterfaceDpdIntervalOptionsDef3,
            ]
        ]
        dpd_retries: Optional[
            Union[
                SigSecuritySigOneOfInterfaceDpdRetriesOptionsDef1,
                OneOfInterfaceDpdRetriesOptionsDef2,
                SigSecuritySigOneOfInterfaceDpdRetriesOptionsDef3,
            ]
        ]
        ike_ciphersuite: Optional[
            Union[
                SigSecuritySigOneOfInterfaceIkeCiphersuiteOptionsDef1,
                OneOfInterfaceIkeCiphersuiteOptionsDef2,
                SigSecuritySigOneOfInterfaceIkeCiphersuiteOptionsDef3,
            ]
        ]
        ike_group: Optional[
            Union[
                SigSecuritySigOneOfInterfaceIkeGroupOptionsDef1,
                OneOfInterfaceIkeGroupOptionsDef2,
                SigSecuritySigOneOfInterfaceIkeGroupOptionsDef3,
            ]
        ]
        ike_local_id: Optional[
            Union[
                SigSecuritySigOneOfInterfaceIkeLocalIdOptionsDef1,
                OneOfInterfaceIkeLocalIdOptionsDef2,
                OneOfInterfaceIkeLocalIdOptionsDef3,
            ]
        ]
        ike_rekey_interval: Optional[
            Union[
                SigSecuritySigOneOfInterfaceIkeRekeyIntervalOptionsDef1,
                OneOfInterfaceIkeRekeyIntervalOptionsDef2,
                SigSecuritySigOneOfInterfaceIkeRekeyIntervalOptionsDef3,
            ]
        ]
        ike_remote_id: Optional[
            Union[
                SigSecuritySigOneOfInterfaceIkeRemoteIdOptionsDef1,
                OneOfInterfaceIkeRemoteIdOptionsDef2,
                OneOfInterfaceIkeRemoteIdOptionsDef3,
            ]
        ]
        ike_version: Optional[
            Union[
                SigSecuritySigOneOfInterfaceIkeVersionOptionsDef1,
                OneOfInterfaceIkeVersionOptionsDef2,
                SigSecuritySigOneOfInterfaceIkeVersionOptionsDef3,
            ]
        ]
        ipsec_ciphersuite: Optional[
            Union[
                SigSecuritySigOneOfInterfaceIpsecCiphersuiteOptionsDef1,
                OneOfInterfaceIpsecCiphersuiteOptionsDef2,
                SigSecuritySigOneOfInterfaceIpsecCiphersuiteOptionsDef3,
            ]
        ]
        ipsec_rekey_interval: Optional[
            Union[
                SigSecuritySigOneOfInterfaceIpsecRekeyIntervalOptionsDef1,
                OneOfInterfaceIpsecRekeyIntervalOptionsDef2,
                SigSecuritySigOneOfInterfaceIpsecRekeyIntervalOptionsDef3,
            ]
        ]
        ipsec_replay_window: Optional[
            Union[
                SigSecuritySigOneOfInterfaceIpsecReplayWindowOptionsDef1,
                OneOfInterfaceIpsecReplayWindowOptionsDef2,
                SigSecuritySigOneOfInterfaceIpsecReplayWindowOptionsDef3,
            ]
        ]
        mtu: Optional[
            Union[
                SigSecuritySigOneOfInterfaceMtuOptionsDef1,
                OneOfInterfaceMtuOptionsDef2,
            ]
        ]
        perfect_forward_secrecy: Optional[
            Union[
                SigSecuritySigOneOfInterfacePerfectForwardSecrecyOptionsDef1,
                OneOfInterfacePerfectForwardSecrecyOptionsDef2,
                SigSecuritySigOneOfInterfacePerfectForwardSecrecyOptionsDef3,
            ]
        ]
        pre_shared_key_dynamic: Optional[
            OneOfInterfacePreSharedKeyDynamicOptionsDef
        ]
        pre_shared_secret: Optional[
            Union[
                SigSecuritySigOneOfInterfacePreSharedSecretOptionsDef1,
                OneOfInterfacePreSharedSecretOptionsDef2,
                OneOfInterfacePreSharedSecretOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfInterfaceShutdownOptionsDef1,
                OneOfInterfaceShutdownOptionsDef2,
            ]
        ]
        tcp_mss_adjust: Optional[
            Union[
                SigSecuritySigOneOfInterfaceTcpMssAdjustOptionsDef1,
                OneOfInterfaceTcpMssAdjustOptionsDef2,
                OneOfInterfaceTcpMssAdjustOptionsDef3,
            ]
        ]
        track_enable: Optional[
            Union[
                OneOfInterfaceTrackEnableOptionsDef1,
                OneOfInterfaceTrackEnableOptionsDef2,
            ]
        ]
        tracker: Optional[
            Union[
                SigSecuritySigOneOfInterfaceTrackerOptionsDef1,
                OneOfInterfaceTrackerOptionsDef2,
            ]
        ]
        tunnel_dc_preference: Optional[
            SigSecuritySigOneOfInterfaceTunnelDcPreferenceOptionsDef
        ]
        tunnel_destination: Optional[
            Union[
                SigSecuritySigOneOfInterfaceTunnelDestinationOptionsDef1,
                OneOfInterfaceTunnelDestinationOptionsDef2,
            ]
        ]
        tunnel_public_ip: Optional[
            Union[
                SigSecuritySigOneOfInterfaceTunnelPublicIpOptionsDef1,
                OneOfInterfaceTunnelPublicIpOptionsDef2,
                SigSecuritySigOneOfInterfaceTunnelPublicIpOptionsDef3,
            ]
        ]
        tunnel_route_via: Optional[
            Union[
                SigSecuritySigOneOfInterfaceTunnelRouteViaOptionsDef1,
                OneOfInterfaceTunnelRouteViaOptionsDef2,
            ]
        ]
        tunnel_set: Optional[
            SigSecuritySigOneOfInterfaceTunnelSetOptionsDef
        ]
        tunnel_source: Optional[
            Union[
                SigSecuritySigOneOfInterfaceTunnelSourceOptionsDef1,
                OneOfInterfaceTunnelSourceOptionsDef2,
            ]
        ]
        unnumbered: Optional[OneOfInterfaceUnnumberedOptionsDef]


    class SigSecuritySigOneOfServiceInterfacePairActiveInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfServiceInterfacePairActiveInterfaceWeightOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigOneOfServiceInterfacePairBackupInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfServiceInterfacePairBackupInterfaceWeightOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigInterfacePair:
        active_interface: SigSecuritySigOneOfServiceInterfacePairActiveInterfaceOptionsDef
        backup_interface: SigSecuritySigOneOfServiceInterfacePairBackupInterfaceOptionsDef
        active_interface_weight: Optional[
            SigSecuritySigOneOfServiceInterfacePairActiveInterfaceWeightOptionsDef
        ]
        backup_interface_weight: Optional[
            SigSecuritySigOneOfServiceInterfacePairBackupInterfaceWeightOptionsDef
        ]


    class SigSecuritySigOneOfServicePrimaryDataCenterOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfServicePrimaryDataCenterOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class SigSecuritySigOneOfServiceSecondaryDataCenterOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfServiceSecondaryDataCenterOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class SigSecuritySigOneOfServiceIdleTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigOneOfServiceIdleTimeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class SigSecuritySigOneOfServiceDisplayTimeUnitOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SigSecuritySigServiceDisplayTimeUnitDef


    class SigSecuritySigOneOfServiceDisplayTimeUnitOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SigSecuritySigDefaultServiceDisplayTimeUnitDef]


    class SigSecuritySigOneOfServiceRefreshTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigOneOfServiceRefreshTimeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class SigSecuritySigOneOfServiceRefreshTimeUnitOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SigSecuritySigServiceRefreshTimeUnitDef


    class SigSecuritySigOneOfServiceRefreshTimeUnitOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[SigSecuritySigDefaultServiceRefreshTimeUnitDef]


    class SigSecuritySigOneOfServiceTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigOneOfServiceTimeoutOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigSecuritySigOneOfServiceLocationNameOptionsDef1:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class SigSecuritySigOneOfServiceDataCenterPrimaryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfServiceDataCenterPrimaryOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class SigSecuritySigOneOfServiceDataCenterSecondaryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfServiceDataCenterSecondaryOptionsDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[str]


    class SigSecuritySigService:
        """
        Configure services
        """

        auth_required: Optional[
            Union[
                OneOfServiceAuthRequiredOptionsDef1,
                OneOfServiceAuthRequiredOptionsDef2,
            ]
        ]
        block_internet_until_accepted: Optional[
            Union[
                OneOfServiceBlockInternetUntilAcceptedOptionsDef1,
                OneOfServiceBlockInternetUntilAcceptedOptionsDef2,
            ]
        ]
        caution_enabled: Optional[
            Union[
                OneOfServiceCautionEnabledOptionsDef1,
                OneOfServiceCautionEnabledOptionsDef2,
            ]
        ]
        data_center_primary: Optional[
            Union[
                SigSecuritySigOneOfServiceDataCenterPrimaryOptionsDef1,
                SigSecuritySigOneOfServiceDataCenterPrimaryOptionsDef2,
                OneOfServiceDataCenterPrimaryOptionsDef3,
            ]
        ]
        data_center_secondary: Optional[
            Union[
                SigSecuritySigOneOfServiceDataCenterSecondaryOptionsDef1,
                SigSecuritySigOneOfServiceDataCenterSecondaryOptionsDef2,
                OneOfServiceDataCenterSecondaryOptionsDef3,
            ]
        ]
        display_time_unit: Optional[
            Union[
                SigSecuritySigOneOfServiceDisplayTimeUnitOptionsDef1,
                SigSecuritySigOneOfServiceDisplayTimeUnitOptionsDef2,
            ]
        ]
        enabled: Optional[
            Union[
                OneOfServiceEnabledOptionsDef1,
                OneOfServiceEnabledOptionsDef2,
            ]
        ]
        force_ssl_inspection: Optional[
            Union[
                OneOfServiceForceSslInspectionOptionsDef1,
                OneOfServiceForceSslInspectionOptionsDef2,
            ]
        ]
        idle_time: Optional[
            Union[
                SigSecuritySigOneOfServiceIdleTimeOptionsDef1,
                SigSecuritySigOneOfServiceIdleTimeOptionsDef2,
            ]
        ]
        # Interface Pair for active and backup
        interface_pair: Optional[List[SigSecuritySigInterfacePair]]
        ip: Optional[
            Union[OneOfServiceIpOptionsDef1, OneOfServiceIpOptionsDef2]
        ]
        ip_enforced_for_known_browsers: Optional[
            Union[
                OneOfServiceIpEnforcedForKnownBrowsersOptionsDef1,
                OneOfServiceIpEnforcedForKnownBrowsersOptionsDef2,
            ]
        ]
        ips_control: Optional[
            Union[
                OneOfServiceIpsControlOptionsDef1,
                OneOfServiceIpsControlOptionsDef2,
            ]
        ]
        location_name: Optional[
            Union[
                SigSecuritySigOneOfServiceLocationNameOptionsDef1,
                OneOfServiceLocationNameOptionsDef2,
            ]
        ]
        ofw_enabled: Optional[
            Union[
                OneOfServiceOfwEnabledOptionsDef1,
                OneOfServiceOfwEnabledOptionsDef2,
            ]
        ]
        primary_data_center: Optional[
            Union[
                SigSecuritySigOneOfServicePrimaryDataCenterOptionsDef1,
                SigSecuritySigOneOfServicePrimaryDataCenterOptionsDef2,
                OneOfServicePrimaryDataCenterOptionsDef3,
            ]
        ]
        refresh_time: Optional[
            Union[
                SigSecuritySigOneOfServiceRefreshTimeOptionsDef1,
                SigSecuritySigOneOfServiceRefreshTimeOptionsDef2,
            ]
        ]
        refresh_time_unit: Optional[
            Union[
                SigSecuritySigOneOfServiceRefreshTimeUnitOptionsDef1,
                SigSecuritySigOneOfServiceRefreshTimeUnitOptionsDef2,
            ]
        ]
        secondary_data_center: Optional[
            Union[
                SigSecuritySigOneOfServiceSecondaryDataCenterOptionsDef1,
                SigSecuritySigOneOfServiceSecondaryDataCenterOptionsDef2,
                OneOfServiceSecondaryDataCenterOptionsDef3,
            ]
        ]
        timeout: Optional[
            Union[
                SigSecuritySigOneOfServiceTimeoutOptionsDef1,
                SigSecuritySigOneOfServiceTimeoutOptionsDef2,
            ]
        ]
        xff_forward_enabled: Optional[
            Union[
                OneOfServiceXffForwardEnabledOptionsDef1,
                OneOfServiceXffForwardEnabledOptionsDef2,
            ]
        ]


    class SigSecuritySigOneOfTrackerNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfTrackerEndpointApiUrlOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SigSecuritySigOneOfTrackerThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigOneOfTrackerThresholdOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigSecuritySigOneOfTrackerIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigOneOfTrackerIntervalOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigSecuritySigOneOfTrackerMultiplierOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SigSecuritySigOneOfTrackerMultiplierOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[int]


    class SigSecuritySigOneOfTrackerTrackerTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SigSecuritySigTrackerTrackerTypeDef


    class SigSecuritySigTracker:
        endpoint_api_url: Union[
            SigSecuritySigOneOfTrackerEndpointApiUrlOptionsDef1,
            OneOfTrackerEndpointApiUrlOptionsDef2,
        ]
        name: SigSecuritySigOneOfTrackerNameOptionsDef
        tracker_type: SigSecuritySigOneOfTrackerTrackerTypeOptionsDef
        interval: Optional[
            Union[
                SigSecuritySigOneOfTrackerIntervalOptionsDef1,
                OneOfTrackerIntervalOptionsDef2,
                SigSecuritySigOneOfTrackerIntervalOptionsDef3,
            ]
        ]
        multiplier: Optional[
            Union[
                SigSecuritySigOneOfTrackerMultiplierOptionsDef1,
                OneOfTrackerMultiplierOptionsDef2,
                SigSecuritySigOneOfTrackerMultiplierOptionsDef3,
            ]
        ]
        threshold: Optional[
            Union[
                SigSecuritySigOneOfTrackerThresholdOptionsDef1,
                OneOfTrackerThresholdOptionsDef2,
                SigSecuritySigOneOfTrackerThresholdOptionsDef3,
            ]
        ]


    class FeatureProfileSdwanSigSecuritySigData:
        tracker_src_ip: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        # Interface name: IPsec when present
        interface: Optional[List[SigSecuritySigInterface]]
        interface_metadata_sharing: Optional[
            SigSecuritySigInterfaceMetadataSharing
        ]
        # Configure services
        service: Optional[SigSecuritySigService]
        sig_provider: Optional[SigSecuritySigOneOfSigProviderOptionsDef]
        # Tracker configuration
        tracker: Optional[List[SigSecuritySigTracker]]


    class EditSigSecurityProfileParcel1PutRequest:
        """
        SIG schema for PUT request
        """

        data: FeatureProfileSdwanSigSecuritySigData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


