======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanTrueDef = Literal[True]

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

    BooleanFalseDef = Literal[False]

    DuplexDef = Literal["auto", "full", "half"]

    SpeedDef = Literal["10", "100", "1000", "10000", "2500", "25000"]

    MediaTypeDef = Literal["auto-select", "rj45", "sfp"]

    EthernetDuplexDef = Literal["auto", "full", "half"]

    EthernetSpeedDef = Literal[
        "10", "100", "1000", "10000", "2500", "25000"
    ]

    EthernetMediaTypeDef = Literal["auto-select", "rj45", "sfp"]

    InterfaceEthernetDuplexDef = Literal["auto", "full", "half"]

    InterfaceEthernetSpeedDef = Literal[
        "10", "100", "1000", "10000", "2500", "25000"
    ]

    InterfaceEthernetMediaTypeDef = Literal["auto-select", "rj45", "sfp"]


    class OneOfShutdownOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfShutdownOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfShutdownOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDescriptionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDescriptionOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfDynamicDhcpDistanceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDynamicDhcpDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDynamicDhcpDistanceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Dynamic:
        dynamic_dhcp_distance: Union[
            OneOfDynamicDhcpDistanceOptionsDef1,
            OneOfDynamicDhcpDistanceOptionsDef2,
            OneOfDynamicDhcpDistanceOptionsDef3,
        ]


    class IntfIpAddress1:
        dynamic: Dynamic


    class OneOfIpV4AddressGlobalVariableDefaultOptionNoDefaultDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressGlobalVariableDefaultOptionNoDefaultDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfIpV4AddressGlobalVariableDefaultOptionNoDefaultDef3:
        option_type: DefaultOptionTypeDef


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


    class OneOfIpV4SubnetMaskOptionsDef3:
        option_type: DefaultOptionTypeDef


    class StaticIpV4AddressPrimary:
        """
        Static IpV4Address Primary
        """

        ip_address: Union[
            OneOfIpV4AddressGlobalVariableDefaultOptionNoDefaultDef1,
            OneOfIpV4AddressGlobalVariableDefaultOptionNoDefaultDef2,
            OneOfIpV4AddressGlobalVariableDefaultOptionNoDefaultDef3,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1,
            OneOfIpV4SubnetMaskOptionsDef2,
            OneOfIpV4SubnetMaskOptionsDef3,
        ]


    class OneOfIpV4AddressOptionsWithoutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfIpV4SubnetMaskOptionsWithoutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4SubnetMaskOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: (
            Ipv4SubnetMaskDef  # pytype: disable=annotation-type-mismatch
        )


    class StaticIpV4AddressSecondary:
        ip_address: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsWithoutDefault1,
            OneOfIpV4SubnetMaskOptionsWithoutDefault2,
        ]


    class Static:
        # Static IpV4Address Primary
        static_ip_v4_address_primary: StaticIpV4AddressPrimary
        # Secondary IpV4 Addresses
        static_ip_v4_address_secondary: Optional[
            List[StaticIpV4AddressSecondary]
        ]


    class IntfIpAddress2:
        static: Static


    class OneOfListOfIpV4OptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfListOfIpV4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfListOfIpV4OptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfIperfServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIperfServerOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIperfServerOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfAutoBandwidthDetectOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAutoBandwidthDetectOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAutoBandwidthDetectOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class DhcpClient:
        """
        Enable DHCPv6
        """

        option_type: GlobalOptionTypeDef
        value: Any


    class EthernetDynamic:
        # Enable DHCPv6
        dhcp_client: DhcpClient


    class IntfIpV6Address1:
        dynamic: EthernetDynamic


    class OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef3:
        option_type: DefaultOptionTypeDef


    class PrimaryIpV6Address:
        """
        Static IpV6Address Primary
        """

        address: Union[
            OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef1,
            OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef2,
            OneOfIpv6PrefixGlobalVariableDefaultNoValueOptionsDef3,
        ]


    class EthernetStatic:
        # Static IpV6Address Primary
        primary_ip_v6_address: Optional[PrimaryIpV6Address]


    class IntfIpV6Address2:
        static: EthernetStatic


    class OneOfIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfMacAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfMacAddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Arp:
        ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        mac_address: Union[
            OneOfMacAddressOptionsDef1, OneOfMacAddressOptionsDef2
        ]


    class OneOfDuplexOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: DuplexDef  # pytype: disable=annotation-type-mismatch


    class OneOfDuplexOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDuplexOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfAdvMacAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAdvMacAddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAdvMacAddressOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMtuOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIntrfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIntrfMtuOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIntrfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Any


    class OneOfTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTcpMssAdjustOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTcpMssAdjustOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfSpeedOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SpeedDef  # pytype: disable=annotation-type-mismatch


    class OneOfSpeedOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSpeedOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfArpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfArpTimeoutOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfArpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfAutonegotiateOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAutonegotiateOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAutonegotiateOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfMediaTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: MediaTypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfMediaTypeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMediaTypeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfLoadIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfLoadIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLoadIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIcmpRedirectDisableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfIcmpRedirectDisableOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIcmpRedirectDisableOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfIpDirectedBroadcastOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfIpDirectedBroadcastOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpDirectedBroadcastOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class Advanced:
        """
        Advanced Attributes
        """

        arp_timeout: Union[
            OneOfArpTimeoutOptionsDef1,
            OneOfArpTimeoutOptionsDef2,
            OneOfArpTimeoutOptionsDef3,
        ]
        ip_directed_broadcast: Union[
            OneOfIpDirectedBroadcastOptionsDef1,
            OneOfIpDirectedBroadcastOptionsDef2,
            OneOfIpDirectedBroadcastOptionsDef3,
        ]
        ip_mtu: Union[
            OneOfMtuOptionsDef1, OneOfMtuOptionsDef2, OneOfMtuOptionsDef3
        ]
        load_interval: Union[
            OneOfLoadIntervalOptionsDef1,
            OneOfLoadIntervalOptionsDef2,
            OneOfLoadIntervalOptionsDef3,
        ]
        autonegotiate: Optional[
            Union[
                OneOfAutonegotiateOptionsDef1,
                OneOfAutonegotiateOptionsDef2,
                OneOfAutonegotiateOptionsDef3,
            ]
        ]
        duplex: Optional[
            Union[
                OneOfDuplexOptionsDef1,
                OneOfDuplexOptionsDef2,
                OneOfDuplexOptionsDef3,
            ]
        ]
        icmp_redirect_disable: Optional[
            Union[
                OneOfIcmpRedirectDisableOptionsDef1,
                OneOfIcmpRedirectDisableOptionsDef2,
                OneOfIcmpRedirectDisableOptionsDef3,
            ]
        ]
        intrf_mtu: Optional[
            Union[
                OneOfIntrfMtuOptionsDef1,
                OneOfIntrfMtuOptionsDef2,
                OneOfIntrfMtuOptionsDef3,
            ]
        ]
        mac_address: Optional[
            Union[
                OneOfAdvMacAddressOptionsDef1,
                OneOfAdvMacAddressOptionsDef2,
                OneOfAdvMacAddressOptionsDef3,
            ]
        ]
        media_type: Optional[
            Union[
                OneOfMediaTypeOptionsDef1,
                OneOfMediaTypeOptionsDef2,
                OneOfMediaTypeOptionsDef3,
            ]
        ]
        speed: Optional[
            Union[
                OneOfSpeedOptionsDef1,
                OneOfSpeedOptionsDef2,
                OneOfSpeedOptionsDef3,
            ]
        ]
        tcp_mss: Optional[
            Union[
                OneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]


    class EthernetData:
        # Advanced Attributes
        advanced: Advanced
        interface_name: Union[
            OneOfInterfaceNameOptionsDef1, OneOfInterfaceNameOptionsDef2
        ]
        intf_ip_address: Union[IntfIpAddress1, IntfIpAddress2]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        # Configure ARP entries
        arp: Optional[List[Arp]]
        auto_detect_bandwidth: Optional[
            Union[
                OneOfAutoBandwidthDetectOptionsDef1,
                OneOfAutoBandwidthDetectOptionsDef2,
                OneOfAutoBandwidthDetectOptionsDef3,
            ]
        ]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                OneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        intf_ip_v6_address: Optional[
            Union[IntfIpV6Address1, IntfIpV6Address2]
        ]
        iperf_server: Optional[
            Union[
                OneOfIperfServerOptionsDef1,
                OneOfIperfServerOptionsDef2,
                OneOfIperfServerOptionsDef3,
            ]
        ]


    class Payload:
        """
        Management VPN Interface Ethernet profile parcel schema for POST request
        """

        data: EthernetData
        name: str
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
        # Management VPN Interface Ethernet profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanTransportManagementVpnInterfaceEthernetPayload:
        data: Optional[List[Data]]


    class CreateManagementVpnInterfaceEthernetParcelForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class InterfaceEthernetData:
        # Advanced Attributes
        advanced: Advanced
        interface_name: Union[
            OneOfInterfaceNameOptionsDef1, OneOfInterfaceNameOptionsDef2
        ]
        intf_ip_address: Union[IntfIpAddress1, IntfIpAddress2]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        # Configure ARP entries
        arp: Optional[List[Arp]]
        auto_detect_bandwidth: Optional[
            Union[
                OneOfAutoBandwidthDetectOptionsDef1,
                OneOfAutoBandwidthDetectOptionsDef2,
                OneOfAutoBandwidthDetectOptionsDef3,
            ]
        ]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                OneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        intf_ip_v6_address: Optional[
            Union[IntfIpV6Address1, IntfIpV6Address2]
        ]
        iperf_server: Optional[
            Union[
                OneOfIperfServerOptionsDef1,
                OneOfIperfServerOptionsDef2,
                OneOfIperfServerOptionsDef3,
            ]
        ]


    class CreateManagementVpnInterfaceEthernetParcelForTransportPostRequest:
        """
        Management VPN Interface Ethernet profile parcel schema for POST request
        """

        data: InterfaceEthernetData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class EthernetOneOfDynamicDhcpDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfDynamicDhcpDistanceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetDynamic:
        dynamic_dhcp_distance: Union[
            OneOfDynamicDhcpDistanceOptionsDef1,
            EthernetOneOfDynamicDhcpDistanceOptionsDef2,
            EthernetOneOfDynamicDhcpDistanceOptionsDef3,
        ]


    class EthernetIntfIpAddress1:
        dynamic: InterfaceEthernetDynamic


    class EthernetStaticIpV4AddressPrimary:
        """
        Static IpV4Address Primary
        """

        ip_address: Union[
            OneOfIpV4AddressGlobalVariableDefaultOptionNoDefaultDef1,
            OneOfIpV4AddressGlobalVariableDefaultOptionNoDefaultDef2,
            OneOfIpV4AddressGlobalVariableDefaultOptionNoDefaultDef3,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1,
            OneOfIpV4SubnetMaskOptionsDef2,
            OneOfIpV4SubnetMaskOptionsDef3,
        ]


    class InterfaceEthernetStatic:
        # Static IpV4Address Primary
        static_ip_v4_address_primary: EthernetStaticIpV4AddressPrimary
        # Secondary IpV4 Addresses
        static_ip_v4_address_secondary: Optional[
            List[StaticIpV4AddressSecondary]
        ]


    class EthernetIntfIpAddress2:
        static: InterfaceEthernetStatic


    class EthernetOneOfListOfIpV4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class EthernetOneOfIperfServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfMacAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetArp:
        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            EthernetOneOfIpV4AddressOptionsDef2,
        ]
        mac_address: Union[
            EthernetOneOfMacAddressOptionsDef1, OneOfMacAddressOptionsDef2
        ]


    class EthernetOneOfDuplexOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            EthernetDuplexDef  # pytype: disable=annotation-type-mismatch
        )


    class EthernetOneOfAdvMacAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EthernetOneOfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetOneOfIntrfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfSpeedOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            EthernetSpeedDef  # pytype: disable=annotation-type-mismatch
        )


    class EthernetOneOfArpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetOneOfArpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class EthernetOneOfMediaTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EthernetMediaTypeDef  # pytype: disable=annotation-type-mismatch


    class EthernetOneOfLoadIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class EthernetAdvanced:
        """
        Advanced Attributes
        """

        arp_timeout: Union[
            EthernetOneOfArpTimeoutOptionsDef1,
            OneOfArpTimeoutOptionsDef2,
            EthernetOneOfArpTimeoutOptionsDef3,
        ]
        ip_directed_broadcast: Union[
            OneOfIpDirectedBroadcastOptionsDef1,
            OneOfIpDirectedBroadcastOptionsDef2,
            OneOfIpDirectedBroadcastOptionsDef3,
        ]
        ip_mtu: Union[
            EthernetOneOfMtuOptionsDef1,
            OneOfMtuOptionsDef2,
            EthernetOneOfMtuOptionsDef3,
        ]
        load_interval: Union[
            EthernetOneOfLoadIntervalOptionsDef1,
            OneOfLoadIntervalOptionsDef2,
            OneOfLoadIntervalOptionsDef3,
        ]
        autonegotiate: Optional[
            Union[
                OneOfAutonegotiateOptionsDef1,
                OneOfAutonegotiateOptionsDef2,
                OneOfAutonegotiateOptionsDef3,
            ]
        ]
        duplex: Optional[
            Union[
                EthernetOneOfDuplexOptionsDef1,
                OneOfDuplexOptionsDef2,
                OneOfDuplexOptionsDef3,
            ]
        ]
        icmp_redirect_disable: Optional[
            Union[
                OneOfIcmpRedirectDisableOptionsDef1,
                OneOfIcmpRedirectDisableOptionsDef2,
                OneOfIcmpRedirectDisableOptionsDef3,
            ]
        ]
        intrf_mtu: Optional[
            Union[
                EthernetOneOfIntrfMtuOptionsDef1,
                OneOfIntrfMtuOptionsDef2,
                OneOfIntrfMtuOptionsDef3,
            ]
        ]
        mac_address: Optional[
            Union[
                EthernetOneOfAdvMacAddressOptionsDef1,
                OneOfAdvMacAddressOptionsDef2,
                OneOfAdvMacAddressOptionsDef3,
            ]
        ]
        media_type: Optional[
            Union[
                EthernetOneOfMediaTypeOptionsDef1,
                OneOfMediaTypeOptionsDef2,
                OneOfMediaTypeOptionsDef3,
            ]
        ]
        speed: Optional[
            Union[
                EthernetOneOfSpeedOptionsDef1,
                OneOfSpeedOptionsDef2,
                OneOfSpeedOptionsDef3,
            ]
        ]
        tcp_mss: Optional[
            Union[
                EthernetOneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]


    class VpnInterfaceEthernetData:
        # Advanced Attributes
        advanced: EthernetAdvanced
        interface_name: Union[
            OneOfInterfaceNameOptionsDef1, OneOfInterfaceNameOptionsDef2
        ]
        intf_ip_address: Union[
            EthernetIntfIpAddress1, EthernetIntfIpAddress2
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        # Configure ARP entries
        arp: Optional[List[EthernetArp]]
        auto_detect_bandwidth: Optional[
            Union[
                OneOfAutoBandwidthDetectOptionsDef1,
                OneOfAutoBandwidthDetectOptionsDef2,
                OneOfAutoBandwidthDetectOptionsDef3,
            ]
        ]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                EthernetOneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        intf_ip_v6_address: Optional[
            Union[IntfIpV6Address1, IntfIpV6Address2]
        ]
        iperf_server: Optional[
            Union[
                EthernetOneOfIperfServerOptionsDef1,
                OneOfIperfServerOptionsDef2,
                OneOfIperfServerOptionsDef3,
            ]
        ]


    class EthernetPayload:
        """
        Management VPN Interface Ethernet profile parcel schema for PUT request
        """

        data: VpnInterfaceEthernetData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanTransportManagementVpnInterfaceEthernetPayload:
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
        # Management VPN Interface Ethernet profile parcel schema for PUT request
        payload: Optional[EthernetPayload]


    class EditManagementVpnInterfaceEthernetParcelForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class InterfaceEthernetOneOfDynamicDhcpDistanceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfDynamicDhcpDistanceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class VpnInterfaceEthernetDynamic:
        dynamic_dhcp_distance: Union[
            OneOfDynamicDhcpDistanceOptionsDef1,
            InterfaceEthernetOneOfDynamicDhcpDistanceOptionsDef2,
            InterfaceEthernetOneOfDynamicDhcpDistanceOptionsDef3,
        ]


    class InterfaceEthernetIntfIpAddress1:
        dynamic: VpnInterfaceEthernetDynamic


    class InterfaceEthernetStaticIpV4AddressPrimary:
        """
        Static IpV4Address Primary
        """

        ip_address: Union[
            OneOfIpV4AddressGlobalVariableDefaultOptionNoDefaultDef1,
            OneOfIpV4AddressGlobalVariableDefaultOptionNoDefaultDef2,
            OneOfIpV4AddressGlobalVariableDefaultOptionNoDefaultDef3,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1,
            OneOfIpV4SubnetMaskOptionsDef2,
            OneOfIpV4SubnetMaskOptionsDef3,
        ]


    class VpnInterfaceEthernetStatic:
        # Static IpV4Address Primary
        static_ip_v4_address_primary: (
            InterfaceEthernetStaticIpV4AddressPrimary
        )
        # Secondary IpV4 Addresses
        static_ip_v4_address_secondary: Optional[
            List[StaticIpV4AddressSecondary]
        ]


    class InterfaceEthernetIntfIpAddress2:
        static: VpnInterfaceEthernetStatic


    class InterfaceEthernetOneOfListOfIpV4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class InterfaceEthernetOneOfIperfServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetOneOfMacAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetArp:
        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            InterfaceEthernetOneOfIpV4AddressOptionsDef2,
        ]
        mac_address: Union[
            InterfaceEthernetOneOfMacAddressOptionsDef1,
            OneOfMacAddressOptionsDef2,
        ]


    class InterfaceEthernetOneOfDuplexOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetDuplexDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfAdvMacAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceEthernetOneOfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetOneOfIntrfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfSpeedOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetSpeedDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfArpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetOneOfArpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceEthernetOneOfMediaTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceEthernetMediaTypeDef  # pytype: disable=annotation-type-mismatch


    class InterfaceEthernetOneOfLoadIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceEthernetAdvanced:
        """
        Advanced Attributes
        """

        arp_timeout: Union[
            InterfaceEthernetOneOfArpTimeoutOptionsDef1,
            OneOfArpTimeoutOptionsDef2,
            InterfaceEthernetOneOfArpTimeoutOptionsDef3,
        ]
        ip_directed_broadcast: Union[
            OneOfIpDirectedBroadcastOptionsDef1,
            OneOfIpDirectedBroadcastOptionsDef2,
            OneOfIpDirectedBroadcastOptionsDef3,
        ]
        ip_mtu: Union[
            InterfaceEthernetOneOfMtuOptionsDef1,
            OneOfMtuOptionsDef2,
            InterfaceEthernetOneOfMtuOptionsDef3,
        ]
        load_interval: Union[
            InterfaceEthernetOneOfLoadIntervalOptionsDef1,
            OneOfLoadIntervalOptionsDef2,
            OneOfLoadIntervalOptionsDef3,
        ]
        autonegotiate: Optional[
            Union[
                OneOfAutonegotiateOptionsDef1,
                OneOfAutonegotiateOptionsDef2,
                OneOfAutonegotiateOptionsDef3,
            ]
        ]
        duplex: Optional[
            Union[
                InterfaceEthernetOneOfDuplexOptionsDef1,
                OneOfDuplexOptionsDef2,
                OneOfDuplexOptionsDef3,
            ]
        ]
        icmp_redirect_disable: Optional[
            Union[
                OneOfIcmpRedirectDisableOptionsDef1,
                OneOfIcmpRedirectDisableOptionsDef2,
                OneOfIcmpRedirectDisableOptionsDef3,
            ]
        ]
        intrf_mtu: Optional[
            Union[
                InterfaceEthernetOneOfIntrfMtuOptionsDef1,
                OneOfIntrfMtuOptionsDef2,
                OneOfIntrfMtuOptionsDef3,
            ]
        ]
        mac_address: Optional[
            Union[
                InterfaceEthernetOneOfAdvMacAddressOptionsDef1,
                OneOfAdvMacAddressOptionsDef2,
                OneOfAdvMacAddressOptionsDef3,
            ]
        ]
        media_type: Optional[
            Union[
                InterfaceEthernetOneOfMediaTypeOptionsDef1,
                OneOfMediaTypeOptionsDef2,
                OneOfMediaTypeOptionsDef3,
            ]
        ]
        speed: Optional[
            Union[
                InterfaceEthernetOneOfSpeedOptionsDef1,
                OneOfSpeedOptionsDef2,
                OneOfSpeedOptionsDef3,
            ]
        ]
        tcp_mss: Optional[
            Union[
                InterfaceEthernetOneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]


    class ManagementVpnInterfaceEthernetData:
        # Advanced Attributes
        advanced: InterfaceEthernetAdvanced
        interface_name: Union[
            OneOfInterfaceNameOptionsDef1, OneOfInterfaceNameOptionsDef2
        ]
        intf_ip_address: Union[
            InterfaceEthernetIntfIpAddress1,
            InterfaceEthernetIntfIpAddress2,
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        # Configure ARP entries
        arp: Optional[List[InterfaceEthernetArp]]
        auto_detect_bandwidth: Optional[
            Union[
                OneOfAutoBandwidthDetectOptionsDef1,
                OneOfAutoBandwidthDetectOptionsDef2,
                OneOfAutoBandwidthDetectOptionsDef3,
            ]
        ]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                InterfaceEthernetOneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        intf_ip_v6_address: Optional[
            Union[IntfIpV6Address1, IntfIpV6Address2]
        ]
        iperf_server: Optional[
            Union[
                InterfaceEthernetOneOfIperfServerOptionsDef1,
                OneOfIperfServerOptionsDef2,
                OneOfIperfServerOptionsDef3,
            ]
        ]


    class EditManagementVpnInterfaceEthernetParcelForTransportPutRequest:
        """
        Management VPN Interface Ethernet profile parcel schema for PUT request
        """

        data: ManagementVpnInterfaceEthernetData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


