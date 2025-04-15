======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    TunnelModeDef = Literal["ipv4", "ipv4-v6overlay", "ipv6"]

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

    IkeV1ModeDef = Literal["aggressive", "main"]

    DefaultIkeV1ModeDef = Literal["main"]

    IkeV1CipherSuiteDef = Literal[
        "aes128-cbc-sha1",
        "aes128-cbc-sha2",
        "aes256-cbc-sha1",
        "aes256-cbc-sha2",
    ]

    DefaultIkeV1CipherSuiteDef = Literal["aes256-cbc-sha1"]

    IkeGroupDef = Literal["14", "15", "16", "19", "20", "21"]

    DefaultIkeGroupDef = Literal["16"]

    IpsecCipherSuiteDef = Literal[
        "aes256-cbc-sha1",
        "aes256-cbc-sha256",
        "aes256-cbc-sha384",
        "aes256-cbc-sha512",
        "aes256-gcm",
    ]

    DefaultIpsecCipherSuiteDef = Literal["aes256-gcm"]

    PerfectForwardSecrecyDef = Literal[
        "group-14",
        "group-15",
        "group-16",
        "group-19",
        "group-20",
        "group-21",
        "none",
    ]

    DefaultPerfectForwardSecrecyDef = Literal["group-16"]


    class OneOfIpsecIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpsecIfNameOptionsDef2:
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


    class OneOfTunnelModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: TunnelModeDef


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


    class TunnelSource1:
        source_ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]


    class OneOfTunnelSourceInterfaceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTunnelSourceInterfaceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class TunnelSource2:
        source_interface: Union[
            OneOfTunnelSourceInterfaceOptionsDef1,
            OneOfTunnelSourceInterfaceOptionsDef2,
        ]


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


    class TunnelConfig4O4:
        """
        Tunnel Config for Mode ipv4
        """

        clear_dont_fragment: Union[
            OneOfClearDontFragmentOptionsDef1,
            OneOfClearDontFragmentOptionsDef2,
            OneOfClearDontFragmentOptionsDef3,
        ]
        ip_address: Ipv4AddressAndMaskDef
        mtu: Union[
            OneOfMtuOptionsDef1, OneOfMtuOptionsDef2, OneOfMtuOptionsDef3
        ]
        tunnel_dest_ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        # Tunnel Source
        tunnel_source: Union[TunnelSource1, TunnelSource2]
        tcp_mss_adjust: Optional[
            Union[
                OneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
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


    class OneOfIpv6AddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6AddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class IpsecTunnelSource1:
        source_ipv6_address: Union[
            OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
        ]


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


    class TunnelConfig6O6:
        """
        Tunnel Config for Mode ipv6
        """

        ipv6_address: Union[
            OneOfIpv6PrefixOptionsDef1, OneOfIpv6PrefixOptionsDef2
        ]
        tunnel_dest_ipv6_address: Union[
            OneOfIpv6AddressOptionsDef1, OneOfIpv6AddressOptionsDef2
        ]
        # Tunnel Source
        tunnel_source: Union[IpsecTunnelSource1, TunnelSource2]
        ipv6_mtu: Optional[
            Union[
                OneOfMtuV6OptionsDef1,
                OneOfMtuV6OptionsDef2,
                OneOfMtuV6OptionsDef3,
            ]
        ]
        ipv6_tcp_mss_adjust: Optional[
            Union[
                OneOfTcpMssAdjustV6OptionsDef1,
                OneOfTcpMssAdjustV6OptionsDef2,
                OneOfTcpMssAdjustV6OptionsDef3,
            ]
        ]


    class TunnelConfig6O4:
        """
        Tunnel Config for Mode ipv6 over ipv4
        """

        ipv6_address: Union[
            OneOfIpv6PrefixOptionsDef1, OneOfIpv6PrefixOptionsDef2
        ]
        tunnel_dest_ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        # Tunnel Source
        tunnel_source: Union[TunnelSource1, TunnelSource2]
        ipv6_mtu: Optional[
            Union[
                OneOfMtuV6OptionsDef1,
                OneOfMtuV6OptionsDef2,
                OneOfMtuV6OptionsDef3,
            ]
        ]
        ipv6_tcp_mss_adjust: Optional[
            Union[
                OneOfTcpMssAdjustV6OptionsDef1,
                OneOfTcpMssAdjustV6OptionsDef2,
                OneOfTcpMssAdjustV6OptionsDef3,
            ]
        ]


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


    class OneOfTunnelVrfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTunnelVrfNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class TunnelVrf1:
        vrf: Union[
            OneOfTunnelVrfNameOptionsDef1, OneOfTunnelVrfNameOptionsDef2
        ]


    class OneOfTunnelVrfGlobalVrfOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class TunnelVrf2:
        global_vrf: OneOfTunnelVrfGlobalVrfOptionsDef


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


    class Dpd:
        """
        dead-peer detection
        """

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


    class IkeVersion:
        value: Optional[Any]


    class OneOfIkeV1ModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: IkeV1ModeDef


    class OneOfIkeV1ModeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeV1ModeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultIkeV1ModeDef  # pytype: disable=annotation-type-mismatch


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


    class OneOfIkeV1CipherSuiteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: IkeV1CipherSuiteDef


    class OneOfIkeV1CipherSuiteOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeV1CipherSuiteOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultIkeV1CipherSuiteDef  # pytype: disable=annotation-type-mismatch


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


    class OneOfIpV4AddressOptionsWithoutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfIkeV1LocalIdentityOptionsDef1:
        ipv4_addr: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]


    class OneOfIpv6NextHopAddressOptionsWithOutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6NextHopAddressOptionsWithOutDefault2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIkeV1LocalIdentityOptionsDef2:
        ipv6_addr: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]


    class OneOfIdentityValueFqdnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIdentityValueFqdnOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeV1LocalIdentityOptionsDef3:
        fqdn: Union[
            OneOfIdentityValueFqdnOptionsDef1,
            OneOfIdentityValueFqdnOptionsDef2,
        ]


    class OneOfIdentityValueEmailOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIdentityValueEmailOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeV1LocalIdentityOptionsDef4:
        email: Union[
            OneOfIdentityValueEmailOptionsDef1,
            OneOfIdentityValueEmailOptionsDef2,
        ]


    class OneOfIkeV1LocalIdentityOptionsDef5:
        option_type: DefaultOptionTypeDef


    class OneOfIkeV1RemoteIdentityOptionsDef1:
        ipv4_addr: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]


    class OneOfIpv6PrefixGlobalVariableWithoutDefault1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6PrefixGlobalVariableWithoutDefault2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeV1RemoteIdentityOptionsDef2:
        ipv6_prefix: Union[
            OneOfIpv6PrefixGlobalVariableWithoutDefault1,
            OneOfIpv6PrefixGlobalVariableWithoutDefault2,
        ]


    class OneOfIkeV1RemoteIdentityOptionsDef3:
        fqdn: Union[
            OneOfIdentityValueFqdnOptionsDef1,
            OneOfIdentityValueFqdnOptionsDef2,
        ]


    class OneOfIkeV1RemoteIdentityOptionsDef4:
        email: Union[
            OneOfIdentityValueEmailOptionsDef1,
            OneOfIdentityValueEmailOptionsDef2,
        ]


    class OneOfIkeV1RemoteIdentityOptionsDef5:
        option_type: DefaultOptionTypeDef


    class IkeV1:
        """
        IKEv1 config
        """

        ike_dh_group: Union[
            OneOfIkeGroupOptionsDef1,
            OneOfIkeGroupOptionsDef2,
            OneOfIkeGroupOptionsDef3,
        ]
        ike_rekey_interval: Union[
            OneOfIkeRekeyIntervalOptionsDef1,
            OneOfIkeRekeyIntervalOptionsDef2,
            OneOfIkeRekeyIntervalOptionsDef3,
        ]
        ike_v1_cipher_suite: Union[
            OneOfIkeV1CipherSuiteOptionsDef1,
            OneOfIkeV1CipherSuiteOptionsDef2,
            OneOfIkeV1CipherSuiteOptionsDef3,
        ]
        ike_v1_mode: Union[
            OneOfIkeV1ModeOptionsDef1,
            OneOfIkeV1ModeOptionsDef2,
            OneOfIkeV1ModeOptionsDef3,
        ]
        pre_shared_secret: Union[
            OneOfPreSharedSecretOptionsDef1,
            OneOfPreSharedSecretOptionsDef2,
        ]
        ike_local_id: Optional[
            Union[
                OneOfIkeV1LocalIdentityOptionsDef1,
                OneOfIkeV1LocalIdentityOptionsDef2,
                OneOfIkeV1LocalIdentityOptionsDef3,
                OneOfIkeV1LocalIdentityOptionsDef4,
                OneOfIkeV1LocalIdentityOptionsDef5,
            ]
        ]
        ike_remote_id: Optional[
            Union[
                OneOfIkeV1RemoteIdentityOptionsDef1,
                OneOfIkeV1RemoteIdentityOptionsDef2,
                OneOfIkeV1RemoteIdentityOptionsDef3,
                OneOfIkeV1RemoteIdentityOptionsDef4,
                OneOfIkeV1RemoteIdentityOptionsDef5,
            ]
        ]


    class OneOfIkeV2LocalIdentityOptionsDef1:
        ipv4_addr: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]


    class OneOfIkeV2LocalIdentityOptionsDef2:
        ipv6_addr: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]


    class OneOfIkeV2LocalIdentityOptionsDef3:
        fqdn: Union[
            OneOfIdentityValueFqdnOptionsDef1,
            OneOfIdentityValueFqdnOptionsDef2,
        ]


    class OneOfIkeV2LocalIdentityOptionsDef4:
        email: Union[
            OneOfIdentityValueEmailOptionsDef1,
            OneOfIdentityValueEmailOptionsDef2,
        ]


    class OneOfIdentityValueKeyIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIdentityValueKeyIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIkeV2LocalIdentityOptionsDef5:
        key_id: Union[
            OneOfIdentityValueKeyIdOptionsDef1,
            OneOfIdentityValueKeyIdOptionsDef2,
        ]


    class OneOfIkeV2LocalIdentityOptionsDef6:
        option_type: DefaultOptionTypeDef


    class OneOfIkeV2RemoteIdentityOptionsDef1:
        ipv4_addr: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]


    class OneOfIkeV2RemoteIdentityOptionsDef2:
        ipv6_prefix: Union[
            OneOfIpv6PrefixGlobalVariableWithoutDefault1,
            OneOfIpv6PrefixGlobalVariableWithoutDefault2,
        ]


    class OneOfIkeV2RemoteIdentityOptionsDef3:
        fqdn: Union[
            OneOfIdentityValueFqdnOptionsDef1,
            OneOfIdentityValueFqdnOptionsDef2,
        ]


    class OneOfIkeV2RemoteIdentityOptionsDef4:
        email: Union[
            OneOfIdentityValueEmailOptionsDef1,
            OneOfIdentityValueEmailOptionsDef2,
        ]


    class OneOfIkeV2RemoteIdentityOptionsDef5:
        key_id: Union[
            OneOfIdentityValueKeyIdOptionsDef1,
            OneOfIdentityValueKeyIdOptionsDef2,
        ]


    class OneOfIkeV2RemoteIdentityOptionsDef6:
        option_type: DefaultOptionTypeDef


    class IkeV2:
        """
        IKE V2 config
        """

        ike_rekey_interval: Union[
            OneOfIkeRekeyIntervalOptionsDef1,
            OneOfIkeRekeyIntervalOptionsDef2,
            OneOfIkeRekeyIntervalOptionsDef3,
        ]
        pre_shared_secret: Union[
            OneOfPreSharedSecretOptionsDef1,
            OneOfPreSharedSecretOptionsDef2,
        ]
        ike_local_id: Optional[
            Union[
                OneOfIkeV2LocalIdentityOptionsDef1,
                OneOfIkeV2LocalIdentityOptionsDef2,
                OneOfIkeV2LocalIdentityOptionsDef3,
                OneOfIkeV2LocalIdentityOptionsDef4,
                OneOfIkeV2LocalIdentityOptionsDef5,
                OneOfIkeV2LocalIdentityOptionsDef6,
            ]
        ]
        ike_remote_id: Optional[
            Union[
                OneOfIkeV2RemoteIdentityOptionsDef1,
                OneOfIkeV2RemoteIdentityOptionsDef2,
                OneOfIkeV2RemoteIdentityOptionsDef3,
                OneOfIkeV2RemoteIdentityOptionsDef4,
                OneOfIkeV2RemoteIdentityOptionsDef5,
                OneOfIkeV2RemoteIdentityOptionsDef6,
            ]
        ]


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


    class OneOfIpsecCipherSuiteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: IpsecCipherSuiteDef


    class OneOfIpsecCipherSuiteOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpsecCipherSuiteOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultIpsecCipherSuiteDef  # pytype: disable=annotation-type-mismatch


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


    class Ipsec:
        """
        ipsec config
        """

        ipsec_cipher_suite: Union[
            OneOfIpsecCipherSuiteOptionsDef1,
            OneOfIpsecCipherSuiteOptionsDef2,
            OneOfIpsecCipherSuiteOptionsDef3,
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
        perfect_forward_secrecy: Union[
            OneOfPerfectForwardSecrecyOptionsDef1,
            OneOfPerfectForwardSecrecyOptionsDef2,
            OneOfPerfectForwardSecrecyOptionsDef3,
        ]


    class Data1:
        # dead-peer detection
        dpd: Dpd
        if_name: Union[
            OneOfIpsecIfNameOptionsDef1, OneOfIpsecIfNameOptionsDef2
        ]
        # IKE V2 config
        ike_v2: IkeV2
        ike_version: IkeVersion
        # ipsec config
        ipsec: Ipsec
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tunnel_mode: OneOfTunnelModeOptionsDef
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]
        # IKEv1 config
        ike_v1: Optional[IkeV1]
        # Tunnel Config for Mode ipv4
        tunnel_config4o4: Optional[TunnelConfig4O4]
        # Tunnel Config for Mode ipv6 over ipv4
        tunnel_config6o4: Optional[TunnelConfig6O4]
        # Tunnel Config for Mode ipv6
        tunnel_config6o6: Optional[TunnelConfig6O6]
        tunnel_route_via: Optional[
            Union[
                OneOfTunnelRouteViaOptionsDef1,
                OneOfTunnelRouteViaOptionsDef2,
                OneOfTunnelRouteViaOptionsDef3,
            ]
        ]
        # Tunnel Vrf
        tunnel_vrf: Optional[Union[TunnelVrf1, TunnelVrf2]]


    class OneOfIkeVersionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Data2:
        # dead-peer detection
        dpd: Dpd
        if_name: Union[
            OneOfIpsecIfNameOptionsDef1, OneOfIpsecIfNameOptionsDef2
        ]
        ike_version: OneOfIkeVersionOptionsDef
        # ipsec config
        ipsec: Ipsec
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tunnel_mode: OneOfTunnelModeOptionsDef
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]
        # IKEv1 config
        ike_v1: Optional[IkeV1]
        # IKE V2 config
        ike_v2: Optional[IkeV2]
        # Tunnel Config for Mode ipv4
        tunnel_config4o4: Optional[TunnelConfig4O4]
        # Tunnel Config for Mode ipv6 over ipv4
        tunnel_config6o4: Optional[TunnelConfig6O4]
        # Tunnel Config for Mode ipv6
        tunnel_config6o6: Optional[TunnelConfig6O6]
        tunnel_route_via: Optional[
            Union[
                OneOfTunnelRouteViaOptionsDef1,
                OneOfTunnelRouteViaOptionsDef2,
                OneOfTunnelRouteViaOptionsDef3,
            ]
        ]
        # Tunnel Vrf
        tunnel_vrf: Optional[Union[TunnelVrf1, TunnelVrf2]]


    class Payload:
        """
        IPSec interface feature schema in WAN VRF
        """

        data: Union[Data1, Data2]
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
        # IPSec interface feature schema in WAN VRF
        payload: Optional[Payload]


    class GetListSdRoutingTransportVrfWanInterfaceIpsecPayload:
        data: Optional[List[Data]]


    class CreateSdroutingTransportVrfInterfaceIpsecFeatureForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateSdroutingTransportVrfInterfaceIpsecFeatureForTransportPostRequest:
        """
        IPSec interface feature schema in WAN VRF
        """

        data: Union[Data1, Data2]
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdRoutingTransportVrfWanInterfaceIpsecPayload:
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
        # IPSec interface feature schema in WAN VRF
        payload: Optional[Payload]


    class EditSdroutingTransportVrfInterfaceIpsecFeatureForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditSdroutingTransportVrfInterfaceIpsecFeatureForTransportPutRequest:
        """
        IPSec interface feature schema in WAN VRF
        """

        data: Union[Data1, Data2]
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


