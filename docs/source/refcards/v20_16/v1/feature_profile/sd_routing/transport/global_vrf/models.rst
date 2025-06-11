======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

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

    StaticNatDirectionDef = Literal["inside", "outside"]

    NatPortForwardProtocolDef = Literal["TCP", "UDP"]

    SourceTypeDef = Literal["acl", "route-map"]

    NatTypeDef = Literal["interface", "pool"]


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
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


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
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


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


    class GlobalVrfNextHop:
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
        distance: Optional[
            Union[
                OneOfIpv4NextHopDistanceOptionsDef1,
                OneOfIpv4NextHopDistanceOptionsDef2,
                OneOfIpv4NextHopDistanceOptionsDef3,
            ]
        ]
        next_hop: Optional[List[GlobalVrfNextHop]]


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


    class TransportGlobalVrfNextHop:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            OneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class GlobalVrfNextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[List[TransportGlobalVrfNextHop]]


    class GlobalVrfOneOfIpRoute1:
        next_hop_container: GlobalVrfNextHopContainer


    class GlobalVrfOneOfIpRoute2:
        null0: Union[
            OneOfIpv4V6RouteNull0OptionsWithoutVariable1,
            OneOfIpv4V6RouteNull0OptionsWithoutVariable2,
        ]


    class SdRoutingTransportGlobalVrfNextHop:
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
        distance: Optional[
            Union[
                OneOfIpv6NextHopDistanceOptionsDef1,
                OneOfIpv6NextHopDistanceOptionsDef2,
                OneOfIpv6NextHopDistanceOptionsDef3,
            ]
        ]
        next_hop: Optional[List[SdRoutingTransportGlobalVrfNextHop]]


    class GlobalVrfInterfaceContainer:
        ipv6_static_route_interface: List[Ipv6StaticRouteInterface]


    class GlobalVrfOneOfIpRoute3:
        interface_container: GlobalVrfInterfaceContainer


    class Ipv6Route:
        one_of_ip_route: Union[
            GlobalVrfOneOfIpRoute1,
            GlobalVrfOneOfIpRoute2,
            GlobalVrfOneOfIpRoute3,
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
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


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
        overload: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
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


    class GlobalVrfData:
        enhance_ecmp_keying: Union[
            OneOfOnBooleanDefaultFalseOptionsDef1,
            OneOfOnBooleanDefaultFalseOptionsDef2,
            OneOfOnBooleanDefaultFalseOptionsDef3,
        ]
        dns: Optional[List[Dns]]
        host_mapping: Optional[List[HostMapping]]
        # IPv4 Static Route
        ipv4_route: Optional[List[Ipv4Route]]
        # IPv6 Static Route
        ipv6_route: Optional[List[Ipv6Route]]
        # NAT Attributes Ipv4
        nat_attributes_ipv4: Optional[NatAttributesIpv4]


    class Payload:
        """
        SD-Routing Global VRF feature schema
        """

        data: GlobalVrfData
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
        # SD-Routing Global VRF feature schema
        payload: Optional[Payload]


    class GetListSdRoutingTransportGlobalVrfPayload:
        data: Optional[List[Data]]


    class CreateSdroutingTransportGlobalVrfFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class TransportGlobalVrfData:
        enhance_ecmp_keying: Union[
            OneOfOnBooleanDefaultFalseOptionsDef1,
            OneOfOnBooleanDefaultFalseOptionsDef2,
            OneOfOnBooleanDefaultFalseOptionsDef3,
        ]
        dns: Optional[List[Dns]]
        host_mapping: Optional[List[HostMapping]]
        # IPv4 Static Route
        ipv4_route: Optional[List[Ipv4Route]]
        # IPv6 Static Route
        ipv6_route: Optional[List[Ipv6Route]]
        # NAT Attributes Ipv4
        nat_attributes_ipv4: Optional[NatAttributesIpv4]


    class CreateSdroutingTransportGlobalVrfFeaturePostRequest:
        """
        SD-Routing Global VRF feature schema
        """

        data: TransportGlobalVrfData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingTransportGlobalVrfPayload:
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
        # SD-Routing Global VRF feature schema
        payload: Optional[Payload]


    class EditSdroutingTransportGlobalVrfFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingTransportGlobalVrfData:
        enhance_ecmp_keying: Union[
            OneOfOnBooleanDefaultFalseOptionsDef1,
            OneOfOnBooleanDefaultFalseOptionsDef2,
            OneOfOnBooleanDefaultFalseOptionsDef3,
        ]
        dns: Optional[List[Dns]]
        host_mapping: Optional[List[HostMapping]]
        # IPv4 Static Route
        ipv4_route: Optional[List[Ipv4Route]]
        # IPv6 Static Route
        ipv6_route: Optional[List[Ipv6Route]]
        # NAT Attributes Ipv4
        nat_attributes_ipv4: Optional[NatAttributesIpv4]


    class EditSdroutingTransportGlobalVrfFeaturePutRequest:
        """
        SD-Routing Global VRF feature schema
        """

        data: SdRoutingTransportGlobalVrfData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


