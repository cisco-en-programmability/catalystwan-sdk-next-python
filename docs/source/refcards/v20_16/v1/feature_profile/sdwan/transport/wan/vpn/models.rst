======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

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

    Ipv4GatewayDef = Literal["dhcp", "nextHop", "null0"]

    DefaultIpv4GatewayDef = Literal["nextHop"]

    Ipv6RouteNatDef = Literal["NAT64", "NAT66"]

    ServiceTypeDef = Literal["TE"]

    VpnIpv4GatewayDef = Literal["dhcp", "nextHop", "null0"]

    VpnDefaultIpv4GatewayDef = Literal["nextHop"]

    VpnServiceTypeDef = Literal["TE"]

    WanVpnIpv4GatewayDef = Literal["dhcp", "nextHop", "null0"]

    WanVpnDefaultIpv4GatewayDef = Literal["nextHop"]

    WanVpnServiceTypeDef = Literal["TE"]


    class OneOfVpnIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVpnIdOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfEnhanceEcmpKeyingOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEnhanceEcmpKeyingOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfEnhanceEcmpKeyingOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


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

        ip_address: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
            ]
        ]
        subnet_mask: Optional[
            Union[
                OneOfIpV4SubnetMaskOptionsDef1,
                OneOfIpV4SubnetMaskOptionsDef2,
            ]
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
        address: Optional[
            Union[
                OneOfIpv4NextHopAddressOptionsWithOutDefault1,
                OneOfIpv4NextHopAddressOptionsWithOutDefault2,
            ]
        ]
        distance: Optional[
            Union[
                OneOfIpv4NextHopDistanceOptionsDef1,
                OneOfIpv4NextHopDistanceOptionsDef2,
                OneOfIpv4NextHopDistanceOptionsDef3,
            ]
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
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                OneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]
        # Prefix
        prefix: Optional[Prefix]


    class OneOfIpv4RouteGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Ipv4GatewayDef  # pytype: disable=annotation-type-mismatch


    class OneOfIpv4RouteGatewayOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: DefaultIpv4GatewayDef  # pytype: disable=annotation-type-mismatch


    class Ipv4Route2:
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                OneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]
        gateway: Optional[
            Union[
                OneOfIpv4RouteGatewayOptionsDef1,
                OneOfIpv4RouteGatewayOptionsDef2,
            ]
        ]
        # IPv4 Route Gateway Next Hop
        next_hop: Optional[List[NextHop]]
        # Prefix
        prefix: Optional[Prefix]


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


    class OneOfServiceTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: ServiceTypeDef  # pytype: disable=annotation-type-mismatch


    class Service:
        service_type: OneOfServiceTypeOptionsDef


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


    class VpnData:
        enhance_ecmp_keying: Union[
            OneOfEnhanceEcmpKeyingOptionsDef1,
            OneOfEnhanceEcmpKeyingOptionsDef2,
            OneOfEnhanceEcmpKeyingOptionsDef3,
        ]
        vpn_id: Union[OneOfVpnIdOptionsDef1, OneOfVpnIdOptionsDef2]
        dns_ipv4: Optional[DnsIpv4]
        dns_ipv6: Optional[DnsIpv6]
        # IPv4 Static Route
        ipv4_route: Optional[List[Union[Ipv4Route1, Ipv4Route2]]]
        # IPv6 Static Route
        ipv6_route: Optional[List[Ipv6Route]]
        # NAT64 V4 Pool
        nat64_v4_pool: Optional[List[Nat64V4Pool]]
        new_host_mapping: Optional[List[NewHostMapping]]
        # Service
        service: Optional[List[Service]]


    class Payload:
        """
        WAN VPN profile parcel schema for POST request
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
        # WAN VPN profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanTransportWanVpnPayload:
        data: Optional[List[Data]]


    class CreateWanVpnProfileParcelForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class WanVpnData:
        enhance_ecmp_keying: Union[
            OneOfEnhanceEcmpKeyingOptionsDef1,
            OneOfEnhanceEcmpKeyingOptionsDef2,
            OneOfEnhanceEcmpKeyingOptionsDef3,
        ]
        vpn_id: Union[OneOfVpnIdOptionsDef1, OneOfVpnIdOptionsDef2]
        dns_ipv4: Optional[DnsIpv4]
        dns_ipv6: Optional[DnsIpv6]
        # IPv4 Static Route
        ipv4_route: Optional[List[Union[Ipv4Route1, Ipv4Route2]]]
        # IPv6 Static Route
        ipv6_route: Optional[List[Ipv6Route]]
        # NAT64 V4 Pool
        nat64_v4_pool: Optional[List[Nat64V4Pool]]
        new_host_mapping: Optional[List[NewHostMapping]]
        # Service
        service: Optional[List[Service]]


    class CreateWanVpnProfileParcelForTransportPostRequest:
        """
        WAN VPN profile parcel schema for POST request
        """

        data: WanVpnData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class VpnOneOfVpnIdOptionsDef1:
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


    class VpnOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnPrefix:
        """
        Prefix
        """

        ip_address: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1,
                VpnOneOfIpV4AddressOptionsDef2,
            ]
        ]
        subnet_mask: Optional[
            Union[
                OneOfIpV4SubnetMaskOptionsDef1,
                OneOfIpV4SubnetMaskOptionsDef2,
            ]
        ]


    class VpnOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnNextHop:
        address: Optional[
            Union[
                OneOfIpv4NextHopAddressOptionsWithOutDefault1,
                OneOfIpv4NextHopAddressOptionsWithOutDefault2,
            ]
        ]
        distance: Optional[
            Union[
                OneOfIpv4NextHopDistanceOptionsDef1,
                VpnOneOfIpv4NextHopDistanceOptionsDef2,
                OneOfIpv4NextHopDistanceOptionsDef3,
            ]
        ]


    class VpnOneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnIpv4Route1:
        gateway: Gateway
        # IPv4 Route Gateway Next Hop
        next_hop: List[WanVpnNextHop]
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                VpnOneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]
        # Prefix
        prefix: Optional[VpnPrefix]


    class WanVpnOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class WanVpnPrefix:
        """
        Prefix
        """

        ip_address: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1,
                WanVpnOneOfIpV4AddressOptionsDef2,
            ]
        ]
        subnet_mask: Optional[
            Union[
                OneOfIpV4SubnetMaskOptionsDef1,
                OneOfIpV4SubnetMaskOptionsDef2,
            ]
        ]


    class VpnOneOfIpv4RouteGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            VpnIpv4GatewayDef  # pytype: disable=annotation-type-mismatch
        )


    class VpnOneOfIpv4RouteGatewayOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: VpnDefaultIpv4GatewayDef  # pytype: disable=annotation-type-mismatch


    class WanVpnOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportWanVpnNextHop:
        address: Optional[
            Union[
                OneOfIpv4NextHopAddressOptionsWithOutDefault1,
                OneOfIpv4NextHopAddressOptionsWithOutDefault2,
            ]
        ]
        distance: Optional[
            Union[
                OneOfIpv4NextHopDistanceOptionsDef1,
                WanVpnOneOfIpv4NextHopDistanceOptionsDef2,
                OneOfIpv4NextHopDistanceOptionsDef3,
            ]
        ]


    class WanVpnOneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnIpv4Route2:
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                WanVpnOneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]
        gateway: Optional[
            Union[
                VpnOneOfIpv4RouteGatewayOptionsDef1,
                VpnOneOfIpv4RouteGatewayOptionsDef2,
            ]
        ]
        # IPv4 Route Gateway Next Hop
        next_hop: Optional[List[TransportWanVpnNextHop]]
        # Prefix
        prefix: Optional[WanVpnPrefix]


    class VpnOneOfIpv6NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanTransportWanVpnNextHop:
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
        next_hop: Optional[List[SdwanTransportWanVpnNextHop]]


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


    class VpnOneOfServiceTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            VpnServiceTypeDef  # pytype: disable=annotation-type-mismatch
        )


    class VpnService:
        service_type: VpnOneOfServiceTypeOptionsDef


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


    class TransportWanVpnData:
        enhance_ecmp_keying: Union[
            OneOfEnhanceEcmpKeyingOptionsDef1,
            OneOfEnhanceEcmpKeyingOptionsDef2,
            OneOfEnhanceEcmpKeyingOptionsDef3,
        ]
        vpn_id: Union[VpnOneOfVpnIdOptionsDef1, OneOfVpnIdOptionsDef2]
        dns_ipv4: Optional[VpnDnsIpv4]
        dns_ipv6: Optional[VpnDnsIpv6]
        # IPv4 Static Route
        ipv4_route: Optional[List[Union[VpnIpv4Route1, VpnIpv4Route2]]]
        # IPv6 Static Route
        ipv6_route: Optional[List[VpnIpv6Route]]
        # NAT64 V4 Pool
        nat64_v4_pool: Optional[List[VpnNat64V4Pool]]
        new_host_mapping: Optional[List[NewHostMapping]]
        # Service
        service: Optional[List[VpnService]]


    class VpnPayload:
        """
        WAN VPN profile parcel schema for PUT request
        """

        data: TransportWanVpnData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanTransportWanVpnPayload:
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
        # WAN VPN profile parcel schema for PUT request
        payload: Optional[VpnPayload]


    class EditWanVpnProfileParcelForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class WanVpnOneOfVpnIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnOneOfPrimaryDnsAddressIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class WanVpnOneOfSecondaryDnsAddressIpv4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class WanVpnDnsIpv4:
        primary_dns_address_ipv4: Optional[
            Union[
                OneOfPrimaryDnsAddressIpv4OptionsDef1,
                WanVpnOneOfPrimaryDnsAddressIpv4OptionsDef2,
                OneOfPrimaryDnsAddressIpv4OptionsDef3,
            ]
        ]
        secondary_dns_address_ipv4: Optional[
            Union[
                OneOfSecondaryDnsAddressIpv4OptionsDef1,
                WanVpnOneOfSecondaryDnsAddressIpv4OptionsDef2,
                OneOfSecondaryDnsAddressIpv4OptionsDef3,
            ]
        ]


    class WanVpnDnsIpv6:
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


    class TransportWanVpnOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportWanVpnPrefix:
        """
        Prefix
        """

        ip_address: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1,
                TransportWanVpnOneOfIpV4AddressOptionsDef2,
            ]
        ]
        subnet_mask: Optional[
            Union[
                OneOfIpV4SubnetMaskOptionsDef1,
                OneOfIpV4SubnetMaskOptionsDef2,
            ]
        ]


    class TransportWanVpnOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdwanTransportWanVpnNextHop:
        address: Optional[
            Union[
                OneOfIpv4NextHopAddressOptionsWithOutDefault1,
                OneOfIpv4NextHopAddressOptionsWithOutDefault2,
            ]
        ]
        distance: Optional[
            Union[
                OneOfIpv4NextHopDistanceOptionsDef1,
                TransportWanVpnOneOfIpv4NextHopDistanceOptionsDef2,
                OneOfIpv4NextHopDistanceOptionsDef3,
            ]
        ]


    class TransportWanVpnOneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnIpv4Route1:
        gateway: Gateway
        # IPv4 Route Gateway Next Hop
        next_hop: List[FeatureProfileSdwanTransportWanVpnNextHop]
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                TransportWanVpnOneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]
        # Prefix
        prefix: Optional[TransportWanVpnPrefix]


    class SdwanTransportWanVpnOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanTransportWanVpnPrefix:
        """
        Prefix
        """

        ip_address: Optional[
            Union[
                OneOfIpV4AddressOptionsDef1,
                SdwanTransportWanVpnOneOfIpV4AddressOptionsDef2,
            ]
        ]
        subnet_mask: Optional[
            Union[
                OneOfIpV4SubnetMaskOptionsDef1,
                OneOfIpV4SubnetMaskOptionsDef2,
            ]
        ]


    class WanVpnOneOfIpv4RouteGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: WanVpnIpv4GatewayDef  # pytype: disable=annotation-type-mismatch


    class WanVpnOneOfIpv4RouteGatewayOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: WanVpnDefaultIpv4GatewayDef  # pytype: disable=annotation-type-mismatch


    class SdwanTransportWanVpnOneOfIpv4NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdwanTransportWanVpnNextHop:
        address: Optional[
            Union[
                OneOfIpv4NextHopAddressOptionsWithOutDefault1,
                OneOfIpv4NextHopAddressOptionsWithOutDefault2,
            ]
        ]
        distance: Optional[
            Union[
                OneOfIpv4NextHopDistanceOptionsDef1,
                SdwanTransportWanVpnOneOfIpv4NextHopDistanceOptionsDef2,
                OneOfIpv4NextHopDistanceOptionsDef3,
            ]
        ]


    class SdwanTransportWanVpnOneOfIpv4GatewayDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnIpv4Route2:
        distance: Optional[
            Union[
                OneOfIpv4GatewayDistanceOptionsDef1,
                SdwanTransportWanVpnOneOfIpv4GatewayDistanceOptionsDef2,
                OneOfIpv4GatewayDistanceOptionsDef3,
            ]
        ]
        gateway: Optional[
            Union[
                WanVpnOneOfIpv4RouteGatewayOptionsDef1,
                WanVpnOneOfIpv4RouteGatewayOptionsDef2,
            ]
        ]
        # IPv4 Route Gateway Next Hop
        next_hop: Optional[
            List[V1FeatureProfileSdwanTransportWanVpnNextHop]
        ]
        # Prefix
        prefix: Optional[SdwanTransportWanVpnPrefix]


    class WanVpnOneOfIpv6NextHopDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class NextHop1:
        address: Union[
            OneOfIpv6NextHopAddressOptionsWithOutDefault1,
            OneOfIpv6NextHopAddressOptionsWithOutDefault2,
        ]
        distance: Union[
            OneOfIpv6NextHopDistanceOptionsDef1,
            WanVpnOneOfIpv6NextHopDistanceOptionsDef2,
            OneOfIpv6NextHopDistanceOptionsDef3,
        ]


    class WanVpnNextHopContainer:
        # IPv6 Route Gateway Next Hop
        next_hop: Optional[List[NextHop1]]


    class WanVpnOneOfIpRoute1:
        next_hop_container: WanVpnNextHopContainer


    class WanVpnIpv6Route:
        one_of_ip_route: Union[
            WanVpnOneOfIpRoute1, OneOfIpRoute2, OneOfIpRoute3
        ]
        prefix: Union[
            OneOfIpv6RoutePrefixOptionsDef1,
            OneOfIpv6RoutePrefixOptionsDef2,
        ]


    class WanVpnOneOfServiceTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: WanVpnServiceTypeDef  # pytype: disable=annotation-type-mismatch


    class WanVpnService:
        service_type: WanVpnOneOfServiceTypeOptionsDef


    class WanVpnOneOfNat64V4PoolNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class WanVpnOneOfNat64V4PoolRangeStartOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class WanVpnOneOfNat64V4PoolRangeEndOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class WanVpnNat64V4Pool:
        nat64_v4_pool_name: Union[
            OneOfNat64V4PoolNameOptionsDef1,
            WanVpnOneOfNat64V4PoolNameOptionsDef2,
        ]
        nat64_v4_pool_overload: Union[
            OneOfNat64V4PoolOverloadOptionsDef1,
            OneOfNat64V4PoolOverloadOptionsDef2,
            OneOfNat64V4PoolOverloadOptionsDef3,
        ]
        nat64_v4_pool_range_end: Union[
            OneOfNat64V4PoolRangeEndOptionsDef1,
            WanVpnOneOfNat64V4PoolRangeEndOptionsDef2,
        ]
        nat64_v4_pool_range_start: Union[
            OneOfNat64V4PoolRangeStartOptionsDef1,
            WanVpnOneOfNat64V4PoolRangeStartOptionsDef2,
        ]


    class SdwanTransportWanVpnData:
        enhance_ecmp_keying: Union[
            OneOfEnhanceEcmpKeyingOptionsDef1,
            OneOfEnhanceEcmpKeyingOptionsDef2,
            OneOfEnhanceEcmpKeyingOptionsDef3,
        ]
        vpn_id: Union[WanVpnOneOfVpnIdOptionsDef1, OneOfVpnIdOptionsDef2]
        dns_ipv4: Optional[WanVpnDnsIpv4]
        dns_ipv6: Optional[WanVpnDnsIpv6]
        # IPv4 Static Route
        ipv4_route: Optional[
            List[Union[WanVpnIpv4Route1, WanVpnIpv4Route2]]
        ]
        # IPv6 Static Route
        ipv6_route: Optional[List[WanVpnIpv6Route]]
        # NAT64 V4 Pool
        nat64_v4_pool: Optional[List[WanVpnNat64V4Pool]]
        new_host_mapping: Optional[List[NewHostMapping]]
        # Service
        service: Optional[List[WanVpnService]]


    class EditWanVpnProfileParcelForTransportPutRequest:
        """
        WAN VPN profile parcel schema for PUT request
        """

        data: SdwanTransportWanVpnData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


