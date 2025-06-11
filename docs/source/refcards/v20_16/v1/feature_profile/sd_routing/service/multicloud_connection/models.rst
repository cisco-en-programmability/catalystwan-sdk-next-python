======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    ExtensionsParcelTypeDef = Literal[
        "vrf",
        "vrf/lan/interface/ethernet",
        "vrf/lan/interface/gre",
        "vrf/lan/interface/ipsec",
        "vrf/routing/bgp",
    ]

    DefaultOptionTypeDef = Literal["default"]

    BooleanFalseDef = Literal[False]

    BooleanTrueDef = Literal[True]

    Value = Literal["disable-peer", "warning-only"]

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

    Ipv6RouteNatDef = Literal["NAT64", "NAT66"]

    MulticloudConnectionExtensionsParcelTypeDef = Literal[
        "ivrf",
        "vrf/lan/interface/ethernet",
        "vrf/lan/interface/gre",
        "vrf/lan/interface/ipsec",
        "vrf/routing/bgp",
    ]

    MulticloudConnectionIpv4AddressFamilyRedistributeProtocolDef = (
        Literal["connected", "nat", "ospf", "ospfv3", "static"]
    )

    MulticloudConnectionIpv6AddressFamilyRedistributeProtocolDef = (
        Literal["connected", "ospf", "static"]
    )

    ServiceMulticloudConnectionExtensionsParcelTypeDef = Literal[
        "ivrf",
        "vrf/lan/interface/ethernet",
        "vrf/lan/interface/gre",
        "vrf/lan/interface/ipsec",
        "vrf/routing/bgp",
    ]

    ServiceMulticloudConnectionIpv4AddressFamilyRedistributeProtocolDef = Literal[
        "connected", "nat", "ospf", "ospfv3", "static"
    ]

    ServiceMulticloudConnectionIpv6AddressFamilyRedistributeProtocolDef = Literal[
        "connected", "ospf", "static"
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
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfKeepaliveOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


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


    class LanIpv4NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: Any


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


    class ServiceMulticloudConnectionPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class NeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: ServiceMulticloudConnectionPolicyType
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
        family_type: LanIpv4NeighborAfTypeDef
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


    class LanIpv6NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class MulticloudConnectionAddressFamily:
        family_type: LanIpv6NeighborAfTypeDef
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


    class ServiceMulticloudConnectionAddressFamily:
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


    class Prefix:
        """
        Prefix
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


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


    class OneOfIpv4NextHopTrackerOptionsDef1:
        ref_id: RefId


    class OneOfIpv4NextHopTrackerOptionsDef2:
        option_type: DefaultOptionTypeDef


    class NextHopWithTracker:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            OneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]
        tracker: Union[
            OneOfIpv4NextHopTrackerOptionsDef1,
            OneOfIpv4NextHopTrackerOptionsDef2,
        ]


    class NextHopContainer:
        # IPv4 Route Gateway Next Hop
        next_hop: Optional[List[NextHop]]
        # IPv4 Route Gateway Next Hop with Tracker
        next_hop_with_tracker: Optional[List[NextHopWithTracker]]


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


    class OneOfIpv4RouteDhcpOptionsWithoutVariable1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfIpv4RouteDhcpOptionsWithoutVariable2:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfIpRoute3:
        dhcp: Union[
            OneOfIpv4RouteDhcpOptionsWithoutVariable1,
            OneOfIpv4RouteDhcpOptionsWithoutVariable2,
        ]


    class OneOfIpv4RouteVpnOptionsWithoutVariable1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfIpv4RouteVpnOptionsWithoutVariable2:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfIpRoute4:
        vpn: Union[
            OneOfIpv4RouteVpnOptionsWithoutVariable1,
            OneOfIpv4RouteVpnOptionsWithoutVariable2,
        ]


    class Ipv4Route:
        one_of_ip_route: Union[
            OneOfIpRoute1, OneOfIpRoute2, OneOfIpRoute3, OneOfIpRoute4
        ]
        # Prefix
        prefix: Prefix


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


    class MulticloudConnectionNextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[List[MulticloudConnectionNextHop]]


    class MulticloudConnectionOneOfIpRoute1:
        next_hop_container: MulticloudConnectionNextHopContainer


    class OneOfIpv6RouteNatOptionsWithoutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6RouteNatOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: Ipv6RouteNatDef  # pytype: disable=annotation-type-mismatch


    class MulticloudConnectionOneOfIpRoute3:
        nat: Union[
            OneOfIpv6RouteNatOptionsWithoutDefault1,
            OneOfIpv6RouteNatOptionsWithoutDefault2,
        ]


    class Ipv6Route:
        one_of_ip_route: Union[
            MulticloudConnectionOneOfIpRoute1,
            OneOfIpRoute2,
            MulticloudConnectionOneOfIpRoute3,
        ]
        prefix: Union[
            OneOfIpv6RoutePrefixOptionsDef1,
            OneOfIpv6RoutePrefixOptionsDef2,
        ]


    class ServiceMulticloudConnectionData:
        """
        Parameters for the new Connection
        """

        # Set IPv4 unicast BGP address family
        address_family: Optional[ServiceMulticloudConnectionAddressFamily]
        # IPv4 Static Route
        ipv4_route: Optional[List[Ipv4Route]]
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
        data: Optional[ServiceMulticloudConnectionData]
        parcel_id: Optional[
            Union[
                OneOfExtensionsParcelIdOptionsDef1,
                OneOfExtensionsParcelIdOptionsDef2,
            ]
        ]


    class MulticloudConnectionData:
        connection_name: VariableOptionTypeObjectDef
        # Extending Bgp Neighbors, Ip Routes, Interface Parcel Id reference and Route Policy for Service Profile to build new Connections
        extensions: Optional[List[Extensions]]


    class Payload:
        """
        SD-Routing multi-cloud-connection feature schema
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
        # SD-Routing multi-cloud-connection feature schema
        payload: Optional[Payload]


    class GetListSdRoutingServiceVrfLanMulticloudConnectionPayload:
        data: Optional[List[Data]]


    class CreateMultiCloudConnectionPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SdRoutingServiceMulticloudConnectionData:
        connection_name: VariableOptionTypeObjectDef
        # Extending Bgp Neighbors, Ip Routes, Interface Parcel Id reference and Route Policy for Service Profile to build new Connections
        extensions: Optional[List[Extensions]]


    class CreateMultiCloudConnectionPostRequest:
        """
        SD-Routing multi-cloud-connection feature schema
        """

        data: Optional[SdRoutingServiceMulticloudConnectionData]
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


    class MulticloudConnectionOneOfKeepaliveOptionsDef2:
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


    class MulticloudConnectionLanIpv4NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class SdRoutingServiceMulticloudConnectionPolicyType:
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
        policy_type: SdRoutingServiceMulticloudConnectionPolicyType
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


    class FeatureProfileSdRoutingServiceMulticloudConnectionPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class ServiceMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class MulticloudConnectionNeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: (
            FeatureProfileSdRoutingServiceMulticloudConnectionPolicyType
        )
        prefix_num: Union[
            ServiceMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        threshold: Union[
            ServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            ServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class SdRoutingServiceMulticloudConnectionAddressFamily:
        family_type: MulticloudConnectionLanIpv4NeighborAfTypeDef
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
            List[SdRoutingServiceMulticloudConnectionAddressFamily]
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
                OneOfKeepaliveOptionsDef1,
                MulticloudConnectionOneOfKeepaliveOptionsDef2,
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


    class ServiceMulticloudConnectionOneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceMulticloudConnectionOneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class ServiceMulticloudConnectionOneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class ServiceMulticloudConnectionOneOfKeepaliveOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceMulticloudConnectionOneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class ServiceMulticloudConnectionOneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceMulticloudConnectionOneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionLanIpv6NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class V1FeatureProfileSdRoutingServiceMulticloudConnectionPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class SdRoutingServiceMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class ServiceMulticloudConnectionOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceMulticloudConnectionNeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: (
            V1FeatureProfileSdRoutingServiceMulticloudConnectionPolicyType
        )
        prefix_num: Union[
            SdRoutingServiceMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            ServiceMulticloudConnectionOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2,
        ]
        threshold: Union[
            SdRoutingServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            SdRoutingServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class PolicyType1:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class ServiceMulticloudConnectionNeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: PolicyType1
        prefix_num: Union[
            FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        threshold: Union[
            FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class FeatureProfileSdRoutingServiceMulticloudConnectionAddressFamily:
        family_type: MulticloudConnectionLanIpv6NeighborAfTypeDef
        in_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        max_prefix_config: Optional[
            Union[
                NeighborMaxPrefixConfigDef1,
                ServiceMulticloudConnectionNeighborMaxPrefixConfigDef2,
                ServiceMulticloudConnectionNeighborMaxPrefixConfigDef3,
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
            ServiceMulticloudConnectionOneOfAsNumOptionsDef1,
            OneOfAsNumOptionsDef2,
        ]
        # Set IPv6 BGP address family
        address_family: Optional[
            List[
                FeatureProfileSdRoutingServiceMulticloudConnectionAddressFamily
            ]
        ]
        as_number: Optional[
            Union[
                ServiceMulticloudConnectionOneOfNeighborAsNumberOptionsDef1,
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
                ServiceMulticloudConnectionOneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                ServiceMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                ServiceMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                ServiceMulticloudConnectionOneOfHoldtimeOptionsDef1,
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
                OneOfKeepaliveOptionsDef1,
                ServiceMulticloudConnectionOneOfKeepaliveOptionsDef2,
            ]
        ]
        local_as: Optional[
            Union[
                ServiceMulticloudConnectionOneOfLocalAsOptionsDef1,
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
                ServiceMulticloudConnectionOneOfNeighborPasswordOptionsDef1,
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


    class ServiceMulticloudConnectionRedistribute:
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


    class V1FeatureProfileSdRoutingServiceMulticloudConnectionAddressFamily:
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
            List[ServiceMulticloudConnectionRedistribute]
        ]


    class ServiceMulticloudConnectionOneOfAddressFamilyPathsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionOneOfIpv6AddressFamilyRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: MulticloudConnectionIpv6AddressFamilyRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class SdRoutingServiceMulticloudConnectionRedistribute:
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
                ServiceMulticloudConnectionOneOfAddressFamilyPathsOptionsDef1,
                OneOfAddressFamilyPathsOptionsDef2,
                OneOfAddressFamilyPathsOptionsDef3,
            ]
        ]
        # Redistribute routes into BGP
        redistribute: Optional[
            List[SdRoutingServiceMulticloudConnectionRedistribute]
        ]


    class MulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceMulticloudConnectionNextHop:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            MulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class ServiceMulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class MulticloudConnectionNextHopWithTracker:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            ServiceMulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]
        tracker: Union[
            OneOfIpv4NextHopTrackerOptionsDef1,
            OneOfIpv4NextHopTrackerOptionsDef2,
        ]


    class ServiceMulticloudConnectionNextHopContainer:
        # IPv4 Route Gateway Next Hop
        next_hop: Optional[List[ServiceMulticloudConnectionNextHop]]
        # IPv4 Route Gateway Next Hop with Tracker
        next_hop_with_tracker: Optional[
            List[MulticloudConnectionNextHopWithTracker]
        ]


    class ServiceMulticloudConnectionOneOfIpRoute1:
        next_hop_container: ServiceMulticloudConnectionNextHopContainer


    class MulticloudConnectionIpv4Route:
        one_of_ip_route: Union[
            ServiceMulticloudConnectionOneOfIpRoute1,
            OneOfIpRoute2,
            OneOfIpRoute3,
            OneOfIpRoute4,
        ]
        # Prefix
        prefix: Prefix


    class MulticloudConnectionOneOfIpv6NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingServiceMulticloudConnectionNextHop:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            MulticloudConnectionOneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class SdRoutingServiceMulticloudConnectionNextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[
            List[SdRoutingServiceMulticloudConnectionNextHop]
        ]


    class SdRoutingServiceMulticloudConnectionOneOfIpRoute1:
        next_hop_container: (
            SdRoutingServiceMulticloudConnectionNextHopContainer
        )


    class ServiceMulticloudConnectionOneOfIpRoute3:
        nat: Union[
            OneOfIpv6RouteNatOptionsWithoutDefault1,
            OneOfIpv6RouteNatOptionsWithoutDefault2,
        ]


    class MulticloudConnectionIpv6Route:
        one_of_ip_route: Union[
            SdRoutingServiceMulticloudConnectionOneOfIpRoute1,
            OneOfIpRoute2,
            ServiceMulticloudConnectionOneOfIpRoute3,
        ]
        prefix: Union[
            OneOfIpv6RoutePrefixOptionsDef1,
            OneOfIpv6RoutePrefixOptionsDef2,
        ]


    class V1FeatureProfileSdRoutingServiceMulticloudConnectionData:
        """
        Parameters for the new Connection
        """

        # Set IPv4 unicast BGP address family
        address_family: Optional[
            V1FeatureProfileSdRoutingServiceMulticloudConnectionAddressFamily
        ]
        # IPv4 Static Route
        ipv4_route: Optional[List[MulticloudConnectionIpv4Route]]
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
            V1FeatureProfileSdRoutingServiceMulticloudConnectionData
        ]
        parcel_id: Optional[
            Union[
                MulticloudConnectionOneOfExtensionsParcelIdOptionsDef1,
                OneOfExtensionsParcelIdOptionsDef2,
            ]
        ]


    class FeatureProfileSdRoutingServiceMulticloudConnectionData:
        connection_name: VariableOptionTypeObjectDef
        # Extending Bgp Neighbors, Ip Routes, Interface Parcel Id reference and Route Policy for Service Profile to build new Connections
        extensions: Optional[List[MulticloudConnectionExtensions]]


    class MulticloudConnectionPayload:
        """
        SD-Routing multi-cloud-connection feature schema
        """

        data: Optional[
            FeatureProfileSdRoutingServiceMulticloudConnectionData
        ]
        description: Optional[str]
        name: Optional[str]


    class GetSingleSdRoutingServiceVrfLanMulticloudConnectionPayload:
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
        # SD-Routing multi-cloud-connection feature schema
        payload: Optional[MulticloudConnectionPayload]


    class EditMultiCloudConnectionPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class ServiceMulticloudConnectionOneOfExtensionsParcelTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ServiceMulticloudConnectionExtensionsParcelTypeDef  # pytype: disable=annotation-type-mismatch


    class ServiceMulticloudConnectionOneOfExtensionsParcelIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingServiceMulticloudConnectionOneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingServiceMulticloudConnectionOneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class SdRoutingServiceMulticloudConnectionOneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class SdRoutingServiceMulticloudConnectionOneOfKeepaliveOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingServiceMulticloudConnectionOneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingServiceMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingServiceMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SdRoutingServiceMulticloudConnectionOneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingServiceMulticloudConnectionOneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceMulticloudConnectionLanIpv4NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class PolicyType2:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class V1FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SdRoutingServiceMulticloudConnectionOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingServiceMulticloudConnectionNeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: PolicyType2
        prefix_num: Union[
            V1FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            SdRoutingServiceMulticloudConnectionOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2,
        ]
        threshold: Union[
            V1FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            V1FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class PolicyType3:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfNeighborMaxPrefixNumOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef31:
        option_type: DefaultOptionTypeDef
        value: int


    class SdRoutingServiceMulticloudConnectionNeighborMaxPrefixConfigDef3:
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
        family_type: ServiceMulticloudConnectionLanIpv4NeighborAfTypeDef
        in_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        max_prefix_config: Optional[
            Union[
                NeighborMaxPrefixConfigDef1,
                SdRoutingServiceMulticloudConnectionNeighborMaxPrefixConfigDef2,
                SdRoutingServiceMulticloudConnectionNeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class ServiceMulticloudConnectionNeighbor:
        address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        remote_as: Union[
            SdRoutingServiceMulticloudConnectionOneOfAsNumOptionsDef1,
            OneOfAsNumOptionsDef2,
        ]
        # Set BGP address family
        address_family: Optional[List[AddressFamily1]]
        as_number: Optional[
            Union[
                SdRoutingServiceMulticloudConnectionOneOfNeighborAsNumberOptionsDef1,
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
                SdRoutingServiceMulticloudConnectionOneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                SdRoutingServiceMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                SdRoutingServiceMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                SdRoutingServiceMulticloudConnectionOneOfHoldtimeOptionsDef1,
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
                OneOfKeepaliveOptionsDef1,
                SdRoutingServiceMulticloudConnectionOneOfKeepaliveOptionsDef2,
            ]
        ]
        local_as: Optional[
            Union[
                SdRoutingServiceMulticloudConnectionOneOfLocalAsOptionsDef1,
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
                SdRoutingServiceMulticloudConnectionOneOfNeighborPasswordOptionsDef1,
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


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfKeepaliveOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceMulticloudConnectionLanIpv6NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: Any


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


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingServiceMulticloudConnectionNeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: PolicyType4
        prefix_num: Union[
            OneOfNeighborMaxPrefixNumOptionsDef12,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
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
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfNeighborMaxPrefixNumOptionsDef13:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef13:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef33:
        option_type: DefaultOptionTypeDef
        value: int


    class FeatureProfileSdRoutingServiceMulticloudConnectionNeighborMaxPrefixConfigDef3:
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
        family_type: ServiceMulticloudConnectionLanIpv6NeighborAfTypeDef
        in_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        max_prefix_config: Optional[
            Union[
                NeighborMaxPrefixConfigDef1,
                FeatureProfileSdRoutingServiceMulticloudConnectionNeighborMaxPrefixConfigDef2,
                FeatureProfileSdRoutingServiceMulticloudConnectionNeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class ServiceMulticloudConnectionIpv6Neighbor:
        address: Union[
            OneOfIpv6AddrGlobalVariableOptionsDef1,
            OneOfIpv6AddrGlobalVariableOptionsDef2,
        ]
        remote_as: Union[
            FeatureProfileSdRoutingServiceMulticloudConnectionOneOfAsNumOptionsDef1,
            OneOfAsNumOptionsDef2,
        ]
        # Set IPv6 BGP address family
        address_family: Optional[List[AddressFamily2]]
        as_number: Optional[
            Union[
                FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborAsNumberOptionsDef1,
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
                FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                FeatureProfileSdRoutingServiceMulticloudConnectionOneOfHoldtimeOptionsDef1,
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
                OneOfKeepaliveOptionsDef1,
                FeatureProfileSdRoutingServiceMulticloudConnectionOneOfKeepaliveOptionsDef2,
            ]
        ]
        local_as: Optional[
            Union[
                FeatureProfileSdRoutingServiceMulticloudConnectionOneOfLocalAsOptionsDef1,
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
                FeatureProfileSdRoutingServiceMulticloudConnectionOneOfNeighborPasswordOptionsDef1,
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


    class SdRoutingServiceMulticloudConnectionOneOfAddressFamilyPathsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceMulticloudConnectionOneOfIpv4AddressFamilyRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ServiceMulticloudConnectionIpv4AddressFamilyRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdRoutingServiceMulticloudConnectionRedistribute:
        protocol: Union[
            ServiceMulticloudConnectionOneOfIpv4AddressFamilyRedistributeProtocolOptionsDef1,
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
                SdRoutingServiceMulticloudConnectionOneOfAddressFamilyPathsOptionsDef1,
                OneOfAddressFamilyPathsOptionsDef2,
                OneOfAddressFamilyPathsOptionsDef3,
            ]
        ]
        # Redistribute routes into BGP
        redistribute: Optional[
            List[
                FeatureProfileSdRoutingServiceMulticloudConnectionRedistribute
            ]
        ]


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfAddressFamilyPathsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceMulticloudConnectionOneOfIpv6AddressFamilyRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ServiceMulticloudConnectionIpv6AddressFamilyRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class V1FeatureProfileSdRoutingServiceMulticloudConnectionRedistribute:
        protocol: Union[
            ServiceMulticloudConnectionOneOfIpv6AddressFamilyRedistributeProtocolOptionsDef1,
            OneOfIpv6AddressFamilyRedistributeProtocolOptionsDef2,
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class ServiceMulticloudConnectionIpv6AddressFamily:
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
                FeatureProfileSdRoutingServiceMulticloudConnectionOneOfAddressFamilyPathsOptionsDef1,
                OneOfAddressFamilyPathsOptionsDef2,
                OneOfAddressFamilyPathsOptionsDef3,
            ]
        ]
        # Redistribute routes into BGP
        redistribute: Optional[
            List[
                V1FeatureProfileSdRoutingServiceMulticloudConnectionRedistribute
            ]
        ]


    class SdRoutingServiceMulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingServiceMulticloudConnectionNextHop:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            SdRoutingServiceMulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceMulticloudConnectionNextHopWithTracker:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            FeatureProfileSdRoutingServiceMulticloudConnectionOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]
        tracker: Union[
            OneOfIpv4NextHopTrackerOptionsDef1,
            OneOfIpv4NextHopTrackerOptionsDef2,
        ]


    class FeatureProfileSdRoutingServiceMulticloudConnectionNextHopContainer:
        # IPv4 Route Gateway Next Hop
        next_hop: Optional[
            List[
                FeatureProfileSdRoutingServiceMulticloudConnectionNextHop
            ]
        ]
        # IPv4 Route Gateway Next Hop with Tracker
        next_hop_with_tracker: Optional[
            List[ServiceMulticloudConnectionNextHopWithTracker]
        ]


    class FeatureProfileSdRoutingServiceMulticloudConnectionOneOfIpRoute1:
        next_hop_container: FeatureProfileSdRoutingServiceMulticloudConnectionNextHopContainer


    class ServiceMulticloudConnectionIpv4Route:
        one_of_ip_route: Union[
            FeatureProfileSdRoutingServiceMulticloudConnectionOneOfIpRoute1,
            OneOfIpRoute2,
            OneOfIpRoute3,
            OneOfIpRoute4,
        ]
        # Prefix
        prefix: Prefix


    class ServiceMulticloudConnectionOneOfIpv6NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingServiceMulticloudConnectionNextHop:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            ServiceMulticloudConnectionOneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class V1FeatureProfileSdRoutingServiceMulticloudConnectionNextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[
            List[
                V1FeatureProfileSdRoutingServiceMulticloudConnectionNextHop
            ]
        ]


    class V1FeatureProfileSdRoutingServiceMulticloudConnectionOneOfIpRoute1:
        next_hop_container: V1FeatureProfileSdRoutingServiceMulticloudConnectionNextHopContainer


    class SdRoutingServiceMulticloudConnectionOneOfIpRoute3:
        nat: Union[
            OneOfIpv6RouteNatOptionsWithoutDefault1,
            OneOfIpv6RouteNatOptionsWithoutDefault2,
        ]


    class ServiceMulticloudConnectionIpv6Route:
        one_of_ip_route: Union[
            V1FeatureProfileSdRoutingServiceMulticloudConnectionOneOfIpRoute1,
            OneOfIpRoute2,
            SdRoutingServiceMulticloudConnectionOneOfIpRoute3,
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
        ipv4_route: Optional[List[ServiceMulticloudConnectionIpv4Route]]
        # Set BGP address family
        ipv6_address_family: Optional[
            ServiceMulticloudConnectionIpv6AddressFamily
        ]
        # Set BGP IPv6 neighbors
        ipv6_neighbor: Optional[
            List[ServiceMulticloudConnectionIpv6Neighbor]
        ]
        # IPv6 Static Route
        ipv6_route: Optional[List[ServiceMulticloudConnectionIpv6Route]]
        # Set BGP IPv4 neighbors
        neighbor: Optional[List[ServiceMulticloudConnectionNeighbor]]


    class ServiceMulticloudConnectionExtensions:
        parcel_type: Union[
            ServiceMulticloudConnectionOneOfExtensionsParcelTypeOptionsDef1,
            OneOfExtensionsParcelTypeOptionsDef2,
        ]
        #  Parameters for the new Connection
        data: Optional[Data2]
        parcel_id: Optional[
            Union[
                ServiceMulticloudConnectionOneOfExtensionsParcelIdOptionsDef1,
                OneOfExtensionsParcelIdOptionsDef2,
            ]
        ]


    class Data1:
        connection_name: VariableOptionTypeObjectDef
        # Extending Bgp Neighbors, Ip Routes, Interface Parcel Id reference and Route Policy for Service Profile to build new Connections
        extensions: Optional[List[ServiceMulticloudConnectionExtensions]]


    class EditMultiCloudConnectionPutRequest:
        """
        SD-Routing multi-cloud-connection feature schema
        """

        data: Optional[Data1]
        description: Optional[str]
        name: Optional[str]


