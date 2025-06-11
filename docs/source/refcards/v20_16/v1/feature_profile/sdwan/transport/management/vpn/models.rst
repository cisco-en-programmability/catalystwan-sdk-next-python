======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    DefaultOptionTypeDef = Literal["default"]

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

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

    Ipv4GatewayDef = Literal["dhcp", "nextHop", "null0"]

    DefaultIpv4GatewayDef = Literal["nextHop"]

    BooleanTrueDef = Literal[True]

    Ipv6RouteNatDef = Literal["NAT64", "NAT66"]

    VpnIpv4GatewayDef = Literal["dhcp", "nextHop", "null0"]

    VpnDefaultIpv4GatewayDef = Literal["nextHop"]

    ManagementVpnIpv4GatewayDef = Literal["dhcp", "nextHop", "null0"]

    ManagementVpnDefaultIpv4GatewayDef = Literal["nextHop"]


    class OneOfVpnIdOptionsDef:
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


    class OneOfIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


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


    class VpnNextHop:
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
        next_hop: Optional[List[VpnNextHop]]


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


    class VpnData:
        vpn_id: OneOfVpnIdOptionsDef
        dns_ipv4: Optional[DnsIpv4]
        dns_ipv6: Optional[DnsIpv6]
        # IPv4 Static Route
        ipv4_route: Optional[List[Union[Ipv4Route1, Ipv4Route2]]]
        # IPv6 Static Route
        ipv6_route: Optional[List[Ipv6Route]]
        name: Optional[
            Union[
                OneOfVpnNameOptionsDef1,
                OneOfVpnNameOptionsDef2,
                OneOfVpnNameOptionsDef3,
            ]
        ]
        new_host_mapping: Optional[List[NewHostMapping]]


    class Payload:
        """
        Management Vpn Post Request schema
        """

        data: VpnData
        name: str
        # Set the parcel description
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
        # Management Vpn Post Request schema
        payload: Optional[Payload]


    class GetListSdwanTransportManagementVpnPayload:
        data: Optional[List[Data]]


    class CreateManagementVpnProfileParcelForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class ManagementVpnData:
        vpn_id: OneOfVpnIdOptionsDef
        dns_ipv4: Optional[DnsIpv4]
        dns_ipv6: Optional[DnsIpv6]
        # IPv4 Static Route
        ipv4_route: Optional[List[Union[Ipv4Route1, Ipv4Route2]]]
        # IPv6 Static Route
        ipv6_route: Optional[List[Ipv6Route]]
        name: Optional[
            Union[
                OneOfVpnNameOptionsDef1,
                OneOfVpnNameOptionsDef2,
                OneOfVpnNameOptionsDef3,
            ]
        ]
        new_host_mapping: Optional[List[NewHostMapping]]


    class CreateManagementVpnProfileParcelForTransportPostRequest:
        """
        Management Vpn Post Request schema
        """

        data: ManagementVpnData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class VpnOneOfVpnIdOptionsDef:
        option_type: DefaultOptionTypeDef
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


    class VpnOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnPrefix:
        """
        Prefix
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1, VpnOneOfIpV4AddressOptionsDef2
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class VpnOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class ManagementVpnNextHop:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            VpnOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class VpnOneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnIpv4Route1:
        gateway: Gateway
        # IPv4 Route Gateway Next Hop
        next_hop: List[ManagementVpnNextHop]
        # Prefix
        prefix: VpnPrefix
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                VpnOneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]


    class ManagementVpnOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class ManagementVpnPrefix:
        """
        Prefix
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            ManagementVpnOneOfIpV4AddressOptionsDef2,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class VpnOneOfIpv4RouteGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            VpnIpv4GatewayDef  # pytype: disable=annotation-type-mismatch
        )


    class VpnOneOfIpv4RouteGatewayOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: VpnDefaultIpv4GatewayDef  # pytype: disable=annotation-type-mismatch


    class ManagementVpnOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportManagementVpnNextHop:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            ManagementVpnOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class ManagementVpnOneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnIpv4Route2:
        gateway: Union[
            VpnOneOfIpv4RouteGatewayOptionsDef1,
            VpnOneOfIpv4RouteGatewayOptionsDef2,
        ]
        # Prefix
        prefix: ManagementVpnPrefix
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                ManagementVpnOneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]
        # IPv4 Route Gateway Next Hop
        next_hop: Optional[List[TransportManagementVpnNextHop]]


    class VpnOneOfIpv6NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanTransportManagementVpnNextHop:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            VpnOneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class VpnNextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[List[SdwanTransportManagementVpnNextHop]]


    class VpnOneOfIpRoute1:
        next_hop_container: VpnNextHopContainer


    class VpnIpv6Route:
        one_of_ip_route: Union[
            VpnOneOfIpRoute1, OneOfIpRoute2, OneOfIpRoute3
        ]
        prefix: Union[
            OneOfIpv6RoutePrefixOptionsDef1,
            OneOfIpv6RoutePrefixOptionsDef2,
        ]


    class TransportManagementVpnData:
        vpn_id: VpnOneOfVpnIdOptionsDef
        dns_ipv4: Optional[VpnDnsIpv4]
        dns_ipv6: Optional[VpnDnsIpv6]
        # IPv4 Static Route
        ipv4_route: Optional[List[Union[VpnIpv4Route1, VpnIpv4Route2]]]
        # IPv6 Static Route
        ipv6_route: Optional[List[VpnIpv6Route]]
        name: Optional[
            Union[
                OneOfVpnNameOptionsDef1,
                OneOfVpnNameOptionsDef2,
                OneOfVpnNameOptionsDef3,
            ]
        ]
        new_host_mapping: Optional[List[NewHostMapping]]


    class VpnPayload:
        """
        Management Vpn Put Request schema
        """

        data: TransportManagementVpnData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanTransportManagementVpnPayload:
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
        # Management Vpn Put Request schema
        payload: Optional[VpnPayload]


    class EditManagementVpnProfileParcelForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class ManagementVpnOneOfVpnIdOptionsDef:
        option_type: DefaultOptionTypeDef
        value: int


    class ManagementVpnOneOfPrimaryDnsAddressIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class ManagementVpnOneOfSecondaryDnsAddressIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class ManagementVpnDnsIpv4:
        primary_dns_address_ipv4: Optional[
            Union[
                OneOfPrimaryDnsAddressIpv4OptionsDef1,
                ManagementVpnOneOfPrimaryDnsAddressIpv4OptionsDef2,
                OneOfPrimaryDnsAddressIpv4OptionsDef3,
            ]
        ]
        secondary_dns_address_ipv4: Optional[
            Union[
                OneOfSecondaryDnsAddressIpv4OptionsDef1,
                ManagementVpnOneOfSecondaryDnsAddressIpv4OptionsDef2,
                OneOfSecondaryDnsAddressIpv4OptionsDef3,
            ]
        ]


    class ManagementVpnDnsIpv6:
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


    class TransportManagementVpnOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportManagementVpnPrefix:
        """
        Prefix
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            TransportManagementVpnOneOfIpV4AddressOptionsDef2,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class TransportManagementVpnOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdwanTransportManagementVpnNextHop:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            TransportManagementVpnOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class TransportManagementVpnOneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class ManagementVpnIpv4Route1:
        gateway: Gateway
        # IPv4 Route Gateway Next Hop
        next_hop: List[FeatureProfileSdwanTransportManagementVpnNextHop]
        # Prefix
        prefix: TransportManagementVpnPrefix
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                TransportManagementVpnOneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]


    class SdwanTransportManagementVpnOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanTransportManagementVpnPrefix:
        """
        Prefix
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            SdwanTransportManagementVpnOneOfIpV4AddressOptionsDef2,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class ManagementVpnOneOfIpv4RouteGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ManagementVpnIpv4GatewayDef  # pytype: disable=annotation-type-mismatch


    class ManagementVpnOneOfIpv4RouteGatewayOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: ManagementVpnDefaultIpv4GatewayDef  # pytype: disable=annotation-type-mismatch


    class SdwanTransportManagementVpnOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdwanTransportManagementVpnNextHop:
        address: Union[
            OneOfIpv4NextHopAddressOptionsWithOutDefault1,
            OneOfIpv4NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv4NextHopDistanceOptionsDef1,
            SdwanTransportManagementVpnOneOfIpv4NextHopDistanceOptionsDef2,
            OneOfIpv4NextHopDistanceOptionsDef3,
        ]


    class SdwanTransportManagementVpnOneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class ManagementVpnIpv4Route2:
        gateway: Union[
            ManagementVpnOneOfIpv4RouteGatewayOptionsDef1,
            ManagementVpnOneOfIpv4RouteGatewayOptionsDef2,
        ]
        # Prefix
        prefix: SdwanTransportManagementVpnPrefix
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                SdwanTransportManagementVpnOneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]
        # IPv4 Route Gateway Next Hop
        next_hop: Optional[
            List[V1FeatureProfileSdwanTransportManagementVpnNextHop]
        ]


    class ManagementVpnOneOfIpv6NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class NextHop1:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            ManagementVpnOneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class ManagementVpnNextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[List[NextHop1]]


    class ManagementVpnOneOfIpRoute1:
        next_hop_container: ManagementVpnNextHopContainer


    class ManagementVpnIpv6Route:
        one_of_ip_route: Union[
            ManagementVpnOneOfIpRoute1, OneOfIpRoute2, OneOfIpRoute3
        ]
        prefix: Union[
            OneOfIpv6RoutePrefixOptionsDef1,
            OneOfIpv6RoutePrefixOptionsDef2,
        ]


    class SdwanTransportManagementVpnData:
        vpn_id: ManagementVpnOneOfVpnIdOptionsDef
        dns_ipv4: Optional[ManagementVpnDnsIpv4]
        dns_ipv6: Optional[ManagementVpnDnsIpv6]
        # IPv4 Static Route
        ipv4_route: Optional[
            List[Union[ManagementVpnIpv4Route1, ManagementVpnIpv4Route2]]
        ]
        # IPv6 Static Route
        ipv6_route: Optional[List[ManagementVpnIpv6Route]]
        name: Optional[
            Union[
                OneOfVpnNameOptionsDef1,
                OneOfVpnNameOptionsDef2,
                OneOfVpnNameOptionsDef3,
            ]
        ]
        new_host_mapping: Optional[List[NewHostMapping]]


    class EditManagementVpnProfileParcelForTransportPutRequest:
        """
        Management Vpn Put Request schema
        """

        data: SdwanTransportManagementVpnData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


