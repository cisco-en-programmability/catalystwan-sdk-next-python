======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanFalseDef = Literal[False]

    BooleanTrueDef = Literal[True]

    Value = Literal["ipv4-unicast", "vpnv4-unicast", "vpnv6-unicast"]

    BgpValue = Literal["disable-peer", "warning-only"]

    RoutingBgpValue = Literal["ipv6-unicast", "vpnv6-unicast"]

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

    OspfMatchRouteListDef = Literal[
        "External-type1", "External-type2", "Internal"
    ]

    Ipv6AddressFamilyRedistributeProtocolDef = Literal[
        "connected", "ospf", "static"
    ]


    class OneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class OneOfAsNumOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRouterIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRouterIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRouterIdOptionsDef3:
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


    class OneOfExternalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfExternalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfExternalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfInternalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInternalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInternalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfLocalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfLocalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLocalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfKeepaliveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfKeepaliveOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfKeepaliveOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHoldtimeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHoldtimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


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


    class BgpPolicyType:
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
        policy_type: BgpPolicyType
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


    class RoutingBgpPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: BgpValue  # pytype: disable=annotation-type-mismatch


    class NeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: RoutingBgpPolicyType
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
            Union[
                OneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
                OneOfHoldtimeOptionsDef3,
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
                OneOfKeepaliveOptionsDef2,
                OneOfKeepaliveOptionsDef3,
            ]
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
        value: RoutingBgpValue  # pytype: disable=annotation-type-mismatch


    class BgpAddressFamily:
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
        address_family: Optional[List[BgpAddressFamily]]
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
            Union[
                OneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
                OneOfHoldtimeOptionsDef3,
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
                OneOfKeepaliveOptionsDef2,
                OneOfKeepaliveOptionsDef3,
            ]
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


    class OneOfMetricOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMetricOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMetricOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfOspfMatchRouteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[
            OspfMatchRouteListDef
        ]  # pytype: disable=annotation-type-mismatch


    class OneOfOspfMatchRouteOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOspfMatchRouteOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Redistribute:
        protocol: Union[
            OneOfIpv4AddressFamilyRedistributeProtocolOptionsDef1,
            OneOfIpv4AddressFamilyRedistributeProtocolOptionsDef2,
        ]
        metric: Optional[
            Union[
                OneOfMetricOptionsDef1,
                OneOfMetricOptionsDef2,
                OneOfMetricOptionsDef3,
            ]
        ]
        ospf_match_route: Optional[
            Union[
                OneOfOspfMatchRouteOptionsDef1,
                OneOfOspfMatchRouteOptionsDef2,
                OneOfOspfMatchRouteOptionsDef3,
            ]
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class RoutingBgpAddressFamily:
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


    class BgpRedistribute:
        protocol: Union[
            OneOfIpv6AddressFamilyRedistributeProtocolOptionsDef1,
            OneOfIpv6AddressFamilyRedistributeProtocolOptionsDef2,
        ]
        metric: Optional[
            Union[
                OneOfMetricOptionsDef1,
                OneOfMetricOptionsDef2,
                OneOfMetricOptionsDef3,
            ]
        ]
        ospf_match_route: Optional[
            Union[
                OneOfOspfMatchRouteOptionsDef1,
                OneOfOspfMatchRouteOptionsDef2,
                OneOfOspfMatchRouteOptionsDef3,
            ]
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
        redistribute: Optional[List[BgpRedistribute]]


    class OneOfBgpMplsIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfBgpMplsIfNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class MplsInterface:
        if_name: Union[
            OneOfBgpMplsIfNameOptionsDef1, OneOfBgpMplsIfNameOptionsDef2
        ]


    class BgpData:
        as_num: Union[OneOfAsNumOptionsDef1, OneOfAsNumOptionsDef2]
        # Set IPv4 unicast BGP address family
        address_family: Optional[RoutingBgpAddressFamily]
        always_compare: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        compare_router_id: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        deterministic: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        external: Optional[
            Union[
                OneOfExternalOptionsDef1,
                OneOfExternalOptionsDef2,
                OneOfExternalOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                OneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
                OneOfHoldtimeOptionsDef3,
            ]
        ]
        internal: Optional[
            Union[
                OneOfInternalOptionsDef1,
                OneOfInternalOptionsDef2,
                OneOfInternalOptionsDef3,
            ]
        ]
        # Set BGP address family
        ipv6_address_family: Optional[Ipv6AddressFamily]
        # Set BGP IPv6 neighbors
        ipv6_neighbor: Optional[List[Ipv6Neighbor]]
        keepalive: Optional[
            Union[
                OneOfKeepaliveOptionsDef1,
                OneOfKeepaliveOptionsDef2,
                OneOfKeepaliveOptionsDef3,
            ]
        ]
        local: Optional[
            Union[
                OneOfLocalOptionsDef1,
                OneOfLocalOptionsDef2,
                OneOfLocalOptionsDef3,
            ]
        ]
        missing_as_worst: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # MPLS BGP Interface
        mpls_interface: Optional[List[MplsInterface]]
        multipath_relax: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # Set BGP IPv4 neighbors
        neighbor: Optional[List[Neighbor]]
        propagate_aspath: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        propagate_community: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        router_id: Optional[
            Union[
                OneOfRouterIdOptionsDef1,
                OneOfRouterIdOptionsDef2,
                OneOfRouterIdOptionsDef3,
            ]
        ]


    class Payload:
        """
        routing/bgp profile parcel schema for request
        """

        data: BgpData
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
        # routing/bgp profile parcel schema for request
        payload: Optional[Payload]


    class GetListSdwanTransportRoutingBgpPayload:
        data: Optional[List[Data]]


    class CreateRoutingBgpProfileParcelForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class TransportRoutingBgpAddressFamily:
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


    class RoutingBgpData:
        as_num: Union[OneOfAsNumOptionsDef1, OneOfAsNumOptionsDef2]
        # Set IPv4 unicast BGP address family
        address_family: Optional[TransportRoutingBgpAddressFamily]
        always_compare: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        compare_router_id: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        deterministic: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        external: Optional[
            Union[
                OneOfExternalOptionsDef1,
                OneOfExternalOptionsDef2,
                OneOfExternalOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                OneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
                OneOfHoldtimeOptionsDef3,
            ]
        ]
        internal: Optional[
            Union[
                OneOfInternalOptionsDef1,
                OneOfInternalOptionsDef2,
                OneOfInternalOptionsDef3,
            ]
        ]
        # Set BGP address family
        ipv6_address_family: Optional[Ipv6AddressFamily]
        # Set BGP IPv6 neighbors
        ipv6_neighbor: Optional[List[Ipv6Neighbor]]
        keepalive: Optional[
            Union[
                OneOfKeepaliveOptionsDef1,
                OneOfKeepaliveOptionsDef2,
                OneOfKeepaliveOptionsDef3,
            ]
        ]
        local: Optional[
            Union[
                OneOfLocalOptionsDef1,
                OneOfLocalOptionsDef2,
                OneOfLocalOptionsDef3,
            ]
        ]
        missing_as_worst: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # MPLS BGP Interface
        mpls_interface: Optional[List[MplsInterface]]
        multipath_relax: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # Set BGP IPv4 neighbors
        neighbor: Optional[List[Neighbor]]
        propagate_aspath: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        propagate_community: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        router_id: Optional[
            Union[
                OneOfRouterIdOptionsDef1,
                OneOfRouterIdOptionsDef2,
                OneOfRouterIdOptionsDef3,
            ]
        ]


    class CreateRoutingBgpProfileParcelForTransportPostRequest:
        """
        routing/bgp profile parcel schema for request
        """

        data: RoutingBgpData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanTransportRoutingBgpPayload:
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
        # routing/bgp profile parcel schema for request
        payload: Optional[Payload]


    class EditRoutingBgpProfileParcelForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdwanTransportRoutingBgpAddressFamily:
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


    class TransportRoutingBgpData:
        as_num: Union[OneOfAsNumOptionsDef1, OneOfAsNumOptionsDef2]
        # Set IPv4 unicast BGP address family
        address_family: Optional[SdwanTransportRoutingBgpAddressFamily]
        always_compare: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        compare_router_id: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        deterministic: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        external: Optional[
            Union[
                OneOfExternalOptionsDef1,
                OneOfExternalOptionsDef2,
                OneOfExternalOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                OneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
                OneOfHoldtimeOptionsDef3,
            ]
        ]
        internal: Optional[
            Union[
                OneOfInternalOptionsDef1,
                OneOfInternalOptionsDef2,
                OneOfInternalOptionsDef3,
            ]
        ]
        # Set BGP address family
        ipv6_address_family: Optional[Ipv6AddressFamily]
        # Set BGP IPv6 neighbors
        ipv6_neighbor: Optional[List[Ipv6Neighbor]]
        keepalive: Optional[
            Union[
                OneOfKeepaliveOptionsDef1,
                OneOfKeepaliveOptionsDef2,
                OneOfKeepaliveOptionsDef3,
            ]
        ]
        local: Optional[
            Union[
                OneOfLocalOptionsDef1,
                OneOfLocalOptionsDef2,
                OneOfLocalOptionsDef3,
            ]
        ]
        missing_as_worst: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # MPLS BGP Interface
        mpls_interface: Optional[List[MplsInterface]]
        multipath_relax: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # Set BGP IPv4 neighbors
        neighbor: Optional[List[Neighbor]]
        propagate_aspath: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        propagate_community: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        router_id: Optional[
            Union[
                OneOfRouterIdOptionsDef1,
                OneOfRouterIdOptionsDef2,
                OneOfRouterIdOptionsDef3,
            ]
        ]


    class EditRoutingBgpProfileParcelForTransportPutRequest:
        """
        routing/bgp profile parcel schema for request
        """

        data: TransportRoutingBgpData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


