======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    ExtensionsParcelTypeDef = Literal[
        "global-vrf",
        "global-vrf/routing/bgp",
        "global-vrf/wan/interface/ipsec",
        "management-vrf",
        "management-vrf/interface/ethernet",
        "vrf/routing/bgp",
        "vrf/wan/interface/ethernet",
        "vrf/wan/interface/gre",
        "vrf/wan/interface/ipsec",
    ]

    DefaultOptionTypeDef = Literal["default"]

    BooleanFalseDef = Literal[False]

    BooleanTrueDef = Literal[True]

    Value = Literal["ipv4-unicast", "vpnv4-unicast", "vpnv6-unicast"]

    MulticloudConnectionValue = Literal["disable-peer", "warning-only"]

    TransportMulticloudConnectionValue = Literal[
        "ipv6-unicast", "vpnv6-unicast"
    ]

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

    Ipv4AddressFamilyRedistributeProtocolDef = Literal[
        "connected", "nat", "ospf", "ospfv3", "static"
    ]

    Ipv6AddressFamilyRedistributeProtocolDef = Literal[
        "connected", "ospf", "static"
    ]

    Ipv4GatewayDef = Literal["dhcp", "nextHop", "null0"]

    DefaultIpv4GatewayDef = Literal["nextHop"]

    Ipv6RouteNatDef = Literal["NAT64", "NAT66"]

    MulticloudConnectionExtensionsParcelTypeDef = Literal[
        "global-vrf",
        "global-vrf/routing/bgp",
        "global-vrf/wan/interface/ipsec",
        "management-vrf",
        "management-vrf/interface/ethernet",
        "vrf/routing/bgp",
        "vrf/wan/interface/ethernet",
        "vrf/wan/interface/gre",
        "vrf/wan/interface/ipsec",
    ]

    SdRoutingTransportMulticloudConnectionValue = Literal[
        "disable-peer", "warning-only"
    ]

    FeatureProfileSdRoutingTransportMulticloudConnectionValue = Literal[
        "ipv6-unicast", "vpnv6-unicast"
    ]

    V1FeatureProfileSdRoutingTransportMulticloudConnectionValue = Literal[
        "disable-peer", "warning-only"
    ]

    MulticloudConnectionIpv4AddressFamilyRedistributeProtocolDef = (
        Literal["connected", "nat", "ospf", "ospfv3", "static"]
    )

    MulticloudConnectionIpv6AddressFamilyRedistributeProtocolDef = (
        Literal["connected", "ospf", "static"]
    )

    MulticloudConnectionIpv4GatewayDef = Literal[
        "dhcp", "nextHop", "null0"
    ]

    MulticloudConnectionDefaultIpv4GatewayDef = Literal["nextHop"]

    TransportMulticloudConnectionExtensionsParcelTypeDef = Literal[
        "global-vrf",
        "global-vrf/routing/bgp",
        "global-vrf/wan/interface/ipsec",
        "management-vrf",
        "management-vrf/interface/ethernet",
        "vrf/routing/bgp",
        "vrf/wan/interface/ethernet",
        "vrf/wan/interface/gre",
        "vrf/wan/interface/ipsec",
    ]

    Value1 = Literal["disable-peer", "warning-only"]

    Value2 = Literal["ipv6-unicast", "vpnv6-unicast"]

    Value3 = Literal["disable-peer", "warning-only"]

    TransportMulticloudConnectionIpv4AddressFamilyRedistributeProtocolDef = Literal[
        "connected", "nat", "ospf", "ospfv3", "static"
    ]

    TransportMulticloudConnectionIpv6AddressFamilyRedistributeProtocolDef = Literal[
        "connected", "ospf", "static"
    ]

    TransportMulticloudConnectionIpv4GatewayDef = Literal[
        "dhcp", "nextHop", "null0"
    ]

    TransportMulticloudConnectionDefaultIpv4GatewayDef = Literal[
        "nextHop"
    ]


    class VariableOptionTypeObjectDef:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfExtensionsParcelTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ExtensionsParcelTypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfExtensionsParcelTypeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfExtensionsParcelIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfExtensionsParcelIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNeighborDescriptionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNeighborDescriptionOptionsDef3:
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


    class OneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class OneOfAsNumOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class OneOfLocalAsOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLocalAsOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfKeepaliveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfKeepaliveOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHoldtimeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceNameOptionsDef3:
        option_type: DefaultOptionTypeDef


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


    class OneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborEbgpMultihopOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNeighborPasswordOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNeighborPasswordOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAsNumberOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNeighborAsNumberOptionsDef3:
        option_type: DefaultOptionTypeDef


    class WanIpv4NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class PolicyType:
        """
        Neighbor received maximum prefix policy is disabled.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class NeighborMaxPrefixConfigDef1:
        # Neighbor received maximum prefix policy is disabled.
        policy_type: PolicyType


    class MulticloudConnectionPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborMaxPrefixNumOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class NeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: MulticloudConnectionPolicyType
        prefix_num: Union[
            OneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2,
        ]
        threshold: Union[
            OneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            OneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class TransportMulticloudConnectionPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: MulticloudConnectionValue  # pytype: disable=annotation-type-mismatch


    class NeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: TransportMulticloudConnectionPolicyType
        prefix_num: Union[
            OneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        threshold: Union[
            OneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            OneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class OneOfRoutePolicyNameOptionsDef1:
        option_type: DefaultOptionTypeDef


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRoutePolicyNameOptionsDef2:
        ref_id: RefId


    class AddressFamily:
        family_type: WanIpv4NeighborAfTypeDef
        in_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        max_prefix_config: Optional[
            Union[
                NeighborMaxPrefixConfigDef1,
                NeighborMaxPrefixConfigDef2,
                NeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class Neighbor:
        address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        remote_as: Union[OneOfAsNumOptionsDef1, OneOfAsNumOptionsDef2]
        # Set BGP address family
        address_family: Optional[List[AddressFamily]]
        as_number: Optional[
            Union[
                OneOfNeighborAsNumberOptionsDef1,
                OneOfNeighborAsNumberOptionsDef2,
                OneOfNeighborAsNumberOptionsDef3,
            ]
        ]
        as_override: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        description: Optional[
            Union[
                OneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                OneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                OneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[OneOfHoldtimeOptionsDef1, OneOfHoldtimeOptionsDef2]
        ]
        if_name: Optional[
            Union[
                OneOfInterfaceNameOptionsDef1,
                OneOfInterfaceNameOptionsDef2,
                OneOfInterfaceNameOptionsDef3,
            ]
        ]
        keepalive: Optional[
            Union[OneOfKeepaliveOptionsDef1, OneOfKeepaliveOptionsDef2]
        ]
        local_as: Optional[
            Union[
                OneOfLocalAsOptionsDef1,
                OneOfLocalAsOptionsDef2,
                OneOfLocalAsOptionsDef3,
            ]
        ]
        next_hop_self: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        password: Optional[
            Union[
                OneOfNeighborPasswordOptionsDef1,
                OneOfNeighborPasswordOptionsDef2,
                OneOfNeighborPasswordOptionsDef3,
            ]
        ]
        send_community: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        send_ext_community: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        send_label: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        send_label_explicit: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]


    class OneOfIpv6AddrGlobalVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6AddrGlobalVariableOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class WanIpv6NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: TransportMulticloudConnectionValue  # pytype: disable=annotation-type-mismatch


    class MulticloudConnectionAddressFamily:
        family_type: WanIpv6NeighborAfTypeDef
        in_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        max_prefix_config: Optional[
            Union[
                NeighborMaxPrefixConfigDef1,
                NeighborMaxPrefixConfigDef2,
                NeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class Ipv6Neighbor:
        address: Union[
            OneOfIpv6AddrGlobalVariableOptionsDef1,
            OneOfIpv6AddrGlobalVariableOptionsDef2,
        ]
        remote_as: Union[OneOfAsNumOptionsDef1, OneOfAsNumOptionsDef2]
        # Set IPv6 BGP address family
        address_family: Optional[List[MulticloudConnectionAddressFamily]]
        as_number: Optional[
            Union[
                OneOfNeighborAsNumberOptionsDef1,
                OneOfNeighborAsNumberOptionsDef2,
                OneOfNeighborAsNumberOptionsDef3,
            ]
        ]
        as_override: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        description: Optional[
            Union[
                OneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                OneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                OneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[OneOfHoldtimeOptionsDef1, OneOfHoldtimeOptionsDef2]
        ]
        if_name: Optional[
            Union[
                OneOfInterfaceNameOptionsDef1,
                OneOfInterfaceNameOptionsDef2,
                OneOfInterfaceNameOptionsDef3,
            ]
        ]
        keepalive: Optional[
            Union[OneOfKeepaliveOptionsDef1, OneOfKeepaliveOptionsDef2]
        ]
        local_as: Optional[
            Union[
                OneOfLocalAsOptionsDef1,
                OneOfLocalAsOptionsDef2,
                OneOfLocalAsOptionsDef3,
            ]
        ]
        next_hop_self: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        password: Optional[
            Union[
                OneOfNeighborPasswordOptionsDef1,
                OneOfNeighborPasswordOptionsDef2,
                OneOfNeighborPasswordOptionsDef3,
            ]
        ]
        send_community: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        send_ext_community: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]


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


    class AggregateAddress:
        prefix: Ipv4AddressAndMaskDef
        as_set: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        summary_only: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]


    class Network:
        prefix: Ipv4AddressAndMaskDef


    class OneOfAddressFamilyPathsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAddressFamilyPathsOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAddressFamilyPathsOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfIpv4AddressFamilyRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Ipv4AddressFamilyRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class OneOfIpv4AddressFamilyRedistributeProtocolOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Redistribute:
        protocol: Union[
            OneOfIpv4AddressFamilyRedistributeProtocolOptionsDef1,
            OneOfIpv4AddressFamilyRedistributeProtocolOptionsDef2,
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class TransportMulticloudConnectionAddressFamily:
        """
        Set IPv4 unicast BGP address family
        """

        # Aggregate prefixes in specific range
        aggregate_address: Optional[List[AggregateAddress]]
        filter: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        name: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        # Configure the networks for BGP to advertise
        network: Optional[List[Network]]
        originate: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        paths: Optional[
            Union[
                OneOfAddressFamilyPathsOptionsDef1,
                OneOfAddressFamilyPathsOptionsDef2,
                OneOfAddressFamilyPathsOptionsDef3,
            ]
        ]
        # Redistribute routes into BGP
        redistribute: Optional[List[Redistribute]]


    class OneOfIpv6PrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6PrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Ipv6AggregateAddress:
        prefix: Union[
            OneOfIpv6PrefixOptionsDef1, OneOfIpv6PrefixOptionsDef2
        ]
        as_set: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        summary_only: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]


    class Ipv6Network:
        prefix: Union[
            OneOfIpv6PrefixOptionsDef1, OneOfIpv6PrefixOptionsDef2
        ]


    class OneOfIpv6AddressFamilyRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Ipv6AddressFamilyRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class OneOfIpv6AddressFamilyRedistributeProtocolOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class MulticloudConnectionRedistribute:
        protocol: Union[
            OneOfIpv6AddressFamilyRedistributeProtocolOptionsDef1,
            OneOfIpv6AddressFamilyRedistributeProtocolOptionsDef2,
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class Ipv6AddressFamily:
        """
        Set BGP address family
        """

        filter: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # IPv6 Aggregate prefixes in specific range
        ipv6_aggregate_address: Optional[List[Ipv6AggregateAddress]]
        # Configure the networks for BGP to advertise
        ipv6_network: Optional[List[Ipv6Network]]
        name: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        originate: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        paths: Optional[
            Union[
                OneOfAddressFamilyPathsOptionsDef1,
                OneOfAddressFamilyPathsOptionsDef2,
                OneOfAddressFamilyPathsOptionsDef3,
            ]
        ]
        # Redistribute routes into BGP
        redistribute: Optional[List[MulticloudConnectionRedistribute]]


    class MulticloudConnectionOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class Prefix:
        """
        Prefix
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            MulticloudConnectionOneOfIpV4AddressOptionsDef2,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class Gateway:
        value: Optional[Any]


    class OneOfIpv4NextHopAddressOptionsWithOutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv4NextHopAddressOptionsWithOutDefault2:
        option_type: GlobalOptionTypeDef
        value: Union[Any, str]


    class OneOfIpv4NextHopDistanceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv4NextHopDistanceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class NextHop:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            OneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class OneOfIpv4GatewayDistanceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv4GatewayDistanceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Ipv4Route1:
        gateway: Gateway
        # IPv4 Route Gateway Next Hop
        next_hop: List[NextHop]
        # Prefix
        prefix: Prefix
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                OneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]


    class OneOfIpv4RouteGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Ipv4GatewayDef  # pytype: disable=annotation-type-mismatch


    class OneOfIpv4RouteGatewayOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: DefaultIpv4GatewayDef  # pytype: disable=annotation-type-mismatch


    class Ipv4Route2:
        gateway: Union[
            OneOfIpv4RouteGatewayOptionsDef1,
            OneOfIpv4RouteGatewayOptionsDef2,
        ]
        # Prefix
        prefix: Prefix
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                OneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]
        # IPv4 Route Gateway Next Hop
        next_hop: Optional[List[NextHop]]


    class OneOfIpv6RoutePrefixOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6RoutePrefixOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6NextHopAddressOptionsWithOutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6NextHopAddressOptionsWithOutDefault2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6NextHopDistanceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv6NextHopDistanceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class MulticloudConnectionNextHop:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            OneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class NextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[List[MulticloudConnectionNextHop]]


    class OneOfIpRoute1:
        next_hop_container: NextHopContainer


    class OneOfIpv4V6RouteNull0OptionsWithoutVariable1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfIpv4V6RouteNull0OptionsWithoutVariable2:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfIpRoute2:
        null0: Union[
            OneOfIpv4V6RouteNull0OptionsWithoutVariable1,
            OneOfIpv4V6RouteNull0OptionsWithoutVariable2,
        ]


    class OneOfIpv6RouteNatOptionsWithoutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6RouteNatOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: Ipv6RouteNatDef  # pytype: disable=annotation-type-mismatch


    class OneOfIpRoute3:
        nat: Union[
            OneOfIpv6RouteNatOptionsWithoutDefault1,
            OneOfIpv6RouteNatOptionsWithoutDefault2,
        ]


    class Ipv6Route:
        one_of_ip_route: Union[
            OneOfIpRoute1, OneOfIpRoute2, OneOfIpRoute3
        ]
        prefix: Union[
            OneOfIpv6RoutePrefixOptionsDef1,
            OneOfIpv6RoutePrefixOptionsDef2,
        ]


    class TransportMulticloudConnectionData:
        """
        Parameters for the new Connection
        """

        # Set IPv4 unicast BGP address family
        address_family: Optional[
            TransportMulticloudConnectionAddressFamily
        ]
        # IPv4 Static Route
        ipv4_route: Optional[List[Union[Ipv4Route1, Ipv4Route2]]]
        # Set BGP address family
        ipv6_address_family: Optional[Ipv6AddressFamily]
        # Set BGP IPv6 neighbors
        ipv6_neighbor: Optional[List[Ipv6Neighbor]]
        # IPv6 Static Route
        ipv6_route: Optional[List[Ipv6Route]]
        # Set BGP IPv4 neighbors
        neighbor: Optional[List[Neighbor]]


    class Extensions:
        parcel_type: Union[
            OneOfExtensionsParcelTypeOptionsDef1,
            OneOfExtensionsParcelTypeOptionsDef2,
        ]
        #  Parameters for the new Connection
        data: Optional[TransportMulticloudConnectionData]
        parcel_id: Optional[
            Union[
                OneOfExtensionsParcelIdOptionsDef1,
                OneOfExtensionsParcelIdOptionsDef2,
            ]
        ]


    class MulticloudConnectionData:
        connection_name: VariableOptionTypeObjectDef
        # Extending Bgp Neighbors, Ip Routes, Interface Parcel Id reference and Route Policy for Transport Profile to build new Connections
        extensions: Optional[List[Extensions]]


    class Payload:
        """
        multi-cloud-connection profile parcel schema for POST request
        """

        data: Optional[MulticloudConnectionData]
        description: Optional[str]
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
        # multi-cloud-connection profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdRoutingTransportVrfWanMulticloudConnectionPayload:
        data: Optional[List[Data]]


    class CreateMultiCloudConnection1PostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SdRoutingTransportMulticloudConnectionData:
        connection_name: VariableOptionTypeObjectDef
        # Extending Bgp Neighbors, Ip Routes, Interface Parcel Id reference and Route Policy for Transport Profile to build new Connections
        extensions: Optional[List[Extensions]]


    class CreateMultiCloudConnection1PostRequest:
        """
        multi-cloud-connection profile parcel schema for POST request
        """

        data: Optional[SdRoutingTransportMulticloudConnectionData]
        description: Optional[str]
        name: Optional[str]


    class MulticloudConnectionOneOfExtensionsParcelTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: MulticloudConnectionExtensionsParcelTypeDef  # pytype: disable=annotation-type-mismatch


    class MulticloudConnectionOneOfExtensionsParcelIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class MulticloudConnectionOneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class MulticloudConnectionOneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class MulticloudConnectionOneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class MulticloudConnectionOneOfKeepaliveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionOneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class MulticloudConnectionOneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class MulticloudConnectionOneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionWanIpv4NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class SdRoutingTransportMulticloudConnectionPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class MulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class MulticloudConnectionOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionNeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: SdRoutingTransportMulticloudConnectionPolicyType
        prefix_num: Union[
            MulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            MulticloudConnectionOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2,
        ]
        threshold: Union[
            MulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            MulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class FeatureProfileSdRoutingTransportMulticloudConnectionPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: SdRoutingTransportMulticloudConnectionValue  # pytype: disable=annotation-type-mismatch


    class TransportMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class MulticloudConnectionNeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: (
            FeatureProfileSdRoutingTransportMulticloudConnectionPolicyType
        )
        prefix_num: Union[
            TransportMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        threshold: Union[
            TransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            TransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class SdRoutingTransportMulticloudConnectionAddressFamily:
        family_type: MulticloudConnectionWanIpv4NeighborAfTypeDef
        in_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        max_prefix_config: Optional[
            Union[
                NeighborMaxPrefixConfigDef1,
                MulticloudConnectionNeighborMaxPrefixConfigDef2,
                MulticloudConnectionNeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class MulticloudConnectionNeighbor:
        address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        remote_as: Union[
            MulticloudConnectionOneOfAsNumOptionsDef1,
            OneOfAsNumOptionsDef2,
        ]
        # Set BGP address family
        address_family: Optional[
            List[SdRoutingTransportMulticloudConnectionAddressFamily]
        ]
        as_number: Optional[
            Union[
                MulticloudConnectionOneOfNeighborAsNumberOptionsDef1,
                OneOfNeighborAsNumberOptionsDef2,
                OneOfNeighborAsNumberOptionsDef3,
            ]
        ]
        as_override: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        description: Optional[
            Union[
                MulticloudConnectionOneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                MulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                MulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                MulticloudConnectionOneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
            ]
        ]
        if_name: Optional[
            Union[
                OneOfInterfaceNameOptionsDef1,
                OneOfInterfaceNameOptionsDef2,
                OneOfInterfaceNameOptionsDef3,
            ]
        ]
        keepalive: Optional[
            Union[
                MulticloudConnectionOneOfKeepaliveOptionsDef1,
                OneOfKeepaliveOptionsDef2,
            ]
        ]
        local_as: Optional[
            Union[
                MulticloudConnectionOneOfLocalAsOptionsDef1,
                OneOfLocalAsOptionsDef2,
                OneOfLocalAsOptionsDef3,
            ]
        ]
        next_hop_self: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        password: Optional[
            Union[
                MulticloudConnectionOneOfNeighborPasswordOptionsDef1,
                OneOfNeighborPasswordOptionsDef2,
                OneOfNeighborPasswordOptionsDef3,
            ]
        ]
        send_community: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        send_ext_community: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        send_label: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        send_label_explicit: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]


    class TransportMulticloudConnectionOneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportMulticloudConnectionOneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class TransportMulticloudConnectionOneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class TransportMulticloudConnectionOneOfKeepaliveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportMulticloudConnectionOneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class TransportMulticloudConnectionOneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportMulticloudConnectionOneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionWanIpv6NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdRoutingTransportMulticloudConnectionValue  # pytype: disable=annotation-type-mismatch


    class V1FeatureProfileSdRoutingTransportMulticloudConnectionPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class SdRoutingTransportMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class TransportMulticloudConnectionOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportMulticloudConnectionNeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: V1FeatureProfileSdRoutingTransportMulticloudConnectionPolicyType
        prefix_num: Union[
            SdRoutingTransportMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            TransportMulticloudConnectionOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2,
        ]
        threshold: Union[
            SdRoutingTransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            SdRoutingTransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class PolicyType1:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: V1FeatureProfileSdRoutingTransportMulticloudConnectionValue  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class TransportMulticloudConnectionNeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: PolicyType1
        prefix_num: Union[
            FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        threshold: Union[
            FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class FeatureProfileSdRoutingTransportMulticloudConnectionAddressFamily:
        family_type: MulticloudConnectionWanIpv6NeighborAfTypeDef
        in_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        max_prefix_config: Optional[
            Union[
                NeighborMaxPrefixConfigDef1,
                TransportMulticloudConnectionNeighborMaxPrefixConfigDef2,
                TransportMulticloudConnectionNeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class MulticloudConnectionIpv6Neighbor:
        address: Union[
            OneOfIpv6AddrGlobalVariableOptionsDef1,
            OneOfIpv6AddrGlobalVariableOptionsDef2,
        ]
        remote_as: Union[
            TransportMulticloudConnectionOneOfAsNumOptionsDef1,
            OneOfAsNumOptionsDef2,
        ]
        # Set IPv6 BGP address family
        address_family: Optional[
            List[
                FeatureProfileSdRoutingTransportMulticloudConnectionAddressFamily
            ]
        ]
        as_number: Optional[
            Union[
                TransportMulticloudConnectionOneOfNeighborAsNumberOptionsDef1,
                OneOfNeighborAsNumberOptionsDef2,
                OneOfNeighborAsNumberOptionsDef3,
            ]
        ]
        as_override: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        description: Optional[
            Union[
                TransportMulticloudConnectionOneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                TransportMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                TransportMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                TransportMulticloudConnectionOneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
            ]
        ]
        if_name: Optional[
            Union[
                OneOfInterfaceNameOptionsDef1,
                OneOfInterfaceNameOptionsDef2,
                OneOfInterfaceNameOptionsDef3,
            ]
        ]
        keepalive: Optional[
            Union[
                TransportMulticloudConnectionOneOfKeepaliveOptionsDef1,
                OneOfKeepaliveOptionsDef2,
            ]
        ]
        local_as: Optional[
            Union[
                TransportMulticloudConnectionOneOfLocalAsOptionsDef1,
                OneOfLocalAsOptionsDef2,
                OneOfLocalAsOptionsDef3,
            ]
        ]
        next_hop_self: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        password: Optional[
            Union[
                TransportMulticloudConnectionOneOfNeighborPasswordOptionsDef1,
                OneOfNeighborPasswordOptionsDef2,
                OneOfNeighborPasswordOptionsDef3,
            ]
        ]
        send_community: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        send_ext_community: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]


    class MulticloudConnectionOneOfAddressFamilyPathsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionOneOfIpv4AddressFamilyRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: MulticloudConnectionIpv4AddressFamilyRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class TransportMulticloudConnectionRedistribute:
        protocol: Union[
            MulticloudConnectionOneOfIpv4AddressFamilyRedistributeProtocolOptionsDef1,
            OneOfIpv4AddressFamilyRedistributeProtocolOptionsDef2,
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class V1FeatureProfileSdRoutingTransportMulticloudConnectionAddressFamily:
        """
        Set IPv4 unicast BGP address family
        """

        # Aggregate prefixes in specific range
        aggregate_address: Optional[List[AggregateAddress]]
        filter: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        name: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        # Configure the networks for BGP to advertise
        network: Optional[List[Network]]
        originate: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        paths: Optional[
            Union[
                MulticloudConnectionOneOfAddressFamilyPathsOptionsDef1,
                OneOfAddressFamilyPathsOptionsDef2,
                OneOfAddressFamilyPathsOptionsDef3,
            ]
        ]
        # Redistribute routes into BGP
        redistribute: Optional[
            List[TransportMulticloudConnectionRedistribute]
        ]


    class TransportMulticloudConnectionOneOfAddressFamilyPathsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionOneOfIpv6AddressFamilyRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: MulticloudConnectionIpv6AddressFamilyRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class SdRoutingTransportMulticloudConnectionRedistribute:
        protocol: Union[
            MulticloudConnectionOneOfIpv6AddressFamilyRedistributeProtocolOptionsDef1,
            OneOfIpv6AddressFamilyRedistributeProtocolOptionsDef2,
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class MulticloudConnectionIpv6AddressFamily:
        """
        Set BGP address family
        """

        filter: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # IPv6 Aggregate prefixes in specific range
        ipv6_aggregate_address: Optional[List[Ipv6AggregateAddress]]
        # Configure the networks for BGP to advertise
        ipv6_network: Optional[List[Ipv6Network]]
        name: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        originate: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        paths: Optional[
            Union[
                TransportMulticloudConnectionOneOfAddressFamilyPathsOptionsDef1,
                OneOfAddressFamilyPathsOptionsDef2,
                OneOfAddressFamilyPathsOptionsDef3,
            ]
        ]
        # Redistribute routes into BGP
        redistribute: Optional[
            List[SdRoutingTransportMulticloudConnectionRedistribute]
        ]


    class TransportMulticloudConnectionOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class MulticloudConnectionPrefix:
        """
        Prefix
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            TransportMulticloudConnectionOneOfIpV4AddressOptionsDef2,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class MulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportMulticloudConnectionNextHop:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            MulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class MulticloudConnectionOneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionIpv4Route1:
        gateway: Gateway
        # IPv4 Route Gateway Next Hop
        next_hop: List[TransportMulticloudConnectionNextHop]
        # Prefix
        prefix: MulticloudConnectionPrefix
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                MulticloudConnectionOneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]


    class SdRoutingTransportMulticloudConnectionOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportMulticloudConnectionPrefix:
        """
        Prefix
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            SdRoutingTransportMulticloudConnectionOneOfIpV4AddressOptionsDef2,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class MulticloudConnectionOneOfIpv4RouteGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: MulticloudConnectionIpv4GatewayDef  # pytype: disable=annotation-type-mismatch


    class MulticloudConnectionOneOfIpv4RouteGatewayOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: MulticloudConnectionDefaultIpv4GatewayDef  # pytype: disable=annotation-type-mismatch


    class TransportMulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportMulticloudConnectionNextHop:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            TransportMulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class TransportMulticloudConnectionOneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionIpv4Route2:
        gateway: Union[
            MulticloudConnectionOneOfIpv4RouteGatewayOptionsDef1,
            MulticloudConnectionOneOfIpv4RouteGatewayOptionsDef2,
        ]
        # Prefix
        prefix: TransportMulticloudConnectionPrefix
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                TransportMulticloudConnectionOneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]
        # IPv4 Route Gateway Next Hop
        next_hop: Optional[
            List[SdRoutingTransportMulticloudConnectionNextHop]
        ]


    class MulticloudConnectionOneOfIpv6NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportMulticloudConnectionNextHop:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            MulticloudConnectionOneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class MulticloudConnectionNextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[
            List[
                FeatureProfileSdRoutingTransportMulticloudConnectionNextHop
            ]
        ]


    class MulticloudConnectionOneOfIpRoute1:
        next_hop_container: MulticloudConnectionNextHopContainer


    class MulticloudConnectionIpv6Route:
        one_of_ip_route: Union[
            MulticloudConnectionOneOfIpRoute1,
            OneOfIpRoute2,
            OneOfIpRoute3,
        ]
        prefix: Union[
            OneOfIpv6RoutePrefixOptionsDef1,
            OneOfIpv6RoutePrefixOptionsDef2,
        ]


    class V1FeatureProfileSdRoutingTransportMulticloudConnectionData:
        """
        Parameters for the new Connection
        """

        # Set IPv4 unicast BGP address family
        address_family: Optional[
            V1FeatureProfileSdRoutingTransportMulticloudConnectionAddressFamily
        ]
        # IPv4 Static Route
        ipv4_route: Optional[
            List[
                Union[
                    MulticloudConnectionIpv4Route1,
                    MulticloudConnectionIpv4Route2,
                ]
            ]
        ]
        # Set BGP address family
        ipv6_address_family: Optional[
            MulticloudConnectionIpv6AddressFamily
        ]
        # Set BGP IPv6 neighbors
        ipv6_neighbor: Optional[List[MulticloudConnectionIpv6Neighbor]]
        # IPv6 Static Route
        ipv6_route: Optional[List[MulticloudConnectionIpv6Route]]
        # Set BGP IPv4 neighbors
        neighbor: Optional[List[MulticloudConnectionNeighbor]]


    class MulticloudConnectionExtensions:
        parcel_type: Union[
            MulticloudConnectionOneOfExtensionsParcelTypeOptionsDef1,
            OneOfExtensionsParcelTypeOptionsDef2,
        ]
        #  Parameters for the new Connection
        data: Optional[
            V1FeatureProfileSdRoutingTransportMulticloudConnectionData
        ]
        parcel_id: Optional[
            Union[
                MulticloudConnectionOneOfExtensionsParcelIdOptionsDef1,
                OneOfExtensionsParcelIdOptionsDef2,
            ]
        ]


    class FeatureProfileSdRoutingTransportMulticloudConnectionData:
        connection_name: VariableOptionTypeObjectDef
        # Extending Bgp Neighbors, Ip Routes, Interface Parcel Id reference and Route Policy for Transport Profile to build new Connections
        extensions: Optional[List[MulticloudConnectionExtensions]]


    class MulticloudConnectionPayload:
        """
        multi-cloud-connection profile parcel schema for PUT request
        """

        data: Optional[
            FeatureProfileSdRoutingTransportMulticloudConnectionData
        ]
        description: Optional[str]
        name: Optional[str]


    class GetSingleSdRoutingTransportVrfWanMulticloudConnectionPayload:
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
        # multi-cloud-connection profile parcel schema for PUT request
        payload: Optional[MulticloudConnectionPayload]


    class EditMultiCloudConnection1PutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class TransportMulticloudConnectionOneOfExtensionsParcelTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TransportMulticloudConnectionExtensionsParcelTypeDef  # pytype: disable=annotation-type-mismatch


    class TransportMulticloudConnectionOneOfExtensionsParcelIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingTransportMulticloudConnectionOneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingTransportMulticloudConnectionOneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class SdRoutingTransportMulticloudConnectionOneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class SdRoutingTransportMulticloudConnectionOneOfKeepaliveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportMulticloudConnectionOneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SdRoutingTransportMulticloudConnectionOneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingTransportMulticloudConnectionOneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportMulticloudConnectionWanIpv4NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class PolicyType2:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class V1FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SdRoutingTransportMulticloudConnectionOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportMulticloudConnectionNeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: PolicyType2
        prefix_num: Union[
            V1FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            SdRoutingTransportMulticloudConnectionOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2,
        ]
        threshold: Union[
            V1FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            V1FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class PolicyType3:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: Value1  # pytype: disable=annotation-type-mismatch


    class OneOfNeighborMaxPrefixNumOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef31:
        option_type: DefaultOptionTypeDef
        value: int


    class SdRoutingTransportMulticloudConnectionNeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: PolicyType3
        prefix_num: Union[
            OneOfNeighborMaxPrefixNumOptionsDef11,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        threshold: Union[
            OneOfNeighborAddressFamilyThresholdOptionsDef11,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            OneOfNeighborAddressFamilyThresholdOptionsDef31,
        ]


    class AddressFamily1:
        family_type: TransportMulticloudConnectionWanIpv4NeighborAfTypeDef
        in_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        max_prefix_config: Optional[
            Union[
                NeighborMaxPrefixConfigDef1,
                SdRoutingTransportMulticloudConnectionNeighborMaxPrefixConfigDef2,
                SdRoutingTransportMulticloudConnectionNeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class TransportMulticloudConnectionNeighbor:
        address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        remote_as: Union[
            SdRoutingTransportMulticloudConnectionOneOfAsNumOptionsDef1,
            OneOfAsNumOptionsDef2,
        ]
        # Set BGP address family
        address_family: Optional[List[AddressFamily1]]
        as_number: Optional[
            Union[
                SdRoutingTransportMulticloudConnectionOneOfNeighborAsNumberOptionsDef1,
                OneOfNeighborAsNumberOptionsDef2,
                OneOfNeighborAsNumberOptionsDef3,
            ]
        ]
        as_override: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        description: Optional[
            Union[
                SdRoutingTransportMulticloudConnectionOneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                SdRoutingTransportMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                SdRoutingTransportMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                SdRoutingTransportMulticloudConnectionOneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
            ]
        ]
        if_name: Optional[
            Union[
                OneOfInterfaceNameOptionsDef1,
                OneOfInterfaceNameOptionsDef2,
                OneOfInterfaceNameOptionsDef3,
            ]
        ]
        keepalive: Optional[
            Union[
                SdRoutingTransportMulticloudConnectionOneOfKeepaliveOptionsDef1,
                OneOfKeepaliveOptionsDef2,
            ]
        ]
        local_as: Optional[
            Union[
                SdRoutingTransportMulticloudConnectionOneOfLocalAsOptionsDef1,
                OneOfLocalAsOptionsDef2,
                OneOfLocalAsOptionsDef3,
            ]
        ]
        next_hop_self: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        password: Optional[
            Union[
                SdRoutingTransportMulticloudConnectionOneOfNeighborPasswordOptionsDef1,
                OneOfNeighborPasswordOptionsDef2,
                OneOfNeighborPasswordOptionsDef3,
            ]
        ]
        send_community: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        send_ext_community: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        send_label: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        send_label_explicit: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfKeepaliveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportMulticloudConnectionWanIpv6NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: Value2  # pytype: disable=annotation-type-mismatch


    class PolicyType4:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfNeighborMaxPrefixNumOptionsDef12:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef12:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef32:
        option_type: DefaultOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportMulticloudConnectionNeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: PolicyType4
        prefix_num: Union[
            OneOfNeighborMaxPrefixNumOptionsDef12,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2,
        ]
        threshold: Union[
            OneOfNeighborAddressFamilyThresholdOptionsDef12,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            OneOfNeighborAddressFamilyThresholdOptionsDef32,
        ]


    class PolicyType5:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: Value3  # pytype: disable=annotation-type-mismatch


    class OneOfNeighborMaxPrefixNumOptionsDef13:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef13:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef33:
        option_type: DefaultOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportMulticloudConnectionNeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: PolicyType5
        prefix_num: Union[
            OneOfNeighborMaxPrefixNumOptionsDef13,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        threshold: Union[
            OneOfNeighborAddressFamilyThresholdOptionsDef13,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            OneOfNeighborAddressFamilyThresholdOptionsDef33,
        ]


    class AddressFamily2:
        family_type: TransportMulticloudConnectionWanIpv6NeighborAfTypeDef
        in_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        max_prefix_config: Optional[
            Union[
                NeighborMaxPrefixConfigDef1,
                FeatureProfileSdRoutingTransportMulticloudConnectionNeighborMaxPrefixConfigDef2,
                FeatureProfileSdRoutingTransportMulticloudConnectionNeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class TransportMulticloudConnectionIpv6Neighbor:
        address: Union[
            OneOfIpv6AddrGlobalVariableOptionsDef1,
            OneOfIpv6AddrGlobalVariableOptionsDef2,
        ]
        remote_as: Union[
            FeatureProfileSdRoutingTransportMulticloudConnectionOneOfAsNumOptionsDef1,
            OneOfAsNumOptionsDef2,
        ]
        # Set IPv6 BGP address family
        address_family: Optional[List[AddressFamily2]]
        as_number: Optional[
            Union[
                FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborAsNumberOptionsDef1,
                OneOfNeighborAsNumberOptionsDef2,
                OneOfNeighborAsNumberOptionsDef3,
            ]
        ]
        as_override: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        description: Optional[
            Union[
                FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                FeatureProfileSdRoutingTransportMulticloudConnectionOneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
            ]
        ]
        if_name: Optional[
            Union[
                OneOfInterfaceNameOptionsDef1,
                OneOfInterfaceNameOptionsDef2,
                OneOfInterfaceNameOptionsDef3,
            ]
        ]
        keepalive: Optional[
            Union[
                FeatureProfileSdRoutingTransportMulticloudConnectionOneOfKeepaliveOptionsDef1,
                OneOfKeepaliveOptionsDef2,
            ]
        ]
        local_as: Optional[
            Union[
                FeatureProfileSdRoutingTransportMulticloudConnectionOneOfLocalAsOptionsDef1,
                OneOfLocalAsOptionsDef2,
                OneOfLocalAsOptionsDef3,
            ]
        ]
        next_hop_self: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        password: Optional[
            Union[
                FeatureProfileSdRoutingTransportMulticloudConnectionOneOfNeighborPasswordOptionsDef1,
                OneOfNeighborPasswordOptionsDef2,
                OneOfNeighborPasswordOptionsDef3,
            ]
        ]
        send_community: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        send_ext_community: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]


    class SdRoutingTransportMulticloudConnectionOneOfAddressFamilyPathsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportMulticloudConnectionOneOfIpv4AddressFamilyRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TransportMulticloudConnectionIpv4AddressFamilyRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdRoutingTransportMulticloudConnectionRedistribute:
        protocol: Union[
            TransportMulticloudConnectionOneOfIpv4AddressFamilyRedistributeProtocolOptionsDef1,
            OneOfIpv4AddressFamilyRedistributeProtocolOptionsDef2,
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class AddressFamily3:
        """
        Set IPv4 unicast BGP address family
        """

        # Aggregate prefixes in specific range
        aggregate_address: Optional[List[AggregateAddress]]
        filter: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        name: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        # Configure the networks for BGP to advertise
        network: Optional[List[Network]]
        originate: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        paths: Optional[
            Union[
                SdRoutingTransportMulticloudConnectionOneOfAddressFamilyPathsOptionsDef1,
                OneOfAddressFamilyPathsOptionsDef2,
                OneOfAddressFamilyPathsOptionsDef3,
            ]
        ]
        # Redistribute routes into BGP
        redistribute: Optional[
            List[
                FeatureProfileSdRoutingTransportMulticloudConnectionRedistribute
            ]
        ]


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfAddressFamilyPathsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportMulticloudConnectionOneOfIpv6AddressFamilyRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TransportMulticloudConnectionIpv6AddressFamilyRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class V1FeatureProfileSdRoutingTransportMulticloudConnectionRedistribute:
        protocol: Union[
            TransportMulticloudConnectionOneOfIpv6AddressFamilyRedistributeProtocolOptionsDef1,
            OneOfIpv6AddressFamilyRedistributeProtocolOptionsDef2,
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class TransportMulticloudConnectionIpv6AddressFamily:
        """
        Set BGP address family
        """

        filter: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # IPv6 Aggregate prefixes in specific range
        ipv6_aggregate_address: Optional[List[Ipv6AggregateAddress]]
        # Configure the networks for BGP to advertise
        ipv6_network: Optional[List[Ipv6Network]]
        name: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        originate: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        paths: Optional[
            Union[
                FeatureProfileSdRoutingTransportMulticloudConnectionOneOfAddressFamilyPathsOptionsDef1,
                OneOfAddressFamilyPathsOptionsDef2,
                OneOfAddressFamilyPathsOptionsDef3,
            ]
        ]
        # Redistribute routes into BGP
        redistribute: Optional[
            List[
                V1FeatureProfileSdRoutingTransportMulticloudConnectionRedistribute
            ]
        ]


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingTransportMulticloudConnectionPrefix:
        """
        Prefix
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            FeatureProfileSdRoutingTransportMulticloudConnectionOneOfIpV4AddressOptionsDef2,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class SdRoutingTransportMulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingTransportMulticloudConnectionNextHop:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            SdRoutingTransportMulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class SdRoutingTransportMulticloudConnectionOneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportMulticloudConnectionIpv4Route1:
        gateway: Gateway
        # IPv4 Route Gateway Next Hop
        next_hop: List[
            V1FeatureProfileSdRoutingTransportMulticloudConnectionNextHop
        ]
        # Prefix
        prefix: SdRoutingTransportMulticloudConnectionPrefix
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                SdRoutingTransportMulticloudConnectionOneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]


    class V1FeatureProfileSdRoutingTransportMulticloudConnectionOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdRoutingTransportMulticloudConnectionPrefix:
        """
        Prefix
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            V1FeatureProfileSdRoutingTransportMulticloudConnectionOneOfIpV4AddressOptionsDef2,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class TransportMulticloudConnectionOneOfIpv4RouteGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TransportMulticloudConnectionIpv4GatewayDef  # pytype: disable=annotation-type-mismatch


    class TransportMulticloudConnectionOneOfIpv4RouteGatewayOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: TransportMulticloudConnectionDefaultIpv4GatewayDef  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class NextHop1:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            FeatureProfileSdRoutingTransportMulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class FeatureProfileSdRoutingTransportMulticloudConnectionOneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportMulticloudConnectionIpv4Route2:
        gateway: Union[
            TransportMulticloudConnectionOneOfIpv4RouteGatewayOptionsDef1,
            TransportMulticloudConnectionOneOfIpv4RouteGatewayOptionsDef2,
        ]
        # Prefix
        prefix: FeatureProfileSdRoutingTransportMulticloudConnectionPrefix
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                FeatureProfileSdRoutingTransportMulticloudConnectionOneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]
        # IPv4 Route Gateway Next Hop
        next_hop: Optional[List[NextHop1]]


    class TransportMulticloudConnectionOneOfIpv6NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class NextHop2:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            TransportMulticloudConnectionOneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class TransportMulticloudConnectionNextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[List[NextHop2]]


    class TransportMulticloudConnectionOneOfIpRoute1:
        next_hop_container: TransportMulticloudConnectionNextHopContainer


    class TransportMulticloudConnectionIpv6Route:
        one_of_ip_route: Union[
            TransportMulticloudConnectionOneOfIpRoute1,
            OneOfIpRoute2,
            OneOfIpRoute3,
        ]
        prefix: Union[
            OneOfIpv6RoutePrefixOptionsDef1,
            OneOfIpv6RoutePrefixOptionsDef2,
        ]


    class Data2:
        """
        Parameters for the new Connection
        """

        # Set IPv4 unicast BGP address family
        address_family: Optional[AddressFamily3]
        # IPv4 Static Route
        ipv4_route: Optional[
            List[
                Union[
                    TransportMulticloudConnectionIpv4Route1,
                    TransportMulticloudConnectionIpv4Route2,
                ]
            ]
        ]
        # Set BGP address family
        ipv6_address_family: Optional[
            TransportMulticloudConnectionIpv6AddressFamily
        ]
        # Set BGP IPv6 neighbors
        ipv6_neighbor: Optional[
            List[TransportMulticloudConnectionIpv6Neighbor]
        ]
        # IPv6 Static Route
        ipv6_route: Optional[List[TransportMulticloudConnectionIpv6Route]]
        # Set BGP IPv4 neighbors
        neighbor: Optional[List[TransportMulticloudConnectionNeighbor]]


    class TransportMulticloudConnectionExtensions:
        parcel_type: Union[
            TransportMulticloudConnectionOneOfExtensionsParcelTypeOptionsDef1,
            OneOfExtensionsParcelTypeOptionsDef2,
        ]
        #  Parameters for the new Connection
        data: Optional[Data2]
        parcel_id: Optional[
            Union[
                TransportMulticloudConnectionOneOfExtensionsParcelIdOptionsDef1,
                OneOfExtensionsParcelIdOptionsDef2,
            ]
        ]


    class Data1:
        connection_name: VariableOptionTypeObjectDef
        # Extending Bgp Neighbors, Ip Routes, Interface Parcel Id reference and Route Policy for Transport Profile to build new Connections
        extensions: Optional[
            List[TransportMulticloudConnectionExtensions]
        ]


    class EditMultiCloudConnection1PutRequest:
        """
        multi-cloud-connection profile parcel schema for PUT request
        """

        data: Optional[Data1]
        description: Optional[str]
        name: Optional[str]


