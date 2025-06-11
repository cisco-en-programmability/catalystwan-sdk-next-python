======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanTrueDef = Literal[True]

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

    ClockRateDef = Literal[
        "1000000",
        "115200",
        "1200",
        "125000",
        "14400",
        "148000",
        "19200",
        "192000",
        "2000000",
        "2400",
        "250000",
        "256000",
        "28800",
        "32000",
        "38400",
        "384000",
        "4000000",
        "4800",
        "48000",
        "500000",
        "512000",
        "5300000",
        "56000",
        "57600",
        "64000",
        "72000",
        "768000",
        "800000",
        "8000000",
        "9600",
    ]

    EncapsulationSerialDef = Literal["frame-relay", "hdlc", "ppp"]

    BooleanFalseDef = Literal[False]

    ModeDef = Literal["spoke"]

    ValueDef = Literal[
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

    DefaultValueDef = Literal["default"]

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

    CoreRegionDef = Literal["core", "core-shared"]

    DefaultCoreRegionDef = Literal["core-shared"]

    SecondaryRegionDef = Literal["secondary-only", "secondary-shared"]

    DefaultSecondaryRegionDef = Literal["secondary-shared"]

    EncapsulationEncapDef = Literal["gre", "ipsec"]


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


    class OneOfBandwidthOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfBandwidthOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBandwidthOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfClockRateOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ClockRateDef  # pytype: disable=annotation-type-mismatch


    class OneOfClockRateOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfClockRateOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfEncapsulationSerialOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EncapsulationSerialDef  # pytype: disable=annotation-type-mismatch


    class OneOfEncapsulationSerialOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEncapsulationSerialOptionsDef3:
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


    class TunnelInterface:
        option_type: Optional[Any]
        value: Optional[Any]


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
        value: bool


    class OneOfOnOffDefaultFalseWithVariable1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnOffDefaultFalseWithVariable2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOnOffDefaultFalseWithVariable3:
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


    class OneOfValueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ValueDef


    class OneOfValueOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfValueOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultValueDef  # pytype: disable=annotation-type-mismatch


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


    class OneOfExcludeControllerGroupListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class OneOfExcludeControllerGroupListOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfExcludeControllerGroupListOptionsDef3:
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


    class OneOfTunnelClearDontFragmentOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfTunnelClearDontFragmentOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTunnelClearDontFragmentOptionsDef3:
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


    class Tunnel:
        """
        Tunnel Interface Attributes
        """

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
                OneOfTunnelClearDontFragmentOptionsDef1,
                OneOfTunnelClearDontFragmentOptionsDef2,
                OneOfTunnelClearDontFragmentOptionsDef3,
            ]
        ]
        color: Optional[
            Union[
                OneOfValueOptionsDef1,
                OneOfValueOptionsDef2,
                OneOfValueOptionsDef3,
            ]
        ]
        exclude_controller_group_list: Optional[
            Union[
                OneOfExcludeControllerGroupListOptionsDef1,
                OneOfExcludeControllerGroupListOptionsDef2,
                OneOfExcludeControllerGroupListOptionsDef3,
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
        per_tunnel_qos_aggregator: Optional[
            Union[
                OneOfOnOffDefaultFalseWithVariable1,
                OneOfOnOffDefaultFalseWithVariable2,
                OneOfOnOffDefaultFalseWithVariable3,
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
        tunnel_tcp_mss_adjust: Optional[
            Union[
                OneOfTunnelTcpMssAdjustOptionsDef1,
                OneOfTunnelTcpMssAdjustOptionsDef2,
                OneOfTunnelTcpMssAdjustOptionsDef3,
            ]
        ]
        vbond_as_stun_server: Optional[
            Union[
                OneOfVbondAsStunServerOptionsDef1,
                OneOfVbondAsStunServerOptionsDef2,
                OneOfVbondAsStunServerOptionsDef3,
            ]
        ]
        vmanage_connection_preference: Optional[
            Union[
                OneOfVmanageConnectionPreferenceOptionsDef1,
                OneOfVmanageConnectionPreferenceOptionsDef2,
                OneOfVmanageConnectionPreferenceOptionsDef3,
            ]
        ]


    class OneOfAllOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfBgpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfBgpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBgpOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfDhcpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfDhcpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDhcpOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfDnsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfDnsOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDnsOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfIcmpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfIcmpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIcmpOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfNetconfOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfNetconfOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNetconfOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfNtpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfNtpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNtpOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfOspfOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOspfOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOspfOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfSshdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfSshdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSshdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfStunOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfStunOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStunOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfHttpsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfHttpsOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHttpsOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfSnmpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfSnmpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSnmpOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfBfdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfBfdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBfdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class AllowService:
        """
        Tunnel Interface Attributes
        """

        all: Optional[
            Union[
                OneOfAllOptionsDef1,
                OneOfAllOptionsDef2,
                OneOfAllOptionsDef3,
            ]
        ]
        bfd: Optional[
            Union[
                OneOfBfdOptionsDef1,
                OneOfBfdOptionsDef2,
                OneOfBfdOptionsDef3,
            ]
        ]
        bgp: Optional[
            Union[
                OneOfBgpOptionsDef1,
                OneOfBgpOptionsDef2,
                OneOfBgpOptionsDef3,
            ]
        ]
        dhcp: Optional[
            Union[
                OneOfDhcpOptionsDef1,
                OneOfDhcpOptionsDef2,
                OneOfDhcpOptionsDef3,
            ]
        ]
        dns: Optional[
            Union[
                OneOfDnsOptionsDef1,
                OneOfDnsOptionsDef2,
                OneOfDnsOptionsDef3,
            ]
        ]
        https: Optional[
            Union[
                OneOfHttpsOptionsDef1,
                OneOfHttpsOptionsDef2,
                OneOfHttpsOptionsDef3,
            ]
        ]
        icmp: Optional[
            Union[
                OneOfIcmpOptionsDef1,
                OneOfIcmpOptionsDef2,
                OneOfIcmpOptionsDef3,
            ]
        ]
        netconf: Optional[
            Union[
                OneOfNetconfOptionsDef1,
                OneOfNetconfOptionsDef2,
                OneOfNetconfOptionsDef3,
            ]
        ]
        ntp: Optional[
            Union[
                OneOfNtpOptionsDef1,
                OneOfNtpOptionsDef2,
                OneOfNtpOptionsDef3,
            ]
        ]
        ospf: Optional[
            Union[
                OneOfOspfOptionsDef1,
                OneOfOspfOptionsDef2,
                OneOfOspfOptionsDef3,
            ]
        ]
        snmp: Optional[
            Union[
                OneOfSnmpOptionsDef1,
                OneOfSnmpOptionsDef2,
                OneOfSnmpOptionsDef3,
            ]
        ]
        sshd: Optional[
            Union[
                OneOfSshdOptionsDef1,
                OneOfSshdOptionsDef2,
                OneOfSshdOptionsDef3,
            ]
        ]
        stun: Optional[
            Union[
                OneOfStunOptionsDef1,
                OneOfStunOptionsDef2,
                OneOfStunOptionsDef3,
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


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class ParcelReferenceDef:
        ref_id: RefId


    class AclQos:
        """
        ACL part
        """

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


    class OneOfIpMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpMtuOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


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


    class Advanced:
        """
        advanced part
        """

        ip_mtu: Optional[
            Union[
                OneOfIpMtuOptionsDef1,
                OneOfIpMtuOptionsDef2,
                OneOfIpMtuOptionsDef3,
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
        tloc_extension: Optional[
            Union[
                OneOfTlocExtensionOptionsDef1,
                OneOfTlocExtensionOptionsDef2,
                OneOfTlocExtensionOptionsDef3,
            ]
        ]


    class Data1:
        interface_name: Union[
            OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2
        ]
        # ACL part
        acl_qos: Optional[AclQos]
        address_v4: Optional[Ipv4AddressAndMaskWithDefault]
        address_v6: Optional[
            Union[
                OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef1,
                OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef2,
                OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef3,
            ]
        ]
        # advanced part
        advanced: Optional[Advanced]
        # Tunnel Interface Attributes
        allow_service: Optional[AllowService]
        bandwidth: Optional[
            Union[
                OneOfBandwidthOptionsDef1,
                OneOfBandwidthOptionsDef2,
                OneOfBandwidthOptionsDef3,
            ]
        ]
        bandwidth_downstream: Optional[
            Union[
                OneOfBandwidthDownstreamOptionsDef1,
                OneOfBandwidthDownstreamOptionsDef2,
                OneOfBandwidthDownstreamOptionsDef3,
            ]
        ]
        clock_rate: Optional[
            Union[
                OneOfClockRateOptionsDef1,
                OneOfClockRateOptionsDef2,
                OneOfClockRateOptionsDef3,
            ]
        ]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]
        encapsulation: Optional[Any]
        encapsulation_serial: Optional[
            Union[
                OneOfEncapsulationSerialOptionsDef1,
                OneOfEncapsulationSerialOptionsDef2,
                OneOfEncapsulationSerialOptionsDef3,
            ]
        ]
        # Multi-Region Fabric
        multi_region_fabric: Optional[MultiRegionFabric]
        shutdown: Optional[
            Union[
                OneOfShutdownOptionsDef1,
                OneOfShutdownOptionsDef2,
                OneOfShutdownOptionsDef3,
            ]
        ]
        # Tunnel Interface Attributes
        tunnel: Optional[Tunnel]
        tunnel_interface: Optional[TunnelInterface]


    class OneOfTunnelInterfaceDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfTunnelInterfaceDef2:
        option_type: DefaultOptionTypeDef
        value: bool


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


    class Data2:
        interface_name: Union[
            OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2
        ]
        # ACL part
        acl_qos: Optional[AclQos]
        address_v4: Optional[Ipv4AddressAndMaskWithDefault]
        address_v6: Optional[
            Union[
                OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef1,
                OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef2,
                OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef3,
            ]
        ]
        # advanced part
        advanced: Optional[Advanced]
        # Tunnel Interface Attributes
        allow_service: Optional[AllowService]
        bandwidth: Optional[
            Union[
                OneOfBandwidthOptionsDef1,
                OneOfBandwidthOptionsDef2,
                OneOfBandwidthOptionsDef3,
            ]
        ]
        bandwidth_downstream: Optional[
            Union[
                OneOfBandwidthDownstreamOptionsDef1,
                OneOfBandwidthDownstreamOptionsDef2,
                OneOfBandwidthDownstreamOptionsDef3,
            ]
        ]
        clock_rate: Optional[
            Union[
                OneOfClockRateOptionsDef1,
                OneOfClockRateOptionsDef2,
                OneOfClockRateOptionsDef3,
            ]
        ]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]
        # Encapsulation for TLOC
        encapsulation: Optional[List[Encapsulation]]
        encapsulation_serial: Optional[
            Union[
                OneOfEncapsulationSerialOptionsDef1,
                OneOfEncapsulationSerialOptionsDef2,
                OneOfEncapsulationSerialOptionsDef3,
            ]
        ]
        # Multi-Region Fabric
        multi_region_fabric: Optional[MultiRegionFabric]
        shutdown: Optional[
            Union[
                OneOfShutdownOptionsDef1,
                OneOfShutdownOptionsDef2,
                OneOfShutdownOptionsDef3,
            ]
        ]
        # Tunnel Interface Attributes
        tunnel: Optional[Tunnel]
        tunnel_interface: Optional[
            Union[OneOfTunnelInterfaceDef1, OneOfTunnelInterfaceDef2]
        ]


    class Payload:
        """
        Serial profile parcel schema for POST request
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
        # Serial profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanTransportWanVpnInterfaceSerialPayload:
        data: Optional[List[Data]]


    class CreateWanVpnInterfaceSerialParcelForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateWanVpnInterfaceSerialParcelForTransportPostRequest:
        """
        Serial profile parcel schema for POST request
        """

        data: Union[Data1, Data2]
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanTransportWanVpnInterfaceSerialPayload:
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
        # Serial profile parcel schema for POST request
        payload: Optional[Payload]


    class EditWanVpnInterfaceSerialParcelForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditWanVpnInterfaceSerialParcelForTransportPutRequest:
        """
        Serial profile parcel schema for POST request
        """

        data: Union[Data1, Data2]
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


