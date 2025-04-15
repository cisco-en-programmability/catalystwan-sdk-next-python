======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    TunnelModeDef = Literal["ipv4", "ipv4-v6overlay", "ipv6"]

    DefaultTunnelModeDef = Literal["ipv4"]

    Ipv4SubnetMaskDef = Literal[
        "0.0.0.0",
        "128.0.0.0",
        "192.0.0.0",
        "224.0.0.0",
        "240.0.0.0",
        "248.0.0.0",
        "252.0.0.0",
        "254.0.0.0",
        "255.0.0.0",
        "255.128.0.0",
        "255.192.0.0",
        "255.224.0.0",
        "255.240.0.0",
        "255.252.0.0",
        "255.254.0.0",
        "255.255.0.0",
        "255.255.128.0",
        "255.255.192.0",
        "255.255.224.0",
        "255.255.240.0",
        "255.255.248.0",
        "255.255.252.0",
        "255.255.254.0",
        "255.255.255.0",
        "255.255.255.128",
        "255.255.255.192",
        "255.255.255.224",
        "255.255.255.240",
        "255.255.255.248",
        "255.255.255.252",
        "255.255.255.254",
        "255.255.255.255",
    ]

    ApplicationDef = Literal["none", "sig"]

    IkeModeDef = Literal["aggressive", "main"]

    DefaultIkeModeDef = Literal["main"]

    IkeCiphersuiteDef = Literal[
        "aes128-cbc-sha1",
        "aes128-cbc-sha2",
        "aes256-cbc-sha1",
        "aes256-cbc-sha2",
    ]

    DefaultIkeCiphersuiteDef = Literal["aes256-cbc-sha1"]

    IkeGroupDef = Literal["14", "15", "16", "19", "2", "20", "21", "24"]

    DefaultIkeGroupDef = Literal["16"]

    IpsecCiphersuiteDef = Literal[
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-cbc-sha384",
        "aes256-cbc-sha512",
        "aes256-gcm",
        "null-sha1",
        "null-sha256",
        "null-sha384",
        "null-sha512",
    ]

    DefaultIpsecCiphersuiteDef = Literal["aes256-gcm"]

    PerfectForwardSecrecyDef = Literal[
        "group-1",
        "group-14",
        "group-15",
        "group-16",
        "group-19",
        "group-2",
        "group-20",
        "group-21",
        "group-24",
        "group-5",
        "none",
    ]

    DefaultPerfectForwardSecrecyDef = Literal["group-16"]


    class OneOfIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIfNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfShutdownOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfShutdownOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfShutdownOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfTunnelModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TunnelModeDef


    class OneOfTunnelModeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: DefaultTunnelModeDef  # pytype: disable=annotation-type-mismatch


    class OneOfDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDescriptionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDescriptionOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfIpV4SubnetMaskOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4SubnetMaskOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: (
            Ipv4SubnetMaskDef  # pytype: disable=annotation-type-mismatch
        )


    class Ipv4AddressAndMaskDef:
        address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class OneOfIpv6PrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6PrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6AddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6AddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTunnelSourceInterfaceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTunnelSourceInterfaceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfApplicationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ApplicationDef


    class OneOfApplicationOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTcpMssAdjustOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTcpMssAdjustOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfTcpMssAdjustV6OptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTcpMssAdjustV6OptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTcpMssAdjustV6OptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfClearDontFragmentOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfClearDontFragmentOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfClearDontFragmentOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMtuOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfMtuV6OptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMtuV6OptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMtuV6OptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfDpdIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDpdIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDpdIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfDpdRetriesOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDpdRetriesOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDpdRetriesOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIkeVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIkeVersionOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIkeModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: IkeModeDef


    class OneOfIkeModeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeModeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: (
            DefaultIkeModeDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfIkeRekeyIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIkeRekeyIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeRekeyIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIkeCiphersuiteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: IkeCiphersuiteDef


    class OneOfIkeCiphersuiteOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeCiphersuiteOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultIkeCiphersuiteDef  # pytype: disable=annotation-type-mismatch


    class OneOfIkeGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: IkeGroupDef


    class OneOfIkeGroupOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeGroupOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: (
            DefaultIkeGroupDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfPreSharedSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfPreSharedSecretOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeLocalIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIkeLocalIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeLocalIdOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfIkeRemoteIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIkeRemoteIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeRemoteIdOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfIpsecRekeyIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpsecRekeyIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpsecRekeyIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIpsecReplayWindowOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpsecReplayWindowOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpsecReplayWindowOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIpsecCiphersuiteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: IpsecCiphersuiteDef


    class OneOfIpsecCiphersuiteOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpsecCiphersuiteOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultIpsecCiphersuiteDef  # pytype: disable=annotation-type-mismatch


    class OneOfPerfectForwardSecrecyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: PerfectForwardSecrecyDef


    class OneOfPerfectForwardSecrecyOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPerfectForwardSecrecyOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultPerfectForwardSecrecyDef  # pytype: disable=annotation-type-mismatch


    class OneOfTrackerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTrackerOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfTunnelRouteViaOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTunnelRouteViaOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTunnelRouteViaOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Data1:
        address: Ipv4AddressAndMaskDef
        application: Union[
            OneOfApplicationOptionsDef1, OneOfApplicationOptionsDef2
        ]
        clear_dont_fragment: Union[
            OneOfClearDontFragmentOptionsDef1,
            OneOfClearDontFragmentOptionsDef2,
            OneOfClearDontFragmentOptionsDef3,
        ]
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        dpd_interval: Union[
            OneOfDpdIntervalOptionsDef1,
            OneOfDpdIntervalOptionsDef2,
            OneOfDpdIntervalOptionsDef3,
        ]
        dpd_retries: Union[
            OneOfDpdRetriesOptionsDef1,
            OneOfDpdRetriesOptionsDef2,
            OneOfDpdRetriesOptionsDef3,
        ]
        if_name: Union[OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2]
        ike_ciphersuite: Union[
            OneOfIkeCiphersuiteOptionsDef1,
            OneOfIkeCiphersuiteOptionsDef2,
            OneOfIkeCiphersuiteOptionsDef3,
        ]
        ike_group: Union[
            OneOfIkeGroupOptionsDef1,
            OneOfIkeGroupOptionsDef2,
            OneOfIkeGroupOptionsDef3,
        ]
        ike_local_id: Union[
            OneOfIkeLocalIdOptionsDef1,
            OneOfIkeLocalIdOptionsDef2,
            OneOfIkeLocalIdOptionsDef3,
        ]
        ike_rekey_interval: Union[
            OneOfIkeRekeyIntervalOptionsDef1,
            OneOfIkeRekeyIntervalOptionsDef2,
            OneOfIkeRekeyIntervalOptionsDef3,
        ]
        ike_remote_id: Union[
            OneOfIkeRemoteIdOptionsDef1,
            OneOfIkeRemoteIdOptionsDef2,
            OneOfIkeRemoteIdOptionsDef3,
        ]
        ike_version: Union[
            OneOfIkeVersionOptionsDef1, OneOfIkeVersionOptionsDef2
        ]
        ipsec_ciphersuite: Union[
            OneOfIpsecCiphersuiteOptionsDef1,
            OneOfIpsecCiphersuiteOptionsDef2,
            OneOfIpsecCiphersuiteOptionsDef3,
        ]
        ipsec_rekey_interval: Union[
            OneOfIpsecRekeyIntervalOptionsDef1,
            OneOfIpsecRekeyIntervalOptionsDef2,
            OneOfIpsecRekeyIntervalOptionsDef3,
        ]
        ipsec_replay_window: Union[
            OneOfIpsecReplayWindowOptionsDef1,
            OneOfIpsecReplayWindowOptionsDef2,
            OneOfIpsecReplayWindowOptionsDef3,
        ]
        mtu: Union[
            OneOfMtuOptionsDef1, OneOfMtuOptionsDef2, OneOfMtuOptionsDef3
        ]
        perfect_forward_secrecy: Union[
            OneOfPerfectForwardSecrecyOptionsDef1,
            OneOfPerfectForwardSecrecyOptionsDef2,
            OneOfPerfectForwardSecrecyOptionsDef3,
        ]
        pre_shared_secret: Union[
            OneOfPreSharedSecretOptionsDef1,
            OneOfPreSharedSecretOptionsDef2,
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tcp_mss_adjust: Union[
            OneOfTcpMssAdjustOptionsDef1,
            OneOfTcpMssAdjustOptionsDef2,
            OneOfTcpMssAdjustOptionsDef3,
        ]
        tunnel_destination: Ipv4AddressAndMaskDef
        tunnel_source: Ipv4AddressAndMaskDef
        ike_mode: Optional[
            Union[
                OneOfIkeModeOptionsDef1,
                OneOfIkeModeOptionsDef2,
                OneOfIkeModeOptionsDef3,
            ]
        ]
        ipv6_address: Optional[
            Union[OneOfIpv6PrefixOptionsDef1, OneOfIpv6PrefixOptionsDef2]
        ]
        mtu_v6: Optional[
            Union[
                OneOfMtuV6OptionsDef1,
                OneOfMtuV6OptionsDef2,
                OneOfMtuV6OptionsDef3,
            ]
        ]
        tcp_mss_adjust_v6: Optional[
            Union[
                OneOfTcpMssAdjustV6OptionsDef1,
                OneOfTcpMssAdjustV6OptionsDef2,
                OneOfTcpMssAdjustV6OptionsDef3,
            ]
        ]
        tracker: Optional[
            Union[
                OneOfTrackerOptionsDef1,
                OneOfTrackerOptionsDef2,
                OneOfTrackerOptionsDef3,
            ]
        ]
        tunnel_destination_v6: Optional[
            Union[
                OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
            ]
        ]
        tunnel_mode: Optional[
            Union[OneOfTunnelModeOptionsDef1, OneOfTunnelModeOptionsDef2]
        ]
        tunnel_route_via: Optional[
            Union[
                OneOfTunnelRouteViaOptionsDef1,
                OneOfTunnelRouteViaOptionsDef2,
                OneOfTunnelRouteViaOptionsDef3,
            ]
        ]
        tunnel_source_interface: Optional[
            Union[
                OneOfTunnelSourceInterfaceOptionsDef1,
                OneOfTunnelSourceInterfaceOptionsDef2,
            ]
        ]
        tunnel_source_v6: Optional[
            Union[
                OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
            ]
        ]


    class Data2:
        address: Ipv4AddressAndMaskDef
        application: Union[
            OneOfApplicationOptionsDef1, OneOfApplicationOptionsDef2
        ]
        clear_dont_fragment: Union[
            OneOfClearDontFragmentOptionsDef1,
            OneOfClearDontFragmentOptionsDef2,
            OneOfClearDontFragmentOptionsDef3,
        ]
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        dpd_interval: Union[
            OneOfDpdIntervalOptionsDef1,
            OneOfDpdIntervalOptionsDef2,
            OneOfDpdIntervalOptionsDef3,
        ]
        dpd_retries: Union[
            OneOfDpdRetriesOptionsDef1,
            OneOfDpdRetriesOptionsDef2,
            OneOfDpdRetriesOptionsDef3,
        ]
        if_name: Union[OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2]
        ike_ciphersuite: Union[
            OneOfIkeCiphersuiteOptionsDef1,
            OneOfIkeCiphersuiteOptionsDef2,
            OneOfIkeCiphersuiteOptionsDef3,
        ]
        ike_group: Union[
            OneOfIkeGroupOptionsDef1,
            OneOfIkeGroupOptionsDef2,
            OneOfIkeGroupOptionsDef3,
        ]
        ike_local_id: Union[
            OneOfIkeLocalIdOptionsDef1,
            OneOfIkeLocalIdOptionsDef2,
            OneOfIkeLocalIdOptionsDef3,
        ]
        ike_rekey_interval: Union[
            OneOfIkeRekeyIntervalOptionsDef1,
            OneOfIkeRekeyIntervalOptionsDef2,
            OneOfIkeRekeyIntervalOptionsDef3,
        ]
        ike_remote_id: Union[
            OneOfIkeRemoteIdOptionsDef1,
            OneOfIkeRemoteIdOptionsDef2,
            OneOfIkeRemoteIdOptionsDef3,
        ]
        ike_version: Union[
            OneOfIkeVersionOptionsDef1, OneOfIkeVersionOptionsDef2
        ]
        ipsec_ciphersuite: Union[
            OneOfIpsecCiphersuiteOptionsDef1,
            OneOfIpsecCiphersuiteOptionsDef2,
            OneOfIpsecCiphersuiteOptionsDef3,
        ]
        ipsec_rekey_interval: Union[
            OneOfIpsecRekeyIntervalOptionsDef1,
            OneOfIpsecRekeyIntervalOptionsDef2,
            OneOfIpsecRekeyIntervalOptionsDef3,
        ]
        ipsec_replay_window: Union[
            OneOfIpsecReplayWindowOptionsDef1,
            OneOfIpsecReplayWindowOptionsDef2,
            OneOfIpsecReplayWindowOptionsDef3,
        ]
        mtu: Union[
            OneOfMtuOptionsDef1, OneOfMtuOptionsDef2, OneOfMtuOptionsDef3
        ]
        perfect_forward_secrecy: Union[
            OneOfPerfectForwardSecrecyOptionsDef1,
            OneOfPerfectForwardSecrecyOptionsDef2,
            OneOfPerfectForwardSecrecyOptionsDef3,
        ]
        pre_shared_secret: Union[
            OneOfPreSharedSecretOptionsDef1,
            OneOfPreSharedSecretOptionsDef2,
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tcp_mss_adjust: Union[
            OneOfTcpMssAdjustOptionsDef1,
            OneOfTcpMssAdjustOptionsDef2,
            OneOfTcpMssAdjustOptionsDef3,
        ]
        tunnel_destination: Ipv4AddressAndMaskDef
        tunnel_source_interface: Union[
            OneOfTunnelSourceInterfaceOptionsDef1,
            OneOfTunnelSourceInterfaceOptionsDef2,
        ]
        ike_mode: Optional[
            Union[
                OneOfIkeModeOptionsDef1,
                OneOfIkeModeOptionsDef2,
                OneOfIkeModeOptionsDef3,
            ]
        ]
        ipv6_address: Optional[
            Union[OneOfIpv6PrefixOptionsDef1, OneOfIpv6PrefixOptionsDef2]
        ]
        mtu_v6: Optional[
            Union[
                OneOfMtuV6OptionsDef1,
                OneOfMtuV6OptionsDef2,
                OneOfMtuV6OptionsDef3,
            ]
        ]
        tcp_mss_adjust_v6: Optional[
            Union[
                OneOfTcpMssAdjustV6OptionsDef1,
                OneOfTcpMssAdjustV6OptionsDef2,
                OneOfTcpMssAdjustV6OptionsDef3,
            ]
        ]
        tracker: Optional[
            Union[
                OneOfTrackerOptionsDef1,
                OneOfTrackerOptionsDef2,
                OneOfTrackerOptionsDef3,
            ]
        ]
        tunnel_destination_v6: Optional[
            Union[
                OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
            ]
        ]
        tunnel_mode: Optional[
            Union[OneOfTunnelModeOptionsDef1, OneOfTunnelModeOptionsDef2]
        ]
        tunnel_route_via: Optional[
            Union[
                OneOfTunnelRouteViaOptionsDef1,
                OneOfTunnelRouteViaOptionsDef2,
                OneOfTunnelRouteViaOptionsDef3,
            ]
        ]
        tunnel_source: Optional[Ipv4AddressAndMaskDef]
        tunnel_source_v6: Optional[
            Union[
                OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
            ]
        ]


    class Data3:
        application: Union[
            OneOfApplicationOptionsDef1, OneOfApplicationOptionsDef2
        ]
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        dpd_interval: Union[
            OneOfDpdIntervalOptionsDef1,
            OneOfDpdIntervalOptionsDef2,
            OneOfDpdIntervalOptionsDef3,
        ]
        dpd_retries: Union[
            OneOfDpdRetriesOptionsDef1,
            OneOfDpdRetriesOptionsDef2,
            OneOfDpdRetriesOptionsDef3,
        ]
        if_name: Union[OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2]
        ike_ciphersuite: Union[
            OneOfIkeCiphersuiteOptionsDef1,
            OneOfIkeCiphersuiteOptionsDef2,
            OneOfIkeCiphersuiteOptionsDef3,
        ]
        ike_group: Union[
            OneOfIkeGroupOptionsDef1,
            OneOfIkeGroupOptionsDef2,
            OneOfIkeGroupOptionsDef3,
        ]
        ike_local_id: Union[
            OneOfIkeLocalIdOptionsDef1,
            OneOfIkeLocalIdOptionsDef2,
            OneOfIkeLocalIdOptionsDef3,
        ]
        ike_rekey_interval: Union[
            OneOfIkeRekeyIntervalOptionsDef1,
            OneOfIkeRekeyIntervalOptionsDef2,
            OneOfIkeRekeyIntervalOptionsDef3,
        ]
        ike_remote_id: Union[
            OneOfIkeRemoteIdOptionsDef1,
            OneOfIkeRemoteIdOptionsDef2,
            OneOfIkeRemoteIdOptionsDef3,
        ]
        ike_version: Union[
            OneOfIkeVersionOptionsDef1, OneOfIkeVersionOptionsDef2
        ]
        ipsec_ciphersuite: Union[
            OneOfIpsecCiphersuiteOptionsDef1,
            OneOfIpsecCiphersuiteOptionsDef2,
            OneOfIpsecCiphersuiteOptionsDef3,
        ]
        ipsec_rekey_interval: Union[
            OneOfIpsecRekeyIntervalOptionsDef1,
            OneOfIpsecRekeyIntervalOptionsDef2,
            OneOfIpsecRekeyIntervalOptionsDef3,
        ]
        ipsec_replay_window: Union[
            OneOfIpsecReplayWindowOptionsDef1,
            OneOfIpsecReplayWindowOptionsDef2,
            OneOfIpsecReplayWindowOptionsDef3,
        ]
        ipv6_address: Union[
            OneOfIpv6PrefixOptionsDef1, OneOfIpv6PrefixOptionsDef2
        ]
        mtu_v6: Union[
            OneOfMtuV6OptionsDef1,
            OneOfMtuV6OptionsDef2,
            OneOfMtuV6OptionsDef3,
        ]
        perfect_forward_secrecy: Union[
            OneOfPerfectForwardSecrecyOptionsDef1,
            OneOfPerfectForwardSecrecyOptionsDef2,
            OneOfPerfectForwardSecrecyOptionsDef3,
        ]
        pre_shared_secret: Union[
            OneOfPreSharedSecretOptionsDef1,
            OneOfPreSharedSecretOptionsDef2,
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tcp_mss_adjust_v6: Union[
            OneOfTcpMssAdjustV6OptionsDef1,
            OneOfTcpMssAdjustV6OptionsDef2,
            OneOfTcpMssAdjustV6OptionsDef3,
        ]
        tunnel_destination_v6: Union[
            OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
        ]
        tunnel_source_v6: Union[
            OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
        ]
        address: Optional[Ipv4AddressAndMaskDef]
        clear_dont_fragment: Optional[
            Union[
                OneOfClearDontFragmentOptionsDef1,
                OneOfClearDontFragmentOptionsDef2,
                OneOfClearDontFragmentOptionsDef3,
            ]
        ]
        ike_mode: Optional[
            Union[
                OneOfIkeModeOptionsDef1,
                OneOfIkeModeOptionsDef2,
                OneOfIkeModeOptionsDef3,
            ]
        ]
        mtu: Optional[
            Union[
                OneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                OneOfMtuOptionsDef3,
            ]
        ]
        tcp_mss_adjust: Optional[
            Union[
                OneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]
        tracker: Optional[
            Union[
                OneOfTrackerOptionsDef1,
                OneOfTrackerOptionsDef2,
                OneOfTrackerOptionsDef3,
            ]
        ]
        tunnel_destination: Optional[Ipv4AddressAndMaskDef]
        tunnel_mode: Optional[
            Union[OneOfTunnelModeOptionsDef1, OneOfTunnelModeOptionsDef2]
        ]
        tunnel_route_via: Optional[
            Union[
                OneOfTunnelRouteViaOptionsDef1,
                OneOfTunnelRouteViaOptionsDef2,
                OneOfTunnelRouteViaOptionsDef3,
            ]
        ]
        tunnel_source: Optional[Ipv4AddressAndMaskDef]
        tunnel_source_interface: Optional[
            Union[
                OneOfTunnelSourceInterfaceOptionsDef1,
                OneOfTunnelSourceInterfaceOptionsDef2,
            ]
        ]


    class Data4:
        application: Union[
            OneOfApplicationOptionsDef1, OneOfApplicationOptionsDef2
        ]
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        dpd_interval: Union[
            OneOfDpdIntervalOptionsDef1,
            OneOfDpdIntervalOptionsDef2,
            OneOfDpdIntervalOptionsDef3,
        ]
        dpd_retries: Union[
            OneOfDpdRetriesOptionsDef1,
            OneOfDpdRetriesOptionsDef2,
            OneOfDpdRetriesOptionsDef3,
        ]
        if_name: Union[OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2]
        ike_ciphersuite: Union[
            OneOfIkeCiphersuiteOptionsDef1,
            OneOfIkeCiphersuiteOptionsDef2,
            OneOfIkeCiphersuiteOptionsDef3,
        ]
        ike_group: Union[
            OneOfIkeGroupOptionsDef1,
            OneOfIkeGroupOptionsDef2,
            OneOfIkeGroupOptionsDef3,
        ]
        ike_local_id: Union[
            OneOfIkeLocalIdOptionsDef1,
            OneOfIkeLocalIdOptionsDef2,
            OneOfIkeLocalIdOptionsDef3,
        ]
        ike_rekey_interval: Union[
            OneOfIkeRekeyIntervalOptionsDef1,
            OneOfIkeRekeyIntervalOptionsDef2,
            OneOfIkeRekeyIntervalOptionsDef3,
        ]
        ike_remote_id: Union[
            OneOfIkeRemoteIdOptionsDef1,
            OneOfIkeRemoteIdOptionsDef2,
            OneOfIkeRemoteIdOptionsDef3,
        ]
        ike_version: Union[
            OneOfIkeVersionOptionsDef1, OneOfIkeVersionOptionsDef2
        ]
        ipsec_ciphersuite: Union[
            OneOfIpsecCiphersuiteOptionsDef1,
            OneOfIpsecCiphersuiteOptionsDef2,
            OneOfIpsecCiphersuiteOptionsDef3,
        ]
        ipsec_rekey_interval: Union[
            OneOfIpsecRekeyIntervalOptionsDef1,
            OneOfIpsecRekeyIntervalOptionsDef2,
            OneOfIpsecRekeyIntervalOptionsDef3,
        ]
        ipsec_replay_window: Union[
            OneOfIpsecReplayWindowOptionsDef1,
            OneOfIpsecReplayWindowOptionsDef2,
            OneOfIpsecReplayWindowOptionsDef3,
        ]
        ipv6_address: Union[
            OneOfIpv6PrefixOptionsDef1, OneOfIpv6PrefixOptionsDef2
        ]
        mtu_v6: Union[
            OneOfMtuV6OptionsDef1,
            OneOfMtuV6OptionsDef2,
            OneOfMtuV6OptionsDef3,
        ]
        perfect_forward_secrecy: Union[
            OneOfPerfectForwardSecrecyOptionsDef1,
            OneOfPerfectForwardSecrecyOptionsDef2,
            OneOfPerfectForwardSecrecyOptionsDef3,
        ]
        pre_shared_secret: Union[
            OneOfPreSharedSecretOptionsDef1,
            OneOfPreSharedSecretOptionsDef2,
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tcp_mss_adjust_v6: Union[
            OneOfTcpMssAdjustV6OptionsDef1,
            OneOfTcpMssAdjustV6OptionsDef2,
            OneOfTcpMssAdjustV6OptionsDef3,
        ]
        tunnel_destination_v6: Union[
            OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
        ]
        tunnel_source_interface: Union[
            OneOfTunnelSourceInterfaceOptionsDef1,
            OneOfTunnelSourceInterfaceOptionsDef2,
        ]
        address: Optional[Ipv4AddressAndMaskDef]
        clear_dont_fragment: Optional[
            Union[
                OneOfClearDontFragmentOptionsDef1,
                OneOfClearDontFragmentOptionsDef2,
                OneOfClearDontFragmentOptionsDef3,
            ]
        ]
        ike_mode: Optional[
            Union[
                OneOfIkeModeOptionsDef1,
                OneOfIkeModeOptionsDef2,
                OneOfIkeModeOptionsDef3,
            ]
        ]
        mtu: Optional[
            Union[
                OneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                OneOfMtuOptionsDef3,
            ]
        ]
        tcp_mss_adjust: Optional[
            Union[
                OneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]
        tracker: Optional[
            Union[
                OneOfTrackerOptionsDef1,
                OneOfTrackerOptionsDef2,
                OneOfTrackerOptionsDef3,
            ]
        ]
        tunnel_destination: Optional[Ipv4AddressAndMaskDef]
        tunnel_mode: Optional[
            Union[OneOfTunnelModeOptionsDef1, OneOfTunnelModeOptionsDef2]
        ]
        tunnel_route_via: Optional[
            Union[
                OneOfTunnelRouteViaOptionsDef1,
                OneOfTunnelRouteViaOptionsDef2,
                OneOfTunnelRouteViaOptionsDef3,
            ]
        ]
        tunnel_source: Optional[Ipv4AddressAndMaskDef]
        tunnel_source_v6: Optional[
            Union[
                OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
            ]
        ]


    class Data5:
        application: Union[
            OneOfApplicationOptionsDef1, OneOfApplicationOptionsDef2
        ]
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        dpd_interval: Union[
            OneOfDpdIntervalOptionsDef1,
            OneOfDpdIntervalOptionsDef2,
            OneOfDpdIntervalOptionsDef3,
        ]
        dpd_retries: Union[
            OneOfDpdRetriesOptionsDef1,
            OneOfDpdRetriesOptionsDef2,
            OneOfDpdRetriesOptionsDef3,
        ]
        if_name: Union[OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2]
        ike_ciphersuite: Union[
            OneOfIkeCiphersuiteOptionsDef1,
            OneOfIkeCiphersuiteOptionsDef2,
            OneOfIkeCiphersuiteOptionsDef3,
        ]
        ike_group: Union[
            OneOfIkeGroupOptionsDef1,
            OneOfIkeGroupOptionsDef2,
            OneOfIkeGroupOptionsDef3,
        ]
        ike_local_id: Union[
            OneOfIkeLocalIdOptionsDef1,
            OneOfIkeLocalIdOptionsDef2,
            OneOfIkeLocalIdOptionsDef3,
        ]
        ike_rekey_interval: Union[
            OneOfIkeRekeyIntervalOptionsDef1,
            OneOfIkeRekeyIntervalOptionsDef2,
            OneOfIkeRekeyIntervalOptionsDef3,
        ]
        ike_remote_id: Union[
            OneOfIkeRemoteIdOptionsDef1,
            OneOfIkeRemoteIdOptionsDef2,
            OneOfIkeRemoteIdOptionsDef3,
        ]
        ike_version: Union[
            OneOfIkeVersionOptionsDef1, OneOfIkeVersionOptionsDef2
        ]
        ipsec_ciphersuite: Union[
            OneOfIpsecCiphersuiteOptionsDef1,
            OneOfIpsecCiphersuiteOptionsDef2,
            OneOfIpsecCiphersuiteOptionsDef3,
        ]
        ipsec_rekey_interval: Union[
            OneOfIpsecRekeyIntervalOptionsDef1,
            OneOfIpsecRekeyIntervalOptionsDef2,
            OneOfIpsecRekeyIntervalOptionsDef3,
        ]
        ipsec_replay_window: Union[
            OneOfIpsecReplayWindowOptionsDef1,
            OneOfIpsecReplayWindowOptionsDef2,
            OneOfIpsecReplayWindowOptionsDef3,
        ]
        ipv6_address: Union[
            OneOfIpv6PrefixOptionsDef1, OneOfIpv6PrefixOptionsDef2
        ]
        mtu_v6: Union[
            OneOfMtuV6OptionsDef1,
            OneOfMtuV6OptionsDef2,
            OneOfMtuV6OptionsDef3,
        ]
        perfect_forward_secrecy: Union[
            OneOfPerfectForwardSecrecyOptionsDef1,
            OneOfPerfectForwardSecrecyOptionsDef2,
            OneOfPerfectForwardSecrecyOptionsDef3,
        ]
        pre_shared_secret: Union[
            OneOfPreSharedSecretOptionsDef1,
            OneOfPreSharedSecretOptionsDef2,
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tcp_mss_adjust_v6: Union[
            OneOfTcpMssAdjustV6OptionsDef1,
            OneOfTcpMssAdjustV6OptionsDef2,
            OneOfTcpMssAdjustV6OptionsDef3,
        ]
        tunnel_destination: Ipv4AddressAndMaskDef
        tunnel_source: Ipv4AddressAndMaskDef
        address: Optional[Ipv4AddressAndMaskDef]
        clear_dont_fragment: Optional[
            Union[
                OneOfClearDontFragmentOptionsDef1,
                OneOfClearDontFragmentOptionsDef2,
                OneOfClearDontFragmentOptionsDef3,
            ]
        ]
        ike_mode: Optional[
            Union[
                OneOfIkeModeOptionsDef1,
                OneOfIkeModeOptionsDef2,
                OneOfIkeModeOptionsDef3,
            ]
        ]
        mtu: Optional[
            Union[
                OneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                OneOfMtuOptionsDef3,
            ]
        ]
        tcp_mss_adjust: Optional[
            Union[
                OneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]
        tracker: Optional[
            Union[
                OneOfTrackerOptionsDef1,
                OneOfTrackerOptionsDef2,
                OneOfTrackerOptionsDef3,
            ]
        ]
        tunnel_destination_v6: Optional[
            Union[
                OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
            ]
        ]
        tunnel_mode: Optional[
            Union[OneOfTunnelModeOptionsDef1, OneOfTunnelModeOptionsDef2]
        ]
        tunnel_route_via: Optional[
            Union[
                OneOfTunnelRouteViaOptionsDef1,
                OneOfTunnelRouteViaOptionsDef2,
                OneOfTunnelRouteViaOptionsDef3,
            ]
        ]
        tunnel_source_interface: Optional[
            Union[
                OneOfTunnelSourceInterfaceOptionsDef1,
                OneOfTunnelSourceInterfaceOptionsDef2,
            ]
        ]
        tunnel_source_v6: Optional[
            Union[
                OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
            ]
        ]


    class Data6:
        application: Union[
            OneOfApplicationOptionsDef1, OneOfApplicationOptionsDef2
        ]
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        dpd_interval: Union[
            OneOfDpdIntervalOptionsDef1,
            OneOfDpdIntervalOptionsDef2,
            OneOfDpdIntervalOptionsDef3,
        ]
        dpd_retries: Union[
            OneOfDpdRetriesOptionsDef1,
            OneOfDpdRetriesOptionsDef2,
            OneOfDpdRetriesOptionsDef3,
        ]
        if_name: Union[OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2]
        ike_ciphersuite: Union[
            OneOfIkeCiphersuiteOptionsDef1,
            OneOfIkeCiphersuiteOptionsDef2,
            OneOfIkeCiphersuiteOptionsDef3,
        ]
        ike_group: Union[
            OneOfIkeGroupOptionsDef1,
            OneOfIkeGroupOptionsDef2,
            OneOfIkeGroupOptionsDef3,
        ]
        ike_local_id: Union[
            OneOfIkeLocalIdOptionsDef1,
            OneOfIkeLocalIdOptionsDef2,
            OneOfIkeLocalIdOptionsDef3,
        ]
        ike_rekey_interval: Union[
            OneOfIkeRekeyIntervalOptionsDef1,
            OneOfIkeRekeyIntervalOptionsDef2,
            OneOfIkeRekeyIntervalOptionsDef3,
        ]
        ike_remote_id: Union[
            OneOfIkeRemoteIdOptionsDef1,
            OneOfIkeRemoteIdOptionsDef2,
            OneOfIkeRemoteIdOptionsDef3,
        ]
        ike_version: Union[
            OneOfIkeVersionOptionsDef1, OneOfIkeVersionOptionsDef2
        ]
        ipsec_ciphersuite: Union[
            OneOfIpsecCiphersuiteOptionsDef1,
            OneOfIpsecCiphersuiteOptionsDef2,
            OneOfIpsecCiphersuiteOptionsDef3,
        ]
        ipsec_rekey_interval: Union[
            OneOfIpsecRekeyIntervalOptionsDef1,
            OneOfIpsecRekeyIntervalOptionsDef2,
            OneOfIpsecRekeyIntervalOptionsDef3,
        ]
        ipsec_replay_window: Union[
            OneOfIpsecReplayWindowOptionsDef1,
            OneOfIpsecReplayWindowOptionsDef2,
            OneOfIpsecReplayWindowOptionsDef3,
        ]
        ipv6_address: Union[
            OneOfIpv6PrefixOptionsDef1, OneOfIpv6PrefixOptionsDef2
        ]
        mtu_v6: Union[
            OneOfMtuV6OptionsDef1,
            OneOfMtuV6OptionsDef2,
            OneOfMtuV6OptionsDef3,
        ]
        perfect_forward_secrecy: Union[
            OneOfPerfectForwardSecrecyOptionsDef1,
            OneOfPerfectForwardSecrecyOptionsDef2,
            OneOfPerfectForwardSecrecyOptionsDef3,
        ]
        pre_shared_secret: Union[
            OneOfPreSharedSecretOptionsDef1,
            OneOfPreSharedSecretOptionsDef2,
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tcp_mss_adjust_v6: Union[
            OneOfTcpMssAdjustV6OptionsDef1,
            OneOfTcpMssAdjustV6OptionsDef2,
            OneOfTcpMssAdjustV6OptionsDef3,
        ]
        tunnel_destination: Ipv4AddressAndMaskDef
        tunnel_source_interface: Union[
            OneOfTunnelSourceInterfaceOptionsDef1,
            OneOfTunnelSourceInterfaceOptionsDef2,
        ]
        address: Optional[Ipv4AddressAndMaskDef]
        clear_dont_fragment: Optional[
            Union[
                OneOfClearDontFragmentOptionsDef1,
                OneOfClearDontFragmentOptionsDef2,
                OneOfClearDontFragmentOptionsDef3,
            ]
        ]
        ike_mode: Optional[
            Union[
                OneOfIkeModeOptionsDef1,
                OneOfIkeModeOptionsDef2,
                OneOfIkeModeOptionsDef3,
            ]
        ]
        mtu: Optional[
            Union[
                OneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                OneOfMtuOptionsDef3,
            ]
        ]
        tcp_mss_adjust: Optional[
            Union[
                OneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]
        tracker: Optional[
            Union[
                OneOfTrackerOptionsDef1,
                OneOfTrackerOptionsDef2,
                OneOfTrackerOptionsDef3,
            ]
        ]
        tunnel_destination_v6: Optional[
            Union[
                OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
            ]
        ]
        tunnel_mode: Optional[
            Union[OneOfTunnelModeOptionsDef1, OneOfTunnelModeOptionsDef2]
        ]
        tunnel_route_via: Optional[
            Union[
                OneOfTunnelRouteViaOptionsDef1,
                OneOfTunnelRouteViaOptionsDef2,
                OneOfTunnelRouteViaOptionsDef3,
            ]
        ]
        tunnel_source: Optional[Ipv4AddressAndMaskDef]
        tunnel_source_v6: Optional[
            Union[
                OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
            ]
        ]


    class Payload:
        """
        Lan VPN Interface Ipsec profile parcel schema for POST request
        """

        data: Union[Data1, Data2, Data3, Data4, Data5, Data6]
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
        # Lan VPN Interface Ipsec profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanServiceLanVpnInterfaceIpsecPayload:
        data: Optional[List[Data]]


    class CreateIpSecProfileParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateIpSecProfileParcelPostRequest:
        """
        Lan VPN Interface Ipsec profile parcel schema for POST request
        """

        data: Union[Data1, Data2, Data3, Data4, Data5, Data6]
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanServiceLanVpnInterfaceIpsecPayload:
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
        # Lan VPN Interface Ipsec profile parcel schema for POST request
        payload: Optional[Payload]


    class EditProfileParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditProfileParcelPutRequest:
        """
        Lan VPN Interface Ipsec profile parcel schema for POST request
        """

        data: Union[Data1, Data2, Data3, Data4, Data5, Data6]
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


