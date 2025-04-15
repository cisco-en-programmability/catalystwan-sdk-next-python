======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

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

    StaticNatDirectionDef = Literal["inside", "outside"]

    NatPortForwardProtocolDef = Literal["TCP", "UDP"]

    SourceTypeDef = Literal["acl", "route-map"]

    NatTypeDef = Literal["interface", "pool"]

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


    class OneOfVrfOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVrfOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class MplsVpnRouteTargetOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class MplsVpnRouteTargetOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class MplsVpnRouteTargetOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfVpnNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVpnNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVpnNameOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfIpAddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpAddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class Dns:
        ip_address: Union[
            OneOfIpAddressOptionsDef1, OneOfIpAddressOptionsDef2
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


    class HostMapping:
        host_name: Union[
            OneOfHostNameOptionsWithoutDefault1,
            OneOfHostNameOptionsWithoutDefault2,
        ]
        list_of_ip: Union[
            OneOfListOfIpOptionsWithoutDefault1,
            OneOfListOfIpOptionsWithoutDefault2,
        ]


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


    class OneOfIpV4AddressOptionsWithoutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: Any


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


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRefIdOptionsDef1:
        ref_id: RefId


    class OneOfRefIdOptionsDef2:
        option_type: DefaultOptionTypeDef


    class NextHop:
        address: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            OneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]
        tracker_id: Union[OneOfRefIdOptionsDef1, OneOfRefIdOptionsDef2]


    class NextHopContainer:
        # IPv4 Route Gateway Next Hop
        next_hop: List[NextHop]


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
        distance: Optional[
            Union[
                OneOfIpv4NextHopDistanceOptionsDef1,
                OneOfIpv4NextHopDistanceOptionsDef2,
                OneOfIpv4NextHopDistanceOptionsDef3,
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
        distance: Optional[
            Union[
                OneOfIpv4NextHopDistanceOptionsDef1,
                OneOfIpv4NextHopDistanceOptionsDef2,
                OneOfIpv4NextHopDistanceOptionsDef3,
            ]
        ]


    class OneOfVrfInterfaceNameOptionsNoDefaultDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVrfInterfaceNameOptionsNoDefaultDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class VrfNextHop:
        address: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            OneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class IpStaticRouteInterface:
        interface_name: Union[
            OneOfVrfInterfaceNameOptionsNoDefaultDef1,
            OneOfVrfInterfaceNameOptionsNoDefaultDef2,
        ]
        next_hop: List[VrfNextHop]


    class InterfaceContainer:
        ip_static_route_interface: List[IpStaticRouteInterface]


    class OneOfIpRoute4:
        interface_container: InterfaceContainer


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


    class TransportVrfNextHop:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            OneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class VrfNextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[List[TransportVrfNextHop]]


    class VrfOneOfIpRoute1:
        next_hop_container: VrfNextHopContainer


    class VrfOneOfIpRoute2:
        null0: Union[
            OneOfIpv4V6RouteNull0OptionsWithoutVariable1,
            OneOfIpv4V6RouteNull0OptionsWithoutVariable2,
        ]


    class SdRoutingTransportVrfNextHop:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            OneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class Ipv6StaticRouteInterface:
        interface_name: Union[
            OneOfVrfInterfaceNameOptionsNoDefaultDef1,
            OneOfVrfInterfaceNameOptionsNoDefaultDef2,
        ]
        next_hop: Optional[List[SdRoutingTransportVrfNextHop]]


    class VrfInterfaceContainer:
        ipv6_static_route_interface: List[Ipv6StaticRouteInterface]


    class VrfOneOfIpRoute3:
        interface_container: VrfInterfaceContainer


    class Ipv6Route:
        one_of_ip_route: Union[
            VrfOneOfIpRoute1, VrfOneOfIpRoute2, VrfOneOfIpRoute3
        ]
        prefix: Union[
            OneOfIpv6RoutePrefixOptionsDef1,
            OneOfIpv6RoutePrefixOptionsDef2,
        ]


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfDirectionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: StaticNatDirectionDef


    class NatInterfaces:
        direction: OneOfDirectionOptionsDef
        interface: Union[
            OneOfVrfInterfaceNameOptionsNoDefaultDef1,
            OneOfVrfInterfaceNameOptionsNoDefaultDef2,
        ]


    class StaticNat:
        direction: OneOfDirectionOptionsDef
        source_ip: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        translate_ip: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        route_map_id: Optional[
            Union[OneOfRefIdOptionsDef1, OneOfRefIdOptionsDef2]
        ]
        tracker_id: Optional[
            Union[OneOfRefIdOptionsDef1, OneOfRefIdOptionsDef2]
        ]


    class OneOfPrefixLengthOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPrefixLengthOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class StaticNatSubnet:
        direction: OneOfDirectionOptionsDef
        prefix_length: Union[
            OneOfPrefixLengthOptionsDef1, OneOfPrefixLengthOptionsDef2
        ]
        source_ip_subnet: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        translate_ip_subnet: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        tracker_id: Optional[
            Union[OneOfRefIdOptionsDef1, OneOfRefIdOptionsDef2]
        ]


    class OneOfNatPortForwardProtocolOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatPortForwardProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: NatPortForwardProtocolDef  # pytype: disable=annotation-type-mismatch


    class OneOfPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfPortOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class NatPortForward:
        protocol: Union[
            OneOfNatPortForwardProtocolOptionsDef1,
            OneOfNatPortForwardProtocolOptionsDef2,
        ]
        source_ip: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        source_port: Union[OneOfPortOptionsDef1, OneOfPortOptionsDef2]
        translate_port: Union[OneOfPortOptionsDef1, OneOfPortOptionsDef2]
        translated_source_ip: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]


    class NatType:
        value: Optional[Any]


    class OneOfSourceTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SourceTypeDef


    class ParcelReferenceDef:
        ref_id: RefId


    class OneOfPoolNameOptionsNoDefaultDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfPoolNameOptionsNoDefaultDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPrefixLengthWithoutDefaultOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPrefixLengthWithoutDefaultOptionsDef2:
        option_type: GlobalOptionTypeDef
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
        value: bool


    class NatPool:
        """
        NAT Pool
        """

        pool_name: Union[
            OneOfPoolNameOptionsNoDefaultDef1,
            OneOfPoolNameOptionsNoDefaultDef2,
        ]
        prefix_length: Union[
            OneOfPrefixLengthWithoutDefaultOptionsDef1,
            OneOfPrefixLengthWithoutDefaultOptionsDef2,
        ]
        range_end: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        range_start: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        match_in_vrf: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        overload: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        tracker_id: Optional[
            Union[OneOfRefIdOptionsDef1, OneOfRefIdOptionsDef2]
        ]


    class DynamicNat1:
        direction: OneOfDirectionOptionsDef
        egress_interface: Union[
            OneOfVrfInterfaceNameOptionsNoDefaultDef1,
            OneOfVrfInterfaceNameOptionsNoDefaultDef2,
        ]
        nat_type: NatType
        source_type: OneOfSourceTypeOptionsDef
        ipv4_acl_id: Optional[ParcelReferenceDef]
        # NAT Pool
        nat_pool: Optional[NatPool]
        route_map_id: Optional[ParcelReferenceDef]


    class OneOfNatTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: NatTypeDef


    class DynamicNat2:
        direction: OneOfDirectionOptionsDef
        nat_type: OneOfNatTypeOptionsDef
        source_type: OneOfSourceTypeOptionsDef
        egress_interface: Optional[
            Union[
                OneOfVrfInterfaceNameOptionsNoDefaultDef1,
                OneOfVrfInterfaceNameOptionsNoDefaultDef2,
            ]
        ]
        ipv4_acl_id: Optional[ParcelReferenceDef]
        # NAT Pool
        nat_pool: Optional[NatPool]
        route_map_id: Optional[ParcelReferenceDef]


    class NatAttributesIpv4:
        """
        NAT Attributes Ipv4
        """

        nat_enable: Union[
            OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
            OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
        ]
        # NAT Attributes Ipv4
        dynamic_nat: Optional[List[Union[DynamicNat1, DynamicNat2]]]
        # nat interfaces
        nat_interfaces: Optional[List[NatInterfaces]]
        # NAT Port Forward
        nat_port_forward: Optional[List[NatPortForward]]
        # static NAT
        static_nat: Optional[List[StaticNat]]
        # static NAT Subnet
        static_nat_subnet: Optional[List[StaticNatSubnet]]


    class OneOfRouteLeakFromGlobalProtocolOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRouteLeakFromGlobalProtocolOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: RouteLeakProtocolFromGlobalDef  # pytype: disable=annotation-type-mismatch


    class OneOfRoutePolicyNameOptionsDef1:
        option_type: DefaultOptionTypeDef


    class OneOfRoutePolicyNameOptionsDef2:
        ref_id: RefId


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
        # Redistribute Routes to specific Protocol on Service VRF
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


    class VrfRedistributeToProtocol:
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
        # Redistribute Routes to specific Protocol on Global VRF
        redistribute_to_protocol: Optional[
            List[VrfRedistributeToProtocol]
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


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


    class TransportVrfRedistributeToProtocol:
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
        source_vpn: Union[OneOfVrfOptionsDef1, OneOfVrfOptionsDef2]
        # Redistribute Route to specific Protocol on Current Service VRF
        redistribute_to_protocol: Optional[
            List[TransportVrfRedistributeToProtocol]
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class VrfData:
        vrf_name: Union[OneOfVrfOptionsDef1, OneOfVrfOptionsDef2]
        description: Optional[
            Union[
                OneOfVpnNameOptionsDef1,
                OneOfVpnNameOptionsDef2,
                OneOfVpnNameOptionsDef3,
            ]
        ]
        dns: Optional[List[Dns]]
        host_mapping: Optional[List[HostMapping]]
        # IPv4 Static Route
        ipv4_route: Optional[List[Ipv4Route]]
        # IPv6 Static Route
        ipv6_route: Optional[List[Ipv6Route]]
        # NAT Attributes Ipv4
        nat_attributes_ipv4: Optional[NatAttributesIpv4]
        rd: Optional[
            Union[
                MplsVpnRouteTargetOptionsDef1,
                MplsVpnRouteTargetOptionsDef2,
                MplsVpnRouteTargetOptionsDef3,
            ]
        ]
        # Enable route leak from another Service VRF to current Service VRF
        route_leak_between_services: Optional[
            List[RouteLeakBetweenServices]
        ]
        # Enable route leaking from Global to Service VRF
        route_leak_from_global: Optional[List[RouteLeakFromGlobal]]
        # Enable route leaking from Service to Global VRF
        route_leak_from_service: Optional[List[RouteLeakFromService]]


    class Payload:
        """
        SD-Routing VRF feature schema
        """

        data: VrfData
        name: str
        # Set the feature description
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
        # SD-Routing VRF feature schema
        payload: Optional[Payload]


    class GetListSdRoutingTransportVrfPayload:
        data: Optional[List[Data]]


    class CreateSdroutingTransportVrfFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class TransportVrfData:
        vrf_name: Union[OneOfVrfOptionsDef1, OneOfVrfOptionsDef2]
        description: Optional[
            Union[
                OneOfVpnNameOptionsDef1,
                OneOfVpnNameOptionsDef2,
                OneOfVpnNameOptionsDef3,
            ]
        ]
        dns: Optional[List[Dns]]
        host_mapping: Optional[List[HostMapping]]
        # IPv4 Static Route
        ipv4_route: Optional[List[Ipv4Route]]
        # IPv6 Static Route
        ipv6_route: Optional[List[Ipv6Route]]
        # NAT Attributes Ipv4
        nat_attributes_ipv4: Optional[NatAttributesIpv4]
        rd: Optional[
            Union[
                MplsVpnRouteTargetOptionsDef1,
                MplsVpnRouteTargetOptionsDef2,
                MplsVpnRouteTargetOptionsDef3,
            ]
        ]
        # Enable route leak from another Service VRF to current Service VRF
        route_leak_between_services: Optional[
            List[RouteLeakBetweenServices]
        ]
        # Enable route leaking from Global to Service VRF
        route_leak_from_global: Optional[List[RouteLeakFromGlobal]]
        # Enable route leaking from Service to Global VRF
        route_leak_from_service: Optional[List[RouteLeakFromService]]


    class CreateSdroutingTransportVrfFeaturePostRequest:
        """
        SD-Routing VRF feature schema
        """

        data: TransportVrfData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingTransportVrfPayload:
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
        # SD-Routing VRF feature schema
        payload: Optional[Payload]


    class EditSdroutingTransportVrfFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingTransportVrfData:
        vrf_name: Union[OneOfVrfOptionsDef1, OneOfVrfOptionsDef2]
        description: Optional[
            Union[
                OneOfVpnNameOptionsDef1,
                OneOfVpnNameOptionsDef2,
                OneOfVpnNameOptionsDef3,
            ]
        ]
        dns: Optional[List[Dns]]
        host_mapping: Optional[List[HostMapping]]
        # IPv4 Static Route
        ipv4_route: Optional[List[Ipv4Route]]
        # IPv6 Static Route
        ipv6_route: Optional[List[Ipv6Route]]
        # NAT Attributes Ipv4
        nat_attributes_ipv4: Optional[NatAttributesIpv4]
        rd: Optional[
            Union[
                MplsVpnRouteTargetOptionsDef1,
                MplsVpnRouteTargetOptionsDef2,
                MplsVpnRouteTargetOptionsDef3,
            ]
        ]
        # Enable route leak from another Service VRF to current Service VRF
        route_leak_between_services: Optional[
            List[RouteLeakBetweenServices]
        ]
        # Enable route leaking from Global to Service VRF
        route_leak_from_global: Optional[List[RouteLeakFromGlobal]]
        # Enable route leaking from Service to Global VRF
        route_leak_from_service: Optional[List[RouteLeakFromService]]


    class EditSdroutingTransportVrfFeaturePutRequest:
        """
        SD-Routing VRF feature schema
        """

        data: SdRoutingTransportVrfData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


