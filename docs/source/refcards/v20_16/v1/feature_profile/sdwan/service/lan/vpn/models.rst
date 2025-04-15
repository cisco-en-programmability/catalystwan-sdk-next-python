======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    AdvertiseIpv4ProtocolDef = Literal[
        "aggregate",
        "bgp",
        "connected",
        "eigrp",
        "isis",
        "lisp",
        "network",
        "ospf",
        "ospfv3",
        "static",
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

    RegionDef = Literal["access", "core", "core-and-access"]

    Value = Literal["core-and-access"]

    AdvertiseIpv6ProtocolDef = Literal[
        "Aggregate", "BGP", "Connected", "Network", "OSPF", "Static"
    ]

    ProtocolSubTypeDef = Literal["External"]

    Ipv6RouteNatDef = Literal["NAT64", "NAT66"]

    ServiceTypeDef = Literal[
        "FW",
        "IDP",
        "IDS",
        "TE",
        "appqoe",
        "netsvc1",
        "netsvc2",
        "netsvc3",
        "netsvc4",
    ]

    ServiceRouteDef = Literal["SIG", "SSE"]

    VpnValue = Literal["SIG"]

    NatDirectionDef = Literal["inside", "outside"]

    NatPortForwardProtocolDef = Literal["TCP", "UDP"]

    RouteLeakProtocolFromGlobalDef = Literal[
        "bgp", "connected", "ospf", "static"
    ]

    RouteLeakRedistributeGlobalProtocolDef = Literal["bgp", "ospf"]

    RouteLeakProtocolFromServiceDef = Literal[
        "bgp", "connected", "ospf", "static"
    ]

    RouteLeakRedistributeServiceProtocolDef = Literal["bgp", "ospf"]

    RouteImportFromProtocolDef = Literal[
        "bgp", "connected", "ospf", "static"
    ]

    RouteImportFromRedistributeProtocolDef = Literal["bgp", "ospf"]

    VpnAdvertiseIpv4ProtocolDef = Literal[
        "aggregate",
        "bgp",
        "connected",
        "eigrp",
        "isis",
        "lisp",
        "network",
        "ospf",
        "ospfv3",
        "static",
    ]

    VpnRegionDef = Literal["access", "core", "core-and-access"]

    VpnAdvertiseIpv6ProtocolDef = Literal[
        "Aggregate", "BGP", "Connected", "Network", "OSPF", "Static"
    ]

    VpnProtocolSubTypeDef = Literal["External"]

    LanVpnRegionDef = Literal["access", "core", "core-and-access"]

    VpnServiceTypeDef = Literal[
        "FW",
        "IDP",
        "IDS",
        "TE",
        "appqoe",
        "netsvc1",
        "netsvc2",
        "netsvc3",
        "netsvc4",
    ]

    VpnServiceRouteDef = Literal["SIG", "SSE"]

    VpnNatDirectionDef = Literal["inside", "outside"]

    VpnNatPortForwardProtocolDef = Literal["TCP", "UDP"]

    LanVpnNatDirectionDef = Literal["inside", "outside"]

    ServiceLanVpnNatDirectionDef = Literal["inside", "outside"]

    VpnRouteLeakProtocolFromGlobalDef = Literal[
        "bgp", "connected", "ospf", "static"
    ]

    VpnRouteLeakRedistributeGlobalProtocolDef = Literal["bgp", "ospf"]

    VpnRouteLeakProtocolFromServiceDef = Literal[
        "bgp", "connected", "ospf", "static"
    ]

    VpnRouteLeakRedistributeServiceProtocolDef = Literal["bgp", "ospf"]

    VpnRouteImportFromProtocolDef = Literal[
        "bgp", "connected", "ospf", "static"
    ]

    VpnRouteImportFromRedistributeProtocolDef = Literal["bgp", "ospf"]

    LanVpnAdvertiseIpv4ProtocolDef = Literal[
        "aggregate",
        "bgp",
        "connected",
        "eigrp",
        "isis",
        "lisp",
        "network",
        "ospf",
        "ospfv3",
        "static",
    ]

    ServiceLanVpnRegionDef = Literal["access", "core", "core-and-access"]

    LanVpnAdvertiseIpv6ProtocolDef = Literal[
        "Aggregate", "BGP", "Connected", "Network", "OSPF", "Static"
    ]

    LanVpnProtocolSubTypeDef = Literal["External"]

    SdwanServiceLanVpnRegionDef = Literal[
        "access", "core", "core-and-access"
    ]

    LanVpnServiceTypeDef = Literal[
        "FW",
        "IDP",
        "IDS",
        "TE",
        "appqoe",
        "netsvc1",
        "netsvc2",
        "netsvc3",
        "netsvc4",
    ]

    LanVpnServiceRouteDef = Literal["SIG", "SSE"]

    SdwanServiceLanVpnNatDirectionDef = Literal["inside", "outside"]

    LanVpnNatPortForwardProtocolDef = Literal["TCP", "UDP"]

    FeatureProfileSdwanServiceLanVpnNatDirectionDef = Literal[
        "inside", "outside"
    ]

    V1FeatureProfileSdwanServiceLanVpnNatDirectionDef = Literal[
        "inside", "outside"
    ]

    LanVpnRouteLeakProtocolFromGlobalDef = Literal[
        "bgp", "connected", "ospf", "static"
    ]

    LanVpnRouteLeakRedistributeGlobalProtocolDef = Literal["bgp", "ospf"]

    LanVpnRouteLeakProtocolFromServiceDef = Literal[
        "bgp", "connected", "ospf", "static"
    ]

    LanVpnRouteLeakRedistributeServiceProtocolDef = Literal["bgp", "ospf"]

    LanVpnRouteImportFromProtocolDef = Literal[
        "bgp", "connected", "ospf", "static"
    ]

    LanVpnRouteImportFromRedistributeProtocolDef = Literal["bgp", "ospf"]


    class OneOfVpnIdOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVpnIdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVpnIdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfVpnNameOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVpnNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVpnNameOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfOmpAdminIpv4OptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOmpAdminIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfOmpAdminIpv4OptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfOmpAdminIpv6OptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOmpAdminIpv6OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfOmpAdminIpv6OptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfPrimaryDnsAddressIpv4OptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPrimaryDnsAddressIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfPrimaryDnsAddressIpv4OptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfSecondaryDnsAddressIpv4OptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSecondaryDnsAddressIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSecondaryDnsAddressIpv4OptionsDef3:
        option_type: DefaultOptionTypeDef


    class DnsIpv4:
        primary_dns_address_ipv4: Optional[
            Union[
                OneOfPrimaryDnsAddressIpv4OptionsDef1,
                OneOfPrimaryDnsAddressIpv4OptionsDef2,
                OneOfPrimaryDnsAddressIpv4OptionsDef3,
            ]
        ]
        secondary_dns_address_ipv4: Optional[
            Union[
                OneOfSecondaryDnsAddressIpv4OptionsDef1,
                OneOfSecondaryDnsAddressIpv4OptionsDef2,
                OneOfSecondaryDnsAddressIpv4OptionsDef3,
            ]
        ]


    class OneOfPrimaryDnsAddressIpv6OptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPrimaryDnsAddressIpv6OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfPrimaryDnsAddressIpv6OptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfSecondaryDnsAddressIpv6OptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSecondaryDnsAddressIpv6OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSecondaryDnsAddressIpv6OptionsDef3:
        option_type: DefaultOptionTypeDef


    class DnsIpv6:
        primary_dns_address_ipv6: Optional[
            Union[
                OneOfPrimaryDnsAddressIpv6OptionsDef1,
                OneOfPrimaryDnsAddressIpv6OptionsDef2,
                OneOfPrimaryDnsAddressIpv6OptionsDef3,
            ]
        ]
        secondary_dns_address_ipv6: Optional[
            Union[
                OneOfSecondaryDnsAddressIpv6OptionsDef1,
                OneOfSecondaryDnsAddressIpv6OptionsDef2,
                OneOfSecondaryDnsAddressIpv6OptionsDef3,
            ]
        ]


    class OneOfHostNameOptionsWithoutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHostNameOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfListOfIpOptionsWithoutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfListOfIpOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: List[Union[Any, Any]]


    class NewHostMapping:
        host_name: Union[
            OneOfHostNameOptionsWithoutDefault1,
            OneOfHostNameOptionsWithoutDefault2,
        ]
        list_of_ip: Union[
            OneOfListOfIpOptionsWithoutDefault1,
            OneOfListOfIpOptionsWithoutDefault2,
        ]


    class OneOfAdvertiseIpv4ProtocolOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAdvertiseIpv4ProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: AdvertiseIpv4ProtocolDef  # pytype: disable=annotation-type-mismatch


    class OneOfRoutePolicyNameOptionsDef1:
        option_type: DefaultOptionTypeDef


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRoutePolicyNameOptionsDef2:
        ref_id: RefId


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


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfRegionOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRegionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: RegionDef  # pytype: disable=annotation-type-mismatch


    class OneOfRegionOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class PrefixList:
        prefix: Ipv4AddressAndMaskDef
        aggregate_only: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        region: Optional[
            Union[
                OneOfRegionOptionsDef1,
                OneOfRegionOptionsDef2,
                OneOfRegionOptionsDef3,
            ]
        ]


    class OmpAdvertiseIp4:
        omp_protocol: Union[
            OneOfAdvertiseIpv4ProtocolOptionsDef1,
            OneOfAdvertiseIpv4ProtocolOptionsDef2,
        ]
        # IPv4 Prefix List
        prefix_list: Optional[List[PrefixList]]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class OneOfAdvertiseIpv6ProtocolOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAdvertiseIpv6ProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: AdvertiseIpv6ProtocolDef  # pytype: disable=annotation-type-mismatch


    class OneOfAdvertiseIpv6ProtocolSubTypeOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAdvertiseIpv6ProtocolSubTypeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: (
            ProtocolSubTypeDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfAdvertiseIpv6ProtocolSubTypeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfIpv6PrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6PrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class VpnPrefixList:
        prefix: Union[
            OneOfIpv6PrefixOptionsDef1, OneOfIpv6PrefixOptionsDef2
        ]
        aggregate_only: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        region: Optional[
            Union[
                OneOfRegionOptionsDef1,
                OneOfRegionOptionsDef2,
                OneOfRegionOptionsDef3,
            ]
        ]


    class OmpAdvertiseIpv6:
        omp_protocol: Union[
            OneOfAdvertiseIpv6ProtocolOptionsDef1,
            OneOfAdvertiseIpv6ProtocolOptionsDef2,
        ]
        # IPv6 Prefix List
        prefix_list: Optional[List[VpnPrefixList]]
        protocol_sub_type: Optional[
            Union[
                OneOfAdvertiseIpv6ProtocolSubTypeOptionsDef1,
                OneOfAdvertiseIpv6ProtocolSubTypeOptionsDef2,
                OneOfAdvertiseIpv6ProtocolSubTypeOptionsDef3,
            ]
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


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
        value: bool


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


    class OneOfIpRoute2:
        null0: Union[
            OneOfIpv4V6RouteNull0OptionsWithoutVariable1,
            OneOfIpv4V6RouteNull0OptionsWithoutVariable2,
        ]
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                OneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]


    class OneOfIpv4RouteDhcpOptionsWithoutVariable1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfIpv4RouteDhcpOptionsWithoutVariable2:
        option_type: DefaultOptionTypeDef
        value: bool


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
        value: bool


    class OneOfIpRoute4:
        vpn: Union[
            OneOfIpv4RouteVpnOptionsWithoutVariable1,
            OneOfIpv4RouteVpnOptionsWithoutVariable2,
        ]


    class InterfaceName1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class InterfaceName2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv4NextHopAddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv4NextHopAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv4NextHopAddressOptionsDef3:
        option_type: DefaultOptionTypeDef


    class VpnNextHop:
        address: Union[
            OneOfIpv4NextHopAddressOptionsDef1,
            OneOfIpv4NextHopAddressOptionsDef2,
            OneOfIpv4NextHopAddressOptionsDef3,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            OneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class IpStaticRouteInterface:
        interface_name: Union[InterfaceName1, InterfaceName2]
        next_hop: Optional[List[VpnNextHop]]


    class InterfaceContainer:
        ip_static_route_interface: List[IpStaticRouteInterface]


    class OneOfIpRoute5:
        interface_container: InterfaceContainer


    class Ipv4Route:
        one_of_ip_route: Union[
            OneOfIpRoute1,
            OneOfIpRoute2,
            OneOfIpRoute3,
            OneOfIpRoute4,
            OneOfIpRoute5,
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


    class LanVpnNextHop:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            OneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class VpnNextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[List[LanVpnNextHop]]


    class VpnOneOfIpRoute1:
        next_hop_container: VpnNextHopContainer


    class VpnOneOfIpRoute2:
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


    class VpnOneOfIpRoute3:
        nat: Union[
            OneOfIpv6RouteNatOptionsWithoutDefault1,
            OneOfIpv6RouteNatOptionsWithoutDefault2,
        ]


    class OneOfIpv6NextHopAddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6NextHopAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6NextHopAddressOptionsDef3:
        option_type: DefaultOptionTypeDef


    class ServiceLanVpnNextHop:
        address: Union[
            OneOfIpv6NextHopAddressOptionsDef1,
            OneOfIpv6NextHopAddressOptionsDef2,
            OneOfIpv6NextHopAddressOptionsDef3,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            OneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class Ipv6StaticRouteInterface:
        interface_name: Union[InterfaceName1, InterfaceName2]
        next_hop: Optional[List[ServiceLanVpnNextHop]]


    class VpnInterfaceContainer:
        ipv6_static_route_interface: List[Ipv6StaticRouteInterface]


    class VpnOneOfIpRoute4:
        interface_container: VpnInterfaceContainer


    class Ipv6Route:
        one_of_ip_route: Union[
            VpnOneOfIpRoute1,
            VpnOneOfIpRoute2,
            VpnOneOfIpRoute3,
            VpnOneOfIpRoute4,
        ]
        prefix: Union[
            OneOfIpv6RoutePrefixOptionsDef1,
            OneOfIpv6RoutePrefixOptionsDef2,
        ]


    class OneOfServiceTypeOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfServiceTypeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: ServiceTypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfListOfIpV4OptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfListOfIpV4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfServiceTrackingOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfServiceTrackingOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfServiceTrackingOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class Service:
        ipv4_addresses: Union[
            OneOfListOfIpV4OptionsDef1, OneOfListOfIpV4OptionsDef2
        ]
        service_type: Union[
            OneOfServiceTypeOptionsDef1, OneOfServiceTypeOptionsDef2
        ]
        tracking: Union[
            OneOfServiceTrackingOptionsDef1,
            OneOfServiceTrackingOptionsDef2,
            OneOfServiceTrackingOptionsDef3,
        ]


    class VpnPrefix:
        """
        Service Route Ip and Subnet Mask
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class OneOfServiceRouteServiceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfServiceRouteServiceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: ServiceRouteDef  # pytype: disable=annotation-type-mismatch


    class OneOfServiceRouteServiceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: VpnValue  # pytype: disable=annotation-type-mismatch


    class OneOfDefaultVpnIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSseInstanceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSseInstanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceRoute:
        # Service Route Ip and Subnet Mask
        prefix: VpnPrefix
        service: Union[
            OneOfServiceRouteServiceOptionsDef1,
            OneOfServiceRouteServiceOptionsDef2,
            OneOfServiceRouteServiceOptionsDef3,
        ]
        vpn: OneOfDefaultVpnIdOptionsDef
        sse_instance: Optional[
            Union[
                OneOfSseInstanceOptionsDef1, OneOfSseInstanceOptionsDef2
            ]
        ]


    class LanVpnPrefix:
        """
        GRE Route Ip and Subnet Mask
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class OneOfGreRouteInterfaceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfGreRouteInterfaceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfGreRouteInterfaceOptionsDef3:
        option_type: DefaultOptionTypeDef


    class GreRoute:
        interface: Union[
            OneOfGreRouteInterfaceOptionsDef1,
            OneOfGreRouteInterfaceOptionsDef2,
            OneOfGreRouteInterfaceOptionsDef3,
        ]
        # GRE Route Ip and Subnet Mask
        prefix: LanVpnPrefix
        vpn: OneOfDefaultVpnIdOptionsDef


    class ServiceLanVpnPrefix:
        """
        IPSEC Route Ip and Subnet Mask
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class OneOfIpsecRouteInterfaceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpsecRouteInterfaceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfIpsecRouteInterfaceOptionsDef3:
        option_type: DefaultOptionTypeDef


    class IpsecRoute:
        interface: Union[
            OneOfIpsecRouteInterfaceOptionsDef1,
            OneOfIpsecRouteInterfaceOptionsDef2,
            OneOfIpsecRouteInterfaceOptionsDef3,
        ]
        # IPSEC Route Ip and Subnet Mask
        prefix: ServiceLanVpnPrefix


    class OneOfNatPoolNameOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPoolNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNatPoolPrefixLengthOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPoolPrefixLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


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
        value: bool


    class OneOfNatPoolDirectionOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPoolDirectionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: NatDirectionDef  # pytype: disable=annotation-type-mismatch


    class NatPool:
        direction: Union[
            OneOfNatPoolDirectionOptionsDef1,
            OneOfNatPoolDirectionOptionsDef2,
        ]
        nat_pool_name: Union[
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
        # Tracking object for NAT configuration
        tracking_object: Optional[Any]


    class OneOfNatPoolNameInUseOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPoolNameInUseOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNatPoolNameInUseOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfNatPortForwardSourcePortOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPortForwardSourcePortOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNatPortForwardTranslatePortOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPortForwardTranslatePortOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNatPortForwardSourceIpAddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPortForwardSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNatPortForwardTranslatedSourceIpAddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPortForwardTranslatedSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNatPortForwardProtocolOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPortForwardProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: NatPortForwardProtocolDef  # pytype: disable=annotation-type-mismatch


    class NatPortForward:
        nat_pool_name: Union[
            OneOfNatPoolNameInUseOptionsDef1,
            OneOfNatPoolNameInUseOptionsDef2,
            OneOfNatPoolNameInUseOptionsDef3,
        ]
        protocol: Union[
            OneOfNatPortForwardProtocolOptionsDef1,
            OneOfNatPortForwardProtocolOptionsDef2,
        ]
        source_ip: Union[
            OneOfNatPortForwardSourceIpAddressOptionsDef1,
            OneOfNatPortForwardSourceIpAddressOptionsDef2,
        ]
        source_port: Union[
            OneOfNatPortForwardSourcePortOptionsDef1,
            OneOfNatPortForwardSourcePortOptionsDef2,
        ]
        translate_port: Union[
            OneOfNatPortForwardTranslatePortOptionsDef1,
            OneOfNatPortForwardTranslatePortOptionsDef2,
        ]
        translated_source_ip: Union[
            OneOfNatPortForwardTranslatedSourceIpAddressOptionsDef1,
            OneOfNatPortForwardTranslatedSourceIpAddressOptionsDef2,
        ]


    class OneOfStaticNatSourceIpAddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticNatSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfStaticNatTranslatedSourceIpAddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticNatTranslatedSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfStaticNatDirectionOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticNatDirectionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: NatDirectionDef  # pytype: disable=annotation-type-mismatch


    class StaticNat:
        nat_pool_name: Optional[
            Union[
                OneOfNatPoolNameInUseOptionsDef1,
                OneOfNatPoolNameInUseOptionsDef2,
                OneOfNatPoolNameInUseOptionsDef3,
            ]
        ]
        source_ip: Optional[
            Union[
                OneOfStaticNatSourceIpAddressOptionsDef1,
                OneOfStaticNatSourceIpAddressOptionsDef2,
            ]
        ]
        static_nat_direction: Optional[
            Union[
                OneOfStaticNatDirectionOptionsDef1,
                OneOfStaticNatDirectionOptionsDef2,
            ]
        ]
        # Tracking object for NAT configuration
        tracking_object: Optional[Any]
        translated_source_ip: Optional[
            Union[
                OneOfStaticNatTranslatedSourceIpAddressOptionsDef1,
                OneOfStaticNatTranslatedSourceIpAddressOptionsDef2,
            ]
        ]


    class OneOfStaticNatSubnetPrefixLengthOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfStaticNatSubnetPrefixLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class StaticNatSubnet:
        prefix_length: Optional[
            Union[
                OneOfStaticNatSubnetPrefixLengthOptionsDef1,
                OneOfStaticNatSubnetPrefixLengthOptionsDef2,
            ]
        ]
        source_ip_subnet: Optional[
            Union[
                OneOfStaticNatSourceIpAddressOptionsDef1,
                OneOfStaticNatSourceIpAddressOptionsDef2,
            ]
        ]
        static_nat_direction: Optional[
            Union[
                OneOfStaticNatDirectionOptionsDef1,
                OneOfStaticNatDirectionOptionsDef2,
            ]
        ]
        # Tracking object for NAT configuration
        tracking_object: Optional[Any]
        translated_source_ip_subnet: Optional[
            Union[
                OneOfStaticNatTranslatedSourceIpAddressOptionsDef1,
                OneOfStaticNatTranslatedSourceIpAddressOptionsDef2,
            ]
        ]


    class OneOfNat64V4PoolNameOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNat64V4PoolNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNat64V4PoolRangeStartOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNat64V4PoolRangeStartOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNat64V4PoolRangeEndOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNat64V4PoolRangeEndOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNat64V4PoolOverloadOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNat64V4PoolOverloadOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfNat64V4PoolOverloadOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class Nat64V4Pool:
        nat64_v4_pool_name: Union[
            OneOfNat64V4PoolNameOptionsDef1,
            OneOfNat64V4PoolNameOptionsDef2,
        ]
        nat64_v4_pool_overload: Union[
            OneOfNat64V4PoolOverloadOptionsDef1,
            OneOfNat64V4PoolOverloadOptionsDef2,
            OneOfNat64V4PoolOverloadOptionsDef3,
        ]
        nat64_v4_pool_range_end: Union[
            OneOfNat64V4PoolRangeEndOptionsDef1,
            OneOfNat64V4PoolRangeEndOptionsDef2,
        ]
        nat64_v4_pool_range_start: Union[
            OneOfNat64V4PoolRangeStartOptionsDef1,
            OneOfNat64V4PoolRangeStartOptionsDef2,
        ]


    class OneOfRouteLeakFromGlobalProtocolOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRouteLeakFromGlobalProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: RouteLeakProtocolFromGlobalDef  # pytype: disable=annotation-type-mismatch


    class OneOfRouteLeakFromGlobalRedistributeProtocolOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRouteLeakFromGlobalRedistributeProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: RouteLeakRedistributeGlobalProtocolDef  # pytype: disable=annotation-type-mismatch


    class RedistributeToProtocol:
        protocol: Union[
            OneOfRouteLeakFromGlobalRedistributeProtocolOptionsDef1,
            OneOfRouteLeakFromGlobalRedistributeProtocolOptionsDef2,
        ]
        policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class RouteLeakFromGlobal:
        route_protocol: Union[
            OneOfRouteLeakFromGlobalProtocolOptionsDef1,
            OneOfRouteLeakFromGlobalProtocolOptionsDef2,
        ]
        # Redistribute Routes to specific Protocol on Service VPN
        redistribute_to_protocol: Optional[List[RedistributeToProtocol]]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class OneOfRouteLeakFromServiceProtocolOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRouteLeakFromServiceProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: RouteLeakProtocolFromServiceDef  # pytype: disable=annotation-type-mismatch


    class OneOfRouteLeakFromServiceRedistributeProtocolOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRouteLeakFromServiceRedistributeProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: RouteLeakRedistributeServiceProtocolDef  # pytype: disable=annotation-type-mismatch


    class VpnRedistributeToProtocol:
        protocol: Union[
            OneOfRouteLeakFromServiceRedistributeProtocolOptionsDef1,
            OneOfRouteLeakFromServiceRedistributeProtocolOptionsDef2,
        ]
        policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class RouteLeakFromService:
        route_protocol: Union[
            OneOfRouteLeakFromServiceProtocolOptionsDef1,
            OneOfRouteLeakFromServiceProtocolOptionsDef2,
        ]
        # Redistribute Routes to specific Protocol on Global VPN
        redistribute_to_protocol: Optional[
            List[VpnRedistributeToProtocol]
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class OneOfRouteImportFromSourceVpnOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRouteImportFromSourceVpnOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRouteImportFromProtocolOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRouteImportFromProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: RouteImportFromProtocolDef  # pytype: disable=annotation-type-mismatch


    class OneOfRouteImportFromRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: RouteImportFromRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class OneOfRouteImportFromRedistributeProtocolOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class LanVpnRedistributeToProtocol:
        protocol: Union[
            OneOfRouteImportFromRedistributeProtocolOptionsDef1,
            OneOfRouteImportFromRedistributeProtocolOptionsDef2,
        ]
        policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class RouteLeakBetweenServices:
        route_protocol: Union[
            OneOfRouteImportFromProtocolOptionsDef1,
            OneOfRouteImportFromProtocolOptionsDef2,
        ]
        source_vpn: Union[
            OneOfRouteImportFromSourceVpnOptionsDef1,
            OneOfRouteImportFromSourceVpnOptionsDef2,
        ]
        # Redistribute Route to specific Protocol on Current Service VPN
        redistribute_to_protocol: Optional[
            List[LanVpnRedistributeToProtocol]
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class MplsVpnRouteTargetOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class MplsVpnRouteTargetOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class MplsVpnRouteTargetsDef:
        rt: Union[
            MplsVpnRouteTargetOptionsDef1, MplsVpnRouteTargetOptionsDef2
        ]


    class MplsVpnIpv4RouteTarget:
        export_rt_list: Optional[List[MplsVpnRouteTargetsDef]]
        import_rt_list: Optional[List[MplsVpnRouteTargetsDef]]


    class MplsVpnIpv6RouteTarget:
        export_rt_list: Optional[List[MplsVpnRouteTargetsDef]]
        import_rt_list: Optional[List[MplsVpnRouteTargetsDef]]


    class OneOfEnableSdraDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfEnableSdraDef2:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[bool]


    class VpnData:
        name: Union[
            OneOfVpnNameOptionsDef1,
            OneOfVpnNameOptionsDef2,
            OneOfVpnNameOptionsDef3,
        ]
        vpn_id: Union[
            OneOfVpnIdOptionsDef1,
            OneOfVpnIdOptionsDef2,
            OneOfVpnIdOptionsDef3,
        ]
        dns_ipv4: Optional[DnsIpv4]
        dns_ipv6: Optional[DnsIpv6]
        enable_sdra: Optional[
            Union[OneOfEnableSdraDef1, OneOfEnableSdraDef2]
        ]
        # IPv4 Static GRE Route
        gre_route: Optional[List[GreRoute]]
        # IPv4 Static IPSEC Route
        ipsec_route: Optional[List[IpsecRoute]]
        # IPv4 Static Route
        ipv4_route: Optional[List[Ipv4Route]]
        # IPv6 Static Route
        ipv6_route: Optional[List[Ipv6Route]]
        mpls_vpn_ipv4_route_target: Optional[MplsVpnIpv4RouteTarget]
        mpls_vpn_ipv6_route_target: Optional[MplsVpnIpv6RouteTarget]
        # NAT64 V4 Pool
        nat64_v4_pool: Optional[List[Nat64V4Pool]]
        # NAT Pool
        nat_pool: Optional[List[NatPool]]
        # NAT Port Forward
        nat_port_forward: Optional[List[NatPortForward]]
        new_host_mapping: Optional[List[NewHostMapping]]
        omp_admin_distance: Optional[
            Union[
                OneOfOmpAdminIpv4OptionsDef1,
                OneOfOmpAdminIpv4OptionsDef2,
                OneOfOmpAdminIpv4OptionsDef3,
            ]
        ]
        omp_admin_distance_ipv6: Optional[
            Union[
                OneOfOmpAdminIpv6OptionsDef1,
                OneOfOmpAdminIpv6OptionsDef2,
                OneOfOmpAdminIpv6OptionsDef3,
            ]
        ]
        # OMP Advertise IPv4
        omp_advertise_ip4: Optional[List[OmpAdvertiseIp4]]
        # OMP Advertise IPv6
        omp_advertise_ipv6: Optional[List[OmpAdvertiseIpv6]]
        # Enable route leak from another Service VPN to current Service VPN
        route_leak_between_services: Optional[
            List[RouteLeakBetweenServices]
        ]
        # Enable route leaking from Global to Service VPN
        route_leak_from_global: Optional[List[RouteLeakFromGlobal]]
        # Enable route leaking from Service to Global VPN
        route_leak_from_service: Optional[List[RouteLeakFromService]]
        # Service
        service: Optional[List[Service]]
        # Service
        service_route: Optional[List[ServiceRoute]]
        # Static NAT Rules
        static_nat: Optional[List[StaticNat]]
        # Static NAT Subnet Rules
        static_nat_subnet: Optional[List[StaticNatSubnet]]


    class Payload:
        """
        LAN VPN feature schema for POST request
        """

        data: VpnData
        name: str
        # Set the Feature description
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
        # LAN VPN feature schema for POST request
        payload: Optional[Payload]


    class GetListSdwanServiceLanVpnPayload:
        data: Optional[List[Data]]


    class CreateLanVpnProfileParcelForServicePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class LanVpnData:
        name: Union[
            OneOfVpnNameOptionsDef1,
            OneOfVpnNameOptionsDef2,
            OneOfVpnNameOptionsDef3,
        ]
        vpn_id: Union[
            OneOfVpnIdOptionsDef1,
            OneOfVpnIdOptionsDef2,
            OneOfVpnIdOptionsDef3,
        ]
        dns_ipv4: Optional[DnsIpv4]
        dns_ipv6: Optional[DnsIpv6]
        enable_sdra: Optional[
            Union[OneOfEnableSdraDef1, OneOfEnableSdraDef2]
        ]
        # IPv4 Static GRE Route
        gre_route: Optional[List[GreRoute]]
        # IPv4 Static IPSEC Route
        ipsec_route: Optional[List[IpsecRoute]]
        # IPv4 Static Route
        ipv4_route: Optional[List[Ipv4Route]]
        # IPv6 Static Route
        ipv6_route: Optional[List[Ipv6Route]]
        mpls_vpn_ipv4_route_target: Optional[MplsVpnIpv4RouteTarget]
        mpls_vpn_ipv6_route_target: Optional[MplsVpnIpv6RouteTarget]
        # NAT64 V4 Pool
        nat64_v4_pool: Optional[List[Nat64V4Pool]]
        # NAT Pool
        nat_pool: Optional[List[NatPool]]
        # NAT Port Forward
        nat_port_forward: Optional[List[NatPortForward]]
        new_host_mapping: Optional[List[NewHostMapping]]
        omp_admin_distance: Optional[
            Union[
                OneOfOmpAdminIpv4OptionsDef1,
                OneOfOmpAdminIpv4OptionsDef2,
                OneOfOmpAdminIpv4OptionsDef3,
            ]
        ]
        omp_admin_distance_ipv6: Optional[
            Union[
                OneOfOmpAdminIpv6OptionsDef1,
                OneOfOmpAdminIpv6OptionsDef2,
                OneOfOmpAdminIpv6OptionsDef3,
            ]
        ]
        # OMP Advertise IPv4
        omp_advertise_ip4: Optional[List[OmpAdvertiseIp4]]
        # OMP Advertise IPv6
        omp_advertise_ipv6: Optional[List[OmpAdvertiseIpv6]]
        # Enable route leak from another Service VPN to current Service VPN
        route_leak_between_services: Optional[
            List[RouteLeakBetweenServices]
        ]
        # Enable route leaking from Global to Service VPN
        route_leak_from_global: Optional[List[RouteLeakFromGlobal]]
        # Enable route leaking from Service to Global VPN
        route_leak_from_service: Optional[List[RouteLeakFromService]]
        # Service
        service: Optional[List[Service]]
        # Service
        service_route: Optional[List[ServiceRoute]]
        # Static NAT Rules
        static_nat: Optional[List[StaticNat]]
        # Static NAT Subnet Rules
        static_nat_subnet: Optional[List[StaticNatSubnet]]


    class CreateLanVpnProfileParcelForServicePostRequest:
        """
        LAN VPN feature schema for POST request
        """

        data: LanVpnData
        name: str
        # Set the Feature description
        description: Optional[str]
        metadata: Optional[Any]


    class VpnOneOfVpnIdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnOneOfOmpAdminIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnOneOfOmpAdminIpv6OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnOneOfPrimaryDnsAddressIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnOneOfSecondaryDnsAddressIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnDnsIpv4:
        primary_dns_address_ipv4: Optional[
            Union[
                OneOfPrimaryDnsAddressIpv4OptionsDef1,
                VpnOneOfPrimaryDnsAddressIpv4OptionsDef2,
                OneOfPrimaryDnsAddressIpv4OptionsDef3,
            ]
        ]
        secondary_dns_address_ipv4: Optional[
            Union[
                OneOfSecondaryDnsAddressIpv4OptionsDef1,
                VpnOneOfSecondaryDnsAddressIpv4OptionsDef2,
                OneOfSecondaryDnsAddressIpv4OptionsDef3,
            ]
        ]


    class VpnDnsIpv6:
        primary_dns_address_ipv6: Optional[
            Union[
                OneOfPrimaryDnsAddressIpv6OptionsDef1,
                OneOfPrimaryDnsAddressIpv6OptionsDef2,
                OneOfPrimaryDnsAddressIpv6OptionsDef3,
            ]
        ]
        secondary_dns_address_ipv6: Optional[
            Union[
                OneOfSecondaryDnsAddressIpv6OptionsDef1,
                OneOfSecondaryDnsAddressIpv6OptionsDef2,
                OneOfSecondaryDnsAddressIpv6OptionsDef3,
            ]
        ]


    class VpnOneOfAdvertiseIpv4ProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: VpnAdvertiseIpv4ProtocolDef  # pytype: disable=annotation-type-mismatch


    class VpnOneOfRegionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: VpnRegionDef  # pytype: disable=annotation-type-mismatch


    class VpnOneOfRegionOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[Value]


    class LanVpnPrefixList:
        prefix: Ipv4AddressAndMaskDef
        aggregate_only: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        region: Optional[
            Union[
                OneOfRegionOptionsDef1,
                VpnOneOfRegionOptionsDef2,
                VpnOneOfRegionOptionsDef3,
            ]
        ]


    class VpnOmpAdvertiseIp4:
        omp_protocol: Union[
            OneOfAdvertiseIpv4ProtocolOptionsDef1,
            VpnOneOfAdvertiseIpv4ProtocolOptionsDef2,
        ]
        # IPv4 Prefix List
        prefix_list: Optional[List[LanVpnPrefixList]]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class VpnOneOfAdvertiseIpv6ProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: VpnAdvertiseIpv6ProtocolDef  # pytype: disable=annotation-type-mismatch


    class VpnOneOfAdvertiseIpv6ProtocolSubTypeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: VpnProtocolSubTypeDef  # pytype: disable=annotation-type-mismatch


    class LanVpnOneOfRegionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LanVpnRegionDef  # pytype: disable=annotation-type-mismatch


    class LanVpnOneOfRegionOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[Value]


    class ServiceLanVpnPrefixList:
        prefix: Union[
            OneOfIpv6PrefixOptionsDef1, OneOfIpv6PrefixOptionsDef2
        ]
        aggregate_only: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        region: Optional[
            Union[
                OneOfRegionOptionsDef1,
                LanVpnOneOfRegionOptionsDef2,
                LanVpnOneOfRegionOptionsDef3,
            ]
        ]


    class VpnOmpAdvertiseIpv6:
        omp_protocol: Union[
            OneOfAdvertiseIpv6ProtocolOptionsDef1,
            VpnOneOfAdvertiseIpv6ProtocolOptionsDef2,
        ]
        # IPv6 Prefix List
        prefix_list: Optional[List[ServiceLanVpnPrefixList]]
        protocol_sub_type: Optional[
            Union[
                OneOfAdvertiseIpv6ProtocolSubTypeOptionsDef1,
                VpnOneOfAdvertiseIpv6ProtocolSubTypeOptionsDef2,
                OneOfAdvertiseIpv6ProtocolSubTypeOptionsDef3,
            ]
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class VpnOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanServiceLanVpnNextHop:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            VpnOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class LanVpnOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnNextHopWithTracker:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            LanVpnOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]
        tracker: Union[
            OneOfIpv4NextHopTrackerOptionsDef1,
            OneOfIpv4NextHopTrackerOptionsDef2,
        ]


    class LanVpnNextHopContainer:
        # IPv4 Route Gateway Next Hop
        next_hop: Optional[List[SdwanServiceLanVpnNextHop]]
        # IPv4 Route Gateway Next Hop with Tracker
        next_hop_with_tracker: Optional[List[VpnNextHopWithTracker]]


    class LanVpnOneOfIpRoute1:
        next_hop_container: LanVpnNextHopContainer


    class VpnOneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnOneOfIpRoute2:
        null0: Union[
            OneOfIpv4V6RouteNull0OptionsWithoutVariable1,
            OneOfIpv4V6RouteNull0OptionsWithoutVariable2,
        ]
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                VpnOneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]


    class VpnOneOfIpv4NextHopAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceLanVpnOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdwanServiceLanVpnNextHop:
        address: Union[
            OneOfIpv4NextHopAddressOptionsDef1,
            VpnOneOfIpv4NextHopAddressOptionsDef2,
            OneOfIpv4NextHopAddressOptionsDef3,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            ServiceLanVpnOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class VpnIpStaticRouteInterface:
        interface_name: Union[InterfaceName1, InterfaceName2]
        next_hop: Optional[List[FeatureProfileSdwanServiceLanVpnNextHop]]


    class LanVpnInterfaceContainer:
        ip_static_route_interface: List[VpnIpStaticRouteInterface]


    class VpnOneOfIpRoute5:
        interface_container: LanVpnInterfaceContainer


    class VpnIpv4Route:
        one_of_ip_route: Union[
            LanVpnOneOfIpRoute1,
            LanVpnOneOfIpRoute2,
            OneOfIpRoute3,
            OneOfIpRoute4,
            VpnOneOfIpRoute5,
        ]
        # Prefix
        prefix: Prefix


    class VpnOneOfIpv6NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdwanServiceLanVpnNextHop:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            VpnOneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class ServiceLanVpnNextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[
            List[V1FeatureProfileSdwanServiceLanVpnNextHop]
        ]


    class ServiceLanVpnOneOfIpRoute1:
        next_hop_container: ServiceLanVpnNextHopContainer


    class ServiceLanVpnOneOfIpRoute2:
        null0: Union[
            OneOfIpv4V6RouteNull0OptionsWithoutVariable1,
            OneOfIpv4V6RouteNull0OptionsWithoutVariable2,
        ]


    class LanVpnOneOfIpRoute3:
        nat: Union[
            OneOfIpv6RouteNatOptionsWithoutDefault1,
            OneOfIpv6RouteNatOptionsWithoutDefault2,
        ]


    class LanVpnOneOfIpv6NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class NextHop1:
        address: Union[
            OneOfIpv6NextHopAddressOptionsDef1,
            OneOfIpv6NextHopAddressOptionsDef2,
            OneOfIpv6NextHopAddressOptionsDef3,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            LanVpnOneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class VpnIpv6StaticRouteInterface:
        interface_name: Union[InterfaceName1, InterfaceName2]
        next_hop: Optional[List[NextHop1]]


    class ServiceLanVpnInterfaceContainer:
        ipv6_static_route_interface: List[VpnIpv6StaticRouteInterface]


    class LanVpnOneOfIpRoute4:
        interface_container: ServiceLanVpnInterfaceContainer


    class VpnIpv6Route:
        one_of_ip_route: Union[
            ServiceLanVpnOneOfIpRoute1,
            ServiceLanVpnOneOfIpRoute2,
            LanVpnOneOfIpRoute3,
            LanVpnOneOfIpRoute4,
        ]
        prefix: Union[
            OneOfIpv6RoutePrefixOptionsDef1,
            OneOfIpv6RoutePrefixOptionsDef2,
        ]


    class VpnOneOfServiceTypeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: (
            VpnServiceTypeDef  # pytype: disable=annotation-type-mismatch
        )


    class VpnOneOfListOfIpV4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class VpnService:
        ipv4_addresses: Union[
            OneOfListOfIpV4OptionsDef1, VpnOneOfListOfIpV4OptionsDef2
        ]
        service_type: Union[
            OneOfServiceTypeOptionsDef1, VpnOneOfServiceTypeOptionsDef2
        ]
        tracking: Union[
            OneOfServiceTrackingOptionsDef1,
            OneOfServiceTrackingOptionsDef2,
            OneOfServiceTrackingOptionsDef3,
        ]


    class SdwanServiceLanVpnPrefix:
        """
        Service Route Ip and Subnet Mask
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class VpnOneOfServiceRouteServiceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: (
            VpnServiceRouteDef  # pytype: disable=annotation-type-mismatch
        )


    class VpnOneOfSseInstanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnServiceRoute:
        # Service Route Ip and Subnet Mask
        prefix: SdwanServiceLanVpnPrefix
        service: Union[
            OneOfServiceRouteServiceOptionsDef1,
            VpnOneOfServiceRouteServiceOptionsDef2,
            OneOfServiceRouteServiceOptionsDef3,
        ]
        vpn: OneOfDefaultVpnIdOptionsDef
        sse_instance: Optional[
            Union[
                OneOfSseInstanceOptionsDef1,
                VpnOneOfSseInstanceOptionsDef2,
            ]
        ]


    class FeatureProfileSdwanServiceLanVpnPrefix:
        """
        GRE Route Ip and Subnet Mask
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class VpnOneOfGreRouteInterfaceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class VpnGreRoute:
        interface: Union[
            OneOfGreRouteInterfaceOptionsDef1,
            VpnOneOfGreRouteInterfaceOptionsDef2,
            OneOfGreRouteInterfaceOptionsDef3,
        ]
        # GRE Route Ip and Subnet Mask
        prefix: FeatureProfileSdwanServiceLanVpnPrefix
        vpn: OneOfDefaultVpnIdOptionsDef


    class V1FeatureProfileSdwanServiceLanVpnPrefix:
        """
        IPSEC Route Ip and Subnet Mask
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class VpnOneOfIpsecRouteInterfaceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class VpnIpsecRoute:
        interface: Union[
            OneOfIpsecRouteInterfaceOptionsDef1,
            VpnOneOfIpsecRouteInterfaceOptionsDef2,
            OneOfIpsecRouteInterfaceOptionsDef3,
        ]
        # IPSEC Route Ip and Subnet Mask
        prefix: V1FeatureProfileSdwanServiceLanVpnPrefix


    class VpnOneOfNatPoolNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnOneOfNatPoolPrefixLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnOneOfNatPoolRangeStartOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnOneOfNatPoolRangeEndOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnOneOfNatPoolDirectionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: (
            VpnNatDirectionDef  # pytype: disable=annotation-type-mismatch
        )


    class VpnNatPool:
        direction: Union[
            OneOfNatPoolDirectionOptionsDef1,
            VpnOneOfNatPoolDirectionOptionsDef2,
        ]
        nat_pool_name: Union[
            OneOfNatPoolNameOptionsDef1, VpnOneOfNatPoolNameOptionsDef2
        ]
        overload: Union[
            OneOfNatPoolOverloadOptionsDef1,
            OneOfNatPoolOverloadOptionsDef2,
            OneOfNatPoolOverloadOptionsDef3,
        ]
        prefix_length: Union[
            OneOfNatPoolPrefixLengthOptionsDef1,
            VpnOneOfNatPoolPrefixLengthOptionsDef2,
        ]
        range_end: Union[
            OneOfNatPoolRangeEndOptionsDef1,
            VpnOneOfNatPoolRangeEndOptionsDef2,
        ]
        range_start: Union[
            OneOfNatPoolRangeStartOptionsDef1,
            VpnOneOfNatPoolRangeStartOptionsDef2,
        ]
        # Tracking object for NAT configuration
        tracking_object: Optional[Any]


    class VpnOneOfNatPoolNameInUseOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnOneOfNatPortForwardSourcePortOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnOneOfNatPortForwardTranslatePortOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnOneOfNatPortForwardSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnOneOfNatPortForwardTranslatedSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnOneOfNatPortForwardProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: VpnNatPortForwardProtocolDef  # pytype: disable=annotation-type-mismatch


    class VpnNatPortForward:
        nat_pool_name: Union[
            OneOfNatPoolNameInUseOptionsDef1,
            VpnOneOfNatPoolNameInUseOptionsDef2,
            OneOfNatPoolNameInUseOptionsDef3,
        ]
        protocol: Union[
            OneOfNatPortForwardProtocolOptionsDef1,
            VpnOneOfNatPortForwardProtocolOptionsDef2,
        ]
        source_ip: Union[
            OneOfNatPortForwardSourceIpAddressOptionsDef1,
            VpnOneOfNatPortForwardSourceIpAddressOptionsDef2,
        ]
        source_port: Union[
            OneOfNatPortForwardSourcePortOptionsDef1,
            VpnOneOfNatPortForwardSourcePortOptionsDef2,
        ]
        translate_port: Union[
            OneOfNatPortForwardTranslatePortOptionsDef1,
            VpnOneOfNatPortForwardTranslatePortOptionsDef2,
        ]
        translated_source_ip: Union[
            OneOfNatPortForwardTranslatedSourceIpAddressOptionsDef1,
            VpnOneOfNatPortForwardTranslatedSourceIpAddressOptionsDef2,
        ]


    class LanVpnOneOfNatPoolNameInUseOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnOneOfStaticNatSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnOneOfStaticNatTranslatedSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnOneOfStaticNatDirectionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LanVpnNatDirectionDef  # pytype: disable=annotation-type-mismatch


    class VpnStaticNat:
        nat_pool_name: Optional[
            Union[
                OneOfNatPoolNameInUseOptionsDef1,
                LanVpnOneOfNatPoolNameInUseOptionsDef2,
                OneOfNatPoolNameInUseOptionsDef3,
            ]
        ]
        source_ip: Optional[
            Union[
                OneOfStaticNatSourceIpAddressOptionsDef1,
                VpnOneOfStaticNatSourceIpAddressOptionsDef2,
            ]
        ]
        static_nat_direction: Optional[
            Union[
                OneOfStaticNatDirectionOptionsDef1,
                VpnOneOfStaticNatDirectionOptionsDef2,
            ]
        ]
        # Tracking object for NAT configuration
        tracking_object: Optional[Any]
        translated_source_ip: Optional[
            Union[
                OneOfStaticNatTranslatedSourceIpAddressOptionsDef1,
                VpnOneOfStaticNatTranslatedSourceIpAddressOptionsDef2,
            ]
        ]


    class LanVpnOneOfStaticNatSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class LanVpnOneOfStaticNatTranslatedSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnOneOfStaticNatSubnetPrefixLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnOneOfStaticNatDirectionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: ServiceLanVpnNatDirectionDef  # pytype: disable=annotation-type-mismatch


    class VpnStaticNatSubnet:
        prefix_length: Optional[
            Union[
                OneOfStaticNatSubnetPrefixLengthOptionsDef1,
                VpnOneOfStaticNatSubnetPrefixLengthOptionsDef2,
            ]
        ]
        source_ip_subnet: Optional[
            Union[
                OneOfStaticNatSourceIpAddressOptionsDef1,
                LanVpnOneOfStaticNatSourceIpAddressOptionsDef2,
            ]
        ]
        static_nat_direction: Optional[
            Union[
                OneOfStaticNatDirectionOptionsDef1,
                LanVpnOneOfStaticNatDirectionOptionsDef2,
            ]
        ]
        # Tracking object for NAT configuration
        tracking_object: Optional[Any]
        translated_source_ip_subnet: Optional[
            Union[
                OneOfStaticNatTranslatedSourceIpAddressOptionsDef1,
                LanVpnOneOfStaticNatTranslatedSourceIpAddressOptionsDef2,
            ]
        ]


    class VpnOneOfNat64V4PoolNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnOneOfNat64V4PoolRangeStartOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnOneOfNat64V4PoolRangeEndOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnNat64V4Pool:
        nat64_v4_pool_name: Union[
            OneOfNat64V4PoolNameOptionsDef1,
            VpnOneOfNat64V4PoolNameOptionsDef2,
        ]
        nat64_v4_pool_overload: Union[
            OneOfNat64V4PoolOverloadOptionsDef1,
            OneOfNat64V4PoolOverloadOptionsDef2,
            OneOfNat64V4PoolOverloadOptionsDef3,
        ]
        nat64_v4_pool_range_end: Union[
            OneOfNat64V4PoolRangeEndOptionsDef1,
            VpnOneOfNat64V4PoolRangeEndOptionsDef2,
        ]
        nat64_v4_pool_range_start: Union[
            OneOfNat64V4PoolRangeStartOptionsDef1,
            VpnOneOfNat64V4PoolRangeStartOptionsDef2,
        ]


    class VpnOneOfRouteLeakFromGlobalProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: VpnRouteLeakProtocolFromGlobalDef  # pytype: disable=annotation-type-mismatch


    class VpnOneOfRouteLeakFromGlobalRedistributeProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: VpnRouteLeakRedistributeGlobalProtocolDef  # pytype: disable=annotation-type-mismatch


    class ServiceLanVpnRedistributeToProtocol:
        protocol: Union[
            OneOfRouteLeakFromGlobalRedistributeProtocolOptionsDef1,
            VpnOneOfRouteLeakFromGlobalRedistributeProtocolOptionsDef2,
        ]
        policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class VpnRouteLeakFromGlobal:
        route_protocol: Union[
            OneOfRouteLeakFromGlobalProtocolOptionsDef1,
            VpnOneOfRouteLeakFromGlobalProtocolOptionsDef2,
        ]
        # Redistribute Routes to specific Protocol on Service VPN
        redistribute_to_protocol: Optional[
            List[ServiceLanVpnRedistributeToProtocol]
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class VpnOneOfRouteLeakFromServiceProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: VpnRouteLeakProtocolFromServiceDef  # pytype: disable=annotation-type-mismatch


    class VpnOneOfRouteLeakFromServiceRedistributeProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: VpnRouteLeakRedistributeServiceProtocolDef  # pytype: disable=annotation-type-mismatch


    class SdwanServiceLanVpnRedistributeToProtocol:
        protocol: Union[
            OneOfRouteLeakFromServiceRedistributeProtocolOptionsDef1,
            VpnOneOfRouteLeakFromServiceRedistributeProtocolOptionsDef2,
        ]
        policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class VpnRouteLeakFromService:
        route_protocol: Union[
            OneOfRouteLeakFromServiceProtocolOptionsDef1,
            VpnOneOfRouteLeakFromServiceProtocolOptionsDef2,
        ]
        # Redistribute Routes to specific Protocol on Global VPN
        redistribute_to_protocol: Optional[
            List[SdwanServiceLanVpnRedistributeToProtocol]
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class VpnOneOfRouteImportFromSourceVpnOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnOneOfRouteImportFromProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: VpnRouteImportFromProtocolDef  # pytype: disable=annotation-type-mismatch


    class VpnOneOfRouteImportFromRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: VpnRouteImportFromRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdwanServiceLanVpnRedistributeToProtocol:
        protocol: Union[
            VpnOneOfRouteImportFromRedistributeProtocolOptionsDef1,
            OneOfRouteImportFromRedistributeProtocolOptionsDef2,
        ]
        policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class VpnRouteLeakBetweenServices:
        route_protocol: Union[
            OneOfRouteImportFromProtocolOptionsDef1,
            VpnOneOfRouteImportFromProtocolOptionsDef2,
        ]
        source_vpn: Union[
            OneOfRouteImportFromSourceVpnOptionsDef1,
            VpnOneOfRouteImportFromSourceVpnOptionsDef2,
        ]
        # Redistribute Route to specific Protocol on Current Service VPN
        redistribute_to_protocol: Optional[
            List[FeatureProfileSdwanServiceLanVpnRedistributeToProtocol]
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class VpnMplsVpnRouteTargetOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnMplsVpnRouteTargetsDef:
        rt: Union[
            VpnMplsVpnRouteTargetOptionsDef1,
            MplsVpnRouteTargetOptionsDef2,
        ]


    class LanVpnMplsVpnRouteTargetOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class LanVpnMplsVpnRouteTargetsDef:
        rt: Union[
            LanVpnMplsVpnRouteTargetOptionsDef1,
            MplsVpnRouteTargetOptionsDef2,
        ]


    class VpnMplsVpnIpv4RouteTarget:
        export_rt_list: Optional[List[LanVpnMplsVpnRouteTargetsDef]]
        import_rt_list: Optional[List[VpnMplsVpnRouteTargetsDef]]


    class ServiceLanVpnMplsVpnRouteTargetOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceLanVpnMplsVpnRouteTargetsDef:
        rt: Union[
            ServiceLanVpnMplsVpnRouteTargetOptionsDef1,
            MplsVpnRouteTargetOptionsDef2,
        ]


    class SdwanServiceLanVpnMplsVpnRouteTargetOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanServiceLanVpnMplsVpnRouteTargetsDef:
        rt: Union[
            SdwanServiceLanVpnMplsVpnRouteTargetOptionsDef1,
            MplsVpnRouteTargetOptionsDef2,
        ]


    class VpnMplsVpnIpv6RouteTarget:
        export_rt_list: Optional[
            List[SdwanServiceLanVpnMplsVpnRouteTargetsDef]
        ]
        import_rt_list: Optional[
            List[ServiceLanVpnMplsVpnRouteTargetsDef]
        ]


    class ServiceLanVpnData:
        name: Union[
            OneOfVpnNameOptionsDef1,
            OneOfVpnNameOptionsDef2,
            OneOfVpnNameOptionsDef3,
        ]
        vpn_id: Union[
            OneOfVpnIdOptionsDef1,
            VpnOneOfVpnIdOptionsDef2,
            OneOfVpnIdOptionsDef3,
        ]
        dns_ipv4: Optional[VpnDnsIpv4]
        dns_ipv6: Optional[VpnDnsIpv6]
        enable_sdra: Optional[
            Union[OneOfEnableSdraDef1, OneOfEnableSdraDef2]
        ]
        # IPv4 Static GRE Route
        gre_route: Optional[List[VpnGreRoute]]
        # IPv4 Static IPSEC Route
        ipsec_route: Optional[List[VpnIpsecRoute]]
        # IPv4 Static Route
        ipv4_route: Optional[List[VpnIpv4Route]]
        # IPv6 Static Route
        ipv6_route: Optional[List[VpnIpv6Route]]
        mpls_vpn_ipv4_route_target: Optional[VpnMplsVpnIpv4RouteTarget]
        mpls_vpn_ipv6_route_target: Optional[VpnMplsVpnIpv6RouteTarget]
        # NAT64 V4 Pool
        nat64_v4_pool: Optional[List[VpnNat64V4Pool]]
        # NAT Pool
        nat_pool: Optional[List[VpnNatPool]]
        # NAT Port Forward
        nat_port_forward: Optional[List[VpnNatPortForward]]
        new_host_mapping: Optional[List[NewHostMapping]]
        omp_admin_distance: Optional[
            Union[
                OneOfOmpAdminIpv4OptionsDef1,
                VpnOneOfOmpAdminIpv4OptionsDef2,
                OneOfOmpAdminIpv4OptionsDef3,
            ]
        ]
        omp_admin_distance_ipv6: Optional[
            Union[
                OneOfOmpAdminIpv6OptionsDef1,
                VpnOneOfOmpAdminIpv6OptionsDef2,
                OneOfOmpAdminIpv6OptionsDef3,
            ]
        ]
        # OMP Advertise IPv4
        omp_advertise_ip4: Optional[List[VpnOmpAdvertiseIp4]]
        # OMP Advertise IPv6
        omp_advertise_ipv6: Optional[List[VpnOmpAdvertiseIpv6]]
        # Enable route leak from another Service VPN to current Service VPN
        route_leak_between_services: Optional[
            List[VpnRouteLeakBetweenServices]
        ]
        # Enable route leaking from Global to Service VPN
        route_leak_from_global: Optional[List[VpnRouteLeakFromGlobal]]
        # Enable route leaking from Service to Global VPN
        route_leak_from_service: Optional[List[VpnRouteLeakFromService]]
        # Service
        service: Optional[List[VpnService]]
        # Service
        service_route: Optional[List[VpnServiceRoute]]
        # Static NAT Rules
        static_nat: Optional[List[VpnStaticNat]]
        # Static NAT Subnet Rules
        static_nat_subnet: Optional[List[VpnStaticNatSubnet]]


    class VpnPayload:
        """
        LAN VPN feature schema for PUT request
        """

        data: ServiceLanVpnData
        name: str
        # Set the Feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanServiceLanVpnPayload:
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
        # LAN VPN feature schema for PUT request
        payload: Optional[VpnPayload]


    class EditLanVpnProfileParcelForServicePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class LanVpnOneOfVpnIdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnOneOfOmpAdminIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnOneOfOmpAdminIpv6OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnOneOfPrimaryDnsAddressIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class LanVpnOneOfSecondaryDnsAddressIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class LanVpnDnsIpv4:
        primary_dns_address_ipv4: Optional[
            Union[
                OneOfPrimaryDnsAddressIpv4OptionsDef1,
                LanVpnOneOfPrimaryDnsAddressIpv4OptionsDef2,
                OneOfPrimaryDnsAddressIpv4OptionsDef3,
            ]
        ]
        secondary_dns_address_ipv4: Optional[
            Union[
                OneOfSecondaryDnsAddressIpv4OptionsDef1,
                LanVpnOneOfSecondaryDnsAddressIpv4OptionsDef2,
                OneOfSecondaryDnsAddressIpv4OptionsDef3,
            ]
        ]


    class LanVpnDnsIpv6:
        primary_dns_address_ipv6: Optional[
            Union[
                OneOfPrimaryDnsAddressIpv6OptionsDef1,
                OneOfPrimaryDnsAddressIpv6OptionsDef2,
                OneOfPrimaryDnsAddressIpv6OptionsDef3,
            ]
        ]
        secondary_dns_address_ipv6: Optional[
            Union[
                OneOfSecondaryDnsAddressIpv6OptionsDef1,
                OneOfSecondaryDnsAddressIpv6OptionsDef2,
                OneOfSecondaryDnsAddressIpv6OptionsDef3,
            ]
        ]


    class LanVpnOneOfAdvertiseIpv4ProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LanVpnAdvertiseIpv4ProtocolDef  # pytype: disable=annotation-type-mismatch


    class ServiceLanVpnOneOfRegionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: ServiceLanVpnRegionDef  # pytype: disable=annotation-type-mismatch


    class ServiceLanVpnOneOfRegionOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[Value]


    class SdwanServiceLanVpnPrefixList:
        prefix: Ipv4AddressAndMaskDef
        aggregate_only: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        region: Optional[
            Union[
                OneOfRegionOptionsDef1,
                ServiceLanVpnOneOfRegionOptionsDef2,
                ServiceLanVpnOneOfRegionOptionsDef3,
            ]
        ]


    class LanVpnOmpAdvertiseIp4:
        omp_protocol: Union[
            OneOfAdvertiseIpv4ProtocolOptionsDef1,
            LanVpnOneOfAdvertiseIpv4ProtocolOptionsDef2,
        ]
        # IPv4 Prefix List
        prefix_list: Optional[List[SdwanServiceLanVpnPrefixList]]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class LanVpnOneOfAdvertiseIpv6ProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LanVpnAdvertiseIpv6ProtocolDef  # pytype: disable=annotation-type-mismatch


    class LanVpnOneOfAdvertiseIpv6ProtocolSubTypeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LanVpnProtocolSubTypeDef  # pytype: disable=annotation-type-mismatch


    class SdwanServiceLanVpnOneOfRegionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: SdwanServiceLanVpnRegionDef  # pytype: disable=annotation-type-mismatch


    class SdwanServiceLanVpnOneOfRegionOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[Value]


    class FeatureProfileSdwanServiceLanVpnPrefixList:
        prefix: Union[
            OneOfIpv6PrefixOptionsDef1, OneOfIpv6PrefixOptionsDef2
        ]
        aggregate_only: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        region: Optional[
            Union[
                OneOfRegionOptionsDef1,
                SdwanServiceLanVpnOneOfRegionOptionsDef2,
                SdwanServiceLanVpnOneOfRegionOptionsDef3,
            ]
        ]


    class LanVpnOmpAdvertiseIpv6:
        omp_protocol: Union[
            OneOfAdvertiseIpv6ProtocolOptionsDef1,
            LanVpnOneOfAdvertiseIpv6ProtocolOptionsDef2,
        ]
        # IPv6 Prefix List
        prefix_list: Optional[
            List[FeatureProfileSdwanServiceLanVpnPrefixList]
        ]
        protocol_sub_type: Optional[
            Union[
                OneOfAdvertiseIpv6ProtocolSubTypeOptionsDef1,
                LanVpnOneOfAdvertiseIpv6ProtocolSubTypeOptionsDef2,
                OneOfAdvertiseIpv6ProtocolSubTypeOptionsDef3,
            ]
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class SdwanServiceLanVpnOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class NextHop2:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            SdwanServiceLanVpnOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class FeatureProfileSdwanServiceLanVpnOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnNextHopWithTracker:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            FeatureProfileSdwanServiceLanVpnOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]
        tracker: Union[
            OneOfIpv4NextHopTrackerOptionsDef1,
            OneOfIpv4NextHopTrackerOptionsDef2,
        ]


    class SdwanServiceLanVpnNextHopContainer:
        # IPv4 Route Gateway Next Hop
        next_hop: Optional[List[NextHop2]]
        # IPv4 Route Gateway Next Hop with Tracker
        next_hop_with_tracker: Optional[List[LanVpnNextHopWithTracker]]


    class SdwanServiceLanVpnOneOfIpRoute1:
        next_hop_container: SdwanServiceLanVpnNextHopContainer


    class LanVpnOneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanServiceLanVpnOneOfIpRoute2:
        null0: Union[
            OneOfIpv4V6RouteNull0OptionsWithoutVariable1,
            OneOfIpv4V6RouteNull0OptionsWithoutVariable2,
        ]
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                LanVpnOneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]


    class LanVpnOneOfIpv4NextHopAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class V1FeatureProfileSdwanServiceLanVpnOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class NextHop3:
        address: Union[
            OneOfIpv4NextHopAddressOptionsDef1,
            LanVpnOneOfIpv4NextHopAddressOptionsDef2,
            OneOfIpv4NextHopAddressOptionsDef3,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            V1FeatureProfileSdwanServiceLanVpnOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class LanVpnIpStaticRouteInterface:
        interface_name: Union[InterfaceName1, InterfaceName2]
        next_hop: Optional[List[NextHop3]]


    class SdwanServiceLanVpnInterfaceContainer:
        ip_static_route_interface: List[LanVpnIpStaticRouteInterface]


    class LanVpnOneOfIpRoute5:
        interface_container: SdwanServiceLanVpnInterfaceContainer


    class LanVpnIpv4Route:
        one_of_ip_route: Union[
            SdwanServiceLanVpnOneOfIpRoute1,
            SdwanServiceLanVpnOneOfIpRoute2,
            OneOfIpRoute3,
            OneOfIpRoute4,
            LanVpnOneOfIpRoute5,
        ]
        # Prefix
        prefix: Prefix


    class ServiceLanVpnOneOfIpv6NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class NextHop4:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            ServiceLanVpnOneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class FeatureProfileSdwanServiceLanVpnNextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[List[NextHop4]]


    class FeatureProfileSdwanServiceLanVpnOneOfIpRoute1:
        next_hop_container: (
            FeatureProfileSdwanServiceLanVpnNextHopContainer
        )


    class FeatureProfileSdwanServiceLanVpnOneOfIpRoute2:
        null0: Union[
            OneOfIpv4V6RouteNull0OptionsWithoutVariable1,
            OneOfIpv4V6RouteNull0OptionsWithoutVariable2,
        ]


    class ServiceLanVpnOneOfIpRoute3:
        nat: Union[
            OneOfIpv6RouteNatOptionsWithoutDefault1,
            OneOfIpv6RouteNatOptionsWithoutDefault2,
        ]


    class SdwanServiceLanVpnOneOfIpv6NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class NextHop5:
        address: Union[
            OneOfIpv6NextHopAddressOptionsDef1,
            OneOfIpv6NextHopAddressOptionsDef2,
            OneOfIpv6NextHopAddressOptionsDef3,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            SdwanServiceLanVpnOneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class LanVpnIpv6StaticRouteInterface:
        interface_name: Union[InterfaceName1, InterfaceName2]
        next_hop: Optional[List[NextHop5]]


    class FeatureProfileSdwanServiceLanVpnInterfaceContainer:
        ipv6_static_route_interface: List[LanVpnIpv6StaticRouteInterface]


    class ServiceLanVpnOneOfIpRoute4:
        interface_container: (
            FeatureProfileSdwanServiceLanVpnInterfaceContainer
        )


    class LanVpnIpv6Route:
        one_of_ip_route: Union[
            FeatureProfileSdwanServiceLanVpnOneOfIpRoute1,
            FeatureProfileSdwanServiceLanVpnOneOfIpRoute2,
            ServiceLanVpnOneOfIpRoute3,
            ServiceLanVpnOneOfIpRoute4,
        ]
        prefix: Union[
            OneOfIpv6RoutePrefixOptionsDef1,
            OneOfIpv6RoutePrefixOptionsDef2,
        ]


    class LanVpnOneOfServiceTypeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LanVpnServiceTypeDef  # pytype: disable=annotation-type-mismatch


    class LanVpnOneOfListOfIpV4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class LanVpnService:
        ipv4_addresses: Union[
            OneOfListOfIpV4OptionsDef1, LanVpnOneOfListOfIpV4OptionsDef2
        ]
        service_type: Union[
            OneOfServiceTypeOptionsDef1, LanVpnOneOfServiceTypeOptionsDef2
        ]
        tracking: Union[
            OneOfServiceTrackingOptionsDef1,
            OneOfServiceTrackingOptionsDef2,
            OneOfServiceTrackingOptionsDef3,
        ]


    class Prefix1:
        """
        Service Route Ip and Subnet Mask
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class LanVpnOneOfServiceRouteServiceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LanVpnServiceRouteDef  # pytype: disable=annotation-type-mismatch


    class LanVpnOneOfSseInstanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class LanVpnServiceRoute:
        # Service Route Ip and Subnet Mask
        prefix: Prefix1
        service: Union[
            OneOfServiceRouteServiceOptionsDef1,
            LanVpnOneOfServiceRouteServiceOptionsDef2,
            OneOfServiceRouteServiceOptionsDef3,
        ]
        vpn: OneOfDefaultVpnIdOptionsDef
        sse_instance: Optional[
            Union[
                OneOfSseInstanceOptionsDef1,
                LanVpnOneOfSseInstanceOptionsDef2,
            ]
        ]


    class Prefix2:
        """
        GRE Route Ip and Subnet Mask
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class LanVpnOneOfGreRouteInterfaceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class LanVpnGreRoute:
        interface: Union[
            OneOfGreRouteInterfaceOptionsDef1,
            LanVpnOneOfGreRouteInterfaceOptionsDef2,
            OneOfGreRouteInterfaceOptionsDef3,
        ]
        # GRE Route Ip and Subnet Mask
        prefix: Prefix2
        vpn: OneOfDefaultVpnIdOptionsDef


    class Prefix3:
        """
        IPSEC Route Ip and Subnet Mask
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class LanVpnOneOfIpsecRouteInterfaceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class LanVpnIpsecRoute:
        interface: Union[
            OneOfIpsecRouteInterfaceOptionsDef1,
            LanVpnOneOfIpsecRouteInterfaceOptionsDef2,
            OneOfIpsecRouteInterfaceOptionsDef3,
        ]
        # IPSEC Route Ip and Subnet Mask
        prefix: Prefix3


    class LanVpnOneOfNatPoolNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnOneOfNatPoolPrefixLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnOneOfNatPoolRangeStartOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class LanVpnOneOfNatPoolRangeEndOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class LanVpnOneOfNatPoolDirectionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: SdwanServiceLanVpnNatDirectionDef  # pytype: disable=annotation-type-mismatch


    class LanVpnNatPool:
        direction: Union[
            OneOfNatPoolDirectionOptionsDef1,
            LanVpnOneOfNatPoolDirectionOptionsDef2,
        ]
        nat_pool_name: Union[
            OneOfNatPoolNameOptionsDef1, LanVpnOneOfNatPoolNameOptionsDef2
        ]
        overload: Union[
            OneOfNatPoolOverloadOptionsDef1,
            OneOfNatPoolOverloadOptionsDef2,
            OneOfNatPoolOverloadOptionsDef3,
        ]
        prefix_length: Union[
            OneOfNatPoolPrefixLengthOptionsDef1,
            LanVpnOneOfNatPoolPrefixLengthOptionsDef2,
        ]
        range_end: Union[
            OneOfNatPoolRangeEndOptionsDef1,
            LanVpnOneOfNatPoolRangeEndOptionsDef2,
        ]
        range_start: Union[
            OneOfNatPoolRangeStartOptionsDef1,
            LanVpnOneOfNatPoolRangeStartOptionsDef2,
        ]
        # Tracking object for NAT configuration
        tracking_object: Optional[Any]


    class ServiceLanVpnOneOfNatPoolNameInUseOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnOneOfNatPortForwardSourcePortOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnOneOfNatPortForwardTranslatePortOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnOneOfNatPortForwardSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class LanVpnOneOfNatPortForwardTranslatedSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class LanVpnOneOfNatPortForwardProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LanVpnNatPortForwardProtocolDef  # pytype: disable=annotation-type-mismatch


    class LanVpnNatPortForward:
        nat_pool_name: Union[
            OneOfNatPoolNameInUseOptionsDef1,
            ServiceLanVpnOneOfNatPoolNameInUseOptionsDef2,
            OneOfNatPoolNameInUseOptionsDef3,
        ]
        protocol: Union[
            OneOfNatPortForwardProtocolOptionsDef1,
            LanVpnOneOfNatPortForwardProtocolOptionsDef2,
        ]
        source_ip: Union[
            OneOfNatPortForwardSourceIpAddressOptionsDef1,
            LanVpnOneOfNatPortForwardSourceIpAddressOptionsDef2,
        ]
        source_port: Union[
            OneOfNatPortForwardSourcePortOptionsDef1,
            LanVpnOneOfNatPortForwardSourcePortOptionsDef2,
        ]
        translate_port: Union[
            OneOfNatPortForwardTranslatePortOptionsDef1,
            LanVpnOneOfNatPortForwardTranslatePortOptionsDef2,
        ]
        translated_source_ip: Union[
            OneOfNatPortForwardTranslatedSourceIpAddressOptionsDef1,
            LanVpnOneOfNatPortForwardTranslatedSourceIpAddressOptionsDef2,
        ]


    class SdwanServiceLanVpnOneOfNatPoolNameInUseOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class ServiceLanVpnOneOfStaticNatSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceLanVpnOneOfStaticNatTranslatedSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceLanVpnOneOfStaticNatDirectionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanServiceLanVpnNatDirectionDef  # pytype: disable=annotation-type-mismatch


    class LanVpnStaticNat:
        nat_pool_name: Optional[
            Union[
                OneOfNatPoolNameInUseOptionsDef1,
                SdwanServiceLanVpnOneOfNatPoolNameInUseOptionsDef2,
                OneOfNatPoolNameInUseOptionsDef3,
            ]
        ]
        source_ip: Optional[
            Union[
                OneOfStaticNatSourceIpAddressOptionsDef1,
                ServiceLanVpnOneOfStaticNatSourceIpAddressOptionsDef2,
            ]
        ]
        static_nat_direction: Optional[
            Union[
                OneOfStaticNatDirectionOptionsDef1,
                ServiceLanVpnOneOfStaticNatDirectionOptionsDef2,
            ]
        ]
        # Tracking object for NAT configuration
        tracking_object: Optional[Any]
        translated_source_ip: Optional[
            Union[
                OneOfStaticNatTranslatedSourceIpAddressOptionsDef1,
                ServiceLanVpnOneOfStaticNatTranslatedSourceIpAddressOptionsDef2,
            ]
        ]


    class SdwanServiceLanVpnOneOfStaticNatSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanServiceLanVpnOneOfStaticNatTranslatedSourceIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class LanVpnOneOfStaticNatSubnetPrefixLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanServiceLanVpnOneOfStaticNatDirectionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: V1FeatureProfileSdwanServiceLanVpnNatDirectionDef  # pytype: disable=annotation-type-mismatch


    class LanVpnStaticNatSubnet:
        prefix_length: Optional[
            Union[
                OneOfStaticNatSubnetPrefixLengthOptionsDef1,
                LanVpnOneOfStaticNatSubnetPrefixLengthOptionsDef2,
            ]
        ]
        source_ip_subnet: Optional[
            Union[
                OneOfStaticNatSourceIpAddressOptionsDef1,
                SdwanServiceLanVpnOneOfStaticNatSourceIpAddressOptionsDef2,
            ]
        ]
        static_nat_direction: Optional[
            Union[
                OneOfStaticNatDirectionOptionsDef1,
                SdwanServiceLanVpnOneOfStaticNatDirectionOptionsDef2,
            ]
        ]
        # Tracking object for NAT configuration
        tracking_object: Optional[Any]
        translated_source_ip_subnet: Optional[
            Union[
                OneOfStaticNatTranslatedSourceIpAddressOptionsDef1,
                SdwanServiceLanVpnOneOfStaticNatTranslatedSourceIpAddressOptionsDef2,
            ]
        ]


    class LanVpnOneOfNat64V4PoolNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class LanVpnOneOfNat64V4PoolRangeStartOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class LanVpnOneOfNat64V4PoolRangeEndOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class LanVpnNat64V4Pool:
        nat64_v4_pool_name: Union[
            OneOfNat64V4PoolNameOptionsDef1,
            LanVpnOneOfNat64V4PoolNameOptionsDef2,
        ]
        nat64_v4_pool_overload: Union[
            OneOfNat64V4PoolOverloadOptionsDef1,
            OneOfNat64V4PoolOverloadOptionsDef2,
            OneOfNat64V4PoolOverloadOptionsDef3,
        ]
        nat64_v4_pool_range_end: Union[
            OneOfNat64V4PoolRangeEndOptionsDef1,
            LanVpnOneOfNat64V4PoolRangeEndOptionsDef2,
        ]
        nat64_v4_pool_range_start: Union[
            OneOfNat64V4PoolRangeStartOptionsDef1,
            LanVpnOneOfNat64V4PoolRangeStartOptionsDef2,
        ]


    class LanVpnOneOfRouteLeakFromGlobalProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LanVpnRouteLeakProtocolFromGlobalDef  # pytype: disable=annotation-type-mismatch


    class LanVpnOneOfRouteLeakFromGlobalRedistributeProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LanVpnRouteLeakRedistributeGlobalProtocolDef  # pytype: disable=annotation-type-mismatch


    class V1FeatureProfileSdwanServiceLanVpnRedistributeToProtocol:
        protocol: Union[
            OneOfRouteLeakFromGlobalRedistributeProtocolOptionsDef1,
            LanVpnOneOfRouteLeakFromGlobalRedistributeProtocolOptionsDef2,
        ]
        policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class LanVpnRouteLeakFromGlobal:
        route_protocol: Union[
            OneOfRouteLeakFromGlobalProtocolOptionsDef1,
            LanVpnOneOfRouteLeakFromGlobalProtocolOptionsDef2,
        ]
        # Redistribute Routes to specific Protocol on Service VPN
        redistribute_to_protocol: Optional[
            List[V1FeatureProfileSdwanServiceLanVpnRedistributeToProtocol]
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class LanVpnOneOfRouteLeakFromServiceProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LanVpnRouteLeakProtocolFromServiceDef  # pytype: disable=annotation-type-mismatch


    class LanVpnOneOfRouteLeakFromServiceRedistributeProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LanVpnRouteLeakRedistributeServiceProtocolDef  # pytype: disable=annotation-type-mismatch


    class RedistributeToProtocol1:
        protocol: Union[
            OneOfRouteLeakFromServiceRedistributeProtocolOptionsDef1,
            LanVpnOneOfRouteLeakFromServiceRedistributeProtocolOptionsDef2,
        ]
        policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class LanVpnRouteLeakFromService:
        route_protocol: Union[
            OneOfRouteLeakFromServiceProtocolOptionsDef1,
            LanVpnOneOfRouteLeakFromServiceProtocolOptionsDef2,
        ]
        # Redistribute Routes to specific Protocol on Global VPN
        redistribute_to_protocol: Optional[List[RedistributeToProtocol1]]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class LanVpnOneOfRouteImportFromSourceVpnOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnOneOfRouteImportFromProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LanVpnRouteImportFromProtocolDef  # pytype: disable=annotation-type-mismatch


    class LanVpnOneOfRouteImportFromRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: LanVpnRouteImportFromRedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class RedistributeToProtocol2:
        protocol: Union[
            LanVpnOneOfRouteImportFromRedistributeProtocolOptionsDef1,
            OneOfRouteImportFromRedistributeProtocolOptionsDef2,
        ]
        policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class LanVpnRouteLeakBetweenServices:
        route_protocol: Union[
            OneOfRouteImportFromProtocolOptionsDef1,
            LanVpnOneOfRouteImportFromProtocolOptionsDef2,
        ]
        source_vpn: Union[
            OneOfRouteImportFromSourceVpnOptionsDef1,
            LanVpnOneOfRouteImportFromSourceVpnOptionsDef2,
        ]
        # Redistribute Route to specific Protocol on Current Service VPN
        redistribute_to_protocol: Optional[List[RedistributeToProtocol2]]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class FeatureProfileSdwanServiceLanVpnMplsVpnRouteTargetOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanServiceLanVpnMplsVpnRouteTargetsDef:
        rt: Union[
            FeatureProfileSdwanServiceLanVpnMplsVpnRouteTargetOptionsDef1,
            MplsVpnRouteTargetOptionsDef2,
        ]


    class V1FeatureProfileSdwanServiceLanVpnMplsVpnRouteTargetOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class V1FeatureProfileSdwanServiceLanVpnMplsVpnRouteTargetsDef:
        rt: Union[
            V1FeatureProfileSdwanServiceLanVpnMplsVpnRouteTargetOptionsDef1,
            MplsVpnRouteTargetOptionsDef2,
        ]


    class LanVpnMplsVpnIpv4RouteTarget:
        export_rt_list: Optional[
            List[V1FeatureProfileSdwanServiceLanVpnMplsVpnRouteTargetsDef]
        ]
        import_rt_list: Optional[
            List[FeatureProfileSdwanServiceLanVpnMplsVpnRouteTargetsDef]
        ]


    class MplsVpnRouteTargetOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: str


    class MplsVpnRouteTargetsDef1:
        rt: Union[
            MplsVpnRouteTargetOptionsDef11, MplsVpnRouteTargetOptionsDef2
        ]


    class MplsVpnRouteTargetOptionsDef12:
        option_type: GlobalOptionTypeDef
        value: str


    class MplsVpnRouteTargetsDef2:
        rt: Union[
            MplsVpnRouteTargetOptionsDef12, MplsVpnRouteTargetOptionsDef2
        ]


    class LanVpnMplsVpnIpv6RouteTarget:
        export_rt_list: Optional[List[MplsVpnRouteTargetsDef2]]
        import_rt_list: Optional[List[MplsVpnRouteTargetsDef1]]


    class SdwanServiceLanVpnData:
        name: Union[
            OneOfVpnNameOptionsDef1,
            OneOfVpnNameOptionsDef2,
            OneOfVpnNameOptionsDef3,
        ]
        vpn_id: Union[
            OneOfVpnIdOptionsDef1,
            LanVpnOneOfVpnIdOptionsDef2,
            OneOfVpnIdOptionsDef3,
        ]
        dns_ipv4: Optional[LanVpnDnsIpv4]
        dns_ipv6: Optional[LanVpnDnsIpv6]
        enable_sdra: Optional[
            Union[OneOfEnableSdraDef1, OneOfEnableSdraDef2]
        ]
        # IPv4 Static GRE Route
        gre_route: Optional[List[LanVpnGreRoute]]
        # IPv4 Static IPSEC Route
        ipsec_route: Optional[List[LanVpnIpsecRoute]]
        # IPv4 Static Route
        ipv4_route: Optional[List[LanVpnIpv4Route]]
        # IPv6 Static Route
        ipv6_route: Optional[List[LanVpnIpv6Route]]
        mpls_vpn_ipv4_route_target: Optional[LanVpnMplsVpnIpv4RouteTarget]
        mpls_vpn_ipv6_route_target: Optional[LanVpnMplsVpnIpv6RouteTarget]
        # NAT64 V4 Pool
        nat64_v4_pool: Optional[List[LanVpnNat64V4Pool]]
        # NAT Pool
        nat_pool: Optional[List[LanVpnNatPool]]
        # NAT Port Forward
        nat_port_forward: Optional[List[LanVpnNatPortForward]]
        new_host_mapping: Optional[List[NewHostMapping]]
        omp_admin_distance: Optional[
            Union[
                OneOfOmpAdminIpv4OptionsDef1,
                LanVpnOneOfOmpAdminIpv4OptionsDef2,
                OneOfOmpAdminIpv4OptionsDef3,
            ]
        ]
        omp_admin_distance_ipv6: Optional[
            Union[
                OneOfOmpAdminIpv6OptionsDef1,
                LanVpnOneOfOmpAdminIpv6OptionsDef2,
                OneOfOmpAdminIpv6OptionsDef3,
            ]
        ]
        # OMP Advertise IPv4
        omp_advertise_ip4: Optional[List[LanVpnOmpAdvertiseIp4]]
        # OMP Advertise IPv6
        omp_advertise_ipv6: Optional[List[LanVpnOmpAdvertiseIpv6]]
        # Enable route leak from another Service VPN to current Service VPN
        route_leak_between_services: Optional[
            List[LanVpnRouteLeakBetweenServices]
        ]
        # Enable route leaking from Global to Service VPN
        route_leak_from_global: Optional[List[LanVpnRouteLeakFromGlobal]]
        # Enable route leaking from Service to Global VPN
        route_leak_from_service: Optional[
            List[LanVpnRouteLeakFromService]
        ]
        # Service
        service: Optional[List[LanVpnService]]
        # Service
        service_route: Optional[List[LanVpnServiceRoute]]
        # Static NAT Rules
        static_nat: Optional[List[LanVpnStaticNat]]
        # Static NAT Subnet Rules
        static_nat_subnet: Optional[List[LanVpnStaticNatSubnet]]


    class EditLanVpnProfileParcelForServicePutRequest:
        """
        LAN VPN feature schema for PUT request
        """

        data: SdwanServiceLanVpnData
        name: str
        # Set the Feature description
        description: Optional[str]
        metadata: Optional[Any]


