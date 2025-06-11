======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

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

    DefaultShutdownDef = Literal[False, True]

    BooleanFalseDef = Literal[False]

    TunnelModeDef = Literal["ipv4", "ipv6"]

    DefaultTunnelModeDef = Literal["ipv4"]

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

    ApplicationDef = Literal["none", "sig"]


    class OneOfIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIfNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


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


    class OneOfIpV4AddressOptionsWithDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsWithDefault2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfIpV4AddressOptionsWithDefault3:
        option_type: DefaultOptionTypeDef


    class OneOfIpV4SubnetMaskOptionsWithDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4SubnetMaskOptionsWithDefault2:
        option_type: GlobalOptionTypeDef
        value: (
            Ipv4SubnetMaskDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfIpV4SubnetMaskOptionsWithDefault3:
        option_type: DefaultOptionTypeDef


    class Ipv4AddressAndMaskWithDefault:
        address: Optional[
            Union[
                OneOfIpV4AddressOptionsWithDefault1,
                OneOfIpV4AddressOptionsWithDefault2,
                OneOfIpV4AddressOptionsWithDefault3,
            ]
        ]
        mask: Optional[
            Union[
                OneOfIpV4SubnetMaskOptionsWithDefault1,
                OneOfIpV4SubnetMaskOptionsWithDefault2,
                OneOfIpV4SubnetMaskOptionsWithDefault3,
            ]
        ]


    class OneOfIpv6PrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6PrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6PrefixOptionsDef3:
        option_type: DefaultOptionTypeDef


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
        value: Optional[DefaultShutdownDef]


    class OneOfTunnelProtectionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfTunnelProtectionOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfTunnelModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TunnelModeDef


    class OneOfTunnelModeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: DefaultTunnelModeDef  # pytype: disable=annotation-type-mismatch


    class OneOfTunnelSourceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTunnelSourceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


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


    class SourceIp:
        tunnel_source: Union[
            OneOfTunnelSourceOptionsDef1, OneOfTunnelSourceOptionsDef2
        ]
        tunnel_route_via: Optional[
            Union[
                OneOfTunnelRouteViaOptionsDef1,
                OneOfTunnelRouteViaOptionsDef2,
                OneOfTunnelRouteViaOptionsDef3,
            ]
        ]


    class TunnelSourceType1:
        source_ip: SourceIp


    class OneOfTunnelSourceInterfaceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTunnelSourceInterfaceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class SourceNotLoopback:
        tunnel_source_interface: Union[
            OneOfTunnelSourceInterfaceOptionsDef1,
            OneOfTunnelSourceInterfaceOptionsDef2,
        ]
        tunnel_route_via: Optional[
            Union[
                OneOfTunnelRouteViaOptionsDef1,
                OneOfTunnelRouteViaOptionsDef2,
                OneOfTunnelRouteViaOptionsDef3,
            ]
        ]


    class TunnelSourceType2:
        source_not_loopback: SourceNotLoopback


    class SourceLoopback:
        tunnel_source_interface: Union[
            OneOfTunnelSourceInterfaceOptionsDef1,
            OneOfTunnelSourceInterfaceOptionsDef2,
        ]
        tunnel_route_via: Optional[
            Union[
                OneOfTunnelRouteViaOptionsDef1,
                OneOfTunnelRouteViaOptionsDef2,
                OneOfTunnelRouteViaOptionsDef3,
            ]
        ]


    class TunnelSourceType3:
        source_loopback: SourceLoopback


    class OneOfIpv6AddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6AddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class SourceIpv6:
        tunnel_source_v6: Union[
            OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
        ]
        tunnel_route_via: Optional[
            Union[
                OneOfTunnelRouteViaOptionsDef1,
                OneOfTunnelRouteViaOptionsDef2,
                OneOfTunnelRouteViaOptionsDef3,
            ]
        ]


    class TunnelSourceType4:
        source_ipv6: SourceIpv6


    class OneOfTunnelDestinationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTunnelDestinationOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


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
        value: Optional[BooleanFalseDef]


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


    class OneOfPreSharedSecretOptionsDef3:
        option_type: DefaultOptionTypeDef


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


    class Basic1:
        if_name: Union[OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2]
        tunnel_destination: Union[
            OneOfTunnelDestinationOptionsDef1,
            OneOfTunnelDestinationOptionsDef2,
        ]
        address: Optional[Ipv4AddressAndMaskWithDefault]
        clear_dont_fragment: Optional[
            Union[
                OneOfClearDontFragmentOptionsDef1,
                OneOfClearDontFragmentOptionsDef2,
                OneOfClearDontFragmentOptionsDef3,
            ]
        ]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]
        dpd_interval: Optional[
            Union[
                OneOfDpdIntervalOptionsDef1,
                OneOfDpdIntervalOptionsDef2,
                OneOfDpdIntervalOptionsDef3,
            ]
        ]
        dpd_retries: Optional[
            Union[
                OneOfDpdRetriesOptionsDef1,
                OneOfDpdRetriesOptionsDef2,
                OneOfDpdRetriesOptionsDef3,
            ]
        ]
        ike_ciphersuite: Optional[
            Union[
                OneOfIkeCiphersuiteOptionsDef1,
                OneOfIkeCiphersuiteOptionsDef2,
                OneOfIkeCiphersuiteOptionsDef3,
            ]
        ]
        ike_group: Optional[
            Union[
                OneOfIkeGroupOptionsDef1,
                OneOfIkeGroupOptionsDef2,
                OneOfIkeGroupOptionsDef3,
            ]
        ]
        ike_local_id: Optional[
            Union[
                OneOfIkeLocalIdOptionsDef1,
                OneOfIkeLocalIdOptionsDef2,
                OneOfIkeLocalIdOptionsDef3,
            ]
        ]
        ike_mode: Optional[
            Union[
                OneOfIkeModeOptionsDef1,
                OneOfIkeModeOptionsDef2,
                OneOfIkeModeOptionsDef3,
            ]
        ]
        ike_rekey_interval: Optional[
            Union[
                OneOfIkeRekeyIntervalOptionsDef1,
                OneOfIkeRekeyIntervalOptionsDef2,
                OneOfIkeRekeyIntervalOptionsDef3,
            ]
        ]
        ike_remote_id: Optional[
            Union[
                OneOfIkeRemoteIdOptionsDef1,
                OneOfIkeRemoteIdOptionsDef2,
                OneOfIkeRemoteIdOptionsDef3,
            ]
        ]
        ike_version: Optional[
            Union[OneOfIkeVersionOptionsDef1, OneOfIkeVersionOptionsDef2]
        ]
        ipsec_ciphersuite: Optional[
            Union[
                OneOfIpsecCiphersuiteOptionsDef1,
                OneOfIpsecCiphersuiteOptionsDef2,
                OneOfIpsecCiphersuiteOptionsDef3,
            ]
        ]
        ipsec_rekey_interval: Optional[
            Union[
                OneOfIpsecRekeyIntervalOptionsDef1,
                OneOfIpsecRekeyIntervalOptionsDef2,
                OneOfIpsecRekeyIntervalOptionsDef3,
            ]
        ]
        ipsec_replay_window: Optional[
            Union[
                OneOfIpsecReplayWindowOptionsDef1,
                OneOfIpsecReplayWindowOptionsDef2,
                OneOfIpsecReplayWindowOptionsDef3,
            ]
        ]
        ipv6_address: Optional[
            Union[
                OneOfIpv6PrefixOptionsDef1,
                OneOfIpv6PrefixOptionsDef2,
                OneOfIpv6PrefixOptionsDef3,
            ]
        ]
        mtu: Optional[
            Union[
                OneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                OneOfMtuOptionsDef3,
            ]
        ]
        mtu_v6: Optional[
            Union[
                OneOfMtuV6OptionsDef1,
                OneOfMtuV6OptionsDef2,
                OneOfMtuV6OptionsDef3,
            ]
        ]
        perfect_forward_secrecy: Optional[
            Union[
                OneOfPerfectForwardSecrecyOptionsDef1,
                OneOfPerfectForwardSecrecyOptionsDef2,
                OneOfPerfectForwardSecrecyOptionsDef3,
            ]
        ]
        pre_shared_secret: Optional[
            Union[
                OneOfPreSharedSecretOptionsDef1,
                OneOfPreSharedSecretOptionsDef2,
                OneOfPreSharedSecretOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfShutdownOptionsDef1,
                OneOfShutdownOptionsDef2,
                OneOfShutdownOptionsDef3,
            ]
        ]
        tcp_mss_adjust: Optional[
            Union[
                OneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]
        tcp_mss_adjust_v6: Optional[
            Union[
                OneOfTcpMssAdjustV6OptionsDef1,
                OneOfTcpMssAdjustV6OptionsDef2,
                OneOfTcpMssAdjustV6OptionsDef3,
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
        tunnel_protection: Optional[
            Union[
                OneOfTunnelProtectionOptionsDef1,
                OneOfTunnelProtectionOptionsDef2,
            ]
        ]
        tunnel_source_type: Optional[
            Union[
                TunnelSourceType1,
                TunnelSourceType2,
                TunnelSourceType3,
                TunnelSourceType4,
            ]
        ]


    class Basic2:
        if_name: Union[OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2]
        tunnel_destination_v6: Union[
            OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
        ]
        address: Optional[Ipv4AddressAndMaskWithDefault]
        clear_dont_fragment: Optional[
            Union[
                OneOfClearDontFragmentOptionsDef1,
                OneOfClearDontFragmentOptionsDef2,
                OneOfClearDontFragmentOptionsDef3,
            ]
        ]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]
        dpd_interval: Optional[
            Union[
                OneOfDpdIntervalOptionsDef1,
                OneOfDpdIntervalOptionsDef2,
                OneOfDpdIntervalOptionsDef3,
            ]
        ]
        dpd_retries: Optional[
            Union[
                OneOfDpdRetriesOptionsDef1,
                OneOfDpdRetriesOptionsDef2,
                OneOfDpdRetriesOptionsDef3,
            ]
        ]
        ike_ciphersuite: Optional[
            Union[
                OneOfIkeCiphersuiteOptionsDef1,
                OneOfIkeCiphersuiteOptionsDef2,
                OneOfIkeCiphersuiteOptionsDef3,
            ]
        ]
        ike_group: Optional[
            Union[
                OneOfIkeGroupOptionsDef1,
                OneOfIkeGroupOptionsDef2,
                OneOfIkeGroupOptionsDef3,
            ]
        ]
        ike_local_id: Optional[
            Union[
                OneOfIkeLocalIdOptionsDef1,
                OneOfIkeLocalIdOptionsDef2,
                OneOfIkeLocalIdOptionsDef3,
            ]
        ]
        ike_mode: Optional[
            Union[
                OneOfIkeModeOptionsDef1,
                OneOfIkeModeOptionsDef2,
                OneOfIkeModeOptionsDef3,
            ]
        ]
        ike_rekey_interval: Optional[
            Union[
                OneOfIkeRekeyIntervalOptionsDef1,
                OneOfIkeRekeyIntervalOptionsDef2,
                OneOfIkeRekeyIntervalOptionsDef3,
            ]
        ]
        ike_remote_id: Optional[
            Union[
                OneOfIkeRemoteIdOptionsDef1,
                OneOfIkeRemoteIdOptionsDef2,
                OneOfIkeRemoteIdOptionsDef3,
            ]
        ]
        ike_version: Optional[
            Union[OneOfIkeVersionOptionsDef1, OneOfIkeVersionOptionsDef2]
        ]
        ipsec_ciphersuite: Optional[
            Union[
                OneOfIpsecCiphersuiteOptionsDef1,
                OneOfIpsecCiphersuiteOptionsDef2,
                OneOfIpsecCiphersuiteOptionsDef3,
            ]
        ]
        ipsec_rekey_interval: Optional[
            Union[
                OneOfIpsecRekeyIntervalOptionsDef1,
                OneOfIpsecRekeyIntervalOptionsDef2,
                OneOfIpsecRekeyIntervalOptionsDef3,
            ]
        ]
        ipsec_replay_window: Optional[
            Union[
                OneOfIpsecReplayWindowOptionsDef1,
                OneOfIpsecReplayWindowOptionsDef2,
                OneOfIpsecReplayWindowOptionsDef3,
            ]
        ]
        ipv6_address: Optional[
            Union[
                OneOfIpv6PrefixOptionsDef1,
                OneOfIpv6PrefixOptionsDef2,
                OneOfIpv6PrefixOptionsDef3,
            ]
        ]
        mtu: Optional[
            Union[
                OneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                OneOfMtuOptionsDef3,
            ]
        ]
        mtu_v6: Optional[
            Union[
                OneOfMtuV6OptionsDef1,
                OneOfMtuV6OptionsDef2,
                OneOfMtuV6OptionsDef3,
            ]
        ]
        perfect_forward_secrecy: Optional[
            Union[
                OneOfPerfectForwardSecrecyOptionsDef1,
                OneOfPerfectForwardSecrecyOptionsDef2,
                OneOfPerfectForwardSecrecyOptionsDef3,
            ]
        ]
        pre_shared_secret: Optional[
            Union[
                OneOfPreSharedSecretOptionsDef1,
                OneOfPreSharedSecretOptionsDef2,
                OneOfPreSharedSecretOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfShutdownOptionsDef1,
                OneOfShutdownOptionsDef2,
                OneOfShutdownOptionsDef3,
            ]
        ]
        tcp_mss_adjust: Optional[
            Union[
                OneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]
        tcp_mss_adjust_v6: Optional[
            Union[
                OneOfTcpMssAdjustV6OptionsDef1,
                OneOfTcpMssAdjustV6OptionsDef2,
                OneOfTcpMssAdjustV6OptionsDef3,
            ]
        ]
        tunnel_destination: Optional[
            Union[
                OneOfTunnelDestinationOptionsDef1,
                OneOfTunnelDestinationOptionsDef2,
            ]
        ]
        tunnel_mode: Optional[
            Union[OneOfTunnelModeOptionsDef1, OneOfTunnelModeOptionsDef2]
        ]
        tunnel_protection: Optional[
            Union[
                OneOfTunnelProtectionOptionsDef1,
                OneOfTunnelProtectionOptionsDef2,
            ]
        ]
        tunnel_source_type: Optional[
            Union[
                TunnelSourceType1,
                TunnelSourceType2,
                TunnelSourceType3,
                TunnelSourceType4,
            ]
        ]


    class OneOfApplicationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ApplicationDef


    class OneOfApplicationOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Advanced:
        """
        advanced
        """

        application: Optional[
            Union[
                OneOfApplicationOptionsDef1, OneOfApplicationOptionsDef2
            ]
        ]


    class GreData:
        # basic configuration
        basic: Union[Basic1, Basic2]
        advanced: Optional[Advanced]


    class Payload:
        """
        LAN VPN Interface GRE schema for request
        """

        data: GreData
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
        # LAN VPN Interface GRE schema for request
        payload: Optional[Payload]


    class GetListSdwanServiceLanVpnInterfaceGrePayload:
        data: Optional[List[Data]]


    class CreateLanVpnInterfaceGreForServicePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class InterfaceGreData:
        # basic configuration
        basic: Union[Basic1, Basic2]
        advanced: Optional[Advanced]


    class CreateLanVpnInterfaceGreForServicePostRequest:
        """
        LAN VPN Interface GRE schema for request
        """

        data: InterfaceGreData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanServiceLanVpnInterfaceGrePayload:
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
        # LAN VPN Interface GRE schema for request
        payload: Optional[Payload]


    class EditLanVpnInterfaceGreForServicePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class VpnInterfaceGreData:
        # basic configuration
        basic: Union[Basic1, Basic2]
        advanced: Optional[Advanced]


    class EditLanVpnInterfaceGreForServicePutRequest:
        """
        LAN VPN Interface GRE schema for request
        """

        data: VpnInterfaceGreData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


