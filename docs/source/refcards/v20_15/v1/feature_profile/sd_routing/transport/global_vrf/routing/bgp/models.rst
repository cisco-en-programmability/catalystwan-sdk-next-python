======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanFalseDef = Literal[False]

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

    BooleanTrueDef = Literal[True]

    Value = Literal["ipv4-unicast"]

    BgpValue = Literal["disable-peer", "warning-only"]

    RoutingBgpValue = Literal["ipv6-unicast"]

    Ipv4AddressFamilyRedistributeProtocolDef = Literal[
        "connected", "ospf", "ospfv3", "static"
    ]

    OspfMatchRouteListDef = Literal[
        "External-type1", "External-type2", "Internal"
    ]

    Ipv6AddressFamilyRedistributeProtocolDef = Literal[
        "connected", "ospf", "static"
    ]

    GlobalVrfRoutingBgpValue = Literal["disable-peer", "warning-only"]

    TransportGlobalVrfRoutingBgpValue = Literal[
        "disable-peer", "warning-only"
    ]

    SdRoutingTransportGlobalVrfRoutingBgpValue = Literal["ipv6-unicast"]

    FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpValue = Literal[
        "disable-peer", "warning-only"
    ]

    V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpValue = Literal[
        "disable-peer", "warning-only"
    ]

    BgpIpv4AddressFamilyRedistributeProtocolDef = Literal[
        "connected", "eigrp", "ospf", "ospfv3", "static"
    ]

    BgpOspfMatchRouteListDef = Literal[
        "External-type1", "External-type2", "Internal"
    ]

    BgpIpv6AddressFamilyRedistributeProtocolDef = Literal[
        "connected", "ospf", "static"
    ]

    RoutingBgpOspfMatchRouteListDef = Literal[
        "External-type1", "External-type2", "Internal"
    ]

    Value1 = Literal["disable-peer", "warning-only"]

    Value2 = Literal["disable-peer", "warning-only"]

    Value3 = Literal["disable-peer", "warning-only"]

    Value4 = Literal["disable-peer", "warning-only"]

    RoutingBgpIpv4AddressFamilyRedistributeProtocolDef = Literal[
        "connected", "eigrp", "ospf", "ospfv3", "static"
    ]

    GlobalVrfRoutingBgpOspfMatchRouteListDef = Literal[
        "External-type1", "External-type2", "Internal"
    ]

    RoutingBgpIpv6AddressFamilyRedistributeProtocolDef = Literal[
        "connected", "ospf", "static"
    ]

    TransportGlobalVrfRoutingBgpOspfMatchRouteListDef = Literal[
        "External-type1", "External-type2", "Internal"
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


    class OneOfMaxListenPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMaxListenPrefixNumOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMaxListenPrefixNumOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfNeighborPeerGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


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


    class Ipv4Address:
        address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]


    class Ipv4PeerGroup:
        peer_group_name: OneOfNeighborPeerGroupNameOptionsDef
        # Peer Group IPv4 subnet range
        range: List[Ipv4AddressAndMaskDef]
        # Peer Group IPv4 Address list
        ipv4_address: Optional[List[Ipv4Address]]


    class OneOfIpv6PrefixGlobalVariableWithoutDefault1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6PrefixGlobalVariableWithoutDefault2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Range:
        prefix: Union[
            OneOfIpv6PrefixGlobalVariableWithoutDefault1,
            OneOfIpv6PrefixGlobalVariableWithoutDefault2,
        ]


    class OneOfIpv6AddrGlobalVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6AddrGlobalVariableOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Ipv6Address:
        address: Union[
            OneOfIpv6AddrGlobalVariableOptionsDef1,
            OneOfIpv6AddrGlobalVariableOptionsDef2,
        ]


    class Ipv6PeerGroup:
        peer_group_name: OneOfNeighborPeerGroupNameOptionsDef
        # Peer Group IPv6 prefix range
        range: List[Range]
        # Peer Group IPv6 Address list
        ipv6_address: Optional[List[Ipv6Address]]


    class DynamicNeighbor1:
        # IPv4 Peer groups
        ipv4_peer_group: List[Ipv4PeerGroup]
        max_listen_prefix_limit: Union[
            OneOfMaxListenPrefixNumOptionsDef1,
            OneOfMaxListenPrefixNumOptionsDef2,
            OneOfMaxListenPrefixNumOptionsDef3,
        ]
        # IPv6 Peer groups
        ipv6_peer_group: Optional[List[Ipv6PeerGroup]]


    class DynamicNeighbor2:
        # IPv6 Peer groups
        ipv6_peer_group: List[Ipv6PeerGroup]
        max_listen_prefix_limit: Union[
            OneOfMaxListenPrefixNumOptionsDef1,
            OneOfMaxListenPrefixNumOptionsDef2,
            OneOfMaxListenPrefixNumOptionsDef3,
        ]
        # IPv4 Peer groups
        ipv4_peer_group: Optional[List[Ipv4PeerGroup]]


    class DynamicNeighbor3:
        # IPv4 Peer groups
        ipv4_peer_group: List[Ipv4PeerGroup]
        # IPv6 Peer groups
        ipv6_peer_group: List[Ipv6PeerGroup]
        max_listen_prefix_limit: Union[
            OneOfMaxListenPrefixNumOptionsDef1,
            OneOfMaxListenPrefixNumOptionsDef2,
            OneOfMaxListenPrefixNumOptionsDef3,
        ]


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
        value: Value


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


    class Neighbor1:
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
        fall_over_bfd: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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
        peer_group: Optional[OneOfNeighborPeerGroupNameOptionsDef]
        route_reflect_client: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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


    class Neighbor2:
        peer_group: OneOfNeighborPeerGroupNameOptionsDef
        remote_as: Union[OneOfAsNumOptionsDef1, OneOfAsNumOptionsDef2]
        address: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
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
        fall_over_bfd: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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
        route_reflect_client: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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


    class WanIpv6NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: RoutingBgpValue


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


    class Ipv6Neighbor1:
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
        fall_over_bfd: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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
        peer_group: Optional[OneOfNeighborPeerGroupNameOptionsDef]
        route_reflect_client: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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


    class RoutingBgpAddressFamily:
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


    class Ipv6Neighbor2:
        peer_group: OneOfNeighborPeerGroupNameOptionsDef
        remote_as: Union[OneOfAsNumOptionsDef1, OneOfAsNumOptionsDef2]
        address: Optional[
            Union[
                OneOfIpv6AddrGlobalVariableOptionsDef1,
                OneOfIpv6AddrGlobalVariableOptionsDef2,
            ]
        ]
        # Set IPv6 BGP address family
        address_family: Optional[List[RoutingBgpAddressFamily]]
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
        fall_over_bfd: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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
        route_reflect_client: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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


    class GlobalVrfRoutingBgpAddressFamily:
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


    class BgpData:
        as_num: Union[OneOfAsNumOptionsDef1, OneOfAsNumOptionsDef2]
        # Set IPv4 unicast BGP address family
        address_family: Optional[GlobalVrfRoutingBgpAddressFamily]
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
        # BGP dynamic neighbor configuration
        dynamic_neighbor: Optional[
            Union[DynamicNeighbor1, DynamicNeighbor2, DynamicNeighbor3]
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
        ipv6_neighbor: Optional[List[Union[Ipv6Neighbor1, Ipv6Neighbor2]]]
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
        multipath_relax: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # Set BGP IPv4 neighbors
        neighbor: Optional[List[Union[Neighbor1, Neighbor2]]]
        router_id: Optional[
            Union[
                OneOfRouterIdOptionsDef1,
                OneOfRouterIdOptionsDef2,
                OneOfRouterIdOptionsDef3,
            ]
        ]


    class Payload:
        """
        SD-Routing BGP feature schema for global VRF
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
        # SD-Routing BGP feature schema for global VRF
        payload: Optional[Payload]


    class GetListSdRoutingTransportGlobalVrfRoutingBgpPayload:
        data: Optional[List[Data]]


    class CreateSdroutingTransportGlobalVrfBgpFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class TransportGlobalVrfRoutingBgpAddressFamily:
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
        address_family: Optional[
            TransportGlobalVrfRoutingBgpAddressFamily
        ]
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
        # BGP dynamic neighbor configuration
        dynamic_neighbor: Optional[
            Union[DynamicNeighbor1, DynamicNeighbor2, DynamicNeighbor3]
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
        ipv6_neighbor: Optional[List[Union[Ipv6Neighbor1, Ipv6Neighbor2]]]
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
        multipath_relax: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # Set BGP IPv4 neighbors
        neighbor: Optional[List[Union[Neighbor1, Neighbor2]]]
        router_id: Optional[
            Union[
                OneOfRouterIdOptionsDef1,
                OneOfRouterIdOptionsDef2,
                OneOfRouterIdOptionsDef3,
            ]
        ]


    class CreateSdroutingTransportGlobalVrfBgpFeaturePostRequest:
        """
        SD-Routing BGP feature schema for global VRF
        """

        data: RoutingBgpData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdRoutingTransportGlobalVrfRoutingBgpPayload:
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
        # SD-Routing BGP feature schema for global VRF
        payload: Optional[Payload]


    class EditSdroutingTransportGlobalVrfBgpFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingTransportGlobalVrfRoutingBgpAddressFamily:
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


    class GlobalVrfRoutingBgpData:
        as_num: Union[OneOfAsNumOptionsDef1, OneOfAsNumOptionsDef2]
        # Set IPv4 unicast BGP address family
        address_family: Optional[
            SdRoutingTransportGlobalVrfRoutingBgpAddressFamily
        ]
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
        # BGP dynamic neighbor configuration
        dynamic_neighbor: Optional[
            Union[DynamicNeighbor1, DynamicNeighbor2, DynamicNeighbor3]
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
        ipv6_neighbor: Optional[List[Union[Ipv6Neighbor1, Ipv6Neighbor2]]]
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
        multipath_relax: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # Set BGP IPv4 neighbors
        neighbor: Optional[List[Union[Neighbor1, Neighbor2]]]
        router_id: Optional[
            Union[
                OneOfRouterIdOptionsDef1,
                OneOfRouterIdOptionsDef2,
                OneOfRouterIdOptionsDef3,
            ]
        ]


    class EditSdroutingTransportGlobalVrfBgpFeaturePutRequest:
        """
        SD-Routing BGP feature schema for global VRF
        """

        data: GlobalVrfRoutingBgpData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class BgpOneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class BgpOneOfExternalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class BgpOneOfExternalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class BgpOneOfInternalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class BgpOneOfInternalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class BgpOneOfLocalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class BgpOneOfLocalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class BgpOneOfKeepaliveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class BgpOneOfKeepaliveOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class BgpOneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class BgpOneOfHoldtimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class BgpOneOfMaxListenPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class BgpOneOfMaxListenPrefixNumOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class BgpOneOfNeighborPeerGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class BgpIpv4PeerGroup:
        peer_group_name: BgpOneOfNeighborPeerGroupNameOptionsDef
        # Peer Group IPv4 subnet range
        range: List[Ipv4AddressAndMaskDef]
        # Peer Group IPv4 Address list
        ipv4_address: Optional[List[Ipv4Address]]


    class RoutingBgpOneOfNeighborPeerGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class BgpIpv6PeerGroup:
        peer_group_name: RoutingBgpOneOfNeighborPeerGroupNameOptionsDef
        # Peer Group IPv6 prefix range
        range: List[Range]
        # Peer Group IPv6 Address list
        ipv6_address: Optional[List[Ipv6Address]]


    class BgpDynamicNeighbor1:
        # IPv4 Peer groups
        ipv4_peer_group: List[BgpIpv4PeerGroup]
        max_listen_prefix_limit: Union[
            BgpOneOfMaxListenPrefixNumOptionsDef1,
            OneOfMaxListenPrefixNumOptionsDef2,
            BgpOneOfMaxListenPrefixNumOptionsDef3,
        ]
        # IPv6 Peer groups
        ipv6_peer_group: Optional[List[BgpIpv6PeerGroup]]


    class RoutingBgpOneOfMaxListenPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class RoutingBgpOneOfMaxListenPrefixNumOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class GlobalVrfRoutingBgpOneOfNeighborPeerGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class RoutingBgpIpv4PeerGroup:
        peer_group_name: (
            GlobalVrfRoutingBgpOneOfNeighborPeerGroupNameOptionsDef
        )
        # Peer Group IPv4 subnet range
        range: List[Ipv4AddressAndMaskDef]
        # Peer Group IPv4 Address list
        ipv4_address: Optional[List[Ipv4Address]]


    class TransportGlobalVrfRoutingBgpOneOfNeighborPeerGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class RoutingBgpIpv6PeerGroup:
        peer_group_name: TransportGlobalVrfRoutingBgpOneOfNeighborPeerGroupNameOptionsDef
        # Peer Group IPv6 prefix range
        range: List[Range]
        # Peer Group IPv6 Address list
        ipv6_address: Optional[List[Ipv6Address]]


    class BgpDynamicNeighbor2:
        # IPv6 Peer groups
        ipv6_peer_group: List[RoutingBgpIpv6PeerGroup]
        max_listen_prefix_limit: Union[
            RoutingBgpOneOfMaxListenPrefixNumOptionsDef1,
            OneOfMaxListenPrefixNumOptionsDef2,
            RoutingBgpOneOfMaxListenPrefixNumOptionsDef3,
        ]
        # IPv4 Peer groups
        ipv4_peer_group: Optional[List[RoutingBgpIpv4PeerGroup]]


    class GlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborPeerGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalVrfRoutingBgpIpv4PeerGroup:
        peer_group_name: SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborPeerGroupNameOptionsDef
        # Peer Group IPv4 subnet range
        range: List[Ipv4AddressAndMaskDef]
        # Peer Group IPv4 Address list
        ipv4_address: Optional[List[Ipv4Address]]


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborPeerGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalVrfRoutingBgpIpv6PeerGroup:
        peer_group_name: FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborPeerGroupNameOptionsDef
        # Peer Group IPv6 prefix range
        range: List[Range]
        # Peer Group IPv6 Address list
        ipv6_address: Optional[List[Ipv6Address]]


    class BgpDynamicNeighbor3:
        # IPv4 Peer groups
        ipv4_peer_group: List[GlobalVrfRoutingBgpIpv4PeerGroup]
        # IPv6 Peer groups
        ipv6_peer_group: List[GlobalVrfRoutingBgpIpv6PeerGroup]
        max_listen_prefix_limit: Union[
            GlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef1,
            OneOfMaxListenPrefixNumOptionsDef2,
            GlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef3,
        ]


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborPeerGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class BgpOneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class RoutingBgpOneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class BgpOneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class RoutingBgpOneOfKeepaliveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class RoutingBgpOneOfKeepaliveOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class RoutingBgpOneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class RoutingBgpOneOfHoldtimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class BgpOneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class BgpOneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class BgpOneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class BgpOneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class LanIpv4NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: Value


    class GlobalVrfRoutingBgpPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class BgpOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class BgpOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class BgpOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class BgpOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class BgpNeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: GlobalVrfRoutingBgpPolicyType
        prefix_num: Union[
            BgpOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            BgpOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2,
        ]
        threshold: Union[
            BgpOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            BgpOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class TransportGlobalVrfRoutingBgpPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: GlobalVrfRoutingBgpValue  # pytype: disable=annotation-type-mismatch


    class RoutingBgpOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class RoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class RoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class BgpNeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: TransportGlobalVrfRoutingBgpPolicyType
        prefix_num: Union[
            RoutingBgpOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        threshold: Union[
            RoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            RoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpAddressFamily:
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
                BgpNeighborMaxPrefixConfigDef2,
                BgpNeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class BgpNeighbor1:
        address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        remote_as: Union[
            RoutingBgpOneOfAsNumOptionsDef1, OneOfAsNumOptionsDef2
        ]
        # Set BGP address family
        address_family: Optional[
            List[
                FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpAddressFamily
            ]
        ]
        as_number: Optional[
            Union[
                BgpOneOfNeighborAsNumberOptionsDef1,
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
                BgpOneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                BgpOneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                BgpOneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        fall_over_bfd: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                RoutingBgpOneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
                RoutingBgpOneOfHoldtimeOptionsDef3,
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
                RoutingBgpOneOfKeepaliveOptionsDef1,
                OneOfKeepaliveOptionsDef2,
                RoutingBgpOneOfKeepaliveOptionsDef3,
            ]
        ]
        local_as: Optional[
            Union[
                BgpOneOfLocalAsOptionsDef1,
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
                BgpOneOfNeighborPasswordOptionsDef1,
                OneOfNeighborPasswordOptionsDef2,
                OneOfNeighborPasswordOptionsDef3,
            ]
        ]
        peer_group: Optional[
            V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborPeerGroupNameOptionsDef
        ]
        route_reflect_client: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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


    class OneOfNeighborPeerGroupNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class RoutingBgpOneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalVrfRoutingBgpOneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class RoutingBgpOneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class GlobalVrfRoutingBgpOneOfKeepaliveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalVrfRoutingBgpOneOfKeepaliveOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class GlobalVrfRoutingBgpOneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalVrfRoutingBgpOneOfHoldtimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class RoutingBgpOneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class RoutingBgpOneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class RoutingBgpOneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class RoutingBgpOneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportGlobalVrfRoutingBgpPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class GlobalVrfRoutingBgpOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class RoutingBgpOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class RoutingBgpNeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: SdRoutingTransportGlobalVrfRoutingBgpPolicyType
        prefix_num: Union[
            GlobalVrfRoutingBgpOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            RoutingBgpOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2,
        ]
        threshold: Union[
            GlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            GlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: TransportGlobalVrfRoutingBgpValue  # pytype: disable=annotation-type-mismatch


    class TransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class RoutingBgpNeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: (
            FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpPolicyType
        )
        prefix_num: Union[
            TransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        threshold: Union[
            TransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            TransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpAddressFamily:
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
                RoutingBgpNeighborMaxPrefixConfigDef2,
                RoutingBgpNeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class BgpNeighbor2:
        peer_group: OneOfNeighborPeerGroupNameOptionsDef1
        remote_as: Union[
            GlobalVrfRoutingBgpOneOfAsNumOptionsDef1,
            OneOfAsNumOptionsDef2,
        ]
        address: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        # Set BGP address family
        address_family: Optional[
            List[
                V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpAddressFamily
            ]
        ]
        as_number: Optional[
            Union[
                RoutingBgpOneOfNeighborAsNumberOptionsDef1,
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
                RoutingBgpOneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                RoutingBgpOneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                RoutingBgpOneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        fall_over_bfd: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                GlobalVrfRoutingBgpOneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
                GlobalVrfRoutingBgpOneOfHoldtimeOptionsDef3,
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
                GlobalVrfRoutingBgpOneOfKeepaliveOptionsDef1,
                OneOfKeepaliveOptionsDef2,
                GlobalVrfRoutingBgpOneOfKeepaliveOptionsDef3,
            ]
        ]
        local_as: Optional[
            Union[
                RoutingBgpOneOfLocalAsOptionsDef1,
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
                RoutingBgpOneOfNeighborPasswordOptionsDef1,
                OneOfNeighborPasswordOptionsDef2,
                OneOfNeighborPasswordOptionsDef3,
            ]
        ]
        route_reflect_client: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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


    class OneOfNeighborPeerGroupNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalVrfRoutingBgpOneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportGlobalVrfRoutingBgpOneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class GlobalVrfRoutingBgpOneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class TransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class TransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class GlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class GlobalVrfRoutingBgpOneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalVrfRoutingBgpOneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class LanIpv6NeighborAfTypeDef:
        option_type: GlobalOptionTypeDef
        value: SdRoutingTransportGlobalVrfRoutingBgpValue


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class GlobalVrfRoutingBgpOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalVrfRoutingBgpNeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpPolicyType
        prefix_num: Union[
            SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            GlobalVrfRoutingBgpOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2,
        ]
        threshold: Union[
            SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class PolicyType1:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpValue  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class GlobalVrfRoutingBgpNeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: PolicyType1
        prefix_num: Union[
            FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        threshold: Union[
            FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class AddressFamily1:
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
                GlobalVrfRoutingBgpNeighborMaxPrefixConfigDef2,
                GlobalVrfRoutingBgpNeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class BgpIpv6Neighbor1:
        address: Union[
            OneOfIpv6AddrGlobalVariableOptionsDef1,
            OneOfIpv6AddrGlobalVariableOptionsDef2,
        ]
        remote_as: Union[
            TransportGlobalVrfRoutingBgpOneOfAsNumOptionsDef1,
            OneOfAsNumOptionsDef2,
        ]
        # Set IPv6 BGP address family
        address_family: Optional[List[AddressFamily1]]
        as_number: Optional[
            Union[
                GlobalVrfRoutingBgpOneOfNeighborAsNumberOptionsDef1,
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
                GlobalVrfRoutingBgpOneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                GlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                GlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        fall_over_bfd: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                TransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
                TransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef3,
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
                TransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef1,
                OneOfKeepaliveOptionsDef2,
                TransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef3,
            ]
        ]
        local_as: Optional[
            Union[
                GlobalVrfRoutingBgpOneOfLocalAsOptionsDef1,
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
                GlobalVrfRoutingBgpOneOfNeighborPasswordOptionsDef1,
                OneOfNeighborPasswordOptionsDef2,
                OneOfNeighborPasswordOptionsDef3,
            ]
        ]
        peer_group: Optional[OneOfNeighborPeerGroupNameOptionsDef2]
        route_reflect_client: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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


    class OneOfNeighborPeerGroupNameOptionsDef3:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportGlobalVrfRoutingBgpOneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class TransportGlobalVrfRoutingBgpOneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class TransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class TransportGlobalVrfRoutingBgpOneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportGlobalVrfRoutingBgpOneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class PolicyType2:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class TransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: PolicyType2
        prefix_num: Union[
            V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixNumOptionsDef1,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            TransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2,
        ]
        threshold: Union[
            V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef1,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAddressFamilyThresholdOptionsDef3,
        ]


    class PolicyType3:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpValue  # pytype: disable=annotation-type-mismatch


    class OneOfNeighborMaxPrefixNumOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef31:
        option_type: DefaultOptionTypeDef
        value: int


    class TransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef3:
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


    class AddressFamily2:
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
                TransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef2,
                TransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class BgpIpv6Neighbor2:
        peer_group: OneOfNeighborPeerGroupNameOptionsDef3
        remote_as: Union[
            SdRoutingTransportGlobalVrfRoutingBgpOneOfAsNumOptionsDef1,
            OneOfAsNumOptionsDef2,
        ]
        address: Optional[
            Union[
                OneOfIpv6AddrGlobalVariableOptionsDef1,
                OneOfIpv6AddrGlobalVariableOptionsDef2,
            ]
        ]
        # Set IPv6 BGP address family
        address_family: Optional[List[AddressFamily2]]
        as_number: Optional[
            Union[
                TransportGlobalVrfRoutingBgpOneOfNeighborAsNumberOptionsDef1,
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
                TransportGlobalVrfRoutingBgpOneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                TransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                TransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        fall_over_bfd: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                SdRoutingTransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
                SdRoutingTransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef3,
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
                SdRoutingTransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef1,
                OneOfKeepaliveOptionsDef2,
                SdRoutingTransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef3,
            ]
        ]
        local_as: Optional[
            Union[
                TransportGlobalVrfRoutingBgpOneOfLocalAsOptionsDef1,
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
                TransportGlobalVrfRoutingBgpOneOfNeighborPasswordOptionsDef1,
                OneOfNeighborPasswordOptionsDef2,
                OneOfNeighborPasswordOptionsDef3,
            ]
        ]
        route_reflect_client: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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


    class BgpOneOfAddressFamilyPathsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class BgpOneOfIpv4AddressFamilyRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: BgpIpv4AddressFamilyRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class BgpOneOfMetricOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class BgpOneOfOspfMatchRouteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[
            BgpOspfMatchRouteListDef
        ]  # pytype: disable=annotation-type-mismatch


    class RoutingBgpRedistribute:
        protocol: Union[
            BgpOneOfIpv4AddressFamilyRedistributeProtocolOptionsDef1,
            OneOfIpv4AddressFamilyRedistributeProtocolOptionsDef2,
        ]
        metric: Optional[
            Union[
                BgpOneOfMetricOptionsDef1,
                OneOfMetricOptionsDef2,
                OneOfMetricOptionsDef3,
            ]
        ]
        ospf_match_route: Optional[
            Union[
                BgpOneOfOspfMatchRouteOptionsDef1,
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
                BgpOneOfAddressFamilyPathsOptionsDef1,
                OneOfAddressFamilyPathsOptionsDef2,
                OneOfAddressFamilyPathsOptionsDef3,
            ]
        ]
        # Redistribute routes into BGP
        redistribute: Optional[List[RoutingBgpRedistribute]]


    class RoutingBgpOneOfAddressFamilyPathsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class BgpOneOfIpv6AddressFamilyRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: BgpIpv6AddressFamilyRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class RoutingBgpOneOfMetricOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class RoutingBgpOneOfOspfMatchRouteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[
            RoutingBgpOspfMatchRouteListDef
        ]  # pytype: disable=annotation-type-mismatch


    class GlobalVrfRoutingBgpRedistribute:
        protocol: Union[
            BgpOneOfIpv6AddressFamilyRedistributeProtocolOptionsDef1,
            OneOfIpv6AddressFamilyRedistributeProtocolOptionsDef2,
        ]
        metric: Optional[
            Union[
                RoutingBgpOneOfMetricOptionsDef1,
                OneOfMetricOptionsDef2,
                OneOfMetricOptionsDef3,
            ]
        ]
        ospf_match_route: Optional[
            Union[
                RoutingBgpOneOfOspfMatchRouteOptionsDef1,
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


    class BgpIpv6AddressFamily:
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
                RoutingBgpOneOfAddressFamilyPathsOptionsDef1,
                OneOfAddressFamilyPathsOptionsDef2,
                OneOfAddressFamilyPathsOptionsDef3,
            ]
        ]
        # Redistribute routes into BGP
        redistribute: Optional[List[GlobalVrfRoutingBgpRedistribute]]


    class TransportGlobalVrfRoutingBgpData:
        as_num: Union[BgpOneOfAsNumOptionsDef1, OneOfAsNumOptionsDef2]
        # Set IPv4 unicast BGP address family
        address_family: Optional[AddressFamily3]
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
        # BGP dynamic neighbor configuration
        dynamic_neighbor: Optional[
            Union[
                BgpDynamicNeighbor1,
                BgpDynamicNeighbor2,
                BgpDynamicNeighbor3,
            ]
        ]
        external: Optional[
            Union[
                BgpOneOfExternalOptionsDef1,
                OneOfExternalOptionsDef2,
                BgpOneOfExternalOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                BgpOneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
                BgpOneOfHoldtimeOptionsDef3,
            ]
        ]
        internal: Optional[
            Union[
                BgpOneOfInternalOptionsDef1,
                OneOfInternalOptionsDef2,
                BgpOneOfInternalOptionsDef3,
            ]
        ]
        # Set BGP address family
        ipv6_address_family: Optional[BgpIpv6AddressFamily]
        # Set BGP IPv6 neighbors
        ipv6_neighbor: Optional[
            List[Union[BgpIpv6Neighbor1, BgpIpv6Neighbor2]]
        ]
        keepalive: Optional[
            Union[
                BgpOneOfKeepaliveOptionsDef1,
                OneOfKeepaliveOptionsDef2,
                BgpOneOfKeepaliveOptionsDef3,
            ]
        ]
        local: Optional[
            Union[
                BgpOneOfLocalOptionsDef1,
                OneOfLocalOptionsDef2,
                BgpOneOfLocalOptionsDef3,
            ]
        ]
        missing_as_worst: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        multipath_relax: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # Set BGP IPv4 neighbors
        neighbor: Optional[List[Union[BgpNeighbor1, BgpNeighbor2]]]
        router_id: Optional[
            Union[
                OneOfRouterIdOptionsDef1,
                OneOfRouterIdOptionsDef2,
                OneOfRouterIdOptionsDef3,
            ]
        ]


    class BgpPayload:
        """
        SD-Routing Routing BGP for VRF feature schema for request
        """

        data: TransportGlobalVrfRoutingBgpData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetTransportVrfAssociatedRoutingBgpFeaturesGetResponse:
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
        # SD-Routing Routing BGP for VRF feature schema for request
        payload: Optional[BgpPayload]


    class CreateTransportGlobalVrfAndRoutingBgpFeatureAssociationPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateTransportGlobalVrfAndRoutingBgpFeatureAssociationPostRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class RoutingBgpOneOfExternalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class RoutingBgpOneOfExternalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class RoutingBgpOneOfInternalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class RoutingBgpOneOfInternalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class RoutingBgpOneOfLocalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class RoutingBgpOneOfLocalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class TransportGlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportGlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfNeighborPeerGroupNameOptionsDef4:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportGlobalVrfRoutingBgpIpv4PeerGroup:
        peer_group_name: OneOfNeighborPeerGroupNameOptionsDef4
        # Peer Group IPv4 subnet range
        range: List[Ipv4AddressAndMaskDef]
        # Peer Group IPv4 Address list
        ipv4_address: Optional[List[Ipv4Address]]


    class OneOfNeighborPeerGroupNameOptionsDef5:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportGlobalVrfRoutingBgpIpv6PeerGroup:
        peer_group_name: OneOfNeighborPeerGroupNameOptionsDef5
        # Peer Group IPv6 prefix range
        range: List[Range]
        # Peer Group IPv6 Address list
        ipv6_address: Optional[List[Ipv6Address]]


    class RoutingBgpDynamicNeighbor1:
        # IPv4 Peer groups
        ipv4_peer_group: List[TransportGlobalVrfRoutingBgpIpv4PeerGroup]
        max_listen_prefix_limit: Union[
            TransportGlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef1,
            OneOfMaxListenPrefixNumOptionsDef2,
            TransportGlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef3,
        ]
        # IPv6 Peer groups
        ipv6_peer_group: Optional[
            List[TransportGlobalVrfRoutingBgpIpv6PeerGroup]
        ]


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfNeighborPeerGroupNameOptionsDef6:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingTransportGlobalVrfRoutingBgpIpv4PeerGroup:
        peer_group_name: OneOfNeighborPeerGroupNameOptionsDef6
        # Peer Group IPv4 subnet range
        range: List[Ipv4AddressAndMaskDef]
        # Peer Group IPv4 Address list
        ipv4_address: Optional[List[Ipv4Address]]


    class OneOfNeighborPeerGroupNameOptionsDef7:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingTransportGlobalVrfRoutingBgpIpv6PeerGroup:
        peer_group_name: OneOfNeighborPeerGroupNameOptionsDef7
        # Peer Group IPv6 prefix range
        range: List[Range]
        # Peer Group IPv6 Address list
        ipv6_address: Optional[List[Ipv6Address]]


    class RoutingBgpDynamicNeighbor2:
        # IPv6 Peer groups
        ipv6_peer_group: List[
            SdRoutingTransportGlobalVrfRoutingBgpIpv6PeerGroup
        ]
        max_listen_prefix_limit: Union[
            SdRoutingTransportGlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef1,
            OneOfMaxListenPrefixNumOptionsDef2,
            SdRoutingTransportGlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef3,
        ]
        # IPv4 Peer groups
        ipv4_peer_group: Optional[
            List[SdRoutingTransportGlobalVrfRoutingBgpIpv4PeerGroup]
        ]


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfNeighborPeerGroupNameOptionsDef8:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpIpv4PeerGroup:
        peer_group_name: OneOfNeighborPeerGroupNameOptionsDef8
        # Peer Group IPv4 subnet range
        range: List[Ipv4AddressAndMaskDef]
        # Peer Group IPv4 Address list
        ipv4_address: Optional[List[Ipv4Address]]


    class OneOfNeighborPeerGroupNameOptionsDef9:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpIpv6PeerGroup:
        peer_group_name: OneOfNeighborPeerGroupNameOptionsDef9
        # Peer Group IPv6 prefix range
        range: List[Range]
        # Peer Group IPv6 Address list
        ipv6_address: Optional[List[Ipv6Address]]


    class RoutingBgpDynamicNeighbor3:
        # IPv4 Peer groups
        ipv4_peer_group: List[
            FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpIpv4PeerGroup
        ]
        # IPv6 Peer groups
        ipv6_peer_group: List[
            FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpIpv6PeerGroup
        ]
        max_listen_prefix_limit: Union[
            FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef1,
            OneOfMaxListenPrefixNumOptionsDef2,
            FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfMaxListenPrefixNumOptionsDef3,
        ]


    class OneOfNeighborPeerGroupNameOptionsDef10:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfAsNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


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


    class SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdRoutingTransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: PolicyType4
        prefix_num: Union[
            OneOfNeighborMaxPrefixNumOptionsDef12,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
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
        value: Value1  # pytype: disable=annotation-type-mismatch


    class OneOfNeighborMaxPrefixNumOptionsDef13:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef13:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef33:
        option_type: DefaultOptionTypeDef
        value: int


    class SdRoutingTransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef3:
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


    class AddressFamily4:
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
                SdRoutingTransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef2,
                SdRoutingTransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class RoutingBgpNeighbor1:
        address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        remote_as: Union[
            V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfAsNumOptionsDef1,
            OneOfAsNumOptionsDef2,
        ]
        # Set BGP address family
        address_family: Optional[List[AddressFamily4]]
        as_number: Optional[
            Union[
                SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAsNumberOptionsDef1,
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
                SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        fall_over_bfd: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
                V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef3,
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
                V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef1,
                OneOfKeepaliveOptionsDef2,
                V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef3,
            ]
        ]
        local_as: Optional[
            Union[
                SdRoutingTransportGlobalVrfRoutingBgpOneOfLocalAsOptionsDef1,
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
                SdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborPasswordOptionsDef1,
                OneOfNeighborPasswordOptionsDef2,
                OneOfNeighborPasswordOptionsDef3,
            ]
        ]
        peer_group: Optional[OneOfNeighborPeerGroupNameOptionsDef10]
        route_reflect_client: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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


    class OneOfNeighborPeerGroupNameOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAsNumOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class OneOfKeepaliveOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfKeepaliveOptionsDef31:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfHoldtimeOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHoldtimeOptionsDef31:
        option_type: DefaultOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class PolicyType6:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfNeighborMaxPrefixNumOptionsDef14:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef14:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef34:
        option_type: DefaultOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: PolicyType6
        prefix_num: Union[
            OneOfNeighborMaxPrefixNumOptionsDef14,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2,
        ]
        threshold: Union[
            OneOfNeighborAddressFamilyThresholdOptionsDef14,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            OneOfNeighborAddressFamilyThresholdOptionsDef34,
        ]


    class PolicyType7:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: Value2  # pytype: disable=annotation-type-mismatch


    class OneOfNeighborMaxPrefixNumOptionsDef15:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef15:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef35:
        option_type: DefaultOptionTypeDef
        value: int


    class FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: PolicyType7
        prefix_num: Union[
            OneOfNeighborMaxPrefixNumOptionsDef15,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        threshold: Union[
            OneOfNeighborAddressFamilyThresholdOptionsDef15,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            OneOfNeighborAddressFamilyThresholdOptionsDef35,
        ]


    class AddressFamily5:
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
                FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef2,
                FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class RoutingBgpNeighbor2:
        peer_group: OneOfNeighborPeerGroupNameOptionsDef11
        remote_as: Union[OneOfAsNumOptionsDef11, OneOfAsNumOptionsDef2]
        address: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        # Set BGP address family
        address_family: Optional[List[AddressFamily5]]
        as_number: Optional[
            Union[
                FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAsNumberOptionsDef1,
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
                FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        fall_over_bfd: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                OneOfHoldtimeOptionsDef11,
                OneOfHoldtimeOptionsDef2,
                OneOfHoldtimeOptionsDef31,
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
                OneOfKeepaliveOptionsDef11,
                OneOfKeepaliveOptionsDef2,
                OneOfKeepaliveOptionsDef31,
            ]
        ]
        local_as: Optional[
            Union[
                FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfLocalAsOptionsDef1,
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
                FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborPasswordOptionsDef1,
                OneOfNeighborPasswordOptionsDef2,
                OneOfNeighborPasswordOptionsDef3,
            ]
        ]
        route_reflect_client: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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


    class OneOfNeighborPeerGroupNameOptionsDef12:
        option_type: GlobalOptionTypeDef
        value: str


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAsNumOptionsDef12:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfLocalAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class OneOfKeepaliveOptionsDef12:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfKeepaliveOptionsDef32:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfHoldtimeOptionsDef12:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHoldtimeOptionsDef32:
        option_type: DefaultOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAsNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class PolicyType8:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfNeighborMaxPrefixNumOptionsDef16:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef16:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef36:
        option_type: DefaultOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef2:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: PolicyType8
        prefix_num: Union[
            OneOfNeighborMaxPrefixNumOptionsDef16,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborMaxPrefixExceedRestartTimeOptionsDef1,
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2,
        ]
        threshold: Union[
            OneOfNeighborAddressFamilyThresholdOptionsDef16,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            OneOfNeighborAddressFamilyThresholdOptionsDef36,
        ]


    class PolicyType9:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: Value3  # pytype: disable=annotation-type-mismatch


    class OneOfNeighborMaxPrefixNumOptionsDef17:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef17:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef37:
        option_type: DefaultOptionTypeDef
        value: int


    class V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: PolicyType9
        prefix_num: Union[
            OneOfNeighborMaxPrefixNumOptionsDef17,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        threshold: Union[
            OneOfNeighborAddressFamilyThresholdOptionsDef17,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            OneOfNeighborAddressFamilyThresholdOptionsDef37,
        ]


    class AddressFamily6:
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
                V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef2,
                V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpNeighborMaxPrefixConfigDef3,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class RoutingBgpIpv6Neighbor1:
        address: Union[
            OneOfIpv6AddrGlobalVariableOptionsDef1,
            OneOfIpv6AddrGlobalVariableOptionsDef2,
        ]
        remote_as: Union[OneOfAsNumOptionsDef12, OneOfAsNumOptionsDef2]
        # Set IPv6 BGP address family
        address_family: Optional[List[AddressFamily6]]
        as_number: Optional[
            Union[
                V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborAsNumberOptionsDef1,
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
                V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborDescriptionOptionsDef1,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef1,
                OneOfNeighborEbgpMultihopOptionsDef2,
                V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborEbgpMultihopOptionsDef3,
            ]
        ]
        fall_over_bfd: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                OneOfHoldtimeOptionsDef12,
                OneOfHoldtimeOptionsDef2,
                OneOfHoldtimeOptionsDef32,
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
                OneOfKeepaliveOptionsDef12,
                OneOfKeepaliveOptionsDef2,
                OneOfKeepaliveOptionsDef32,
            ]
        ]
        local_as: Optional[
            Union[
                V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfLocalAsOptionsDef1,
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
                V1FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfNeighborPasswordOptionsDef1,
                OneOfNeighborPasswordOptionsDef2,
                OneOfNeighborPasswordOptionsDef3,
            ]
        ]
        peer_group: Optional[OneOfNeighborPeerGroupNameOptionsDef12]
        route_reflect_client: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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


    class OneOfNeighborPeerGroupNameOptionsDef13:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNeighborDescriptionOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAsNumOptionsDef13:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class OneOfLocalAsOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class OneOfKeepaliveOptionsDef13:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfKeepaliveOptionsDef33:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfHoldtimeOptionsDef13:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHoldtimeOptionsDef33:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfNeighborEbgpMultihopOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborEbgpMultihopOptionsDef31:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfNeighborPasswordOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNeighborAsNumberOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: int


    class PolicyType10:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfNeighborMaxPrefixNumOptionsDef18:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef18:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef38:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: int


    class NeighborMaxPrefixConfigDef21:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is restarting device.
        policy_type: PolicyType10
        prefix_num: Union[
            OneOfNeighborMaxPrefixNumOptionsDef18,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        restart_interval: Union[
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef11,
            OneOfNeighborMaxPrefixExceedRestartTimeOptionsDef2,
        ]
        threshold: Union[
            OneOfNeighborAddressFamilyThresholdOptionsDef18,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            OneOfNeighborAddressFamilyThresholdOptionsDef38,
        ]


    class PolicyType11:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: Value4  # pytype: disable=annotation-type-mismatch


    class OneOfNeighborMaxPrefixNumOptionsDef19:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef19:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNeighborAddressFamilyThresholdOptionsDef39:
        option_type: DefaultOptionTypeDef
        value: int


    class NeighborMaxPrefixConfigDef31:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: PolicyType11
        prefix_num: Union[
            OneOfNeighborMaxPrefixNumOptionsDef19,
            OneOfNeighborMaxPrefixNumOptionsDef2,
        ]
        threshold: Union[
            OneOfNeighborAddressFamilyThresholdOptionsDef19,
            OneOfNeighborAddressFamilyThresholdOptionsDef2,
            OneOfNeighborAddressFamilyThresholdOptionsDef39,
        ]


    class AddressFamily7:
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
                NeighborMaxPrefixConfigDef21,
                NeighborMaxPrefixConfigDef31,
            ]
        ]
        out_route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class RoutingBgpIpv6Neighbor2:
        peer_group: OneOfNeighborPeerGroupNameOptionsDef13
        remote_as: Union[OneOfAsNumOptionsDef13, OneOfAsNumOptionsDef2]
        address: Optional[
            Union[
                OneOfIpv6AddrGlobalVariableOptionsDef1,
                OneOfIpv6AddrGlobalVariableOptionsDef2,
            ]
        ]
        # Set IPv6 BGP address family
        address_family: Optional[List[AddressFamily7]]
        as_number: Optional[
            Union[
                OneOfNeighborAsNumberOptionsDef11,
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
                OneOfNeighborDescriptionOptionsDef11,
                OneOfNeighborDescriptionOptionsDef2,
                OneOfNeighborDescriptionOptionsDef3,
            ]
        ]
        ebgp_multihop: Optional[
            Union[
                OneOfNeighborEbgpMultihopOptionsDef11,
                OneOfNeighborEbgpMultihopOptionsDef2,
                OneOfNeighborEbgpMultihopOptionsDef31,
            ]
        ]
        fall_over_bfd: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                OneOfHoldtimeOptionsDef13,
                OneOfHoldtimeOptionsDef2,
                OneOfHoldtimeOptionsDef33,
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
                OneOfKeepaliveOptionsDef13,
                OneOfKeepaliveOptionsDef2,
                OneOfKeepaliveOptionsDef33,
            ]
        ]
        local_as: Optional[
            Union[
                OneOfLocalAsOptionsDef11,
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
                OneOfNeighborPasswordOptionsDef11,
                OneOfNeighborPasswordOptionsDef2,
                OneOfNeighborPasswordOptionsDef3,
            ]
        ]
        route_reflect_client: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
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


    class GlobalVrfRoutingBgpOneOfAddressFamilyPathsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class RoutingBgpOneOfIpv4AddressFamilyRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: RoutingBgpIpv4AddressFamilyRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class GlobalVrfRoutingBgpOneOfMetricOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalVrfRoutingBgpOneOfOspfMatchRouteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[
            GlobalVrfRoutingBgpOspfMatchRouteListDef
        ]  # pytype: disable=annotation-type-mismatch


    class TransportGlobalVrfRoutingBgpRedistribute:
        protocol: Union[
            RoutingBgpOneOfIpv4AddressFamilyRedistributeProtocolOptionsDef1,
            OneOfIpv4AddressFamilyRedistributeProtocolOptionsDef2,
        ]
        metric: Optional[
            Union[
                GlobalVrfRoutingBgpOneOfMetricOptionsDef1,
                OneOfMetricOptionsDef2,
                OneOfMetricOptionsDef3,
            ]
        ]
        ospf_match_route: Optional[
            Union[
                GlobalVrfRoutingBgpOneOfOspfMatchRouteOptionsDef1,
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


    class AddressFamily8:
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
                GlobalVrfRoutingBgpOneOfAddressFamilyPathsOptionsDef1,
                OneOfAddressFamilyPathsOptionsDef2,
                OneOfAddressFamilyPathsOptionsDef3,
            ]
        ]
        # Redistribute routes into BGP
        redistribute: Optional[
            List[TransportGlobalVrfRoutingBgpRedistribute]
        ]


    class TransportGlobalVrfRoutingBgpOneOfAddressFamilyPathsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class RoutingBgpOneOfIpv6AddressFamilyRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: RoutingBgpIpv6AddressFamilyRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class TransportGlobalVrfRoutingBgpOneOfMetricOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportGlobalVrfRoutingBgpOneOfOspfMatchRouteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[
            TransportGlobalVrfRoutingBgpOspfMatchRouteListDef
        ]  # pytype: disable=annotation-type-mismatch


    class SdRoutingTransportGlobalVrfRoutingBgpRedistribute:
        protocol: Union[
            RoutingBgpOneOfIpv6AddressFamilyRedistributeProtocolOptionsDef1,
            OneOfIpv6AddressFamilyRedistributeProtocolOptionsDef2,
        ]
        metric: Optional[
            Union[
                TransportGlobalVrfRoutingBgpOneOfMetricOptionsDef1,
                OneOfMetricOptionsDef2,
                OneOfMetricOptionsDef3,
            ]
        ]
        ospf_match_route: Optional[
            Union[
                TransportGlobalVrfRoutingBgpOneOfOspfMatchRouteOptionsDef1,
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


    class RoutingBgpIpv6AddressFamily:
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
                TransportGlobalVrfRoutingBgpOneOfAddressFamilyPathsOptionsDef1,
                OneOfAddressFamilyPathsOptionsDef2,
                OneOfAddressFamilyPathsOptionsDef3,
            ]
        ]
        # Redistribute routes into BGP
        redistribute: Optional[
            List[SdRoutingTransportGlobalVrfRoutingBgpRedistribute]
        ]


    class SdRoutingTransportGlobalVrfRoutingBgpData:
        as_num: Union[
            FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfAsNumOptionsDef1,
            OneOfAsNumOptionsDef2,
        ]
        # Set IPv4 unicast BGP address family
        address_family: Optional[AddressFamily8]
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
        # BGP dynamic neighbor configuration
        dynamic_neighbor: Optional[
            Union[
                RoutingBgpDynamicNeighbor1,
                RoutingBgpDynamicNeighbor2,
                RoutingBgpDynamicNeighbor3,
            ]
        ]
        external: Optional[
            Union[
                RoutingBgpOneOfExternalOptionsDef1,
                OneOfExternalOptionsDef2,
                RoutingBgpOneOfExternalOptionsDef3,
            ]
        ]
        holdtime: Optional[
            Union[
                FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef1,
                OneOfHoldtimeOptionsDef2,
                FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfHoldtimeOptionsDef3,
            ]
        ]
        internal: Optional[
            Union[
                RoutingBgpOneOfInternalOptionsDef1,
                OneOfInternalOptionsDef2,
                RoutingBgpOneOfInternalOptionsDef3,
            ]
        ]
        # Set BGP address family
        ipv6_address_family: Optional[RoutingBgpIpv6AddressFamily]
        # Set BGP IPv6 neighbors
        ipv6_neighbor: Optional[
            List[Union[RoutingBgpIpv6Neighbor1, RoutingBgpIpv6Neighbor2]]
        ]
        keepalive: Optional[
            Union[
                FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef1,
                OneOfKeepaliveOptionsDef2,
                FeatureProfileSdRoutingTransportGlobalVrfRoutingBgpOneOfKeepaliveOptionsDef3,
            ]
        ]
        local: Optional[
            Union[
                RoutingBgpOneOfLocalOptionsDef1,
                OneOfLocalOptionsDef2,
                RoutingBgpOneOfLocalOptionsDef3,
            ]
        ]
        missing_as_worst: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        multipath_relax: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # Set BGP IPv4 neighbors
        neighbor: Optional[
            List[Union[RoutingBgpNeighbor1, RoutingBgpNeighbor2]]
        ]
        router_id: Optional[
            Union[
                OneOfRouterIdOptionsDef1,
                OneOfRouterIdOptionsDef2,
                OneOfRouterIdOptionsDef3,
            ]
        ]


    class RoutingBgpPayload:
        """
        SD-Routing Routing BGP for VRF feature schema for request
        """

        data: SdRoutingTransportGlobalVrfRoutingBgpData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingTransportGlobalVrfGlobalVrfRoutingBgpPayload:
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
        # SD-Routing Routing BGP for VRF feature schema for request
        payload: Optional[RoutingBgpPayload]


    class EditTransportGlobalVrfAndRoutingBgpFeatureAssociationPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditTransportGlobalVrfAndRoutingBgpFeatureAssociationPutRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


