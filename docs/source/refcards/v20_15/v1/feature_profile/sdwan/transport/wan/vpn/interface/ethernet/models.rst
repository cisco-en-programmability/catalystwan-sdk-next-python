======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanTrueDef = Literal[True]

    BooleanFalseDef = Literal[False]

    PortChannelLoadBalanceDef = Literal["flow", "vlan"]

    PortChannelLacpModeDef = Literal["active", "passive"]

    PortChannelLacpModeActiveDef = Literal["active"]

    LacpRateDef = Literal["fast", "normal"]

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

    ModeDef = Literal["hub", "spoke"]

    CarrierDef = Literal[
        "carrier1",
        "carrier2",
        "carrier3",
        "carrier4",
        "carrier5",
        "carrier6",
        "carrier7",
        "carrier8",
        "default",
    ]

    DefaultCarrierDef = Literal["default"]

    ColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    Value = Literal["mpls"]

    EncapsulationEncapDef = Literal["gre", "ipsec"]

    CoreRegionDef = Literal["core", "core-shared"]

    DefaultCoreRegionDef = Literal["core-shared"]

    SecondaryRegionDef = Literal["secondary-only", "secondary-shared"]

    DefaultSecondaryRegionDef = Literal["secondary-shared"]

    NatChoiceDef = Literal["interface", "loopback", "pool"]

    DefaultNatChoiceDef = Literal["interface"]

    StaticNatDirectionDef = Literal["inside"]

    DefaultStaticNatDirectionDef = Literal["inside"]

    StaticPortForwardProtocolDef = Literal["tcp", "udp"]

    DuplexDef = Literal["auto", "full", "half"]

    SpeedDef = Literal["10", "100", "1000", "10000", "2500", "25000"]

    MediaTypeDef = Literal["auto-select", "rj45", "sfp"]

    EthernetPortChannelLoadBalanceDef = Literal["flow", "vlan"]

    EthernetPortChannelLacpModeDef = Literal["active", "passive"]

    EthernetPortChannelLacpModeActiveDef = Literal["active"]

    EthernetLacpRateDef = Literal["fast", "normal"]

    InterfaceEthernetPortChannelLoadBalanceDef = Literal["flow", "vlan"]

    EthernetModeDef = Literal["hub", "spoke"]

    EthernetCarrierDef = Literal[
        "carrier1",
        "carrier2",
        "carrier3",
        "carrier4",
        "carrier5",
        "carrier6",
        "carrier7",
        "carrier8",
        "default",
    ]

    EthernetDefaultCarrierDef = Literal["default"]

    EthernetColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    EthernetEncapsulationEncapDef = Literal["gre", "ipsec"]

    EthernetCoreRegionDef = Literal["core", "core-shared"]

    EthernetDefaultCoreRegionDef = Literal["core-shared"]

    EthernetSecondaryRegionDef = Literal[
        "secondary-only", "secondary-shared"
    ]

    EthernetDefaultSecondaryRegionDef = Literal["secondary-shared"]

    EthernetNatChoiceDef = Literal["interface", "loopback", "pool"]

    EthernetDefaultNatChoiceDef = Literal["interface"]

    EthernetStaticNatDirectionDef = Literal["inside"]

    EthernetDefaultStaticNatDirectionDef = Literal["inside"]

    EthernetStaticPortForwardProtocolDef = Literal["tcp", "udp"]

    InterfaceEthernetStaticNatDirectionDef = Literal["inside"]

    InterfaceEthernetDefaultStaticNatDirectionDef = Literal["inside"]

    EthernetDuplexDef = Literal["auto", "full", "half"]

    EthernetSpeedDef = Literal[
        "10", "100", "1000", "10000", "2500", "25000"
    ]

    EthernetMediaTypeDef = Literal["auto-select", "rj45", "sfp"]

    VpnInterfaceEthernetPortChannelLoadBalanceDef = Literal[
        "flow", "vlan"
    ]

    InterfaceEthernetPortChannelLacpModeDef = Literal["active", "passive"]

    InterfaceEthernetPortChannelLacpModeActiveDef = Literal["active"]

    InterfaceEthernetLacpRateDef = Literal["fast", "normal"]

    WanVpnInterfaceEthernetPortChannelLoadBalanceDef = Literal[
        "flow", "vlan"
    ]

    InterfaceEthernetModeDef = Literal["hub", "spoke"]

    InterfaceEthernetCarrierDef = Literal[
        "carrier1",
        "carrier2",
        "carrier3",
        "carrier4",
        "carrier5",
        "carrier6",
        "carrier7",
        "carrier8",
        "default",
    ]

    InterfaceEthernetDefaultCarrierDef = Literal["default"]

    InterfaceEthernetColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    InterfaceEthernetEncapsulationEncapDef = Literal["gre", "ipsec"]

    InterfaceEthernetCoreRegionDef = Literal["core", "core-shared"]

    InterfaceEthernetDefaultCoreRegionDef = Literal["core-shared"]

    InterfaceEthernetSecondaryRegionDef = Literal[
        "secondary-only", "secondary-shared"
    ]

    InterfaceEthernetDefaultSecondaryRegionDef = Literal[
        "secondary-shared"
    ]

    InterfaceEthernetNatChoiceDef = Literal[
        "interface", "loopback", "pool"
    ]

    InterfaceEthernetDefaultNatChoiceDef = Literal["interface"]

    VpnInterfaceEthernetStaticNatDirectionDef = Literal["inside"]

    VpnInterfaceEthernetDefaultStaticNatDirectionDef = Literal["inside"]

    InterfaceEthernetStaticPortForwardProtocolDef = Literal["tcp", "udp"]

    WanVpnInterfaceEthernetStaticNatDirectionDef = Literal["inside"]

    WanVpnInterfaceEthernetDefaultStaticNatDirectionDef = Literal[
        "inside"
    ]

    InterfaceEthernetDuplexDef = Literal["auto", "full", "half"]

    InterfaceEthernetSpeedDef = Literal[
        "10", "100", "1000", "10000", "2500", "25000"
    ]

    InterfaceEthernetMediaTypeDef = Literal["auto-select", "rj45", "sfp"]


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
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceNameOptionsDef2:
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


    class OneOfPortChannelOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfPortChannelOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfPortChannelQosAggregateOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfPortChannelQosAggregateOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPortChannelQosAggregateOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfPortChannelLoadBalanceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: PortChannelLoadBalanceDef  # pytype: disable=annotation-type-mismatch


    class OneOfPortChannelLoadBalanceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPortChannelLoadBalanceOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfLacpFastSwitchoverOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfLacpFastSwitchoverOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLacpFastSwitchoverOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfLacpMinBundleOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfLacpMinBundleOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLacpMinBundleOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfLacpMaxBundleOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfLacpMaxBundleOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLacpMaxBundleOptionsDef3:
        option_type: DefaultOptionTypeDef


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class ParcelReferenceDef:
        ref_id: RefId


    class OneOfLacpModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: PortChannelLacpModeDef  # pytype: disable=annotation-type-mismatch


    class OneOfLacpModeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLacpModeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: PortChannelLacpModeActiveDef  # pytype: disable=annotation-type-mismatch


    class OneOfLacpRateOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: LacpRateDef  # pytype: disable=annotation-type-mismatch


    class OneOfLacpRateOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLacpRateOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfLacpPortPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfLacpPortPriorityOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLacpPortPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef


    class PortChannelMemberLinks:
        interface: ParcelReferenceDef
        lacp_mode: Union[
            OneOfLacpModeOptionsDef1,
            OneOfLacpModeOptionsDef2,
            OneOfLacpModeOptionsDef3,
        ]
        lacp_port_priority: Optional[
            Union[
                OneOfLacpPortPriorityOptionsDef1,
                OneOfLacpPortPriorityOptionsDef2,
                OneOfLacpPortPriorityOptionsDef3,
            ]
        ]
        lacp_rate: Optional[
            Union[
                OneOfLacpRateOptionsDef1,
                OneOfLacpRateOptionsDef2,
                OneOfLacpRateOptionsDef3,
            ]
        ]


    class LacpModeMainInterface:
        # Configure Port-Channel member links
        port_channel_member_links: List[PortChannelMemberLinks]
        lacp_fast_switchover: Optional[
            Union[
                OneOfLacpFastSwitchoverOptionsDef1,
                OneOfLacpFastSwitchoverOptionsDef2,
                OneOfLacpFastSwitchoverOptionsDef3,
            ]
        ]
        lacp_max_bundle: Optional[
            Union[
                OneOfLacpMaxBundleOptionsDef1,
                OneOfLacpMaxBundleOptionsDef2,
                OneOfLacpMaxBundleOptionsDef3,
            ]
        ]
        lacp_min_bundle: Optional[
            Union[
                OneOfLacpMinBundleOptionsDef1,
                OneOfLacpMinBundleOptionsDef2,
                OneOfLacpMinBundleOptionsDef3,
            ]
        ]
        load_balance: Optional[
            Union[
                OneOfPortChannelLoadBalanceOptionsDef1,
                OneOfPortChannelLoadBalanceOptionsDef2,
                OneOfPortChannelLoadBalanceOptionsDef3,
            ]
        ]
        port_channel_qos_aggregate: Optional[
            Union[
                OneOfPortChannelQosAggregateOptionsDef1,
                OneOfPortChannelQosAggregateOptionsDef2,
                OneOfPortChannelQosAggregateOptionsDef3,
            ]
        ]


    class MainInterface1:
        """
        Port-channel Lacp mode Main Interface
        """

        lacp_mode_main_interface: LacpModeMainInterface


    class EthernetPortChannelMemberLinks:
        interface: ParcelReferenceDef


    class StaticModeMainInterface:
        # Configure Port-Channel member links
        port_channel_member_links: List[EthernetPortChannelMemberLinks]
        load_balance: Optional[
            Union[
                OneOfPortChannelLoadBalanceOptionsDef1,
                OneOfPortChannelLoadBalanceOptionsDef2,
                OneOfPortChannelLoadBalanceOptionsDef3,
            ]
        ]
        port_channel_qos_aggregate: Optional[
            Union[
                OneOfPortChannelQosAggregateOptionsDef1,
                OneOfPortChannelQosAggregateOptionsDef2,
                OneOfPortChannelQosAggregateOptionsDef3,
            ]
        ]


    class MainInterface2:
        """
        Port-channel Static mode Main Interface
        """

        static_mode_main_interface: StaticModeMainInterface


    class PortChannel1:
        """
        Port-channel Main Interface
        """

        main_interface: Union[MainInterface1, MainInterface2]


    class Wan:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class SubInterface:
        wan: Wan


    class PortChannel2:
        """
        Port-channel Wan Sub Interface
        """

        sub_interface: SubInterface


    class OneOfPortChannelMemberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfPortChannelMemberOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfDynamicDhcpDistanceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDynamicDhcpDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDynamicDhcpDistanceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Dynamic:
        dynamic_dhcp_distance: Union[
            OneOfDynamicDhcpDistanceOptionsDef1,
            OneOfDynamicDhcpDistanceOptionsDef2,
            OneOfDynamicDhcpDistanceOptionsDef3,
        ]


    class IntfIpAddress1:
        dynamic: Dynamic


    class OneOfIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpV4AddressOptionsDef3:
        option_type: DefaultOptionTypeDef


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


    class OneOfIpV4SubnetMaskOptionsDef3:
        option_type: DefaultOptionTypeDef


    class StaticIpV4AddressPrimary:
        """
        Static IpV4Address Primary
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            OneOfIpV4AddressOptionsDef2,
            OneOfIpV4AddressOptionsDef3,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1,
            OneOfIpV4SubnetMaskOptionsDef2,
            OneOfIpV4SubnetMaskOptionsDef3,
        ]


    class OneOfIpV4AddressOptionsWithoutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfIpV4SubnetMaskOptionsWithoutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4SubnetMaskOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: (
            Ipv4SubnetMaskDef  # pytype: disable=annotation-type-mismatch
        )


    class StaticIpV4AddressSecondary:
        ip_address: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsWithoutDefault1,
            OneOfIpV4SubnetMaskOptionsWithoutDefault2,
        ]


    class Static:
        # Static IpV4Address Primary
        static_ip_v4_address_primary: StaticIpV4AddressPrimary
        # Secondary IpV4 Addresses
        static_ip_v4_address_secondary: Optional[
            List[StaticIpV4AddressSecondary]
        ]


    class IntfIpAddress2:
        static: Static


    class OneOfListOfIpV4OptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfListOfIpV4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfListOfIpV4OptionsDef3:
        option_type: DefaultOptionTypeDef


    class DhcpClient:
        """
        Enable DHCPv6
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfIpv6PrefixGlobalVariableWithoutDefault1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6PrefixGlobalVariableWithoutDefault2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class SecondaryIpV6Address:
        address: Union[
            OneOfIpv6PrefixGlobalVariableWithoutDefault1,
            OneOfIpv6PrefixGlobalVariableWithoutDefault2,
        ]


    class EthernetDynamic:
        # Enable DHCPv6
        dhcp_client: DhcpClient
        # secondary IPv6 addresses
        secondary_ip_v6_address: Optional[List[SecondaryIpV6Address]]


    class IntfIpV6Address1:
        dynamic: EthernetDynamic


    class OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef3:
        option_type: DefaultOptionTypeDef


    class PrimaryIpV6Address:
        """
        Static IpV6Address Primary
        """

        address: Union[
            OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef1,
            OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef2,
            OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef3,
        ]


    class EthernetStatic:
        # Static IpV6Address Primary
        primary_ip_v6_address: Optional[PrimaryIpV6Address]
        # Static secondary IPv6 addresses
        secondary_ip_v6_address: Optional[List[SecondaryIpV6Address]]


    class IntfIpV6Address2:
        static: EthernetStatic


    class OneOfIperfServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIperfServerOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIperfServerOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfBlockNonSourceIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfBlockNonSourceIpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBlockNonSourceIpOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfServiceProviderOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfServiceProviderOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfServiceProviderOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfBandwidthUpstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfBandwidthUpstreamOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBandwidthUpstreamOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfBandwidthDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfBandwidthDownstreamOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBandwidthDownstreamOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfAutoBandwidthDetectOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAutoBandwidthDetectOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAutoBandwidthDetectOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfTunnelInterfaceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfTunnelInterfaceOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfPerTunnelQosOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfPerTunnelQosOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPerTunnelQosOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ModeDef  # pytype: disable=annotation-type-mismatch


    class OneOfModeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBandwidthPercentOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfBandwidthPercentOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfBandwidthPercentOptionsDef3:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBindOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfBindOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBindOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfCarrierOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: CarrierDef


    class OneOfCarrierOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfCarrierOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: (
            DefaultCarrierDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfColorOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ColorDef  # pytype: disable=annotation-type-mismatch


    class OneOfColorOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfColorOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfHelloIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHelloIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHelloIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfHelloToleranceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHelloToleranceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHelloToleranceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfLastResortCircuitOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfLastResortCircuitOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLastResortCircuitOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfTlocExtensionGreToOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTlocExtensionGreToOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTlocExtensionGreToOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfRestrictOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfRestrictOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRestrictOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfGroupOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfGroupOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfBorderOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfBorderOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBorderOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfMaxControlConnectionsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMaxControlConnectionsOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMaxControlConnectionsOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfNatRefreshIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNatRefreshIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatRefreshIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfVbondAsStunServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfVbondAsStunServerOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVbondAsStunServerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfControllerGroupListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class OneOfControllerGroupListOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfControllerGroupListOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfVmanageConnectionPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVmanageConnectionPreferenceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVmanageConnectionPreferenceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfPortHopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfPortHopOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPortHopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfLowBandwidthLinkOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfLowBandwidthLinkOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLowBandwidthLinkOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfTunnelTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTunnelTcpMssAdjustOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTunnelTcpMssAdjustOptionsDef3:
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
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfPropagateSgtOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfPropagateSgtOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPropagateSgtOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfNetworkBroadcastOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfNetworkBroadcastOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNetworkBroadcastOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfAllowFragmentationDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowFragmentationDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowFragmentationDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfSetSdwanTunnelMtuToMaxDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfSetSdwanTunnelMtuToMaxDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSetSdwanTunnelMtuToMaxDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class Tunnel:
        """
        Tunnel Interface Attributes
        """

        allow_fragmentation: Optional[
            Union[
                OneOfAllowFragmentationDef1,
                OneOfAllowFragmentationDef2,
                OneOfAllowFragmentationDef3,
            ]
        ]
        bandwidth_percent: Optional[
            Union[
                OneOfBandwidthPercentOptionsDef1,
                OneOfBandwidthPercentOptionsDef2,
                OneOfBandwidthPercentOptionsDef3,
            ]
        ]
        bind: Optional[
            Union[
                OneOfBindOptionsDef1,
                OneOfBindOptionsDef2,
                OneOfBindOptionsDef3,
            ]
        ]
        border: Optional[
            Union[
                OneOfBorderOptionsDef1,
                OneOfBorderOptionsDef2,
                OneOfBorderOptionsDef3,
            ]
        ]
        carrier: Optional[
            Union[
                OneOfCarrierOptionsDef1,
                OneOfCarrierOptionsDef2,
                OneOfCarrierOptionsDef3,
            ]
        ]
        clear_dont_fragment: Optional[
            Union[
                OneOfClearDontFragmentOptionsDef1,
                OneOfClearDontFragmentOptionsDef2,
                OneOfClearDontFragmentOptionsDef3,
            ]
        ]
        color: Optional[
            Union[
                OneOfColorOptionsDef1,
                OneOfColorOptionsDef2,
                OneOfColorOptionsDef3,
            ]
        ]
        cts_sgt_propagation: Optional[
            Union[
                OneOfPropagateSgtOptionsDef1,
                OneOfPropagateSgtOptionsDef2,
                OneOfPropagateSgtOptionsDef3,
            ]
        ]
        exclude_controller_group_list: Optional[
            Union[
                OneOfControllerGroupListOptionsDef1,
                OneOfControllerGroupListOptionsDef2,
                OneOfControllerGroupListOptionsDef3,
            ]
        ]
        group: Optional[
            Union[
                OneOfGroupOptionsDef1,
                OneOfGroupOptionsDef2,
                OneOfGroupOptionsDef3,
            ]
        ]
        hello_interval: Optional[
            Union[
                OneOfHelloIntervalOptionsDef1,
                OneOfHelloIntervalOptionsDef2,
                OneOfHelloIntervalOptionsDef3,
            ]
        ]
        hello_tolerance: Optional[
            Union[
                OneOfHelloToleranceOptionsDef1,
                OneOfHelloToleranceOptionsDef2,
                OneOfHelloToleranceOptionsDef3,
            ]
        ]
        last_resort_circuit: Optional[
            Union[
                OneOfLastResortCircuitOptionsDef1,
                OneOfLastResortCircuitOptionsDef2,
                OneOfLastResortCircuitOptionsDef3,
            ]
        ]
        low_bandwidth_link: Optional[
            Union[
                OneOfLowBandwidthLinkOptionsDef1,
                OneOfLowBandwidthLinkOptionsDef2,
                OneOfLowBandwidthLinkOptionsDef3,
            ]
        ]
        max_control_connections: Optional[
            Union[
                OneOfMaxControlConnectionsOptionsDef1,
                OneOfMaxControlConnectionsOptionsDef2,
                OneOfMaxControlConnectionsOptionsDef3,
            ]
        ]
        mode: Optional[Union[OneOfModeOptionsDef1, OneOfModeOptionsDef2]]
        nat_refresh_interval: Optional[
            Union[
                OneOfNatRefreshIntervalOptionsDef1,
                OneOfNatRefreshIntervalOptionsDef2,
                OneOfNatRefreshIntervalOptionsDef3,
            ]
        ]
        network_broadcast: Optional[
            Union[
                OneOfNetworkBroadcastOptionsDef1,
                OneOfNetworkBroadcastOptionsDef2,
                OneOfNetworkBroadcastOptionsDef3,
            ]
        ]
        per_tunnel_qos: Optional[
            Union[
                OneOfPerTunnelQosOptionsDef1,
                OneOfPerTunnelQosOptionsDef2,
                OneOfPerTunnelQosOptionsDef3,
            ]
        ]
        port_hop: Optional[
            Union[
                OneOfPortHopOptionsDef1,
                OneOfPortHopOptionsDef2,
                OneOfPortHopOptionsDef3,
            ]
        ]
        restrict: Optional[
            Union[
                OneOfRestrictOptionsDef1,
                OneOfRestrictOptionsDef2,
                OneOfRestrictOptionsDef3,
            ]
        ]
        set_sdwan_tunnel_mtu_to_max: Optional[
            Union[
                OneOfSetSdwanTunnelMtuToMaxDef1,
                OneOfSetSdwanTunnelMtuToMaxDef2,
                OneOfSetSdwanTunnelMtuToMaxDef3,
            ]
        ]
        tloc_extension_gre_to: Optional[
            Union[
                OneOfTlocExtensionGreToOptionsDef1,
                OneOfTlocExtensionGreToOptionsDef2,
                OneOfTlocExtensionGreToOptionsDef3,
            ]
        ]
        tunnel_tcp_mss: Optional[
            Union[
                OneOfTunnelTcpMssAdjustOptionsDef1,
                OneOfTunnelTcpMssAdjustOptionsDef2,
                OneOfTunnelTcpMssAdjustOptionsDef3,
            ]
        ]
        v_bond_as_stun_server: Optional[
            Union[
                OneOfVbondAsStunServerOptionsDef1,
                OneOfVbondAsStunServerOptionsDef2,
                OneOfVbondAsStunServerOptionsDef3,
            ]
        ]
        v_manage_connection_preference: Optional[
            Union[
                OneOfVmanageConnectionPreferenceOptionsDef1,
                OneOfVmanageConnectionPreferenceOptionsDef2,
                OneOfVmanageConnectionPreferenceOptionsDef3,
            ]
        ]


    class OneOfAllowAllOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowAllOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowAllOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfAllowBgpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowBgpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowBgpOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfAllowDhcpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowDhcpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowDhcpOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfAllowNtpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowNtpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowNtpOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfAllowSshOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowSshOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowSshOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfAllowServiceTrueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowServiceTrueOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowServiceTrueOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfAllowServiceFalseOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowServiceFalseOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowServiceFalseOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class AllowService:
        """
        Tunnel Interface Attributes
        """

        all: Optional[
            Union[
                OneOfAllowAllOptionsDef1,
                OneOfAllowAllOptionsDef2,
                OneOfAllowAllOptionsDef3,
            ]
        ]
        bfd: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        bgp: Optional[
            Union[
                OneOfAllowBgpOptionsDef1,
                OneOfAllowBgpOptionsDef2,
                OneOfAllowBgpOptionsDef3,
            ]
        ]
        dhcp: Optional[
            Union[
                OneOfAllowDhcpOptionsDef1,
                OneOfAllowDhcpOptionsDef2,
                OneOfAllowDhcpOptionsDef3,
            ]
        ]
        dns: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        https: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        icmp: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        netconf: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        ntp: Optional[
            Union[
                OneOfAllowNtpOptionsDef1,
                OneOfAllowNtpOptionsDef2,
                OneOfAllowNtpOptionsDef3,
            ]
        ]
        ospf: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        snmp: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        ssh: Optional[
            Union[
                OneOfAllowSshOptionsDef1,
                OneOfAllowSshOptionsDef2,
                OneOfAllowSshOptionsDef3,
            ]
        ]
        stun: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]


    class OneOfEncapsulationEncapOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EncapsulationEncapDef  # pytype: disable=annotation-type-mismatch


    class OneOfEncapsulationPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEncapsulationPreferenceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEncapsulationPreferenceOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfEncapsulationWeightOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEncapsulationWeightOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEncapsulationWeightOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Encapsulation:
        encap: OneOfEncapsulationEncapOptionsDef
        preference: Optional[
            Union[
                OneOfEncapsulationPreferenceOptionsDef1,
                OneOfEncapsulationPreferenceOptionsDef2,
                OneOfEncapsulationPreferenceOptionsDef3,
            ]
        ]
        weight: Optional[
            Union[
                OneOfEncapsulationWeightOptionsDef1,
                OneOfEncapsulationWeightOptionsDef2,
                OneOfEncapsulationWeightOptionsDef3,
            ]
        ]


    class OneOfEnableRegionDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfEnableRegionDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfCoreRegionDef1:
        option_type: GlobalOptionTypeDef
        value: CoreRegionDef  # pytype: disable=annotation-type-mismatch


    class OneOfCoreRegionDef2:
        option_type: DefaultOptionTypeDef
        value: DefaultCoreRegionDef  # pytype: disable=annotation-type-mismatch


    class OneOfSecondaryRegionDef1:
        option_type: GlobalOptionTypeDef
        value: (
            SecondaryRegionDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfSecondaryRegionDef2:
        option_type: DefaultOptionTypeDef
        value: DefaultSecondaryRegionDef  # pytype: disable=annotation-type-mismatch


    class MultiRegionFabric:
        """
        Multi-Region Fabric
        """

        core_region: Optional[
            Union[OneOfCoreRegionDef1, OneOfCoreRegionDef2]
        ]
        enable_core_region: Optional[
            Union[OneOfEnableRegionDef1, OneOfEnableRegionDef2]
        ]
        enable_secondary_region: Optional[
            Union[OneOfEnableRegionDef1, OneOfEnableRegionDef2]
        ]
        secondary_region: Optional[
            Union[OneOfSecondaryRegionDef1, OneOfSecondaryRegionDef2]
        ]


    class OneOfNatOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfNatOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfNatTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: NatChoiceDef


    class OneOfNatTypeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: DefaultNatChoiceDef  # pytype: disable=annotation-type-mismatch


    class OneOfNatPoolRangeStartOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPoolRangeStartOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNatPoolRangeEndOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPoolRangeEndOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNatPoolPrefixLengthOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPoolPrefixLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNatPoolOverloadOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPoolOverloadOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfNatPoolOverloadOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class NatPool:
        """
        NAT Pool
        """

        prefix_length: Union[
            OneOfNatPoolPrefixLengthOptionsDef1,
            OneOfNatPoolPrefixLengthOptionsDef2,
        ]
        range_end: Union[
            OneOfNatPoolRangeEndOptionsDef1,
            OneOfNatPoolRangeEndOptionsDef2,
        ]
        range_start: Union[
            OneOfNatPoolRangeStartOptionsDef1,
            OneOfNatPoolRangeStartOptionsDef2,
        ]
        overload: Optional[
            Union[
                OneOfNatPoolOverloadOptionsDef1,
                OneOfNatPoolOverloadOptionsDef2,
                OneOfNatPoolOverloadOptionsDef3,
            ]
        ]


    class OneOfLoopbackInterfaceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfLoopbackInterfaceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLoopbackInterfaceOptionsDef3:
        option_type: DefaultOptionTypeDef


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


    class OneOfNatPoolNameOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPoolNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class MultiplePool:
        name: Union[
            OneOfNatPoolNameOptionsDef1, OneOfNatPoolNameOptionsDef2
        ]
        overload: Union[
            OneOfNatPoolOverloadOptionsDef1,
            OneOfNatPoolOverloadOptionsDef2,
            OneOfNatPoolOverloadOptionsDef3,
        ]
        prefix_length: Union[
            OneOfNatPoolPrefixLengthOptionsDef1,
            OneOfNatPoolPrefixLengthOptionsDef2,
        ]
        range_end: Union[
            OneOfNatPoolRangeEndOptionsDef1,
            OneOfNatPoolRangeEndOptionsDef2,
        ]
        range_start: Union[
            OneOfNatPoolRangeStartOptionsDef1,
            OneOfNatPoolRangeStartOptionsDef2,
        ]
        enable_dual_router_ha_mapping: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]


    class MultipleLoopback:
        loopback_interface: Union[
            OneOfLoopbackInterfaceOptionsDef1,
            OneOfLoopbackInterfaceOptionsDef2,
            OneOfLoopbackInterfaceOptionsDef3,
        ]


    class OneOfUdpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfUdpTimeoutOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUdpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfTcpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTcpTimeoutOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTcpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfStaticSourceIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfStaticSourceIpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticTranslateIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfStaticTranslateIpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticNatDirectionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: StaticNatDirectionDef


    class OneOfStaticNatDirectionOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: DefaultStaticNatDirectionDef  # pytype: disable=annotation-type-mismatch


    class OneOfStaticSourceVpnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfStaticSourceVpnOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticSourceVpnOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class NewStaticNat:
        source_ip: Union[
            OneOfStaticSourceIpOptionsDef1, OneOfStaticSourceIpOptionsDef2
        ]
        source_vpn: Union[
            OneOfStaticSourceVpnOptionsDef1,
            OneOfStaticSourceVpnOptionsDef2,
            OneOfStaticSourceVpnOptionsDef3,
        ]
        static_nat_direction: Union[
            OneOfStaticNatDirectionOptionsDef1,
            OneOfStaticNatDirectionOptionsDef2,
        ]
        translate_ip: Union[
            OneOfStaticTranslateIpOptionsDef1,
            OneOfStaticTranslateIpOptionsDef2,
        ]
        enable_dual_router_ha_mapping: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]


    class OneOfStaticPortForwardProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: StaticPortForwardProtocolDef  # pytype: disable=annotation-type-mismatch


    class OneOfStaticPortForwardProtocolOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticSourcePortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfStaticSourcePortOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticTranslatePortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfStaticTranslatePortOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class StaticPortForward:
        protocol: Union[
            OneOfStaticPortForwardProtocolOptionsDef1,
            OneOfStaticPortForwardProtocolOptionsDef2,
        ]
        source_ip: Union[
            OneOfStaticSourceIpOptionsDef1, OneOfStaticSourceIpOptionsDef2
        ]
        source_port: Union[
            OneOfStaticSourcePortOptionsDef1,
            OneOfStaticSourcePortOptionsDef2,
        ]
        source_vpn: Union[
            OneOfStaticSourceVpnOptionsDef1,
            OneOfStaticSourceVpnOptionsDef2,
            OneOfStaticSourceVpnOptionsDef3,
        ]
        static_nat_direction: Union[
            OneOfStaticNatDirectionOptionsDef1,
            OneOfStaticNatDirectionOptionsDef2,
        ]
        translate_ip: Union[
            OneOfStaticTranslateIpOptionsDef1,
            OneOfStaticTranslateIpOptionsDef2,
        ]
        translate_port: Union[
            OneOfStaticTranslatePortOptionsDef1,
            OneOfStaticTranslatePortOptionsDef2,
        ]
        enable_dual_router_ha_mapping: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]


    class NatAttributesIpv4:
        """
        NAT Attributes IpV4
        """

        nat_type: Union[OneOfNatTypeOptionsDef1, OneOfNatTypeOptionsDef2]
        tcp_timeout: Union[
            OneOfTcpTimeoutOptionsDef1,
            OneOfTcpTimeoutOptionsDef2,
            OneOfTcpTimeoutOptionsDef3,
        ]
        udp_timeout: Union[
            OneOfUdpTimeoutOptionsDef1,
            OneOfUdpTimeoutOptionsDef2,
            OneOfUdpTimeoutOptionsDef3,
        ]
        match_interface: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # NAT Multiple Loopback
        multiple_loopback: Optional[List[MultipleLoopback]]
        # NAT Multiple Pool
        multiple_pool: Optional[List[MultiplePool]]
        nat_loopback: Optional[
            Union[
                OneOfLoopbackInterfaceOptionsDef1,
                OneOfLoopbackInterfaceOptionsDef2,
                OneOfLoopbackInterfaceOptionsDef3,
            ]
        ]
        # NAT Pool
        nat_pool: Optional[NatPool]
        # static NAT
        new_static_nat: Optional[List[NewStaticNat]]
        # Configure Port Forward entries
        static_port_forward: Optional[List[StaticPortForward]]


    class OneOfNat64Nat66OptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfNat64Nat66OptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfStaticNat66SourcePrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfStaticNat66SourcePrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticNat66TranslatedSourcePrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfStaticNat66TranslatedSourcePrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticNat66TranslatedSourcePrefixOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfStaticNat66SourceVpnIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfStaticNat66SourceVpnIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticNat66SourceVpnIdOptionsDef3:
        option_type: DefaultOptionTypeDef


    class StaticNat66:
        source_prefix: Union[
            OneOfStaticNat66SourcePrefixOptionsDef1,
            OneOfStaticNat66SourcePrefixOptionsDef2,
        ]
        source_vpn_id: Union[
            OneOfStaticNat66SourceVpnIdOptionsDef1,
            OneOfStaticNat66SourceVpnIdOptionsDef2,
            OneOfStaticNat66SourceVpnIdOptionsDef3,
        ]
        egress_interface: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        translated_source_prefix: Optional[
            Union[
                OneOfStaticNat66TranslatedSourcePrefixOptionsDef1,
                OneOfStaticNat66TranslatedSourcePrefixOptionsDef2,
                OneOfStaticNat66TranslatedSourcePrefixOptionsDef3,
            ]
        ]


    class NatAttributesIpv6:
        """
        NAT Attributes Ipv6
        """

        nat64: Optional[
            Union[OneOfNat64Nat66OptionsDef1, OneOfNat64Nat66OptionsDef2]
        ]
        nat66: Optional[
            Union[OneOfNat64Nat66OptionsDef1, OneOfNat64Nat66OptionsDef2]
        ]
        # static NAT66
        static_nat66: Optional[List[StaticNat66]]


    class OneOfQosAdaptiveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfQosAdaptiveOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfPeriodOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfPeriodOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPeriodOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class ShapingRateUpstream:
        value: Optional[Any]


    class OneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class ShapingRateUpstreamConfig:
        """
        adaptiveQoS Shaping Rate Upstream config
        """

        default_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class OneOfShapingRateDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfShapingRateDownstreamOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class ShapingRateDownstreamConfig:
        """
        adaptiveQoS Shaping Rate Downstream config
        """

        default_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class OneOfShapingRateOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfShapingRateOptionsDef3:
        option_type: DefaultOptionTypeDef


    class AclQos1:
        adaptive_qo_s: Union[
            OneOfQosAdaptiveOptionsDef1, OneOfQosAdaptiveOptionsDef2
        ]
        shaping_rate_upstream: ShapingRateUpstream
        # adaptiveQoS Shaping Rate Upstream config
        shaping_rate_upstream_config: ShapingRateUpstreamConfig
        adapt_period: Optional[
            Union[
                OneOfPeriodOptionsDef1,
                OneOfPeriodOptionsDef2,
                OneOfPeriodOptionsDef3,
            ]
        ]
        ipv4_acl_egress: Optional[ParcelReferenceDef]
        ipv4_acl_ingress: Optional[ParcelReferenceDef]
        ipv6_acl_egress: Optional[ParcelReferenceDef]
        ipv6_acl_ingress: Optional[ParcelReferenceDef]
        shaping_rate: Optional[
            Union[
                OneOfShapingRateOptionsDef1,
                OneOfShapingRateOptionsDef2,
                OneOfShapingRateOptionsDef3,
            ]
        ]
        shaping_rate_downstream: Optional[
            Union[
                OneOfShapingRateDownstreamOptionsDef1,
                OneOfShapingRateDownstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Downstream config
        shaping_rate_downstream_config: Optional[
            ShapingRateDownstreamConfig
        ]


    class OneOfShapingRateUpstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfShapingRateUpstreamOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class AclQos2:
        adaptive_qo_s: Union[
            OneOfQosAdaptiveOptionsDef1, OneOfQosAdaptiveOptionsDef2
        ]
        adapt_period: Optional[
            Union[
                OneOfPeriodOptionsDef1,
                OneOfPeriodOptionsDef2,
                OneOfPeriodOptionsDef3,
            ]
        ]
        ipv4_acl_egress: Optional[ParcelReferenceDef]
        ipv4_acl_ingress: Optional[ParcelReferenceDef]
        ipv6_acl_egress: Optional[ParcelReferenceDef]
        ipv6_acl_ingress: Optional[ParcelReferenceDef]
        shaping_rate: Optional[
            Union[
                OneOfShapingRateOptionsDef1,
                OneOfShapingRateOptionsDef2,
                OneOfShapingRateOptionsDef3,
            ]
        ]
        shaping_rate_downstream: Optional[
            Union[
                OneOfShapingRateDownstreamOptionsDef1,
                OneOfShapingRateDownstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Downstream config
        shaping_rate_downstream_config: Optional[
            ShapingRateDownstreamConfig
        ]
        shaping_rate_upstream: Optional[
            Union[
                OneOfShapingRateUpstreamOptionsDef1,
                OneOfShapingRateUpstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Upstream config
        shaping_rate_upstream_config: Optional[ShapingRateUpstreamConfig]


    class OneOfMacAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfMacAddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMacAddressOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Arp:
        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            OneOfIpV4AddressOptionsDef2,
            OneOfIpV4AddressOptionsDef3,
        ]
        mac_address: Union[
            OneOfMacAddressOptionsDef1,
            OneOfMacAddressOptionsDef2,
            OneOfMacAddressOptionsDef3,
        ]


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


    class OneOfDuplexOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: DuplexDef  # pytype: disable=annotation-type-mismatch


    class OneOfDuplexOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDuplexOptionsDef3:
        option_type: DefaultOptionTypeDef


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


    class OneOfIntrfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIntrfMtuOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIntrfMtuOptionsDef3:
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


    class OneOfSpeedOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SpeedDef  # pytype: disable=annotation-type-mismatch


    class OneOfSpeedOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSpeedOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfArpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfArpTimeoutOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfArpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfAutonegotiateOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAutonegotiateOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAutonegotiateOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfMediaTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: MediaTypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfMediaTypeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMediaTypeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfTlocExtensionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTlocExtensionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTlocExtensionOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfTlocExtensionGreFromOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTlocExtensionGreFromOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTlocExtensionGreFromOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfXconnectOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfXconnectOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfXconnectOptionsDef3:
        option_type: DefaultOptionTypeDef


    class TlocExtensionGreFrom:
        """
        Extend remote TLOC over a GRE tunnel to a local WAN interface
        """

        source_ip: Optional[
            Union[
                OneOfTlocExtensionGreFromOptionsDef1,
                OneOfTlocExtensionGreFromOptionsDef2,
                OneOfTlocExtensionGreFromOptionsDef3,
            ]
        ]
        xconnect: Optional[
            Union[
                OneOfXconnectOptionsDef1,
                OneOfXconnectOptionsDef2,
                OneOfXconnectOptionsDef3,
            ]
        ]


    class OneOfLoadIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfLoadIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLoadIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


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


    class OneOfIpDirectedBroadcastOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfIpDirectedBroadcastOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpDirectedBroadcastOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class Advanced:
        """
        Advanced Attributes
        """

        arp_timeout: Optional[
            Union[
                OneOfArpTimeoutOptionsDef1,
                OneOfArpTimeoutOptionsDef2,
                OneOfArpTimeoutOptionsDef3,
            ]
        ]
        autonegotiate: Optional[
            Union[
                OneOfAutonegotiateOptionsDef1,
                OneOfAutonegotiateOptionsDef2,
                OneOfAutonegotiateOptionsDef3,
            ]
        ]
        duplex: Optional[
            Union[
                OneOfDuplexOptionsDef1,
                OneOfDuplexOptionsDef2,
                OneOfDuplexOptionsDef3,
            ]
        ]
        icmp_redirect_disable: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        intrf_mtu: Optional[
            Union[
                OneOfIntrfMtuOptionsDef1,
                OneOfIntrfMtuOptionsDef2,
                OneOfIntrfMtuOptionsDef3,
            ]
        ]
        ip_directed_broadcast: Optional[
            Union[
                OneOfIpDirectedBroadcastOptionsDef1,
                OneOfIpDirectedBroadcastOptionsDef2,
                OneOfIpDirectedBroadcastOptionsDef3,
            ]
        ]
        ip_mtu: Optional[
            Union[
                OneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                OneOfMtuOptionsDef3,
            ]
        ]
        load_interval: Optional[
            Union[
                OneOfLoadIntervalOptionsDef1,
                OneOfLoadIntervalOptionsDef2,
                OneOfLoadIntervalOptionsDef3,
            ]
        ]
        mac_address: Optional[
            Union[
                OneOfMacAddressOptionsDef1,
                OneOfMacAddressOptionsDef2,
                OneOfMacAddressOptionsDef3,
            ]
        ]
        media_type: Optional[
            Union[
                OneOfMediaTypeOptionsDef1,
                OneOfMediaTypeOptionsDef2,
                OneOfMediaTypeOptionsDef3,
            ]
        ]
        speed: Optional[
            Union[
                OneOfSpeedOptionsDef1,
                OneOfSpeedOptionsDef2,
                OneOfSpeedOptionsDef3,
            ]
        ]
        tcp_mss: Optional[
            Union[
                OneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]
        tloc_extension: Optional[
            Union[
                OneOfTlocExtensionOptionsDef1,
                OneOfTlocExtensionOptionsDef2,
                OneOfTlocExtensionOptionsDef3,
            ]
        ]
        # Extend remote TLOC over a GRE tunnel to a local WAN interface
        tloc_extension_gre_from: Optional[TlocExtensionGreFrom]
        tracker: Optional[
            Union[
                OneOfTrackerOptionsDef1,
                OneOfTrackerOptionsDef2,
                OneOfTrackerOptionsDef3,
            ]
        ]


    class EthernetData:
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        interface_name: Union[
            OneOfInterfaceNameOptionsDef1, OneOfInterfaceNameOptionsDef2
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tunnel_interface: Union[
            OneOfTunnelInterfaceOptionsDef1,
            OneOfTunnelInterfaceOptionsDef2,
        ]
        # ACL/QOS
        acl_qos: Optional[Union[AclQos1, AclQos2]]
        # Advanced Attributes
        advanced: Optional[Advanced]
        # Tunnel Interface Attributes
        allow_service: Optional[AllowService]
        # Configure ARP entries
        arp: Optional[List[Arp]]
        auto_detect_bandwidth: Optional[
            Union[
                OneOfAutoBandwidthDetectOptionsDef1,
                OneOfAutoBandwidthDetectOptionsDef2,
                OneOfAutoBandwidthDetectOptionsDef3,
            ]
        ]
        bandwidth_downstream: Optional[
            Union[
                OneOfBandwidthDownstreamOptionsDef1,
                OneOfBandwidthDownstreamOptionsDef2,
                OneOfBandwidthDownstreamOptionsDef3,
            ]
        ]
        bandwidth_upstream: Optional[
            Union[
                OneOfBandwidthUpstreamOptionsDef1,
                OneOfBandwidthUpstreamOptionsDef2,
                OneOfBandwidthUpstreamOptionsDef3,
            ]
        ]
        block_non_source_ip: Optional[
            Union[
                OneOfBlockNonSourceIpOptionsDef1,
                OneOfBlockNonSourceIpOptionsDef2,
                OneOfBlockNonSourceIpOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                OneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        enable_ha_interlink_interface: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        # Encapsulation for TLOC
        encapsulation: Optional[List[Encapsulation]]
        intf_ip_address: Optional[Union[IntfIpAddress1, IntfIpAddress2]]
        intf_ip_v6_address: Optional[
            Union[IntfIpV6Address1, IntfIpV6Address2]
        ]
        iperf_server: Optional[
            Union[
                OneOfIperfServerOptionsDef1,
                OneOfIperfServerOptionsDef2,
                OneOfIperfServerOptionsDef3,
            ]
        ]
        # Multi-Region Fabric
        multi_region_fabric: Optional[MultiRegionFabric]
        nat: Optional[
            Union[
                OneOfNatOptionsDef1,
                OneOfNatOptionsDef2,
                OneOfNatOptionsDef3,
            ]
        ]
        # NAT Attributes IpV4
        nat_attributes_ipv4: Optional[NatAttributesIpv4]
        # NAT Attributes Ipv6
        nat_attributes_ipv6: Optional[NatAttributesIpv6]
        nat_ipv6: Optional[
            Union[
                OneOfNatOptionsDef1,
                OneOfNatOptionsDef2,
                OneOfNatOptionsDef3,
            ]
        ]
        port_channel: Optional[Union[PortChannel1, PortChannel2]]
        port_channel_interface: Optional[
            Union[
                OneOfPortChannelOptionsDef1, OneOfPortChannelOptionsDef2
            ]
        ]
        port_channel_member_interface: Optional[
            Union[
                OneOfPortChannelMemberOptionsDef1,
                OneOfPortChannelMemberOptionsDef2,
            ]
        ]
        service_provider: Optional[
            Union[
                OneOfServiceProviderOptionsDef1,
                OneOfServiceProviderOptionsDef2,
                OneOfServiceProviderOptionsDef3,
            ]
        ]
        # Tunnel Interface Attributes
        tunnel: Optional[Tunnel]


    class Payload:
        """
        WAN VPN Interface Ethernet profile parcel schema for POST request
        """

        data: EthernetData
        name: str
        description: Optional[str]
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
        # WAN VPN Interface Ethernet profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanTransportWanVpnInterfaceEthernetPayload:
        data: Optional[List[Data]]


    class CreateWanVpnInterfaceEthernetParcelForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class InterfaceEthernetData:
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        interface_name: Union[
            OneOfInterfaceNameOptionsDef1, OneOfInterfaceNameOptionsDef2
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tunnel_interface: Union[
            OneOfTunnelInterfaceOptionsDef1,
            OneOfTunnelInterfaceOptionsDef2,
        ]
        # ACL/QOS
        acl_qos: Optional[Union[AclQos1, AclQos2]]
        # Advanced Attributes
        advanced: Optional[Advanced]
        # Tunnel Interface Attributes
        allow_service: Optional[AllowService]
        # Configure ARP entries
        arp: Optional[List[Arp]]
        auto_detect_bandwidth: Optional[
            Union[
                OneOfAutoBandwidthDetectOptionsDef1,
                OneOfAutoBandwidthDetectOptionsDef2,
                OneOfAutoBandwidthDetectOptionsDef3,
            ]
        ]
        bandwidth_downstream: Optional[
            Union[
                OneOfBandwidthDownstreamOptionsDef1,
                OneOfBandwidthDownstreamOptionsDef2,
                OneOfBandwidthDownstreamOptionsDef3,
            ]
        ]
        bandwidth_upstream: Optional[
            Union[
                OneOfBandwidthUpstreamOptionsDef1,
                OneOfBandwidthUpstreamOptionsDef2,
                OneOfBandwidthUpstreamOptionsDef3,
            ]
        ]
        block_non_source_ip: Optional[
            Union[
                OneOfBlockNonSourceIpOptionsDef1,
                OneOfBlockNonSourceIpOptionsDef2,
                OneOfBlockNonSourceIpOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                OneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        enable_ha_interlink_interface: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        # Encapsulation for TLOC
        encapsulation: Optional[List[Encapsulation]]
        intf_ip_address: Optional[Union[IntfIpAddress1, IntfIpAddress2]]
        intf_ip_v6_address: Optional[
            Union[IntfIpV6Address1, IntfIpV6Address2]
        ]
        iperf_server: Optional[
            Union[
                OneOfIperfServerOptionsDef1,
                OneOfIperfServerOptionsDef2,
                OneOfIperfServerOptionsDef3,
            ]
        ]
        # Multi-Region Fabric
        multi_region_fabric: Optional[MultiRegionFabric]
        nat: Optional[
            Union[
                OneOfNatOptionsDef1,
                OneOfNatOptionsDef2,
                OneOfNatOptionsDef3,
            ]
        ]
        # NAT Attributes IpV4
        nat_attributes_ipv4: Optional[NatAttributesIpv4]
        # NAT Attributes Ipv6
        nat_attributes_ipv6: Optional[NatAttributesIpv6]
        nat_ipv6: Optional[
            Union[
                OneOfNatOptionsDef1,
                OneOfNatOptionsDef2,
                OneOfNatOptionsDef3,
            ]
        ]
        port_channel: Optional[Union[PortChannel1, PortChannel2]]
        port_channel_interface: Optional[
            Union[
                OneOfPortChannelOptionsDef1, OneOfPortChannelOptionsDef2
            ]
        ]
        port_channel_member_interface: Optional[
            Union[
                OneOfPortChannelMemberOptionsDef1,
                OneOfPortChannelMemberOptionsDef2,
            ]
        ]
        service_provider: Optional[
            Union[
                OneOfServiceProviderOptionsDef1,
                OneOfServiceProviderOptionsDef2,
                OneOfServiceProviderOptionsDef3,
            ]
        ]
        # Tunnel Interface Attributes
        tunnel: Optional[Tunnel]


    class CreateWanVpnInterfaceEthernetParcelForTransportPostRequest:
        """
        WAN VPN Interface Ethernet profile parcel schema for POST request
        """

        data: InterfaceEthernetData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class EthernetOneOfPortChannelLoadBalanceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EthernetPortChannelLoadBalanceDef  # pytype: disable=annotation-type-mismatch


    class EthernetOneOfLacpMinBundleOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfLacpMaxBundleOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfLacpModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EthernetPortChannelLacpModeDef  # pytype: disable=annotation-type-mismatch


    class EthernetOneOfLacpModeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: EthernetPortChannelLacpModeActiveDef  # pytype: disable=annotation-type-mismatch


    class EthernetOneOfLacpRateOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EthernetLacpRateDef  # pytype: disable=annotation-type-mismatch


    class EthernetOneOfLacpPortPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetPortChannelMemberLinks:
        interface: ParcelReferenceDef
        lacp_mode: Union[
            EthernetOneOfLacpModeOptionsDef1,
            OneOfLacpModeOptionsDef2,
            EthernetOneOfLacpModeOptionsDef3,
        ]
        lacp_port_priority: Optional[
            Union[
                EthernetOneOfLacpPortPriorityOptionsDef1,
                OneOfLacpPortPriorityOptionsDef2,
                OneOfLacpPortPriorityOptionsDef3,
            ]
        ]
        lacp_rate: Optional[
            Union[
                EthernetOneOfLacpRateOptionsDef1,
                OneOfLacpRateOptionsDef2,
                OneOfLacpRateOptionsDef3,
            ]
        ]


    class EthernetLacpModeMainInterface:
        # Configure Port-Channel member links
        port_channel_member_links: List[
            InterfaceEthernetPortChannelMemberLinks
        ]
        lacp_fast_switchover: Optional[
            Union[
                OneOfLacpFastSwitchoverOptionsDef1,
                OneOfLacpFastSwitchoverOptionsDef2,
                OneOfLacpFastSwitchoverOptionsDef3,
            ]
        ]
        lacp_max_bundle: Optional[
            Union[
                EthernetOneOfLacpMaxBundleOptionsDef1,
                OneOfLacpMaxBundleOptionsDef2,
                OneOfLacpMaxBundleOptionsDef3,
            ]
        ]
        lacp_min_bundle: Optional[
            Union[
                EthernetOneOfLacpMinBundleOptionsDef1,
                OneOfLacpMinBundleOptionsDef2,
                OneOfLacpMinBundleOptionsDef3,
            ]
        ]
        load_balance: Optional[
            Union[
                EthernetOneOfPortChannelLoadBalanceOptionsDef1,
                OneOfPortChannelLoadBalanceOptionsDef2,
                OneOfPortChannelLoadBalanceOptionsDef3,
            ]
        ]
        port_channel_qos_aggregate: Optional[
            Union[
                OneOfPortChannelQosAggregateOptionsDef1,
                OneOfPortChannelQosAggregateOptionsDef2,
                OneOfPortChannelQosAggregateOptionsDef3,
            ]
        ]


    class EthernetMainInterface1:
        """
        Port-channel Lacp mode Main Interface
        """

        lacp_mode_main_interface: EthernetLacpModeMainInterface


    class InterfaceEthernetOneOfPortChannelLoadBalanceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetPortChannelLoadBalanceDef  # pytype: disable=annotation-type-mismatch


    class VpnInterfaceEthernetPortChannelMemberLinks:
        interface: ParcelReferenceDef


    class EthernetStaticModeMainInterface:
        # Configure Port-Channel member links
        port_channel_member_links: List[
            VpnInterfaceEthernetPortChannelMemberLinks
        ]
        load_balance: Optional[
            Union[
                InterfaceEthernetOneOfPortChannelLoadBalanceOptionsDef1,
                OneOfPortChannelLoadBalanceOptionsDef2,
                OneOfPortChannelLoadBalanceOptionsDef3,
            ]
        ]
        port_channel_qos_aggregate: Optional[
            Union[
                OneOfPortChannelQosAggregateOptionsDef1,
                OneOfPortChannelQosAggregateOptionsDef2,
                OneOfPortChannelQosAggregateOptionsDef3,
            ]
        ]


    class EthernetMainInterface2:
        """
        Port-channel Static mode Main Interface
        """

        static_mode_main_interface: EthernetStaticModeMainInterface


    class EthernetPortChannel1:
        """
        Port-channel Main Interface
        """

        main_interface: Union[
            EthernetMainInterface1, EthernetMainInterface2
        ]


    class EthernetOneOfDynamicDhcpDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfDynamicDhcpDistanceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetDynamic:
        dynamic_dhcp_distance: Union[
            OneOfDynamicDhcpDistanceOptionsDef1,
            EthernetOneOfDynamicDhcpDistanceOptionsDef2,
            EthernetOneOfDynamicDhcpDistanceOptionsDef3,
        ]


    class EthernetIntfIpAddress1:
        dynamic: InterfaceEthernetDynamic


    class EthernetOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetStaticIpV4AddressPrimary:
        """
        Static IpV4Address Primary
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            EthernetOneOfIpV4AddressOptionsDef2,
            OneOfIpV4AddressOptionsDef3,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1,
            OneOfIpV4SubnetMaskOptionsDef2,
            OneOfIpV4SubnetMaskOptionsDef3,
        ]


    class InterfaceEthernetStatic:
        # Static IpV4Address Primary
        static_ip_v4_address_primary: EthernetStaticIpV4AddressPrimary
        # Secondary IpV4 Addresses
        static_ip_v4_address_secondary: Optional[
            List[StaticIpV4AddressSecondary]
        ]


    class EthernetIntfIpAddress2:
        static: InterfaceEthernetStatic


    class EthernetOneOfListOfIpV4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class EthernetOneOfIperfServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfBandwidthUpstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfBandwidthDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EthernetModeDef  # pytype: disable=annotation-type-mismatch


    class EthernetOneOfBindOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfCarrierOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EthernetCarrierDef


    class EthernetOneOfCarrierOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: EthernetDefaultCarrierDef  # pytype: disable=annotation-type-mismatch


    class EthernetOneOfColorOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            EthernetColorDef  # pytype: disable=annotation-type-mismatch
        )


    class EthernetOneOfHelloIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfHelloIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetOneOfHelloToleranceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfHelloToleranceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetOneOfTlocExtensionGreToOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfMaxControlConnectionsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfNatRefreshIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfNatRefreshIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetOneOfControllerGroupListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class EthernetOneOfVmanageConnectionPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfVmanageConnectionPreferenceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetOneOfTunnelTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetTunnel:
        """
        Tunnel Interface Attributes
        """

        allow_fragmentation: Optional[
            Union[
                OneOfAllowFragmentationDef1,
                OneOfAllowFragmentationDef2,
                OneOfAllowFragmentationDef3,
            ]
        ]
        bandwidth_percent: Optional[
            Union[
                OneOfBandwidthPercentOptionsDef1,
                OneOfBandwidthPercentOptionsDef2,
                OneOfBandwidthPercentOptionsDef3,
            ]
        ]
        bind: Optional[
            Union[
                EthernetOneOfBindOptionsDef1,
                OneOfBindOptionsDef2,
                OneOfBindOptionsDef3,
            ]
        ]
        border: Optional[
            Union[
                OneOfBorderOptionsDef1,
                OneOfBorderOptionsDef2,
                OneOfBorderOptionsDef3,
            ]
        ]
        carrier: Optional[
            Union[
                EthernetOneOfCarrierOptionsDef1,
                OneOfCarrierOptionsDef2,
                EthernetOneOfCarrierOptionsDef3,
            ]
        ]
        clear_dont_fragment: Optional[
            Union[
                OneOfClearDontFragmentOptionsDef1,
                OneOfClearDontFragmentOptionsDef2,
                OneOfClearDontFragmentOptionsDef3,
            ]
        ]
        color: Optional[
            Union[
                EthernetOneOfColorOptionsDef1,
                OneOfColorOptionsDef2,
                OneOfColorOptionsDef3,
            ]
        ]
        cts_sgt_propagation: Optional[
            Union[
                OneOfPropagateSgtOptionsDef1,
                OneOfPropagateSgtOptionsDef2,
                OneOfPropagateSgtOptionsDef3,
            ]
        ]
        exclude_controller_group_list: Optional[
            Union[
                EthernetOneOfControllerGroupListOptionsDef1,
                OneOfControllerGroupListOptionsDef2,
                OneOfControllerGroupListOptionsDef3,
            ]
        ]
        group: Optional[
            Union[
                EthernetOneOfGroupOptionsDef1,
                OneOfGroupOptionsDef2,
                OneOfGroupOptionsDef3,
            ]
        ]
        hello_interval: Optional[
            Union[
                EthernetOneOfHelloIntervalOptionsDef1,
                OneOfHelloIntervalOptionsDef2,
                EthernetOneOfHelloIntervalOptionsDef3,
            ]
        ]
        hello_tolerance: Optional[
            Union[
                EthernetOneOfHelloToleranceOptionsDef1,
                OneOfHelloToleranceOptionsDef2,
                EthernetOneOfHelloToleranceOptionsDef3,
            ]
        ]
        last_resort_circuit: Optional[
            Union[
                OneOfLastResortCircuitOptionsDef1,
                OneOfLastResortCircuitOptionsDef2,
                OneOfLastResortCircuitOptionsDef3,
            ]
        ]
        low_bandwidth_link: Optional[
            Union[
                OneOfLowBandwidthLinkOptionsDef1,
                OneOfLowBandwidthLinkOptionsDef2,
                OneOfLowBandwidthLinkOptionsDef3,
            ]
        ]
        max_control_connections: Optional[
            Union[
                EthernetOneOfMaxControlConnectionsOptionsDef1,
                OneOfMaxControlConnectionsOptionsDef2,
                OneOfMaxControlConnectionsOptionsDef3,
            ]
        ]
        mode: Optional[
            Union[EthernetOneOfModeOptionsDef1, OneOfModeOptionsDef2]
        ]
        nat_refresh_interval: Optional[
            Union[
                EthernetOneOfNatRefreshIntervalOptionsDef1,
                OneOfNatRefreshIntervalOptionsDef2,
                EthernetOneOfNatRefreshIntervalOptionsDef3,
            ]
        ]
        network_broadcast: Optional[
            Union[
                OneOfNetworkBroadcastOptionsDef1,
                OneOfNetworkBroadcastOptionsDef2,
                OneOfNetworkBroadcastOptionsDef3,
            ]
        ]
        per_tunnel_qos: Optional[
            Union[
                OneOfPerTunnelQosOptionsDef1,
                OneOfPerTunnelQosOptionsDef2,
                OneOfPerTunnelQosOptionsDef3,
            ]
        ]
        port_hop: Optional[
            Union[
                OneOfPortHopOptionsDef1,
                OneOfPortHopOptionsDef2,
                OneOfPortHopOptionsDef3,
            ]
        ]
        restrict: Optional[
            Union[
                OneOfRestrictOptionsDef1,
                OneOfRestrictOptionsDef2,
                OneOfRestrictOptionsDef3,
            ]
        ]
        set_sdwan_tunnel_mtu_to_max: Optional[
            Union[
                OneOfSetSdwanTunnelMtuToMaxDef1,
                OneOfSetSdwanTunnelMtuToMaxDef2,
                OneOfSetSdwanTunnelMtuToMaxDef3,
            ]
        ]
        tloc_extension_gre_to: Optional[
            Union[
                EthernetOneOfTlocExtensionGreToOptionsDef1,
                OneOfTlocExtensionGreToOptionsDef2,
                OneOfTlocExtensionGreToOptionsDef3,
            ]
        ]
        tunnel_tcp_mss: Optional[
            Union[
                EthernetOneOfTunnelTcpMssAdjustOptionsDef1,
                OneOfTunnelTcpMssAdjustOptionsDef2,
                OneOfTunnelTcpMssAdjustOptionsDef3,
            ]
        ]
        v_bond_as_stun_server: Optional[
            Union[
                OneOfVbondAsStunServerOptionsDef1,
                OneOfVbondAsStunServerOptionsDef2,
                OneOfVbondAsStunServerOptionsDef3,
            ]
        ]
        v_manage_connection_preference: Optional[
            Union[
                EthernetOneOfVmanageConnectionPreferenceOptionsDef1,
                OneOfVmanageConnectionPreferenceOptionsDef2,
                EthernetOneOfVmanageConnectionPreferenceOptionsDef3,
            ]
        ]


    class EthernetAllowService:
        """
        Tunnel Interface Attributes
        """

        all: Optional[
            Union[
                OneOfAllowAllOptionsDef1,
                OneOfAllowAllOptionsDef2,
                OneOfAllowAllOptionsDef3,
            ]
        ]
        bfd: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        bgp: Optional[
            Union[
                OneOfAllowBgpOptionsDef1,
                OneOfAllowBgpOptionsDef2,
                OneOfAllowBgpOptionsDef3,
            ]
        ]
        dhcp: Optional[
            Union[
                OneOfAllowDhcpOptionsDef1,
                OneOfAllowDhcpOptionsDef2,
                OneOfAllowDhcpOptionsDef3,
            ]
        ]
        dns: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        https: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        icmp: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        netconf: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        ntp: Optional[
            Union[
                OneOfAllowNtpOptionsDef1,
                OneOfAllowNtpOptionsDef2,
                OneOfAllowNtpOptionsDef3,
            ]
        ]
        ospf: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        snmp: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        ssh: Optional[
            Union[
                OneOfAllowSshOptionsDef1,
                OneOfAllowSshOptionsDef2,
                OneOfAllowSshOptionsDef3,
            ]
        ]
        stun: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]


    class EthernetOneOfEncapsulationEncapOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EthernetEncapsulationEncapDef  # pytype: disable=annotation-type-mismatch


    class EthernetOneOfEncapsulationPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfEncapsulationWeightOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfEncapsulationWeightOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetEncapsulation:
        encap: EthernetOneOfEncapsulationEncapOptionsDef
        preference: Optional[
            Union[
                EthernetOneOfEncapsulationPreferenceOptionsDef1,
                OneOfEncapsulationPreferenceOptionsDef2,
                OneOfEncapsulationPreferenceOptionsDef3,
            ]
        ]
        weight: Optional[
            Union[
                EthernetOneOfEncapsulationWeightOptionsDef1,
                OneOfEncapsulationWeightOptionsDef2,
                EthernetOneOfEncapsulationWeightOptionsDef3,
            ]
        ]


    class EthernetOneOfCoreRegionDef1:
        option_type: GlobalOptionTypeDef
        value: EthernetCoreRegionDef  # pytype: disable=annotation-type-mismatch


    class EthernetOneOfCoreRegionDef2:
        option_type: DefaultOptionTypeDef
        value: EthernetDefaultCoreRegionDef  # pytype: disable=annotation-type-mismatch


    class EthernetOneOfSecondaryRegionDef1:
        option_type: GlobalOptionTypeDef
        value: EthernetSecondaryRegionDef  # pytype: disable=annotation-type-mismatch


    class EthernetOneOfSecondaryRegionDef2:
        option_type: DefaultOptionTypeDef
        value: EthernetDefaultSecondaryRegionDef  # pytype: disable=annotation-type-mismatch


    class EthernetMultiRegionFabric:
        """
        Multi-Region Fabric
        """

        core_region: Optional[
            Union[
                EthernetOneOfCoreRegionDef1, EthernetOneOfCoreRegionDef2
            ]
        ]
        enable_core_region: Optional[
            Union[OneOfEnableRegionDef1, OneOfEnableRegionDef2]
        ]
        enable_secondary_region: Optional[
            Union[OneOfEnableRegionDef1, OneOfEnableRegionDef2]
        ]
        secondary_region: Optional[
            Union[
                EthernetOneOfSecondaryRegionDef1,
                EthernetOneOfSecondaryRegionDef2,
            ]
        ]


    class EthernetOneOfNatTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EthernetNatChoiceDef


    class EthernetOneOfNatTypeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: EthernetDefaultNatChoiceDef  # pytype: disable=annotation-type-mismatch


    class EthernetOneOfNatPoolRangeStartOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfNatPoolRangeEndOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfNatPoolPrefixLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetNatPool:
        """
        NAT Pool
        """

        prefix_length: Union[
            OneOfNatPoolPrefixLengthOptionsDef1,
            EthernetOneOfNatPoolPrefixLengthOptionsDef2,
        ]
        range_end: Union[
            OneOfNatPoolRangeEndOptionsDef1,
            EthernetOneOfNatPoolRangeEndOptionsDef2,
        ]
        range_start: Union[
            OneOfNatPoolRangeStartOptionsDef1,
            EthernetOneOfNatPoolRangeStartOptionsDef2,
        ]
        overload: Optional[
            Union[
                OneOfNatPoolOverloadOptionsDef1,
                OneOfNatPoolOverloadOptionsDef2,
                OneOfNatPoolOverloadOptionsDef3,
            ]
        ]


    class EthernetOneOfNatPoolNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfNatPoolRangeStartOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetOneOfNatPoolRangeEndOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetOneOfNatPoolPrefixLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetMultiplePool:
        name: Union[
            OneOfNatPoolNameOptionsDef1,
            EthernetOneOfNatPoolNameOptionsDef2,
        ]
        overload: Union[
            OneOfNatPoolOverloadOptionsDef1,
            OneOfNatPoolOverloadOptionsDef2,
            OneOfNatPoolOverloadOptionsDef3,
        ]
        prefix_length: Union[
            OneOfNatPoolPrefixLengthOptionsDef1,
            InterfaceEthernetOneOfNatPoolPrefixLengthOptionsDef2,
        ]
        range_end: Union[
            OneOfNatPoolRangeEndOptionsDef1,
            InterfaceEthernetOneOfNatPoolRangeEndOptionsDef2,
        ]
        range_start: Union[
            OneOfNatPoolRangeStartOptionsDef1,
            InterfaceEthernetOneOfNatPoolRangeStartOptionsDef2,
        ]
        enable_dual_router_ha_mapping: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]


    class EthernetMultipleLoopback:
        loopback_interface: Union[
            OneOfLoopbackInterfaceOptionsDef1,
            OneOfLoopbackInterfaceOptionsDef2,
            OneOfLoopbackInterfaceOptionsDef3,
        ]


    class EthernetOneOfUdpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfUdpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetOneOfTcpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfTcpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetOneOfStaticSourceIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfStaticTranslateIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfStaticNatDirectionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EthernetStaticNatDirectionDef


    class EthernetOneOfStaticNatDirectionOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: EthernetDefaultStaticNatDirectionDef  # pytype: disable=annotation-type-mismatch


    class EthernetOneOfStaticSourceVpnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfStaticSourceVpnOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetNewStaticNat:
        source_ip: Union[
            EthernetOneOfStaticSourceIpOptionsDef1,
            OneOfStaticSourceIpOptionsDef2,
        ]
        source_vpn: Union[
            EthernetOneOfStaticSourceVpnOptionsDef1,
            OneOfStaticSourceVpnOptionsDef2,
            EthernetOneOfStaticSourceVpnOptionsDef3,
        ]
        static_nat_direction: Union[
            EthernetOneOfStaticNatDirectionOptionsDef1,
            EthernetOneOfStaticNatDirectionOptionsDef2,
        ]
        translate_ip: Union[
            EthernetOneOfStaticTranslateIpOptionsDef1,
            OneOfStaticTranslateIpOptionsDef2,
        ]
        enable_dual_router_ha_mapping: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]


    class EthernetOneOfStaticPortForwardProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EthernetStaticPortForwardProtocolDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfStaticSourceIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfStaticSourcePortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfStaticTranslateIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfStaticTranslatePortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfStaticNatDirectionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetStaticNatDirectionDef


    class InterfaceEthernetOneOfStaticNatDirectionOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: InterfaceEthernetDefaultStaticNatDirectionDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfStaticSourceVpnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfStaticSourceVpnOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetStaticPortForward:
        protocol: Union[
            EthernetOneOfStaticPortForwardProtocolOptionsDef1,
            OneOfStaticPortForwardProtocolOptionsDef2,
        ]
        source_ip: Union[
            InterfaceEthernetOneOfStaticSourceIpOptionsDef1,
            OneOfStaticSourceIpOptionsDef2,
        ]
        source_port: Union[
            EthernetOneOfStaticSourcePortOptionsDef1,
            OneOfStaticSourcePortOptionsDef2,
        ]
        source_vpn: Union[
            InterfaceEthernetOneOfStaticSourceVpnOptionsDef1,
            OneOfStaticSourceVpnOptionsDef2,
            InterfaceEthernetOneOfStaticSourceVpnOptionsDef3,
        ]
        static_nat_direction: Union[
            InterfaceEthernetOneOfStaticNatDirectionOptionsDef1,
            InterfaceEthernetOneOfStaticNatDirectionOptionsDef2,
        ]
        translate_ip: Union[
            InterfaceEthernetOneOfStaticTranslateIpOptionsDef1,
            OneOfStaticTranslateIpOptionsDef2,
        ]
        translate_port: Union[
            EthernetOneOfStaticTranslatePortOptionsDef1,
            OneOfStaticTranslatePortOptionsDef2,
        ]
        enable_dual_router_ha_mapping: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]


    class EthernetNatAttributesIpv4:
        """
        NAT Attributes IpV4
        """

        nat_type: Union[
            EthernetOneOfNatTypeOptionsDef1,
            EthernetOneOfNatTypeOptionsDef2,
        ]
        tcp_timeout: Union[
            EthernetOneOfTcpTimeoutOptionsDef1,
            OneOfTcpTimeoutOptionsDef2,
            EthernetOneOfTcpTimeoutOptionsDef3,
        ]
        udp_timeout: Union[
            EthernetOneOfUdpTimeoutOptionsDef1,
            OneOfUdpTimeoutOptionsDef2,
            EthernetOneOfUdpTimeoutOptionsDef3,
        ]
        match_interface: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # NAT Multiple Loopback
        multiple_loopback: Optional[List[EthernetMultipleLoopback]]
        # NAT Multiple Pool
        multiple_pool: Optional[List[EthernetMultiplePool]]
        nat_loopback: Optional[
            Union[
                OneOfLoopbackInterfaceOptionsDef1,
                OneOfLoopbackInterfaceOptionsDef2,
                OneOfLoopbackInterfaceOptionsDef3,
            ]
        ]
        # NAT Pool
        nat_pool: Optional[EthernetNatPool]
        # static NAT
        new_static_nat: Optional[List[EthernetNewStaticNat]]
        # Configure Port Forward entries
        static_port_forward: Optional[List[EthernetStaticPortForward]]


    class EthernetOneOfStaticNat66TranslatedSourcePrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfStaticNat66SourceVpnIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetStaticNat66:
        source_prefix: Union[
            OneOfStaticNat66SourcePrefixOptionsDef1,
            OneOfStaticNat66SourcePrefixOptionsDef2,
        ]
        source_vpn_id: Union[
            EthernetOneOfStaticNat66SourceVpnIdOptionsDef1,
            OneOfStaticNat66SourceVpnIdOptionsDef2,
            OneOfStaticNat66SourceVpnIdOptionsDef3,
        ]
        egress_interface: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        translated_source_prefix: Optional[
            Union[
                EthernetOneOfStaticNat66TranslatedSourcePrefixOptionsDef1,
                OneOfStaticNat66TranslatedSourcePrefixOptionsDef2,
                OneOfStaticNat66TranslatedSourcePrefixOptionsDef3,
            ]
        ]


    class EthernetNatAttributesIpv6:
        """
        NAT Attributes Ipv6
        """

        nat64: Optional[
            Union[OneOfNat64Nat66OptionsDef1, OneOfNat64Nat66OptionsDef2]
        ]
        nat66: Optional[
            Union[OneOfNat64Nat66OptionsDef1, OneOfNat64Nat66OptionsDef2]
        ]
        # static NAT66
        static_nat66: Optional[List[EthernetStaticNat66]]


    class EthernetOneOfPeriodOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfPeriodOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnInterfaceEthernetOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetShapingRateUpstreamConfig:
        """
        adaptiveQoS Shaping Rate Upstream config
        """

        default_shaping_rate_upstream: Union[
            VpnInterfaceEthernetOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_upstream: Union[
            InterfaceEthernetOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_upstream: Union[
            EthernetOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class WanVpnInterfaceEthernetOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportWanVpnInterfaceEthernetOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanTransportWanVpnInterfaceEthernetOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetShapingRateDownstreamConfig:
        """
        adaptiveQoS Shaping Rate Downstream config
        """

        default_shaping_rate_downstream: Union[
            SdwanTransportWanVpnInterfaceEthernetOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_downstream: Union[
            TransportWanVpnInterfaceEthernetOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_downstream: Union[
            WanVpnInterfaceEthernetOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class EthernetAclQos1:
        adaptive_qo_s: Union[
            OneOfQosAdaptiveOptionsDef1, OneOfQosAdaptiveOptionsDef2
        ]
        shaping_rate_upstream: ShapingRateUpstream
        # adaptiveQoS Shaping Rate Upstream config
        shaping_rate_upstream_config: EthernetShapingRateUpstreamConfig
        adapt_period: Optional[
            Union[
                EthernetOneOfPeriodOptionsDef1,
                OneOfPeriodOptionsDef2,
                EthernetOneOfPeriodOptionsDef3,
            ]
        ]
        ipv4_acl_egress: Optional[ParcelReferenceDef]
        ipv4_acl_ingress: Optional[ParcelReferenceDef]
        ipv6_acl_egress: Optional[ParcelReferenceDef]
        ipv6_acl_ingress: Optional[ParcelReferenceDef]
        shaping_rate: Optional[
            Union[
                OneOfShapingRateOptionsDef1,
                OneOfShapingRateOptionsDef2,
                OneOfShapingRateOptionsDef3,
            ]
        ]
        shaping_rate_downstream: Optional[
            Union[
                OneOfShapingRateDownstreamOptionsDef1,
                OneOfShapingRateDownstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Downstream config
        shaping_rate_downstream_config: Optional[
            EthernetShapingRateDownstreamConfig
        ]


    class InterfaceEthernetOneOfPeriodOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfPeriodOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class FeatureProfileSdwanTransportWanVpnInterfaceEthernetOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdwanTransportWanVpnInterfaceEthernetOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetShapingRateUpstreamConfig:
        """
        adaptiveQoS Shaping Rate Upstream config
        """

        default_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef11,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_upstream: Union[
            V1FeatureProfileSdwanTransportWanVpnInterfaceEthernetOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_upstream: Union[
            FeatureProfileSdwanTransportWanVpnInterfaceEthernetOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class OneOfShapingRateUpOrDownstreamOptionsDef12:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef13:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef14:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetShapingRateDownstreamConfig:
        """
        adaptiveQoS Shaping Rate Downstream config
        """

        default_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef14,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef13,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef12,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class EthernetAclQos2:
        adaptive_qo_s: Union[
            OneOfQosAdaptiveOptionsDef1, OneOfQosAdaptiveOptionsDef2
        ]
        adapt_period: Optional[
            Union[
                InterfaceEthernetOneOfPeriodOptionsDef1,
                OneOfPeriodOptionsDef2,
                InterfaceEthernetOneOfPeriodOptionsDef3,
            ]
        ]
        ipv4_acl_egress: Optional[ParcelReferenceDef]
        ipv4_acl_ingress: Optional[ParcelReferenceDef]
        ipv6_acl_egress: Optional[ParcelReferenceDef]
        ipv6_acl_ingress: Optional[ParcelReferenceDef]
        shaping_rate: Optional[
            Union[
                OneOfShapingRateOptionsDef1,
                OneOfShapingRateOptionsDef2,
                OneOfShapingRateOptionsDef3,
            ]
        ]
        shaping_rate_downstream: Optional[
            Union[
                OneOfShapingRateDownstreamOptionsDef1,
                OneOfShapingRateDownstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Downstream config
        shaping_rate_downstream_config: Optional[
            InterfaceEthernetShapingRateDownstreamConfig
        ]
        shaping_rate_upstream: Optional[
            Union[
                OneOfShapingRateUpstreamOptionsDef1,
                OneOfShapingRateUpstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Upstream config
        shaping_rate_upstream_config: Optional[
            InterfaceEthernetShapingRateUpstreamConfig
        ]


    class InterfaceEthernetOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetArp:
        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            InterfaceEthernetOneOfIpV4AddressOptionsDef2,
            OneOfIpV4AddressOptionsDef3,
        ]
        mac_address: Union[
            OneOfMacAddressOptionsDef1,
            OneOfMacAddressOptionsDef2,
            OneOfMacAddressOptionsDef3,
        ]


    class EthernetOneOfDuplexOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            EthernetDuplexDef  # pytype: disable=annotation-type-mismatch
        )


    class EthernetOneOfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetOneOfIntrfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfIntrfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetOneOfTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfSpeedOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            EthernetSpeedDef  # pytype: disable=annotation-type-mismatch
        )


    class EthernetOneOfArpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfArpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetOneOfMediaTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EthernetMediaTypeDef  # pytype: disable=annotation-type-mismatch


    class EthernetOneOfTlocExtensionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfTlocExtensionGreFromOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfXconnectOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetTlocExtensionGreFrom:
        """
        Extend remote TLOC over a GRE tunnel to a local WAN interface
        """

        source_ip: Optional[
            Union[
                EthernetOneOfTlocExtensionGreFromOptionsDef1,
                OneOfTlocExtensionGreFromOptionsDef2,
                OneOfTlocExtensionGreFromOptionsDef3,
            ]
        ]
        xconnect: Optional[
            Union[
                EthernetOneOfXconnectOptionsDef1,
                OneOfXconnectOptionsDef2,
                OneOfXconnectOptionsDef3,
            ]
        ]


    class EthernetOneOfLoadIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfTrackerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetAdvanced:
        """
        Advanced Attributes
        """

        arp_timeout: Optional[
            Union[
                EthernetOneOfArpTimeoutOptionsDef1,
                OneOfArpTimeoutOptionsDef2,
                EthernetOneOfArpTimeoutOptionsDef3,
            ]
        ]
        autonegotiate: Optional[
            Union[
                OneOfAutonegotiateOptionsDef1,
                OneOfAutonegotiateOptionsDef2,
                OneOfAutonegotiateOptionsDef3,
            ]
        ]
        duplex: Optional[
            Union[
                EthernetOneOfDuplexOptionsDef1,
                OneOfDuplexOptionsDef2,
                OneOfDuplexOptionsDef3,
            ]
        ]
        icmp_redirect_disable: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        intrf_mtu: Optional[
            Union[
                EthernetOneOfIntrfMtuOptionsDef1,
                OneOfIntrfMtuOptionsDef2,
                EthernetOneOfIntrfMtuOptionsDef3,
            ]
        ]
        ip_directed_broadcast: Optional[
            Union[
                OneOfIpDirectedBroadcastOptionsDef1,
                OneOfIpDirectedBroadcastOptionsDef2,
                OneOfIpDirectedBroadcastOptionsDef3,
            ]
        ]
        ip_mtu: Optional[
            Union[
                EthernetOneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                EthernetOneOfMtuOptionsDef3,
            ]
        ]
        load_interval: Optional[
            Union[
                EthernetOneOfLoadIntervalOptionsDef1,
                OneOfLoadIntervalOptionsDef2,
                OneOfLoadIntervalOptionsDef3,
            ]
        ]
        mac_address: Optional[
            Union[
                OneOfMacAddressOptionsDef1,
                OneOfMacAddressOptionsDef2,
                OneOfMacAddressOptionsDef3,
            ]
        ]
        media_type: Optional[
            Union[
                EthernetOneOfMediaTypeOptionsDef1,
                OneOfMediaTypeOptionsDef2,
                OneOfMediaTypeOptionsDef3,
            ]
        ]
        speed: Optional[
            Union[
                EthernetOneOfSpeedOptionsDef1,
                OneOfSpeedOptionsDef2,
                OneOfSpeedOptionsDef3,
            ]
        ]
        tcp_mss: Optional[
            Union[
                EthernetOneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]
        tloc_extension: Optional[
            Union[
                EthernetOneOfTlocExtensionOptionsDef1,
                OneOfTlocExtensionOptionsDef2,
                OneOfTlocExtensionOptionsDef3,
            ]
        ]
        # Extend remote TLOC over a GRE tunnel to a local WAN interface
        tloc_extension_gre_from: Optional[EthernetTlocExtensionGreFrom]
        tracker: Optional[
            Union[
                EthernetOneOfTrackerOptionsDef1,
                OneOfTrackerOptionsDef2,
                OneOfTrackerOptionsDef3,
            ]
        ]


    class VpnInterfaceEthernetData:
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        interface_name: Union[
            OneOfInterfaceNameOptionsDef1, OneOfInterfaceNameOptionsDef2
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tunnel_interface: Union[
            OneOfTunnelInterfaceOptionsDef1,
            OneOfTunnelInterfaceOptionsDef2,
        ]
        # ACL/QOS
        acl_qos: Optional[Union[EthernetAclQos1, EthernetAclQos2]]
        # Advanced Attributes
        advanced: Optional[EthernetAdvanced]
        # Tunnel Interface Attributes
        allow_service: Optional[EthernetAllowService]
        # Configure ARP entries
        arp: Optional[List[EthernetArp]]
        auto_detect_bandwidth: Optional[
            Union[
                OneOfAutoBandwidthDetectOptionsDef1,
                OneOfAutoBandwidthDetectOptionsDef2,
                OneOfAutoBandwidthDetectOptionsDef3,
            ]
        ]
        bandwidth_downstream: Optional[
            Union[
                EthernetOneOfBandwidthDownstreamOptionsDef1,
                OneOfBandwidthDownstreamOptionsDef2,
                OneOfBandwidthDownstreamOptionsDef3,
            ]
        ]
        bandwidth_upstream: Optional[
            Union[
                EthernetOneOfBandwidthUpstreamOptionsDef1,
                OneOfBandwidthUpstreamOptionsDef2,
                OneOfBandwidthUpstreamOptionsDef3,
            ]
        ]
        block_non_source_ip: Optional[
            Union[
                OneOfBlockNonSourceIpOptionsDef1,
                OneOfBlockNonSourceIpOptionsDef2,
                OneOfBlockNonSourceIpOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                EthernetOneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        enable_ha_interlink_interface: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        # Encapsulation for TLOC
        encapsulation: Optional[List[EthernetEncapsulation]]
        intf_ip_address: Optional[
            Union[EthernetIntfIpAddress1, EthernetIntfIpAddress2]
        ]
        intf_ip_v6_address: Optional[
            Union[IntfIpV6Address1, IntfIpV6Address2]
        ]
        iperf_server: Optional[
            Union[
                EthernetOneOfIperfServerOptionsDef1,
                OneOfIperfServerOptionsDef2,
                OneOfIperfServerOptionsDef3,
            ]
        ]
        # Multi-Region Fabric
        multi_region_fabric: Optional[EthernetMultiRegionFabric]
        nat: Optional[
            Union[
                OneOfNatOptionsDef1,
                OneOfNatOptionsDef2,
                OneOfNatOptionsDef3,
            ]
        ]
        # NAT Attributes IpV4
        nat_attributes_ipv4: Optional[EthernetNatAttributesIpv4]
        # NAT Attributes Ipv6
        nat_attributes_ipv6: Optional[EthernetNatAttributesIpv6]
        nat_ipv6: Optional[
            Union[
                OneOfNatOptionsDef1,
                OneOfNatOptionsDef2,
                OneOfNatOptionsDef3,
            ]
        ]
        port_channel: Optional[Union[EthernetPortChannel1, PortChannel2]]
        port_channel_interface: Optional[
            Union[
                OneOfPortChannelOptionsDef1, OneOfPortChannelOptionsDef2
            ]
        ]
        port_channel_member_interface: Optional[
            Union[
                OneOfPortChannelMemberOptionsDef1,
                OneOfPortChannelMemberOptionsDef2,
            ]
        ]
        service_provider: Optional[
            Union[
                OneOfServiceProviderOptionsDef1,
                OneOfServiceProviderOptionsDef2,
                OneOfServiceProviderOptionsDef3,
            ]
        ]
        # Tunnel Interface Attributes
        tunnel: Optional[EthernetTunnel]


    class EthernetPayload:
        """
        WAN VPN Interface Ethernet profile parcel schema for PUT request
        """

        data: VpnInterfaceEthernetData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanTransportWanVpnInterfaceEthernetPayload:
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
        # WAN VPN Interface Ethernet profile parcel schema for PUT request
        payload: Optional[EthernetPayload]


    class EditWanVpnInterfaceEthernetParcelForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class VpnInterfaceEthernetOneOfPortChannelLoadBalanceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: VpnInterfaceEthernetPortChannelLoadBalanceDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfLacpMinBundleOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfLacpMaxBundleOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfLacpModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetPortChannelLacpModeDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfLacpModeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: InterfaceEthernetPortChannelLacpModeActiveDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfLacpRateOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetLacpRateDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfLacpPortPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnInterfaceEthernetPortChannelMemberLinks:
        interface: ParcelReferenceDef
        lacp_mode: Union[
            InterfaceEthernetOneOfLacpModeOptionsDef1,
            OneOfLacpModeOptionsDef2,
            InterfaceEthernetOneOfLacpModeOptionsDef3,
        ]
        lacp_port_priority: Optional[
            Union[
                InterfaceEthernetOneOfLacpPortPriorityOptionsDef1,
                OneOfLacpPortPriorityOptionsDef2,
                OneOfLacpPortPriorityOptionsDef3,
            ]
        ]
        lacp_rate: Optional[
            Union[
                InterfaceEthernetOneOfLacpRateOptionsDef1,
                OneOfLacpRateOptionsDef2,
                OneOfLacpRateOptionsDef3,
            ]
        ]


    class InterfaceEthernetLacpModeMainInterface:
        # Configure Port-Channel member links
        port_channel_member_links: List[
            WanVpnInterfaceEthernetPortChannelMemberLinks
        ]
        lacp_fast_switchover: Optional[
            Union[
                OneOfLacpFastSwitchoverOptionsDef1,
                OneOfLacpFastSwitchoverOptionsDef2,
                OneOfLacpFastSwitchoverOptionsDef3,
            ]
        ]
        lacp_max_bundle: Optional[
            Union[
                InterfaceEthernetOneOfLacpMaxBundleOptionsDef1,
                OneOfLacpMaxBundleOptionsDef2,
                OneOfLacpMaxBundleOptionsDef3,
            ]
        ]
        lacp_min_bundle: Optional[
            Union[
                InterfaceEthernetOneOfLacpMinBundleOptionsDef1,
                OneOfLacpMinBundleOptionsDef2,
                OneOfLacpMinBundleOptionsDef3,
            ]
        ]
        load_balance: Optional[
            Union[
                VpnInterfaceEthernetOneOfPortChannelLoadBalanceOptionsDef1,
                OneOfPortChannelLoadBalanceOptionsDef2,
                OneOfPortChannelLoadBalanceOptionsDef3,
            ]
        ]
        port_channel_qos_aggregate: Optional[
            Union[
                OneOfPortChannelQosAggregateOptionsDef1,
                OneOfPortChannelQosAggregateOptionsDef2,
                OneOfPortChannelQosAggregateOptionsDef3,
            ]
        ]


    class InterfaceEthernetMainInterface1:
        """
        Port-channel Lacp mode Main Interface
        """

        lacp_mode_main_interface: InterfaceEthernetLacpModeMainInterface


    class WanVpnInterfaceEthernetOneOfPortChannelLoadBalanceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: WanVpnInterfaceEthernetPortChannelLoadBalanceDef  # pytype: disable=annotation-type-mismatch


    class TransportWanVpnInterfaceEthernetPortChannelMemberLinks:
        interface: ParcelReferenceDef


    class InterfaceEthernetStaticModeMainInterface:
        # Configure Port-Channel member links
        port_channel_member_links: List[
            TransportWanVpnInterfaceEthernetPortChannelMemberLinks
        ]
        load_balance: Optional[
            Union[
                WanVpnInterfaceEthernetOneOfPortChannelLoadBalanceOptionsDef1,
                OneOfPortChannelLoadBalanceOptionsDef2,
                OneOfPortChannelLoadBalanceOptionsDef3,
            ]
        ]
        port_channel_qos_aggregate: Optional[
            Union[
                OneOfPortChannelQosAggregateOptionsDef1,
                OneOfPortChannelQosAggregateOptionsDef2,
                OneOfPortChannelQosAggregateOptionsDef3,
            ]
        ]


    class InterfaceEthernetMainInterface2:
        """
        Port-channel Static mode Main Interface
        """

        static_mode_main_interface: (
            InterfaceEthernetStaticModeMainInterface
        )


    class InterfaceEthernetPortChannel1:
        """
        Port-channel Main Interface
        """

        main_interface: Union[
            InterfaceEthernetMainInterface1,
            InterfaceEthernetMainInterface2,
        ]


    class InterfaceEthernetOneOfDynamicDhcpDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfDynamicDhcpDistanceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class VpnInterfaceEthernetDynamic:
        dynamic_dhcp_distance: Union[
            OneOfDynamicDhcpDistanceOptionsDef1,
            InterfaceEthernetOneOfDynamicDhcpDistanceOptionsDef2,
            InterfaceEthernetOneOfDynamicDhcpDistanceOptionsDef3,
        ]


    class InterfaceEthernetIntfIpAddress1:
        dynamic: VpnInterfaceEthernetDynamic


    class VpnInterfaceEthernetOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetStaticIpV4AddressPrimary:
        """
        Static IpV4Address Primary
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            VpnInterfaceEthernetOneOfIpV4AddressOptionsDef2,
            OneOfIpV4AddressOptionsDef3,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1,
            OneOfIpV4SubnetMaskOptionsDef2,
            OneOfIpV4SubnetMaskOptionsDef3,
        ]


    class VpnInterfaceEthernetStatic:
        # Static IpV4Address Primary
        static_ip_v4_address_primary: (
            InterfaceEthernetStaticIpV4AddressPrimary
        )
        # Secondary IpV4 Addresses
        static_ip_v4_address_secondary: Optional[
            List[StaticIpV4AddressSecondary]
        ]


    class InterfaceEthernetIntfIpAddress2:
        static: VpnInterfaceEthernetStatic


    class InterfaceEthernetOneOfListOfIpV4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class InterfaceEthernetOneOfIperfServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetOneOfBandwidthUpstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfBandwidthDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetModeDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfBindOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetOneOfCarrierOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetCarrierDef


    class InterfaceEthernetOneOfCarrierOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: InterfaceEthernetDefaultCarrierDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfColorOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetColorDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfHelloIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfHelloIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetOneOfHelloToleranceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfHelloToleranceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetOneOfTlocExtensionGreToOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetOneOfGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfMaxControlConnectionsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfNatRefreshIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfNatRefreshIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetOneOfControllerGroupListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class InterfaceEthernetOneOfVmanageConnectionPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfVmanageConnectionPreferenceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetOneOfTunnelTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetTunnel:
        """
        Tunnel Interface Attributes
        """

        allow_fragmentation: Optional[
            Union[
                OneOfAllowFragmentationDef1,
                OneOfAllowFragmentationDef2,
                OneOfAllowFragmentationDef3,
            ]
        ]
        bandwidth_percent: Optional[
            Union[
                OneOfBandwidthPercentOptionsDef1,
                OneOfBandwidthPercentOptionsDef2,
                OneOfBandwidthPercentOptionsDef3,
            ]
        ]
        bind: Optional[
            Union[
                InterfaceEthernetOneOfBindOptionsDef1,
                OneOfBindOptionsDef2,
                OneOfBindOptionsDef3,
            ]
        ]
        border: Optional[
            Union[
                OneOfBorderOptionsDef1,
                OneOfBorderOptionsDef2,
                OneOfBorderOptionsDef3,
            ]
        ]
        carrier: Optional[
            Union[
                InterfaceEthernetOneOfCarrierOptionsDef1,
                OneOfCarrierOptionsDef2,
                InterfaceEthernetOneOfCarrierOptionsDef3,
            ]
        ]
        clear_dont_fragment: Optional[
            Union[
                OneOfClearDontFragmentOptionsDef1,
                OneOfClearDontFragmentOptionsDef2,
                OneOfClearDontFragmentOptionsDef3,
            ]
        ]
        color: Optional[
            Union[
                InterfaceEthernetOneOfColorOptionsDef1,
                OneOfColorOptionsDef2,
                OneOfColorOptionsDef3,
            ]
        ]
        cts_sgt_propagation: Optional[
            Union[
                OneOfPropagateSgtOptionsDef1,
                OneOfPropagateSgtOptionsDef2,
                OneOfPropagateSgtOptionsDef3,
            ]
        ]
        exclude_controller_group_list: Optional[
            Union[
                InterfaceEthernetOneOfControllerGroupListOptionsDef1,
                OneOfControllerGroupListOptionsDef2,
                OneOfControllerGroupListOptionsDef3,
            ]
        ]
        group: Optional[
            Union[
                InterfaceEthernetOneOfGroupOptionsDef1,
                OneOfGroupOptionsDef2,
                OneOfGroupOptionsDef3,
            ]
        ]
        hello_interval: Optional[
            Union[
                InterfaceEthernetOneOfHelloIntervalOptionsDef1,
                OneOfHelloIntervalOptionsDef2,
                InterfaceEthernetOneOfHelloIntervalOptionsDef3,
            ]
        ]
        hello_tolerance: Optional[
            Union[
                InterfaceEthernetOneOfHelloToleranceOptionsDef1,
                OneOfHelloToleranceOptionsDef2,
                InterfaceEthernetOneOfHelloToleranceOptionsDef3,
            ]
        ]
        last_resort_circuit: Optional[
            Union[
                OneOfLastResortCircuitOptionsDef1,
                OneOfLastResortCircuitOptionsDef2,
                OneOfLastResortCircuitOptionsDef3,
            ]
        ]
        low_bandwidth_link: Optional[
            Union[
                OneOfLowBandwidthLinkOptionsDef1,
                OneOfLowBandwidthLinkOptionsDef2,
                OneOfLowBandwidthLinkOptionsDef3,
            ]
        ]
        max_control_connections: Optional[
            Union[
                InterfaceEthernetOneOfMaxControlConnectionsOptionsDef1,
                OneOfMaxControlConnectionsOptionsDef2,
                OneOfMaxControlConnectionsOptionsDef3,
            ]
        ]
        mode: Optional[
            Union[
                InterfaceEthernetOneOfModeOptionsDef1,
                OneOfModeOptionsDef2,
            ]
        ]
        nat_refresh_interval: Optional[
            Union[
                InterfaceEthernetOneOfNatRefreshIntervalOptionsDef1,
                OneOfNatRefreshIntervalOptionsDef2,
                InterfaceEthernetOneOfNatRefreshIntervalOptionsDef3,
            ]
        ]
        network_broadcast: Optional[
            Union[
                OneOfNetworkBroadcastOptionsDef1,
                OneOfNetworkBroadcastOptionsDef2,
                OneOfNetworkBroadcastOptionsDef3,
            ]
        ]
        per_tunnel_qos: Optional[
            Union[
                OneOfPerTunnelQosOptionsDef1,
                OneOfPerTunnelQosOptionsDef2,
                OneOfPerTunnelQosOptionsDef3,
            ]
        ]
        port_hop: Optional[
            Union[
                OneOfPortHopOptionsDef1,
                OneOfPortHopOptionsDef2,
                OneOfPortHopOptionsDef3,
            ]
        ]
        restrict: Optional[
            Union[
                OneOfRestrictOptionsDef1,
                OneOfRestrictOptionsDef2,
                OneOfRestrictOptionsDef3,
            ]
        ]
        set_sdwan_tunnel_mtu_to_max: Optional[
            Union[
                OneOfSetSdwanTunnelMtuToMaxDef1,
                OneOfSetSdwanTunnelMtuToMaxDef2,
                OneOfSetSdwanTunnelMtuToMaxDef3,
            ]
        ]
        tloc_extension_gre_to: Optional[
            Union[
                InterfaceEthernetOneOfTlocExtensionGreToOptionsDef1,
                OneOfTlocExtensionGreToOptionsDef2,
                OneOfTlocExtensionGreToOptionsDef3,
            ]
        ]
        tunnel_tcp_mss: Optional[
            Union[
                InterfaceEthernetOneOfTunnelTcpMssAdjustOptionsDef1,
                OneOfTunnelTcpMssAdjustOptionsDef2,
                OneOfTunnelTcpMssAdjustOptionsDef3,
            ]
        ]
        v_bond_as_stun_server: Optional[
            Union[
                OneOfVbondAsStunServerOptionsDef1,
                OneOfVbondAsStunServerOptionsDef2,
                OneOfVbondAsStunServerOptionsDef3,
            ]
        ]
        v_manage_connection_preference: Optional[
            Union[
                InterfaceEthernetOneOfVmanageConnectionPreferenceOptionsDef1,
                OneOfVmanageConnectionPreferenceOptionsDef2,
                InterfaceEthernetOneOfVmanageConnectionPreferenceOptionsDef3,
            ]
        ]


    class InterfaceEthernetAllowService:
        """
        Tunnel Interface Attributes
        """

        all: Optional[
            Union[
                OneOfAllowAllOptionsDef1,
                OneOfAllowAllOptionsDef2,
                OneOfAllowAllOptionsDef3,
            ]
        ]
        bfd: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        bgp: Optional[
            Union[
                OneOfAllowBgpOptionsDef1,
                OneOfAllowBgpOptionsDef2,
                OneOfAllowBgpOptionsDef3,
            ]
        ]
        dhcp: Optional[
            Union[
                OneOfAllowDhcpOptionsDef1,
                OneOfAllowDhcpOptionsDef2,
                OneOfAllowDhcpOptionsDef3,
            ]
        ]
        dns: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        https: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        icmp: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        netconf: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        ntp: Optional[
            Union[
                OneOfAllowNtpOptionsDef1,
                OneOfAllowNtpOptionsDef2,
                OneOfAllowNtpOptionsDef3,
            ]
        ]
        ospf: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        snmp: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        ssh: Optional[
            Union[
                OneOfAllowSshOptionsDef1,
                OneOfAllowSshOptionsDef2,
                OneOfAllowSshOptionsDef3,
            ]
        ]
        stun: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]


    class InterfaceEthernetOneOfEncapsulationEncapOptionsDef:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetEncapsulationEncapDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfEncapsulationPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfEncapsulationWeightOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfEncapsulationWeightOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetEncapsulation:
        encap: InterfaceEthernetOneOfEncapsulationEncapOptionsDef
        preference: Optional[
            Union[
                InterfaceEthernetOneOfEncapsulationPreferenceOptionsDef1,
                OneOfEncapsulationPreferenceOptionsDef2,
                OneOfEncapsulationPreferenceOptionsDef3,
            ]
        ]
        weight: Optional[
            Union[
                InterfaceEthernetOneOfEncapsulationWeightOptionsDef1,
                OneOfEncapsulationWeightOptionsDef2,
                InterfaceEthernetOneOfEncapsulationWeightOptionsDef3,
            ]
        ]


    class InterfaceEthernetOneOfCoreRegionDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetCoreRegionDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfCoreRegionDef2:
        option_type: DefaultOptionTypeDef
        value: InterfaceEthernetDefaultCoreRegionDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfSecondaryRegionDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetSecondaryRegionDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfSecondaryRegionDef2:
        option_type: DefaultOptionTypeDef
        value: InterfaceEthernetDefaultSecondaryRegionDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetMultiRegionFabric:
        """
        Multi-Region Fabric
        """

        core_region: Optional[
            Union[
                InterfaceEthernetOneOfCoreRegionDef1,
                InterfaceEthernetOneOfCoreRegionDef2,
            ]
        ]
        enable_core_region: Optional[
            Union[OneOfEnableRegionDef1, OneOfEnableRegionDef2]
        ]
        enable_secondary_region: Optional[
            Union[OneOfEnableRegionDef1, OneOfEnableRegionDef2]
        ]
        secondary_region: Optional[
            Union[
                InterfaceEthernetOneOfSecondaryRegionDef1,
                InterfaceEthernetOneOfSecondaryRegionDef2,
            ]
        ]


    class InterfaceEthernetOneOfNatTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetNatChoiceDef


    class InterfaceEthernetOneOfNatTypeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: InterfaceEthernetDefaultNatChoiceDef  # pytype: disable=annotation-type-mismatch


    class VpnInterfaceEthernetOneOfNatPoolRangeStartOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnInterfaceEthernetOneOfNatPoolRangeEndOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnInterfaceEthernetOneOfNatPoolPrefixLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetNatPool:
        """
        NAT Pool
        """

        prefix_length: Union[
            OneOfNatPoolPrefixLengthOptionsDef1,
            VpnInterfaceEthernetOneOfNatPoolPrefixLengthOptionsDef2,
        ]
        range_end: Union[
            OneOfNatPoolRangeEndOptionsDef1,
            VpnInterfaceEthernetOneOfNatPoolRangeEndOptionsDef2,
        ]
        range_start: Union[
            OneOfNatPoolRangeStartOptionsDef1,
            VpnInterfaceEthernetOneOfNatPoolRangeStartOptionsDef2,
        ]
        overload: Optional[
            Union[
                OneOfNatPoolOverloadOptionsDef1,
                OneOfNatPoolOverloadOptionsDef2,
                OneOfNatPoolOverloadOptionsDef3,
            ]
        ]


    class InterfaceEthernetOneOfNatPoolNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnInterfaceEthernetOneOfNatPoolRangeStartOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class WanVpnInterfaceEthernetOneOfNatPoolRangeEndOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class WanVpnInterfaceEthernetOneOfNatPoolPrefixLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetMultiplePool:
        name: Union[
            OneOfNatPoolNameOptionsDef1,
            InterfaceEthernetOneOfNatPoolNameOptionsDef2,
        ]
        overload: Union[
            OneOfNatPoolOverloadOptionsDef1,
            OneOfNatPoolOverloadOptionsDef2,
            OneOfNatPoolOverloadOptionsDef3,
        ]
        prefix_length: Union[
            OneOfNatPoolPrefixLengthOptionsDef1,
            WanVpnInterfaceEthernetOneOfNatPoolPrefixLengthOptionsDef2,
        ]
        range_end: Union[
            OneOfNatPoolRangeEndOptionsDef1,
            WanVpnInterfaceEthernetOneOfNatPoolRangeEndOptionsDef2,
        ]
        range_start: Union[
            OneOfNatPoolRangeStartOptionsDef1,
            WanVpnInterfaceEthernetOneOfNatPoolRangeStartOptionsDef2,
        ]
        enable_dual_router_ha_mapping: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]


    class InterfaceEthernetMultipleLoopback:
        loopback_interface: Union[
            OneOfLoopbackInterfaceOptionsDef1,
            OneOfLoopbackInterfaceOptionsDef2,
            OneOfLoopbackInterfaceOptionsDef3,
        ]


    class InterfaceEthernetOneOfUdpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfUdpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetOneOfTcpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfTcpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class VpnInterfaceEthernetOneOfStaticSourceIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnInterfaceEthernetOneOfStaticTranslateIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnInterfaceEthernetOneOfStaticNatDirectionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: VpnInterfaceEthernetStaticNatDirectionDef


    class VpnInterfaceEthernetOneOfStaticNatDirectionOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: VpnInterfaceEthernetDefaultStaticNatDirectionDef  # pytype: disable=annotation-type-mismatch


    class VpnInterfaceEthernetOneOfStaticSourceVpnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnInterfaceEthernetOneOfStaticSourceVpnOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetNewStaticNat:
        source_ip: Union[
            VpnInterfaceEthernetOneOfStaticSourceIpOptionsDef1,
            OneOfStaticSourceIpOptionsDef2,
        ]
        source_vpn: Union[
            VpnInterfaceEthernetOneOfStaticSourceVpnOptionsDef1,
            OneOfStaticSourceVpnOptionsDef2,
            VpnInterfaceEthernetOneOfStaticSourceVpnOptionsDef3,
        ]
        static_nat_direction: Union[
            VpnInterfaceEthernetOneOfStaticNatDirectionOptionsDef1,
            VpnInterfaceEthernetOneOfStaticNatDirectionOptionsDef2,
        ]
        translate_ip: Union[
            VpnInterfaceEthernetOneOfStaticTranslateIpOptionsDef1,
            OneOfStaticTranslateIpOptionsDef2,
        ]
        enable_dual_router_ha_mapping: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]


    class InterfaceEthernetOneOfStaticPortForwardProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetStaticPortForwardProtocolDef  # pytype: disable=annotation-type-mismatch


    class WanVpnInterfaceEthernetOneOfStaticSourceIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetOneOfStaticSourcePortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnInterfaceEthernetOneOfStaticTranslateIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetOneOfStaticTranslatePortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnInterfaceEthernetOneOfStaticNatDirectionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: WanVpnInterfaceEthernetStaticNatDirectionDef


    class WanVpnInterfaceEthernetOneOfStaticNatDirectionOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: WanVpnInterfaceEthernetDefaultStaticNatDirectionDef  # pytype: disable=annotation-type-mismatch


    class WanVpnInterfaceEthernetOneOfStaticSourceVpnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnInterfaceEthernetOneOfStaticSourceVpnOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetStaticPortForward:
        protocol: Union[
            InterfaceEthernetOneOfStaticPortForwardProtocolOptionsDef1,
            OneOfStaticPortForwardProtocolOptionsDef2,
        ]
        source_ip: Union[
            WanVpnInterfaceEthernetOneOfStaticSourceIpOptionsDef1,
            OneOfStaticSourceIpOptionsDef2,
        ]
        source_port: Union[
            InterfaceEthernetOneOfStaticSourcePortOptionsDef1,
            OneOfStaticSourcePortOptionsDef2,
        ]
        source_vpn: Union[
            WanVpnInterfaceEthernetOneOfStaticSourceVpnOptionsDef1,
            OneOfStaticSourceVpnOptionsDef2,
            WanVpnInterfaceEthernetOneOfStaticSourceVpnOptionsDef3,
        ]
        static_nat_direction: Union[
            WanVpnInterfaceEthernetOneOfStaticNatDirectionOptionsDef1,
            WanVpnInterfaceEthernetOneOfStaticNatDirectionOptionsDef2,
        ]
        translate_ip: Union[
            WanVpnInterfaceEthernetOneOfStaticTranslateIpOptionsDef1,
            OneOfStaticTranslateIpOptionsDef2,
        ]
        translate_port: Union[
            InterfaceEthernetOneOfStaticTranslatePortOptionsDef1,
            OneOfStaticTranslatePortOptionsDef2,
        ]
        enable_dual_router_ha_mapping: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]


    class InterfaceEthernetNatAttributesIpv4:
        """
        NAT Attributes IpV4
        """

        nat_type: Union[
            InterfaceEthernetOneOfNatTypeOptionsDef1,
            InterfaceEthernetOneOfNatTypeOptionsDef2,
        ]
        tcp_timeout: Union[
            InterfaceEthernetOneOfTcpTimeoutOptionsDef1,
            OneOfTcpTimeoutOptionsDef2,
            InterfaceEthernetOneOfTcpTimeoutOptionsDef3,
        ]
        udp_timeout: Union[
            InterfaceEthernetOneOfUdpTimeoutOptionsDef1,
            OneOfUdpTimeoutOptionsDef2,
            InterfaceEthernetOneOfUdpTimeoutOptionsDef3,
        ]
        match_interface: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # NAT Multiple Loopback
        multiple_loopback: Optional[
            List[InterfaceEthernetMultipleLoopback]
        ]
        # NAT Multiple Pool
        multiple_pool: Optional[List[InterfaceEthernetMultiplePool]]
        nat_loopback: Optional[
            Union[
                OneOfLoopbackInterfaceOptionsDef1,
                OneOfLoopbackInterfaceOptionsDef2,
                OneOfLoopbackInterfaceOptionsDef3,
            ]
        ]
        # NAT Pool
        nat_pool: Optional[InterfaceEthernetNatPool]
        # static NAT
        new_static_nat: Optional[List[InterfaceEthernetNewStaticNat]]
        # Configure Port Forward entries
        static_port_forward: Optional[
            List[InterfaceEthernetStaticPortForward]
        ]


    class InterfaceEthernetOneOfStaticNat66TranslatedSourcePrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetOneOfStaticNat66SourceVpnIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetStaticNat66:
        source_prefix: Union[
            OneOfStaticNat66SourcePrefixOptionsDef1,
            OneOfStaticNat66SourcePrefixOptionsDef2,
        ]
        source_vpn_id: Union[
            InterfaceEthernetOneOfStaticNat66SourceVpnIdOptionsDef1,
            OneOfStaticNat66SourceVpnIdOptionsDef2,
            OneOfStaticNat66SourceVpnIdOptionsDef3,
        ]
        egress_interface: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        translated_source_prefix: Optional[
            Union[
                InterfaceEthernetOneOfStaticNat66TranslatedSourcePrefixOptionsDef1,
                OneOfStaticNat66TranslatedSourcePrefixOptionsDef2,
                OneOfStaticNat66TranslatedSourcePrefixOptionsDef3,
            ]
        ]


    class InterfaceEthernetNatAttributesIpv6:
        """
        NAT Attributes Ipv6
        """

        nat64: Optional[
            Union[OneOfNat64Nat66OptionsDef1, OneOfNat64Nat66OptionsDef2]
        ]
        nat66: Optional[
            Union[OneOfNat64Nat66OptionsDef1, OneOfNat64Nat66OptionsDef2]
        ]
        # static NAT66
        static_nat66: Optional[List[InterfaceEthernetStaticNat66]]


    class VpnInterfaceEthernetOneOfPeriodOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnInterfaceEthernetOneOfPeriodOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef15:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef16:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef17:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnInterfaceEthernetShapingRateUpstreamConfig:
        """
        adaptiveQoS Shaping Rate Upstream config
        """

        default_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef17,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef16,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef15,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class OneOfShapingRateUpOrDownstreamOptionsDef18:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef19:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef110:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnInterfaceEthernetShapingRateDownstreamConfig:
        """
        adaptiveQoS Shaping Rate Downstream config
        """

        default_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef110,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef19,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef18,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class InterfaceEthernetAclQos1:
        adaptive_qo_s: Union[
            OneOfQosAdaptiveOptionsDef1, OneOfQosAdaptiveOptionsDef2
        ]
        shaping_rate_upstream: ShapingRateUpstream
        # adaptiveQoS Shaping Rate Upstream config
        shaping_rate_upstream_config: (
            VpnInterfaceEthernetShapingRateUpstreamConfig
        )
        adapt_period: Optional[
            Union[
                VpnInterfaceEthernetOneOfPeriodOptionsDef1,
                OneOfPeriodOptionsDef2,
                VpnInterfaceEthernetOneOfPeriodOptionsDef3,
            ]
        ]
        ipv4_acl_egress: Optional[ParcelReferenceDef]
        ipv4_acl_ingress: Optional[ParcelReferenceDef]
        ipv6_acl_egress: Optional[ParcelReferenceDef]
        ipv6_acl_ingress: Optional[ParcelReferenceDef]
        shaping_rate: Optional[
            Union[
                OneOfShapingRateOptionsDef1,
                OneOfShapingRateOptionsDef2,
                OneOfShapingRateOptionsDef3,
            ]
        ]
        shaping_rate_downstream: Optional[
            Union[
                OneOfShapingRateDownstreamOptionsDef1,
                OneOfShapingRateDownstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Downstream config
        shaping_rate_downstream_config: Optional[
            VpnInterfaceEthernetShapingRateDownstreamConfig
        ]


    class WanVpnInterfaceEthernetOneOfPeriodOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnInterfaceEthernetOneOfPeriodOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef111:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef112:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef113:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnInterfaceEthernetShapingRateUpstreamConfig:
        """
        adaptiveQoS Shaping Rate Upstream config
        """

        default_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef113,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef112,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef111,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class OneOfShapingRateUpOrDownstreamOptionsDef114:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef115:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef116:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnInterfaceEthernetShapingRateDownstreamConfig:
        """
        adaptiveQoS Shaping Rate Downstream config
        """

        default_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef116,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef115,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef114,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class InterfaceEthernetAclQos2:
        adaptive_qo_s: Union[
            OneOfQosAdaptiveOptionsDef1, OneOfQosAdaptiveOptionsDef2
        ]
        adapt_period: Optional[
            Union[
                WanVpnInterfaceEthernetOneOfPeriodOptionsDef1,
                OneOfPeriodOptionsDef2,
                WanVpnInterfaceEthernetOneOfPeriodOptionsDef3,
            ]
        ]
        ipv4_acl_egress: Optional[ParcelReferenceDef]
        ipv4_acl_ingress: Optional[ParcelReferenceDef]
        ipv6_acl_egress: Optional[ParcelReferenceDef]
        ipv6_acl_ingress: Optional[ParcelReferenceDef]
        shaping_rate: Optional[
            Union[
                OneOfShapingRateOptionsDef1,
                OneOfShapingRateOptionsDef2,
                OneOfShapingRateOptionsDef3,
            ]
        ]
        shaping_rate_downstream: Optional[
            Union[
                OneOfShapingRateDownstreamOptionsDef1,
                OneOfShapingRateDownstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Downstream config
        shaping_rate_downstream_config: Optional[
            WanVpnInterfaceEthernetShapingRateDownstreamConfig
        ]
        shaping_rate_upstream: Optional[
            Union[
                OneOfShapingRateUpstreamOptionsDef1,
                OneOfShapingRateUpstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Upstream config
        shaping_rate_upstream_config: Optional[
            WanVpnInterfaceEthernetShapingRateUpstreamConfig
        ]


    class WanVpnInterfaceEthernetOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetArp:
        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            WanVpnInterfaceEthernetOneOfIpV4AddressOptionsDef2,
            OneOfIpV4AddressOptionsDef3,
        ]
        mac_address: Union[
            OneOfMacAddressOptionsDef1,
            OneOfMacAddressOptionsDef2,
            OneOfMacAddressOptionsDef3,
        ]


    class InterfaceEthernetOneOfDuplexOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetDuplexDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetOneOfIntrfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfIntrfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetOneOfTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfSpeedOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetSpeedDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfArpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfArpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetOneOfMediaTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetMediaTypeDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfTlocExtensionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetOneOfTlocExtensionGreFromOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetOneOfXconnectOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetTlocExtensionGreFrom:
        """
        Extend remote TLOC over a GRE tunnel to a local WAN interface
        """

        source_ip: Optional[
            Union[
                InterfaceEthernetOneOfTlocExtensionGreFromOptionsDef1,
                OneOfTlocExtensionGreFromOptionsDef2,
                OneOfTlocExtensionGreFromOptionsDef3,
            ]
        ]
        xconnect: Optional[
            Union[
                InterfaceEthernetOneOfXconnectOptionsDef1,
                OneOfXconnectOptionsDef2,
                OneOfXconnectOptionsDef3,
            ]
        ]


    class InterfaceEthernetOneOfLoadIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfTrackerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetAdvanced:
        """
        Advanced Attributes
        """

        arp_timeout: Optional[
            Union[
                InterfaceEthernetOneOfArpTimeoutOptionsDef1,
                OneOfArpTimeoutOptionsDef2,
                InterfaceEthernetOneOfArpTimeoutOptionsDef3,
            ]
        ]
        autonegotiate: Optional[
            Union[
                OneOfAutonegotiateOptionsDef1,
                OneOfAutonegotiateOptionsDef2,
                OneOfAutonegotiateOptionsDef3,
            ]
        ]
        duplex: Optional[
            Union[
                InterfaceEthernetOneOfDuplexOptionsDef1,
                OneOfDuplexOptionsDef2,
                OneOfDuplexOptionsDef3,
            ]
        ]
        icmp_redirect_disable: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        intrf_mtu: Optional[
            Union[
                InterfaceEthernetOneOfIntrfMtuOptionsDef1,
                OneOfIntrfMtuOptionsDef2,
                InterfaceEthernetOneOfIntrfMtuOptionsDef3,
            ]
        ]
        ip_directed_broadcast: Optional[
            Union[
                OneOfIpDirectedBroadcastOptionsDef1,
                OneOfIpDirectedBroadcastOptionsDef2,
                OneOfIpDirectedBroadcastOptionsDef3,
            ]
        ]
        ip_mtu: Optional[
            Union[
                InterfaceEthernetOneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                InterfaceEthernetOneOfMtuOptionsDef3,
            ]
        ]
        load_interval: Optional[
            Union[
                InterfaceEthernetOneOfLoadIntervalOptionsDef1,
                OneOfLoadIntervalOptionsDef2,
                OneOfLoadIntervalOptionsDef3,
            ]
        ]
        mac_address: Optional[
            Union[
                OneOfMacAddressOptionsDef1,
                OneOfMacAddressOptionsDef2,
                OneOfMacAddressOptionsDef3,
            ]
        ]
        media_type: Optional[
            Union[
                InterfaceEthernetOneOfMediaTypeOptionsDef1,
                OneOfMediaTypeOptionsDef2,
                OneOfMediaTypeOptionsDef3,
            ]
        ]
        speed: Optional[
            Union[
                InterfaceEthernetOneOfSpeedOptionsDef1,
                OneOfSpeedOptionsDef2,
                OneOfSpeedOptionsDef3,
            ]
        ]
        tcp_mss: Optional[
            Union[
                InterfaceEthernetOneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]
        tloc_extension: Optional[
            Union[
                InterfaceEthernetOneOfTlocExtensionOptionsDef1,
                OneOfTlocExtensionOptionsDef2,
                OneOfTlocExtensionOptionsDef3,
            ]
        ]
        # Extend remote TLOC over a GRE tunnel to a local WAN interface
        tloc_extension_gre_from: Optional[
            InterfaceEthernetTlocExtensionGreFrom
        ]
        tracker: Optional[
            Union[
                InterfaceEthernetOneOfTrackerOptionsDef1,
                OneOfTrackerOptionsDef2,
                OneOfTrackerOptionsDef3,
            ]
        ]


    class WanVpnInterfaceEthernetData:
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        interface_name: Union[
            OneOfInterfaceNameOptionsDef1, OneOfInterfaceNameOptionsDef2
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tunnel_interface: Union[
            OneOfTunnelInterfaceOptionsDef1,
            OneOfTunnelInterfaceOptionsDef2,
        ]
        # ACL/QOS
        acl_qos: Optional[
            Union[InterfaceEthernetAclQos1, InterfaceEthernetAclQos2]
        ]
        # Advanced Attributes
        advanced: Optional[InterfaceEthernetAdvanced]
        # Tunnel Interface Attributes
        allow_service: Optional[InterfaceEthernetAllowService]
        # Configure ARP entries
        arp: Optional[List[InterfaceEthernetArp]]
        auto_detect_bandwidth: Optional[
            Union[
                OneOfAutoBandwidthDetectOptionsDef1,
                OneOfAutoBandwidthDetectOptionsDef2,
                OneOfAutoBandwidthDetectOptionsDef3,
            ]
        ]
        bandwidth_downstream: Optional[
            Union[
                InterfaceEthernetOneOfBandwidthDownstreamOptionsDef1,
                OneOfBandwidthDownstreamOptionsDef2,
                OneOfBandwidthDownstreamOptionsDef3,
            ]
        ]
        bandwidth_upstream: Optional[
            Union[
                InterfaceEthernetOneOfBandwidthUpstreamOptionsDef1,
                OneOfBandwidthUpstreamOptionsDef2,
                OneOfBandwidthUpstreamOptionsDef3,
            ]
        ]
        block_non_source_ip: Optional[
            Union[
                OneOfBlockNonSourceIpOptionsDef1,
                OneOfBlockNonSourceIpOptionsDef2,
                OneOfBlockNonSourceIpOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                InterfaceEthernetOneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        enable_ha_interlink_interface: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        # Encapsulation for TLOC
        encapsulation: Optional[List[InterfaceEthernetEncapsulation]]
        intf_ip_address: Optional[
            Union[
                InterfaceEthernetIntfIpAddress1,
                InterfaceEthernetIntfIpAddress2,
            ]
        ]
        intf_ip_v6_address: Optional[
            Union[IntfIpV6Address1, IntfIpV6Address2]
        ]
        iperf_server: Optional[
            Union[
                InterfaceEthernetOneOfIperfServerOptionsDef1,
                OneOfIperfServerOptionsDef2,
                OneOfIperfServerOptionsDef3,
            ]
        ]
        # Multi-Region Fabric
        multi_region_fabric: Optional[InterfaceEthernetMultiRegionFabric]
        nat: Optional[
            Union[
                OneOfNatOptionsDef1,
                OneOfNatOptionsDef2,
                OneOfNatOptionsDef3,
            ]
        ]
        # NAT Attributes IpV4
        nat_attributes_ipv4: Optional[InterfaceEthernetNatAttributesIpv4]
        # NAT Attributes Ipv6
        nat_attributes_ipv6: Optional[InterfaceEthernetNatAttributesIpv6]
        nat_ipv6: Optional[
            Union[
                OneOfNatOptionsDef1,
                OneOfNatOptionsDef2,
                OneOfNatOptionsDef3,
            ]
        ]
        port_channel: Optional[
            Union[InterfaceEthernetPortChannel1, PortChannel2]
        ]
        port_channel_interface: Optional[
            Union[
                OneOfPortChannelOptionsDef1, OneOfPortChannelOptionsDef2
            ]
        ]
        port_channel_member_interface: Optional[
            Union[
                OneOfPortChannelMemberOptionsDef1,
                OneOfPortChannelMemberOptionsDef2,
            ]
        ]
        service_provider: Optional[
            Union[
                OneOfServiceProviderOptionsDef1,
                OneOfServiceProviderOptionsDef2,
                OneOfServiceProviderOptionsDef3,
            ]
        ]
        # Tunnel Interface Attributes
        tunnel: Optional[InterfaceEthernetTunnel]


    class EditWanVpnInterfaceEthernetParcelForTransportPutRequest:
        """
        WAN VPN Interface Ethernet profile parcel schema for PUT request
        """

        data: WanVpnInterfaceEthernetData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


