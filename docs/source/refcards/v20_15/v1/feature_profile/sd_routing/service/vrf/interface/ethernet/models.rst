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

    NetworkRedundancyDef = Literal["hsrp", "off", "vrrp"]

    DefaultNetworkRedundancyDef = Literal["off"]

    TrackerActionDef = Literal["Decrement", "Shutdown"]

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
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


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
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


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
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


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


    class OneOfNetworkRedundancyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: NetworkRedundancyDef


    class OneOfNetworkRedundancyOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: DefaultNetworkRedundancyDef  # pytype: disable=annotation-type-mismatch


    class OneOfGroupIdOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfGroupIdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVrrpPriorityOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVrrpPriorityOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVrrpPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfVrrpTimerOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVrrpTimerOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVrrpTimerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class IpAddressSecondary:
        ip_address: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsWithoutDefault1,
            OneOfIpV4SubnetMaskOptionsWithoutDefault2,
        ]


    class OneOfMinPreemptDelayOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMinPreemptDelayOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMinPreemptDelayOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfTrackerActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            TrackerActionDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfDecrementValueOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDecrementValueOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class TrackingObject:
        tracker_action: OneOfTrackerActionOptionsDef
        tracker_id: ParcelReferenceDef
        decrement_value: Optional[
            Union[
                OneOfDecrementValueOptionsDef1,
                OneOfDecrementValueOptionsDef2,
            ]
        ]


    class Vrrp:
        """
        Enable VRRP
        """

        group_id: Union[OneOfGroupIdOptionsDef1, OneOfGroupIdOptionsDef2]
        ip_address: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]
        priority: Union[
            OneOfVrrpPriorityOptionsDef1,
            OneOfVrrpPriorityOptionsDef2,
            OneOfVrrpPriorityOptionsDef3,
        ]
        timer: Union[
            OneOfVrrpTimerOptionsDef1,
            OneOfVrrpTimerOptionsDef2,
            OneOfVrrpTimerOptionsDef3,
        ]
        # VRRP Secondary Ip Addresses
        ip_address_secondary: Optional[List[IpAddressSecondary]]
        min_preempt_delay: Optional[
            Union[
                OneOfMinPreemptDelayOptionsDef1,
                OneOfMinPreemptDelayOptionsDef2,
                OneOfMinPreemptDelayOptionsDef3,
            ]
        ]
        # Tracking object for VRRP configuration
        tracking_object: Optional[List[TrackingObject]]


    class OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfIpv6VrrpIpv6PrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6VrrpIpv6PrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6VrrpIpv6PrefixOptionsDef3:
        option_type: DefaultOptionTypeDef


    class VrrpIpv6:
        """
        Enable VRRP Ipv6
        """

        group_id: Union[OneOfGroupIdOptionsDef1, OneOfGroupIdOptionsDef2]
        ipv6_link_local: Union[
            OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef1,
            OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef2,
            OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef3,
        ]
        priority: Union[
            OneOfVrrpPriorityOptionsDef1,
            OneOfVrrpPriorityOptionsDef2,
            OneOfVrrpPriorityOptionsDef3,
        ]
        timer: Union[
            OneOfVrrpTimerOptionsDef1,
            OneOfVrrpTimerOptionsDef2,
            OneOfVrrpTimerOptionsDef3,
        ]
        ipv6_prefix: Optional[
            Union[
                OneOfIpv6VrrpIpv6PrefixOptionsDef1,
                OneOfIpv6VrrpIpv6PrefixOptionsDef2,
                OneOfIpv6VrrpIpv6PrefixOptionsDef3,
            ]
        ]
        min_preempt_delay: Optional[
            Union[
                OneOfMinPreemptDelayOptionsDef1,
                OneOfMinPreemptDelayOptionsDef2,
                OneOfMinPreemptDelayOptionsDef3,
            ]
        ]


    class OneOfHsrpPriorityOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHsrpPriorityOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHsrpPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfHsrpHelloTimerOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHsrpHelloTimerOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHsrpHelloTimerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfHsrpHoldTimerOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHsrpHoldTimerOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHsrpHoldTimerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfHsrpReloadPreemptDelayOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHsrpReloadPreemptDelayOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHsrpReloadPreemptDelayOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfHsrpMd5AuthKeyOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHsrpMd5AuthKeyOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfHsrpMd5AuthKeyOptionsDef3:
        option_type: DefaultOptionTypeDef


    class SecondaryAddress:
        address: Optional[
            Union[
                OneOfIpV4AddressOptionsWithoutDefault1,
                OneOfIpV4AddressOptionsWithoutDefault2,
            ]
        ]


    class Hsrp:
        """
        Enable HSRP
        """

        group_id: Union[OneOfGroupIdOptionsDef1, OneOfGroupIdOptionsDef2]
        ip_address: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]
        priority: Union[
            OneOfHsrpPriorityOptionsDef1,
            OneOfHsrpPriorityOptionsDef2,
            OneOfHsrpPriorityOptionsDef3,
        ]
        hello_timer: Optional[
            Union[
                OneOfHsrpHelloTimerOptionsDef1,
                OneOfHsrpHelloTimerOptionsDef2,
                OneOfHsrpHelloTimerOptionsDef3,
            ]
        ]
        hold_timer: Optional[
            Union[
                OneOfHsrpHoldTimerOptionsDef1,
                OneOfHsrpHoldTimerOptionsDef2,
                OneOfHsrpHoldTimerOptionsDef3,
            ]
        ]
        md5_auth_key: Optional[
            Union[
                OneOfHsrpMd5AuthKeyOptionsDef1,
                OneOfHsrpMd5AuthKeyOptionsDef2,
                OneOfHsrpMd5AuthKeyOptionsDef3,
            ]
        ]
        min_preempt_delay: Optional[
            Union[
                OneOfMinPreemptDelayOptionsDef1,
                OneOfMinPreemptDelayOptionsDef2,
                OneOfMinPreemptDelayOptionsDef3,
            ]
        ]
        reload_preempt_delay: Optional[
            Union[
                OneOfHsrpReloadPreemptDelayOptionsDef1,
                OneOfHsrpReloadPreemptDelayOptionsDef2,
                OneOfHsrpReloadPreemptDelayOptionsDef3,
            ]
        ]
        # HSRP Secondary Ip Address
        secondary_address: Optional[List[SecondaryAddress]]
        # Tracking object for HSRP configuration
        tracking_object: Optional[List[TrackingObject]]


    class OneOfIpv6HsrpIpv6AutoConfigOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfIpv6HsrpIpv6AutoConfigOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6HsrpIpv6AutoConfigOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class HsrpIpv6:
        """
        Enable HSRP Ipv6
        """

        autoconfig: Union[
            OneOfIpv6HsrpIpv6AutoConfigOptionsDef1,
            OneOfIpv6HsrpIpv6AutoConfigOptionsDef2,
            OneOfIpv6HsrpIpv6AutoConfigOptionsDef3,
        ]
        group_id: Union[OneOfGroupIdOptionsDef1, OneOfGroupIdOptionsDef2]
        priority: Union[
            OneOfHsrpPriorityOptionsDef1,
            OneOfHsrpPriorityOptionsDef2,
            OneOfHsrpPriorityOptionsDef3,
        ]
        hello_timer: Optional[
            Union[
                OneOfHsrpHelloTimerOptionsDef1,
                OneOfHsrpHelloTimerOptionsDef2,
                OneOfHsrpHelloTimerOptionsDef3,
            ]
        ]
        hold_timer: Optional[
            Union[
                OneOfHsrpHoldTimerOptionsDef1,
                OneOfHsrpHoldTimerOptionsDef2,
                OneOfHsrpHoldTimerOptionsDef3,
            ]
        ]
        ipv6_link_local: Optional[
            Union[
                OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef1,
                OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef2,
                OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef3,
            ]
        ]
        ipv6_prefix: Optional[
            Union[
                OneOfIpv6VrrpIpv6PrefixOptionsDef1,
                OneOfIpv6VrrpIpv6PrefixOptionsDef2,
                OneOfIpv6VrrpIpv6PrefixOptionsDef3,
            ]
        ]
        md5_auth_key: Optional[
            Union[
                OneOfHsrpMd5AuthKeyOptionsDef1,
                OneOfHsrpMd5AuthKeyOptionsDef2,
                OneOfHsrpMd5AuthKeyOptionsDef3,
            ]
        ]
        min_preempt_delay: Optional[
            Union[
                OneOfMinPreemptDelayOptionsDef1,
                OneOfMinPreemptDelayOptionsDef2,
                OneOfMinPreemptDelayOptionsDef3,
            ]
        ]
        reload_preempt_delay: Optional[
            Union[
                OneOfHsrpReloadPreemptDelayOptionsDef1,
                OneOfHsrpReloadPreemptDelayOptionsDef2,
                OneOfHsrpReloadPreemptDelayOptionsDef3,
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
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


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
        # Enable HSRP
        hsrp: Optional[Hsrp]
        # Enable HSRP Ipv6
        hsrp_ipv6: Optional[HsrpIpv6]
        intf_ip_address: Optional[Union[IntfIpAddress1, IntfIpAddress2]]
        intf_ip_v6_address: Optional[
            Union[IntfIpV6Address1, IntfIpV6Address2]
        ]
        network_redundancy: Optional[
            Union[
                OneOfNetworkRedundancyOptionsDef1,
                OneOfNetworkRedundancyOptionsDef2,
            ]
        ]
        # Enable VRRP
        vrrp: Optional[Vrrp]
        # Enable VRRP Ipv6
        vrrp_ipv6: Optional[VrrpIpv6]


    class Payload:
        """
        SD-Routing Service LAN Interface Ethernet feature schema for request
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
        # SD-Routing Service LAN Interface Ethernet feature schema for request
        payload: Optional[Payload]


    class GetListSdRoutingServiceVrfLanInterfaceEthernetPayload:
        data: Optional[List[Data]]


    class CreateSdroutingServiceVrfInterfaceEthernetParcelForServicePostResponse:
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
        # Enable HSRP
        hsrp: Optional[Hsrp]
        # Enable HSRP Ipv6
        hsrp_ipv6: Optional[HsrpIpv6]
        intf_ip_address: Optional[Union[IntfIpAddress1, IntfIpAddress2]]
        intf_ip_v6_address: Optional[
            Union[IntfIpV6Address1, IntfIpV6Address2]
        ]
        network_redundancy: Optional[
            Union[
                OneOfNetworkRedundancyOptionsDef1,
                OneOfNetworkRedundancyOptionsDef2,
            ]
        ]
        # Enable VRRP
        vrrp: Optional[Vrrp]
        # Enable VRRP Ipv6
        vrrp_ipv6: Optional[VrrpIpv6]


    class CreateSdroutingServiceVrfInterfaceEthernetParcelForServicePostRequest:
        """
        SD-Routing Service LAN Interface Ethernet feature schema for request
        """

        data: InterfaceEthernetData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingServiceVrfLanInterfaceEthernetPayload:
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
        # SD-Routing Service LAN Interface Ethernet feature schema for request
        payload: Optional[Payload]


    class EditSdroutingServiceVrfInterfaceEthernetParcelForServicePutResponse:
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
        # Enable HSRP
        hsrp: Optional[Hsrp]
        # Enable HSRP Ipv6
        hsrp_ipv6: Optional[HsrpIpv6]
        intf_ip_address: Optional[Union[IntfIpAddress1, IntfIpAddress2]]
        intf_ip_v6_address: Optional[
            Union[IntfIpV6Address1, IntfIpV6Address2]
        ]
        network_redundancy: Optional[
            Union[
                OneOfNetworkRedundancyOptionsDef1,
                OneOfNetworkRedundancyOptionsDef2,
            ]
        ]
        # Enable VRRP
        vrrp: Optional[Vrrp]
        # Enable VRRP Ipv6
        vrrp_ipv6: Optional[VrrpIpv6]


    class EditSdroutingServiceVrfInterfaceEthernetParcelForServicePutRequest:
        """
        SD-Routing Service LAN Interface Ethernet feature schema for request
        """

        data: VrfInterfaceEthernetData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


