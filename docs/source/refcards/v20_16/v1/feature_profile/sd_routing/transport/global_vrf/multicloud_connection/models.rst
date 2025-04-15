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

    Value = Literal["ipv4-unicast", "vpnv4-unicast", "vpnv6-unicast"]

    MulticloudConnectionValue = Literal["disable-peer", "warning-only"]

    GlobalVrfMulticloudConnectionValue = Literal[
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


    class CreateTransportGlobalVrfAndMulticloudConnectionParcelAssociationPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


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
        value: bool


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
        value: bool


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
        value: bool


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


    class GlobalVrfMulticloudConnectionPolicyType:
        """
        Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        """

        option_type: GlobalOptionTypeDef
        value: MulticloudConnectionValue  # pytype: disable=annotation-type-mismatch


    class NeighborMaxPrefixConfigDef3:
        # Neighbor maximum prefix policy is enabled, when maximum prefix threshold is exceeded, policy action is warning-only or disable-peer.
        policy_type: GlobalVrfMulticloudConnectionPolicyType
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
        value: GlobalVrfMulticloudConnectionValue  # pytype: disable=annotation-type-mismatch


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


    class GlobalVrfMulticloudConnectionAddressFamily:
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
        value: bool


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


    class MulticloudConnectionData:
        """
        Parameters for the new Connection
        """

        # Set IPv4 unicast BGP address family
        address_family: Optional[
            GlobalVrfMulticloudConnectionAddressFamily
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
        data: Optional[MulticloudConnectionData]
        parcel_id: Optional[
            Union[
                OneOfExtensionsParcelIdOptionsDef1,
                OneOfExtensionsParcelIdOptionsDef2,
            ]
        ]


    class Data:
        connection_name: VariableOptionTypeObjectDef
        # Extending Bgp Neighbors, Ip Routes, Interface Parcel Id reference and Route Policy for Transport Profile to build new Connections
        extensions: Optional[List[Extensions]]


    class CreateTransportGlobalVrfAndMulticloudConnectionParcelAssociationPostRequest:
        """
        multi-cloud-connection profile parcel schema for POST request
        """

        data: Optional[Data]
        description: Optional[str]
        name: Optional[str]


