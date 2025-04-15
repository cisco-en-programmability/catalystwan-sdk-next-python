======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

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

    DuplexDef = Literal["auto", "full", "half"]

    SpeedDef = Literal["10", "100", "1000", "10000", "2500"]

    MediaTypeDef = Literal["auto-select", "rj45", "sfp"]


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
        value: bool


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


    class OneOfIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfIpV4AddressOptionsDef3:
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
            OneOfIpV4AddressOptionsDef1,
            OneOfIpV4AddressOptionsDef2,
            OneOfIpV4AddressOptionsDef3,
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
        value: List[Any]


    class OneOfListOfIpV4OptionsDef3:
        option_type: DefaultOptionTypeDef


    class DhcpClient:
        """
        Enable DHCPv6
        """

        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfIpv6PrefixGlobalVariableWithoutDefault1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6PrefixGlobalVariableWithoutDefault2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class SecondaryIpV6Address:
        address: Union[
            OneOfIpv6PrefixGlobalVariableWithoutDefault1,
            OneOfIpv6PrefixGlobalVariableWithoutDefault2,
        ]


    class EthernetDynamic:
        # Enable DHCPv6
        dhcp_client: DhcpClient
        # secondary IPv6 addresses
        secondary_ip_v6_address: Optional[List[SecondaryIpV6Address]]


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
        # Static secondary IPv6 addresses
        secondary_ip_v6_address: Optional[List[SecondaryIpV6Address]]


    class IntfIpV6Address2:
        static: EthernetStatic


    class OneOfControlConnectionOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfControlConnectionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfControlConnectionOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfBindInterfaceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBindInterfaceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfBindInterfaceOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfControlConnectionPreferenceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfControlConnectionPreferenceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfControlConnectionPreferenceOptionsDef3:
        option_type: DefaultOptionTypeDef


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class ParcelReferenceDef:
        ref_id: RefId


    class Acl:
        """
        ACL
        """

        ipv4_acl_egress: Optional[ParcelReferenceDef]
        ipv4_acl_ingress: Optional[ParcelReferenceDef]


    class OneOfMacAddressOptionsNoDefaultDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfMacAddressOptionsNoDefaultDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Arp:
        ip_address: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]
        mac_address: Union[
            OneOfMacAddressOptionsNoDefaultDef1,
            OneOfMacAddressOptionsNoDefaultDef2,
        ]


    class OneOfEnableBfdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfEnableBfdOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfEnableBfdOptionsDef3:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTransmitIntervalOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTransmitIntervalOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTransmitIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfMinRecvIntervalOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMinRecvIntervalOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMinRecvIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfMultiplierOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMultiplierOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMultiplierOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Bfd:
        """
        Configure BFD
        """

        min_recv_interval: Optional[
            Union[
                OneOfMinRecvIntervalOptionsDef1,
                OneOfMinRecvIntervalOptionsDef2,
                OneOfMinRecvIntervalOptionsDef3,
            ]
        ]
        multiplier: Optional[
            Union[
                OneOfMultiplierOptionsDef1,
                OneOfMultiplierOptionsDef2,
                OneOfMultiplierOptionsDef3,
            ]
        ]
        transmit_interval: Optional[
            Union[
                OneOfTransmitIntervalOptionsDef1,
                OneOfTransmitIntervalOptionsDef2,
                OneOfTransmitIntervalOptionsDef3,
            ]
        ]


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


    class OneOfMacAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfMacAddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMacAddressOptionsDef3:
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
        value: int


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


    class OneOfTrackerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTrackerOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerOptionsDef3:
        option_type: DefaultOptionTypeDef


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
        value: bool


    class Advanced:
        """
        Advanced Attributes
        """

        arp_timeout: Optional[
            Union[
                OneOfArpTimeoutOptionsDef1,
                OneOfArpTimeoutOptionsDef2,
                OneOfArpTimeoutOptionsDef3,
            ]
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
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        intrf_mtu: Optional[
            Union[
                OneOfIntrfMtuOptionsDef1,
                OneOfIntrfMtuOptionsDef2,
                OneOfIntrfMtuOptionsDef3,
            ]
        ]
        ip_directed_broadcast: Optional[
            Union[
                OneOfIpDirectedBroadcastOptionsDef1,
                OneOfIpDirectedBroadcastOptionsDef2,
                OneOfIpDirectedBroadcastOptionsDef3,
            ]
        ]
        ip_mtu: Optional[
            Union[
                OneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                OneOfMtuOptionsDef3,
            ]
        ]
        load_interval: Optional[
            Union[
                OneOfLoadIntervalOptionsDef1,
                OneOfLoadIntervalOptionsDef2,
                OneOfLoadIntervalOptionsDef3,
            ]
        ]
        mac_address: Optional[
            Union[
                OneOfMacAddressOptionsDef1,
                OneOfMacAddressOptionsDef2,
                OneOfMacAddressOptionsDef3,
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
        tracker: Optional[
            Union[
                OneOfTrackerOptionsDef1,
                OneOfTrackerOptionsDef2,
                OneOfTrackerOptionsDef3,
            ]
        ]


    class EthernetData:
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        interface_name: Union[
            OneOfInterfaceNameOptionsDef1, OneOfInterfaceNameOptionsDef2
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        # ACL
        acl: Optional[Acl]
        # Advanced Attributes
        advanced: Optional[Advanced]
        # Configure ARP entries
        arp: Optional[List[Arp]]
        # Configure BFD
        bfd: Optional[Bfd]
        bind_interface: Optional[
            Union[
                OneOfBindInterfaceOptionsDef1,
                OneOfBindInterfaceOptionsDef2,
                OneOfBindInterfaceOptionsDef3,
            ]
        ]
        control_connection: Optional[
            Union[
                OneOfControlConnectionOptionsDef1,
                OneOfControlConnectionOptionsDef2,
                OneOfControlConnectionOptionsDef3,
            ]
        ]
        control_connection_preference: Optional[
            Union[
                OneOfControlConnectionPreferenceOptionsDef1,
                OneOfControlConnectionPreferenceOptionsDef2,
                OneOfControlConnectionPreferenceOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                OneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        enable_bfd: Optional[
            Union[
                OneOfEnableBfdOptionsDef1,
                OneOfEnableBfdOptionsDef2,
                OneOfEnableBfdOptionsDef3,
            ]
        ]
        intf_ip_address: Optional[Union[IntfIpAddress1, IntfIpAddress2]]
        intf_ip_v6_address: Optional[
            Union[IntfIpV6Address1, IntfIpV6Address2]
        ]


    class Payload:
        """
        SD-Routing WAN Interface ethernet feature schema
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
        # SD-Routing WAN Interface ethernet feature schema
        payload: Optional[Payload]


    class GetListSdRoutingTransportVrfWanInterfaceEthernetPayload:
        data: Optional[List[Data]]


    class CreateSdroutingTransportVrfInterfaceEthernetParcelForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class InterfaceEthernetData:
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        interface_name: Union[
            OneOfInterfaceNameOptionsDef1, OneOfInterfaceNameOptionsDef2
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        # ACL
        acl: Optional[Acl]
        # Advanced Attributes
        advanced: Optional[Advanced]
        # Configure ARP entries
        arp: Optional[List[Arp]]
        # Configure BFD
        bfd: Optional[Bfd]
        bind_interface: Optional[
            Union[
                OneOfBindInterfaceOptionsDef1,
                OneOfBindInterfaceOptionsDef2,
                OneOfBindInterfaceOptionsDef3,
            ]
        ]
        control_connection: Optional[
            Union[
                OneOfControlConnectionOptionsDef1,
                OneOfControlConnectionOptionsDef2,
                OneOfControlConnectionOptionsDef3,
            ]
        ]
        control_connection_preference: Optional[
            Union[
                OneOfControlConnectionPreferenceOptionsDef1,
                OneOfControlConnectionPreferenceOptionsDef2,
                OneOfControlConnectionPreferenceOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                OneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        enable_bfd: Optional[
            Union[
                OneOfEnableBfdOptionsDef1,
                OneOfEnableBfdOptionsDef2,
                OneOfEnableBfdOptionsDef3,
            ]
        ]
        intf_ip_address: Optional[Union[IntfIpAddress1, IntfIpAddress2]]
        intf_ip_v6_address: Optional[
            Union[IntfIpV6Address1, IntfIpV6Address2]
        ]


    class CreateSdroutingTransportVrfInterfaceEthernetParcelForTransportPostRequest:
        """
        SD-Routing WAN Interface ethernet feature schema
        """

        data: InterfaceEthernetData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingTransportVrfWanInterfaceEthernetPayload:
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
        # SD-Routing WAN Interface ethernet feature schema
        payload: Optional[Payload]


    class EditSdroutingTransportVrfInterfaceEthernetParcelForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class VrfInterfaceEthernetData:
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        interface_name: Union[
            OneOfInterfaceNameOptionsDef1, OneOfInterfaceNameOptionsDef2
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        # ACL
        acl: Optional[Acl]
        # Advanced Attributes
        advanced: Optional[Advanced]
        # Configure ARP entries
        arp: Optional[List[Arp]]
        # Configure BFD
        bfd: Optional[Bfd]
        bind_interface: Optional[
            Union[
                OneOfBindInterfaceOptionsDef1,
                OneOfBindInterfaceOptionsDef2,
                OneOfBindInterfaceOptionsDef3,
            ]
        ]
        control_connection: Optional[
            Union[
                OneOfControlConnectionOptionsDef1,
                OneOfControlConnectionOptionsDef2,
                OneOfControlConnectionOptionsDef3,
            ]
        ]
        control_connection_preference: Optional[
            Union[
                OneOfControlConnectionPreferenceOptionsDef1,
                OneOfControlConnectionPreferenceOptionsDef2,
                OneOfControlConnectionPreferenceOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                OneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        enable_bfd: Optional[
            Union[
                OneOfEnableBfdOptionsDef1,
                OneOfEnableBfdOptionsDef2,
                OneOfEnableBfdOptionsDef3,
            ]
        ]
        intf_ip_address: Optional[Union[IntfIpAddress1, IntfIpAddress2]]
        intf_ip_v6_address: Optional[
            Union[IntfIpV6Address1, IntfIpV6Address2]
        ]


    class EditSdroutingTransportVrfInterfaceEthernetParcelForTransportPutRequest:
        """
        SD-Routing WAN Interface ethernet feature schema
        """

        data: VrfInterfaceEthernetData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


