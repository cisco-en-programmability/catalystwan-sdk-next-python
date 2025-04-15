======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    DefaultOptionTypeDef = Literal["default"]

    ManagementVrfDef = Literal["Mgmt-intf"]

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

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


    class OneOfVrfNameOptionsDef:
        option_type: DefaultOptionTypeDef
        value: (
            ManagementVrfDef  # pytype: disable=annotation-type-mismatch
        )


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
        next_hop: Optional[List[NextHop]]


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


    class ManagementVrfNextHop:
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
        next_hop: Optional[List[ManagementVrfNextHop]]


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


    class TransportManagementVrfNextHop:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            OneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class ManagementVrfNextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[List[TransportManagementVrfNextHop]]


    class ManagementVrfOneOfIpRoute1:
        next_hop_container: ManagementVrfNextHopContainer


    class ManagementVrfOneOfIpRoute2:
        null0: Union[
            OneOfIpv4V6RouteNull0OptionsWithoutVariable1,
            OneOfIpv4V6RouteNull0OptionsWithoutVariable2,
        ]


    class SdRoutingTransportManagementVrfNextHop:
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
        next_hop: Optional[List[SdRoutingTransportManagementVrfNextHop]]


    class ManagementVrfInterfaceContainer:
        ipv6_static_route_interface: List[Ipv6StaticRouteInterface]


    class ManagementVrfOneOfIpRoute3:
        interface_container: ManagementVrfInterfaceContainer


    class Ipv6Route:
        one_of_ip_route: Union[
            ManagementVrfOneOfIpRoute1,
            ManagementVrfOneOfIpRoute2,
            ManagementVrfOneOfIpRoute3,
        ]
        prefix: Union[
            OneOfIpv6RoutePrefixOptionsDef1,
            OneOfIpv6RoutePrefixOptionsDef2,
        ]


    class ManagementVrfData:
        vrf_name: OneOfVrfNameOptionsDef
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


    class Payload:
        """
        SD-Routing Management VRF feature schema
        """

        data: ManagementVrfData
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
        # SD-Routing Management VRF feature schema
        payload: Optional[Payload]


    class GetListSdRoutingTransportManagementVrfPayload:
        data: Optional[List[Data]]


    class CreateSdroutingManagementVrfFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class TransportManagementVrfData:
        vrf_name: OneOfVrfNameOptionsDef
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


    class CreateSdroutingManagementVrfFeaturePostRequest:
        """
        SD-Routing Management VRF feature schema
        """

        data: TransportManagementVrfData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingTransportManagementVrfPayload:
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
        # SD-Routing Management VRF feature schema
        payload: Optional[Payload]


    class EditSdroutingManagementVrfFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingTransportManagementVrfData:
        vrf_name: OneOfVrfNameOptionsDef
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


    class EditSdroutingManagementVrfFeaturePutRequest:
        """
        SD-Routing Management VRF feature schema
        """

        data: SdRoutingTransportManagementVrfData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


