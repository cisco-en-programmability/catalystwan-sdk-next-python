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

    Ipv4VrrpTrackingObjectTrackActionDef = Literal[
        "decrement", "shutdown"
    ]

    DefaultIpv4VrrpTimerDef = Literal[100, 1000]

    SviIpv4VrrpTrackingObjectTrackActionDef = Literal[
        "decrement", "shutdown"
    ]

    InterfaceSviIpv4VrrpTrackingObjectTrackActionDef = Literal[
        "decrement", "shutdown"
    ]

    DefaultIpv6VrrpTimerDef = Literal[100, 1000]

    VpnInterfaceSviIpv4VrrpTrackingObjectTrackActionDef = Literal[
        "decrement", "shutdown"
    ]

    LanVpnInterfaceSviIpv4VrrpTrackingObjectTrackActionDef = Literal[
        "decrement", "shutdown"
    ]


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


    class OneOfIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIfNameOptionsDef2:
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


    class OneOfIfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIfMtuOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


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


    class AddressV4:
        """
        IpV4Address Primary
        """

        ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class SecondaryAddressV4:
        ip_address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        subnet_mask: Union[
            OneOfIpV4SubnetMaskOptionsDef1, OneOfIpV4SubnetMaskOptionsDef2
        ]


    class OneOfDhcpHelperV4OptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfDhcpHelperV4OptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDhcpHelperV4OptionsDef3:
        option_type: DefaultOptionTypeDef


    class Ipv4:
        """
        ipv4 Attributes
        """

        # IpV4Address Primary
        address_v4: AddressV4
        dhcp_helper_v4: Optional[
            Union[
                OneOfDhcpHelperV4OptionsDef1,
                OneOfDhcpHelperV4OptionsDef2,
                OneOfDhcpHelperV4OptionsDef3,
            ]
        ]
        # Assign secondary IP addresses
        secondary_address_v4: Optional[List[SecondaryAddressV4]]


    class OneOfAddressV6OptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAddressV6OptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAddressV6OptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfSecondaryAddressV6AddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSecondaryAddressV6AddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSecondaryAddressV6AddressOptionsDef3:
        option_type: DefaultOptionTypeDef


    class SecondaryAddressV6:
        address: Union[
            OneOfSecondaryAddressV6AddressOptionsDef1,
            OneOfSecondaryAddressV6AddressOptionsDef2,
            OneOfSecondaryAddressV6AddressOptionsDef3,
        ]


    class OneOfDhcpHelperV6AddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDhcpHelperV6AddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDhcpHelperV6VpnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDhcpHelperV6VpnOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDhcpHelperV6VpnOptionsDef3:
        option_type: DefaultOptionTypeDef


    class DhcpHelperV6:
        address: Union[
            OneOfDhcpHelperV6AddressOptionsDef1,
            OneOfDhcpHelperV6AddressOptionsDef2,
        ]
        vpn: Optional[
            Union[
                OneOfDhcpHelperV6VpnOptionsDef1,
                OneOfDhcpHelperV6VpnOptionsDef2,
                OneOfDhcpHelperV6VpnOptionsDef3,
            ]
        ]


    class Ipv6:
        """
        Advanced Attributes
        """

        address_v6: Optional[
            Union[
                OneOfAddressV6OptionsDef1,
                OneOfAddressV6OptionsDef2,
                OneOfAddressV6OptionsDef3,
            ]
        ]
        # DHCPv6 Helper
        dhcp_helper_v6: Optional[List[DhcpHelperV6]]
        # Assign secondary IPv6 addresses
        secondary_address_v6: Optional[List[SecondaryAddressV6]]


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class ParcelReferenceDef:
        ref_id: RefId


    class AclQos:
        """
        ACL
        """

        ipv4_acl_egress: Optional[ParcelReferenceDef]
        ipv4_acl_ingress: Optional[ParcelReferenceDef]
        ipv6_acl_egress: Optional[ParcelReferenceDef]
        ipv6_acl_ingress: Optional[ParcelReferenceDef]


    class OneOfArpAddrOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfArpAddrOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfArpMacOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfArpMacOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Arp:
        ip_address: Union[
            OneOfArpAddrOptionsDef1, OneOfArpAddrOptionsDef2
        ]
        mac_address: Union[OneOfArpMacOptionsDef1, OneOfArpMacOptionsDef2]


    class OneOfIpv4VrrpGrpIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv4VrrpGrpIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv4VrrpPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv4VrrpPriorityOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv4VrrpPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIpv4VrrpTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv4VrrpTimerOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv4VrrpTimerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIpv4VrrpTrackOmpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfIpv4VrrpTrackOmpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv4VrrpTrackOmpOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfIpv4VrrpTrackPrefixListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv4VrrpTrackPrefixListOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv4VrrpTrackPrefixListOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfIpV4AddressOptionsWithoutDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsWithoutDefault2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfIpv4VrrpIpv4SecondaryAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfIpv4VrrpIpv4SecondaryAddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class IpAddressSecondary:
        address: Union[
            OneOfIpv4VrrpIpv4SecondaryAddressOptionsDef1,
            OneOfIpv4VrrpIpv4SecondaryAddressOptionsDef2,
        ]


    class OneOfIpv4VrrpTlocChangePrefOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfIpv4VrrpTlocChangePrefOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class TlocPrefChangeValue:
        value: Optional[Any]


    class OneOfIpv4VrrpTrackingObjectNameOptionsDef1:
        option_type: DefaultOptionTypeDef


    class OneOfIpv4VrrpTrackingObjectNameOptionsDef2:
        ref_id: RefId


    class OneOfIpv4VrrpTrackingObjectTrackActionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Ipv4VrrpTrackingObjectTrackActionDef


    class OneOfIpv4VrrpTrackingObjectTrackActionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv4VrrpTrackingObjectDecrementOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv4VrrpTrackingObjectDecrementOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class TrackingObject:
        track_action: Union[
            OneOfIpv4VrrpTrackingObjectTrackActionOptionsDef1,
            OneOfIpv4VrrpTrackingObjectTrackActionOptionsDef2,
        ]
        tracker_id: Union[
            OneOfIpv4VrrpTrackingObjectNameOptionsDef1,
            OneOfIpv4VrrpTrackingObjectNameOptionsDef2,
        ]
        decrement_value: Optional[
            Union[
                OneOfIpv4VrrpTrackingObjectDecrementOptionsDef1,
                OneOfIpv4VrrpTrackingObjectDecrementOptionsDef2,
            ]
        ]


    class OneOfOnBooleanDefaultTrueNoVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultTrueNoVariableOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class Vrrp1:
        group_id: Union[
            OneOfIpv4VrrpGrpIdOptionsDef1, OneOfIpv4VrrpGrpIdOptionsDef2
        ]
        ip_address: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]
        priority: Union[
            OneOfIpv4VrrpPriorityOptionsDef1,
            OneOfIpv4VrrpPriorityOptionsDef2,
            OneOfIpv4VrrpPriorityOptionsDef3,
        ]
        timer: Union[
            OneOfIpv4VrrpTimerOptionsDef1,
            OneOfIpv4VrrpTimerOptionsDef2,
            OneOfIpv4VrrpTimerOptionsDef3,
        ]
        tloc_pref_change: Union[
            OneOfIpv4VrrpTlocChangePrefOptionsDef1,
            OneOfIpv4VrrpTlocChangePrefOptionsDef2,
        ]
        track_omp: Union[
            OneOfIpv4VrrpTrackOmpOptionsDef1,
            OneOfIpv4VrrpTrackOmpOptionsDef2,
            OneOfIpv4VrrpTrackOmpOptionsDef3,
        ]
        follow_dual_router_ha_availability: Optional[
            Union[
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef1,
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef2,
            ]
        ]
        # VRRP Secondary IPV4 address
        ip_address_secondary: Optional[List[IpAddressSecondary]]
        prefix_list: Optional[
            Union[
                OneOfIpv4VrrpTrackPrefixListOptionsDef1,
                OneOfIpv4VrrpTrackPrefixListOptionsDef2,
                OneOfIpv4VrrpTrackPrefixListOptionsDef3,
            ]
        ]
        tloc_pref_change_value: Optional[TlocPrefChangeValue]
        # tracking object for VRRP configuration
        tracking_object: Optional[List[TrackingObject]]


    class OneOfIpv4VrrpValueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv4VrrpValueOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Vrrp2:
        group_id: Union[
            OneOfIpv4VrrpGrpIdOptionsDef1, OneOfIpv4VrrpGrpIdOptionsDef2
        ]
        ip_address: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]
        priority: Union[
            OneOfIpv4VrrpPriorityOptionsDef1,
            OneOfIpv4VrrpPriorityOptionsDef2,
            OneOfIpv4VrrpPriorityOptionsDef3,
        ]
        timer: Union[
            OneOfIpv4VrrpTimerOptionsDef1,
            OneOfIpv4VrrpTimerOptionsDef2,
            OneOfIpv4VrrpTimerOptionsDef3,
        ]
        tloc_pref_change: Union[
            OneOfIpv4VrrpTlocChangePrefOptionsDef1,
            OneOfIpv4VrrpTlocChangePrefOptionsDef2,
        ]
        track_omp: Union[
            OneOfIpv4VrrpTrackOmpOptionsDef1,
            OneOfIpv4VrrpTrackOmpOptionsDef2,
            OneOfIpv4VrrpTrackOmpOptionsDef3,
        ]
        follow_dual_router_ha_availability: Optional[
            Union[
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef1,
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef2,
            ]
        ]
        # VRRP Secondary IPV4 address
        ip_address_secondary: Optional[List[IpAddressSecondary]]
        prefix_list: Optional[
            Union[
                OneOfIpv4VrrpTrackPrefixListOptionsDef1,
                OneOfIpv4VrrpTrackPrefixListOptionsDef2,
                OneOfIpv4VrrpTrackPrefixListOptionsDef3,
            ]
        ]
        tloc_pref_change_value: Optional[
            Union[
                OneOfIpv4VrrpValueOptionsDef1,
                OneOfIpv4VrrpValueOptionsDef2,
            ]
        ]
        # tracking object for VRRP configuration
        tracking_object: Optional[List[TrackingObject]]


    class OneOfIpv6VrrpGrpIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv6VrrpGrpIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6VrrpPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv6VrrpPriorityOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6VrrpPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIpv6VrrpTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIpv6VrrpTimerOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6VrrpTimerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIpv6VrrpTrackOmpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfIpv6VrrpTrackOmpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6VrrpTrackOmpOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfIpv6VrrpTrackPrefixListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6VrrpTrackPrefixListOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpv6VrrpTrackPrefixListOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


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


    class SviIpv6:
        ipv6_link_local: Union[
            OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef1,
            OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef2,
        ]
        prefix: Optional[
            Union[
                OneOfIpv6VrrpIpv6PrefixOptionsDef1,
                OneOfIpv6VrrpIpv6PrefixOptionsDef2,
                OneOfIpv6VrrpIpv6PrefixOptionsDef3,
            ]
        ]


    class OneOfIpv6VrrpIpv6SecondaryPrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6VrrpIpv6SecondaryPrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Ipv6Secondary:
        prefix: Union[
            OneOfIpv6VrrpIpv6SecondaryPrefixOptionsDef1,
            OneOfIpv6VrrpIpv6SecondaryPrefixOptionsDef2,
        ]


    class VrrpIpv6:
        group_id: Union[
            OneOfIpv6VrrpGrpIdOptionsDef1, OneOfIpv6VrrpGrpIdOptionsDef2
        ]
        # IPv6 VRRP
        ipv6: List[SviIpv6]
        priority: Union[
            OneOfIpv6VrrpPriorityOptionsDef1,
            OneOfIpv6VrrpPriorityOptionsDef2,
            OneOfIpv6VrrpPriorityOptionsDef3,
        ]
        timer: Union[
            OneOfIpv6VrrpTimerOptionsDef1,
            OneOfIpv6VrrpTimerOptionsDef2,
            OneOfIpv6VrrpTimerOptionsDef3,
        ]
        track_omp: Union[
            OneOfIpv6VrrpTrackOmpOptionsDef1,
            OneOfIpv6VrrpTrackOmpOptionsDef2,
            OneOfIpv6VrrpTrackOmpOptionsDef3,
        ]
        follow_dual_router_ha_availability: Optional[
            Union[
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef1,
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef2,
            ]
        ]
        # IPv6 Secondary IP address
        ipv6_secondary: Optional[List[Ipv6Secondary]]
        track_prefix_list: Optional[
            Union[
                OneOfIpv6VrrpTrackPrefixListOptionsDef1,
                OneOfIpv6VrrpTrackPrefixListOptionsDef2,
                OneOfIpv6VrrpTrackPrefixListOptionsDef3,
            ]
        ]


    class OneOfDhcpClientV6OptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfDhcpClientV6OptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDhcpClientV6OptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfTcpMssOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTcpMssOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTcpMssOptionsDef3:
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
        icmp_redirect_disable: Optional[
            Union[
                OneOfIcmpRedirectDisableOptionsDef1,
                OneOfIcmpRedirectDisableOptionsDef2,
                OneOfIcmpRedirectDisableOptionsDef3,
            ]
        ]
        tcp_mss: Optional[
            Union[
                OneOfTcpMssOptionsDef1,
                OneOfTcpMssOptionsDef2,
                OneOfTcpMssOptionsDef3,
            ]
        ]


    class SviData:
        # Advanced Attributes
        advanced: Advanced
        interface_name: Union[
            OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        # ACL
        acl_qos: Optional[AclQos]
        # Configure static ARP entries
        arp: Optional[List[Arp]]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]
        dhcp_client_v6: Optional[
            Union[
                OneOfDhcpClientV6OptionsDef1,
                OneOfDhcpClientV6OptionsDef2,
                OneOfDhcpClientV6OptionsDef3,
            ]
        ]
        if_mtu: Optional[
            Union[
                OneOfIfMtuOptionsDef1,
                OneOfIfMtuOptionsDef2,
                OneOfIfMtuOptionsDef3,
            ]
        ]
        ip_mtu: Optional[
            Union[
                OneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                OneOfMtuOptionsDef3,
            ]
        ]
        # ipv4 Attributes
        ipv4: Optional[Ipv4]
        # Advanced Attributes
        ipv6: Optional[Ipv6]
        # Enable ipv4 VRRP
        vrrp: Optional[List[Union[Vrrp1, Vrrp2]]]
        # Enable ipv6 VRRP
        vrrp_ipv6: Optional[List[VrrpIpv6]]


    class Payload:
        """
        LAN VPN Interface SVI profile parcel schema for POST request
        """

        data: SviData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


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
        # LAN VPN Interface SVI profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanServiceLanVpnInterfaceSviPayload:
        data: Optional[List[Data]]


    class CreateLanVpnInterfaceSviParcelForServicePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class InterfaceSviData:
        # Advanced Attributes
        advanced: Advanced
        interface_name: Union[
            OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        # ACL
        acl_qos: Optional[AclQos]
        # Configure static ARP entries
        arp: Optional[List[Arp]]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]
        dhcp_client_v6: Optional[
            Union[
                OneOfDhcpClientV6OptionsDef1,
                OneOfDhcpClientV6OptionsDef2,
                OneOfDhcpClientV6OptionsDef3,
            ]
        ]
        if_mtu: Optional[
            Union[
                OneOfIfMtuOptionsDef1,
                OneOfIfMtuOptionsDef2,
                OneOfIfMtuOptionsDef3,
            ]
        ]
        ip_mtu: Optional[
            Union[
                OneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                OneOfMtuOptionsDef3,
            ]
        ]
        # ipv4 Attributes
        ipv4: Optional[Ipv4]
        # Advanced Attributes
        ipv6: Optional[Ipv6]
        # Enable ipv4 VRRP
        vrrp: Optional[List[Union[Vrrp1, Vrrp2]]]
        # Enable ipv6 VRRP
        vrrp_ipv6: Optional[List[VrrpIpv6]]


    class CreateLanVpnInterfaceSviParcelForServicePostRequest:
        """
        LAN VPN Interface SVI profile parcel schema for POST request
        """

        data: InterfaceSviData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class SviOneOfIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SviOneOfDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SviOneOfIfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SviOneOfIfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SviOneOfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SviOneOfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SviOneOfDhcpHelperV4OptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class SviIpv4:
        """
        ipv4 Attributes
        """

        # IpV4Address Primary
        address_v4: AddressV4
        dhcp_helper_v4: Optional[
            Union[
                SviOneOfDhcpHelperV4OptionsDef1,
                OneOfDhcpHelperV4OptionsDef2,
                OneOfDhcpHelperV4OptionsDef3,
            ]
        ]
        # Assign secondary IP addresses
        secondary_address_v4: Optional[List[SecondaryAddressV4]]


    class SviSecondaryAddressV6:
        address: Union[
            OneOfSecondaryAddressV6AddressOptionsDef1,
            OneOfSecondaryAddressV6AddressOptionsDef2,
            OneOfSecondaryAddressV6AddressOptionsDef3,
        ]


    class SviOneOfDhcpHelperV6VpnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SviDhcpHelperV6:
        address: Union[
            OneOfDhcpHelperV6AddressOptionsDef1,
            OneOfDhcpHelperV6AddressOptionsDef2,
        ]
        vpn: Optional[
            Union[
                SviOneOfDhcpHelperV6VpnOptionsDef1,
                OneOfDhcpHelperV6VpnOptionsDef2,
                OneOfDhcpHelperV6VpnOptionsDef3,
            ]
        ]


    class InterfaceSviIpv6:
        """
        Advanced Attributes
        """

        address_v6: Optional[
            Union[
                OneOfAddressV6OptionsDef1,
                OneOfAddressV6OptionsDef2,
                OneOfAddressV6OptionsDef3,
            ]
        ]
        # DHCPv6 Helper
        dhcp_helper_v6: Optional[List[SviDhcpHelperV6]]
        # Assign secondary IPv6 addresses
        secondary_address_v6: Optional[List[SviSecondaryAddressV6]]


    class SviOneOfArpMacOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class SviArp:
        ip_address: Union[
            OneOfArpAddrOptionsDef1, OneOfArpAddrOptionsDef2
        ]
        mac_address: Union[
            SviOneOfArpMacOptionsDef1, OneOfArpMacOptionsDef2
        ]


    class SviOneOfIpv4VrrpGrpIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SviOneOfIpv4VrrpPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SviOneOfIpv4VrrpPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SviOneOfIpv4VrrpTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SviOneOfIpv4VrrpTimerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultIpv4VrrpTimerDef  # pytype: disable=annotation-type-mismatch


    class SviOneOfIpv4VrrpTrackPrefixListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SviIpAddressSecondary:
        address: Union[
            OneOfIpv4VrrpIpv4SecondaryAddressOptionsDef1,
            OneOfIpv4VrrpIpv4SecondaryAddressOptionsDef2,
        ]


    class SviOneOfIpv4VrrpTrackingObjectTrackActionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SviIpv4VrrpTrackingObjectTrackActionDef


    class SviOneOfIpv4VrrpTrackingObjectDecrementOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SviTrackingObject:
        track_action: Union[
            SviOneOfIpv4VrrpTrackingObjectTrackActionOptionsDef1,
            OneOfIpv4VrrpTrackingObjectTrackActionOptionsDef2,
        ]
        tracker_id: Union[
            OneOfIpv4VrrpTrackingObjectNameOptionsDef1,
            OneOfIpv4VrrpTrackingObjectNameOptionsDef2,
        ]
        decrement_value: Optional[
            Union[
                SviOneOfIpv4VrrpTrackingObjectDecrementOptionsDef1,
                OneOfIpv4VrrpTrackingObjectDecrementOptionsDef2,
            ]
        ]


    class SviVrrp1:
        group_id: Union[
            SviOneOfIpv4VrrpGrpIdOptionsDef1,
            OneOfIpv4VrrpGrpIdOptionsDef2,
        ]
        ip_address: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]
        priority: Union[
            SviOneOfIpv4VrrpPriorityOptionsDef1,
            OneOfIpv4VrrpPriorityOptionsDef2,
            SviOneOfIpv4VrrpPriorityOptionsDef3,
        ]
        timer: Union[
            SviOneOfIpv4VrrpTimerOptionsDef1,
            OneOfIpv4VrrpTimerOptionsDef2,
            SviOneOfIpv4VrrpTimerOptionsDef3,
        ]
        tloc_pref_change: Union[
            OneOfIpv4VrrpTlocChangePrefOptionsDef1,
            OneOfIpv4VrrpTlocChangePrefOptionsDef2,
        ]
        track_omp: Union[
            OneOfIpv4VrrpTrackOmpOptionsDef1,
            OneOfIpv4VrrpTrackOmpOptionsDef2,
            OneOfIpv4VrrpTrackOmpOptionsDef3,
        ]
        follow_dual_router_ha_availability: Optional[
            Union[
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef1,
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef2,
            ]
        ]
        # VRRP Secondary IPV4 address
        ip_address_secondary: Optional[List[SviIpAddressSecondary]]
        prefix_list: Optional[
            Union[
                SviOneOfIpv4VrrpTrackPrefixListOptionsDef1,
                OneOfIpv4VrrpTrackPrefixListOptionsDef2,
                OneOfIpv4VrrpTrackPrefixListOptionsDef3,
            ]
        ]
        tloc_pref_change_value: Optional[TlocPrefChangeValue]
        # tracking object for VRRP configuration
        tracking_object: Optional[List[SviTrackingObject]]


    class InterfaceSviOneOfIpv4VrrpGrpIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceSviOneOfIpv4VrrpPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceSviOneOfIpv4VrrpPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceSviOneOfIpv4VrrpTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceSviOneOfIpv4VrrpTimerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultIpv4VrrpTimerDef  # pytype: disable=annotation-type-mismatch


    class InterfaceSviOneOfIpv4VrrpTrackPrefixListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceSviIpAddressSecondary:
        address: Union[
            OneOfIpv4VrrpIpv4SecondaryAddressOptionsDef1,
            OneOfIpv4VrrpIpv4SecondaryAddressOptionsDef2,
        ]


    class SviOneOfIpv4VrrpValueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceSviOneOfIpv4VrrpTrackingObjectTrackActionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceSviIpv4VrrpTrackingObjectTrackActionDef


    class InterfaceSviOneOfIpv4VrrpTrackingObjectDecrementOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceSviTrackingObject:
        track_action: Union[
            InterfaceSviOneOfIpv4VrrpTrackingObjectTrackActionOptionsDef1,
            OneOfIpv4VrrpTrackingObjectTrackActionOptionsDef2,
        ]
        tracker_id: Union[
            OneOfIpv4VrrpTrackingObjectNameOptionsDef1,
            OneOfIpv4VrrpTrackingObjectNameOptionsDef2,
        ]
        decrement_value: Optional[
            Union[
                InterfaceSviOneOfIpv4VrrpTrackingObjectDecrementOptionsDef1,
                OneOfIpv4VrrpTrackingObjectDecrementOptionsDef2,
            ]
        ]


    class SviVrrp2:
        group_id: Union[
            InterfaceSviOneOfIpv4VrrpGrpIdOptionsDef1,
            OneOfIpv4VrrpGrpIdOptionsDef2,
        ]
        ip_address: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]
        priority: Union[
            InterfaceSviOneOfIpv4VrrpPriorityOptionsDef1,
            OneOfIpv4VrrpPriorityOptionsDef2,
            InterfaceSviOneOfIpv4VrrpPriorityOptionsDef3,
        ]
        timer: Union[
            InterfaceSviOneOfIpv4VrrpTimerOptionsDef1,
            OneOfIpv4VrrpTimerOptionsDef2,
            InterfaceSviOneOfIpv4VrrpTimerOptionsDef3,
        ]
        tloc_pref_change: Union[
            OneOfIpv4VrrpTlocChangePrefOptionsDef1,
            OneOfIpv4VrrpTlocChangePrefOptionsDef2,
        ]
        track_omp: Union[
            OneOfIpv4VrrpTrackOmpOptionsDef1,
            OneOfIpv4VrrpTrackOmpOptionsDef2,
            OneOfIpv4VrrpTrackOmpOptionsDef3,
        ]
        follow_dual_router_ha_availability: Optional[
            Union[
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef1,
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef2,
            ]
        ]
        # VRRP Secondary IPV4 address
        ip_address_secondary: Optional[
            List[InterfaceSviIpAddressSecondary]
        ]
        prefix_list: Optional[
            Union[
                InterfaceSviOneOfIpv4VrrpTrackPrefixListOptionsDef1,
                OneOfIpv4VrrpTrackPrefixListOptionsDef2,
                OneOfIpv4VrrpTrackPrefixListOptionsDef3,
            ]
        ]
        tloc_pref_change_value: Optional[
            Union[
                SviOneOfIpv4VrrpValueOptionsDef1,
                OneOfIpv4VrrpValueOptionsDef2,
            ]
        ]
        # tracking object for VRRP configuration
        tracking_object: Optional[List[InterfaceSviTrackingObject]]


    class SviOneOfIpv6VrrpGrpIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SviOneOfIpv6VrrpPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SviOneOfIpv6VrrpPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SviOneOfIpv6VrrpTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SviOneOfIpv6VrrpTimerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultIpv6VrrpTimerDef  # pytype: disable=annotation-type-mismatch


    class SviOneOfIpv6VrrpTrackPrefixListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnInterfaceSviIpv6:
        ipv6_link_local: Union[
            OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef1,
            OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef2,
        ]
        prefix: Optional[
            Union[
                OneOfIpv6VrrpIpv6PrefixOptionsDef1,
                OneOfIpv6VrrpIpv6PrefixOptionsDef2,
                OneOfIpv6VrrpIpv6PrefixOptionsDef3,
            ]
        ]


    class SviIpv6Secondary:
        prefix: Union[
            OneOfIpv6VrrpIpv6SecondaryPrefixOptionsDef1,
            OneOfIpv6VrrpIpv6SecondaryPrefixOptionsDef2,
        ]


    class SviVrrpIpv6:
        group_id: Union[
            SviOneOfIpv6VrrpGrpIdOptionsDef1,
            OneOfIpv6VrrpGrpIdOptionsDef2,
        ]
        # IPv6 VRRP
        ipv6: List[VpnInterfaceSviIpv6]
        priority: Union[
            SviOneOfIpv6VrrpPriorityOptionsDef1,
            OneOfIpv6VrrpPriorityOptionsDef2,
            SviOneOfIpv6VrrpPriorityOptionsDef3,
        ]
        timer: Union[
            SviOneOfIpv6VrrpTimerOptionsDef1,
            OneOfIpv6VrrpTimerOptionsDef2,
            SviOneOfIpv6VrrpTimerOptionsDef3,
        ]
        track_omp: Union[
            OneOfIpv6VrrpTrackOmpOptionsDef1,
            OneOfIpv6VrrpTrackOmpOptionsDef2,
            OneOfIpv6VrrpTrackOmpOptionsDef3,
        ]
        follow_dual_router_ha_availability: Optional[
            Union[
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef1,
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef2,
            ]
        ]
        # IPv6 Secondary IP address
        ipv6_secondary: Optional[List[SviIpv6Secondary]]
        track_prefix_list: Optional[
            Union[
                SviOneOfIpv6VrrpTrackPrefixListOptionsDef1,
                OneOfIpv6VrrpTrackPrefixListOptionsDef2,
                OneOfIpv6VrrpTrackPrefixListOptionsDef3,
            ]
        ]


    class SviOneOfTcpMssOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SviOneOfArpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SviOneOfArpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SviAdvanced:
        """
        Advanced Attributes
        """

        arp_timeout: Union[
            SviOneOfArpTimeoutOptionsDef1,
            OneOfArpTimeoutOptionsDef2,
            SviOneOfArpTimeoutOptionsDef3,
        ]
        ip_directed_broadcast: Union[
            OneOfIpDirectedBroadcastOptionsDef1,
            OneOfIpDirectedBroadcastOptionsDef2,
            OneOfIpDirectedBroadcastOptionsDef3,
        ]
        icmp_redirect_disable: Optional[
            Union[
                OneOfIcmpRedirectDisableOptionsDef1,
                OneOfIcmpRedirectDisableOptionsDef2,
                OneOfIcmpRedirectDisableOptionsDef3,
            ]
        ]
        tcp_mss: Optional[
            Union[
                SviOneOfTcpMssOptionsDef1,
                OneOfTcpMssOptionsDef2,
                OneOfTcpMssOptionsDef3,
            ]
        ]


    class VpnInterfaceSviData:
        # Advanced Attributes
        advanced: SviAdvanced
        interface_name: Union[
            SviOneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        # ACL
        acl_qos: Optional[AclQos]
        # Configure static ARP entries
        arp: Optional[List[SviArp]]
        description: Optional[
            Union[
                SviOneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]
        dhcp_client_v6: Optional[
            Union[
                OneOfDhcpClientV6OptionsDef1,
                OneOfDhcpClientV6OptionsDef2,
                OneOfDhcpClientV6OptionsDef3,
            ]
        ]
        if_mtu: Optional[
            Union[
                SviOneOfIfMtuOptionsDef1,
                OneOfIfMtuOptionsDef2,
                SviOneOfIfMtuOptionsDef3,
            ]
        ]
        ip_mtu: Optional[
            Union[
                SviOneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                SviOneOfMtuOptionsDef3,
            ]
        ]
        # ipv4 Attributes
        ipv4: Optional[SviIpv4]
        # Advanced Attributes
        ipv6: Optional[InterfaceSviIpv6]
        # Enable ipv4 VRRP
        vrrp: Optional[List[Union[SviVrrp1, SviVrrp2]]]
        # Enable ipv6 VRRP
        vrrp_ipv6: Optional[List[SviVrrpIpv6]]


    class SviPayload:
        """
        LAN VPN Interface SVI profile parcel schema for PUT request
        """

        data: VpnInterfaceSviData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanServiceLanVpnInterfaceSviPayload:
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
        # LAN VPN Interface SVI profile parcel schema for PUT request
        payload: Optional[SviPayload]


    class EditLanVpnInterfaceSviParcelForServicePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class InterfaceSviOneOfIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceSviOneOfDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceSviOneOfIfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceSviOneOfIfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceSviOneOfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceSviOneOfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceSviOneOfDhcpHelperV4OptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class InterfaceSviIpv4:
        """
        ipv4 Attributes
        """

        # IpV4Address Primary
        address_v4: AddressV4
        dhcp_helper_v4: Optional[
            Union[
                InterfaceSviOneOfDhcpHelperV4OptionsDef1,
                OneOfDhcpHelperV4OptionsDef2,
                OneOfDhcpHelperV4OptionsDef3,
            ]
        ]
        # Assign secondary IP addresses
        secondary_address_v4: Optional[List[SecondaryAddressV4]]


    class InterfaceSviSecondaryAddressV6:
        address: Union[
            OneOfSecondaryAddressV6AddressOptionsDef1,
            OneOfSecondaryAddressV6AddressOptionsDef2,
            OneOfSecondaryAddressV6AddressOptionsDef3,
        ]


    class InterfaceSviOneOfDhcpHelperV6VpnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceSviDhcpHelperV6:
        address: Union[
            OneOfDhcpHelperV6AddressOptionsDef1,
            OneOfDhcpHelperV6AddressOptionsDef2,
        ]
        vpn: Optional[
            Union[
                InterfaceSviOneOfDhcpHelperV6VpnOptionsDef1,
                OneOfDhcpHelperV6VpnOptionsDef2,
                OneOfDhcpHelperV6VpnOptionsDef3,
            ]
        ]


    class LanVpnInterfaceSviIpv6:
        """
        Advanced Attributes
        """

        address_v6: Optional[
            Union[
                OneOfAddressV6OptionsDef1,
                OneOfAddressV6OptionsDef2,
                OneOfAddressV6OptionsDef3,
            ]
        ]
        # DHCPv6 Helper
        dhcp_helper_v6: Optional[List[InterfaceSviDhcpHelperV6]]
        # Assign secondary IPv6 addresses
        secondary_address_v6: Optional[
            List[InterfaceSviSecondaryAddressV6]
        ]


    class InterfaceSviOneOfArpMacOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class InterfaceSviArp:
        ip_address: Union[
            OneOfArpAddrOptionsDef1, OneOfArpAddrOptionsDef2
        ]
        mac_address: Union[
            InterfaceSviOneOfArpMacOptionsDef1, OneOfArpMacOptionsDef2
        ]


    class VpnInterfaceSviOneOfIpv4VrrpGrpIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnInterfaceSviOneOfIpv4VrrpPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnInterfaceSviOneOfIpv4VrrpPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class VpnInterfaceSviOneOfIpv4VrrpTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnInterfaceSviOneOfIpv4VrrpTimerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultIpv4VrrpTimerDef  # pytype: disable=annotation-type-mismatch


    class VpnInterfaceSviOneOfIpv4VrrpTrackPrefixListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VpnInterfaceSviIpAddressSecondary:
        address: Union[
            OneOfIpv4VrrpIpv4SecondaryAddressOptionsDef1,
            OneOfIpv4VrrpIpv4SecondaryAddressOptionsDef2,
        ]


    class VpnInterfaceSviOneOfIpv4VrrpTrackingObjectTrackActionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: VpnInterfaceSviIpv4VrrpTrackingObjectTrackActionDef


    class VpnInterfaceSviOneOfIpv4VrrpTrackingObjectDecrementOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnInterfaceSviTrackingObject:
        track_action: Union[
            VpnInterfaceSviOneOfIpv4VrrpTrackingObjectTrackActionOptionsDef1,
            OneOfIpv4VrrpTrackingObjectTrackActionOptionsDef2,
        ]
        tracker_id: Union[
            OneOfIpv4VrrpTrackingObjectNameOptionsDef1,
            OneOfIpv4VrrpTrackingObjectNameOptionsDef2,
        ]
        decrement_value: Optional[
            Union[
                VpnInterfaceSviOneOfIpv4VrrpTrackingObjectDecrementOptionsDef1,
                OneOfIpv4VrrpTrackingObjectDecrementOptionsDef2,
            ]
        ]


    class InterfaceSviVrrp1:
        group_id: Union[
            VpnInterfaceSviOneOfIpv4VrrpGrpIdOptionsDef1,
            OneOfIpv4VrrpGrpIdOptionsDef2,
        ]
        ip_address: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]
        priority: Union[
            VpnInterfaceSviOneOfIpv4VrrpPriorityOptionsDef1,
            OneOfIpv4VrrpPriorityOptionsDef2,
            VpnInterfaceSviOneOfIpv4VrrpPriorityOptionsDef3,
        ]
        timer: Union[
            VpnInterfaceSviOneOfIpv4VrrpTimerOptionsDef1,
            OneOfIpv4VrrpTimerOptionsDef2,
            VpnInterfaceSviOneOfIpv4VrrpTimerOptionsDef3,
        ]
        tloc_pref_change: Union[
            OneOfIpv4VrrpTlocChangePrefOptionsDef1,
            OneOfIpv4VrrpTlocChangePrefOptionsDef2,
        ]
        track_omp: Union[
            OneOfIpv4VrrpTrackOmpOptionsDef1,
            OneOfIpv4VrrpTrackOmpOptionsDef2,
            OneOfIpv4VrrpTrackOmpOptionsDef3,
        ]
        follow_dual_router_ha_availability: Optional[
            Union[
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef1,
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef2,
            ]
        ]
        # VRRP Secondary IPV4 address
        ip_address_secondary: Optional[
            List[VpnInterfaceSviIpAddressSecondary]
        ]
        prefix_list: Optional[
            Union[
                VpnInterfaceSviOneOfIpv4VrrpTrackPrefixListOptionsDef1,
                OneOfIpv4VrrpTrackPrefixListOptionsDef2,
                OneOfIpv4VrrpTrackPrefixListOptionsDef3,
            ]
        ]
        tloc_pref_change_value: Optional[TlocPrefChangeValue]
        # tracking object for VRRP configuration
        tracking_object: Optional[List[VpnInterfaceSviTrackingObject]]


    class LanVpnInterfaceSviOneOfIpv4VrrpGrpIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnInterfaceSviOneOfIpv4VrrpPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnInterfaceSviOneOfIpv4VrrpPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class LanVpnInterfaceSviOneOfIpv4VrrpTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnInterfaceSviOneOfIpv4VrrpTimerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultIpv4VrrpTimerDef  # pytype: disable=annotation-type-mismatch


    class LanVpnInterfaceSviOneOfIpv4VrrpTrackPrefixListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class LanVpnInterfaceSviIpAddressSecondary:
        address: Union[
            OneOfIpv4VrrpIpv4SecondaryAddressOptionsDef1,
            OneOfIpv4VrrpIpv4SecondaryAddressOptionsDef2,
        ]


    class InterfaceSviOneOfIpv4VrrpValueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnInterfaceSviOneOfIpv4VrrpTrackingObjectTrackActionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: LanVpnInterfaceSviIpv4VrrpTrackingObjectTrackActionDef


    class LanVpnInterfaceSviOneOfIpv4VrrpTrackingObjectDecrementOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class LanVpnInterfaceSviTrackingObject:
        track_action: Union[
            LanVpnInterfaceSviOneOfIpv4VrrpTrackingObjectTrackActionOptionsDef1,
            OneOfIpv4VrrpTrackingObjectTrackActionOptionsDef2,
        ]
        tracker_id: Union[
            OneOfIpv4VrrpTrackingObjectNameOptionsDef1,
            OneOfIpv4VrrpTrackingObjectNameOptionsDef2,
        ]
        decrement_value: Optional[
            Union[
                LanVpnInterfaceSviOneOfIpv4VrrpTrackingObjectDecrementOptionsDef1,
                OneOfIpv4VrrpTrackingObjectDecrementOptionsDef2,
            ]
        ]


    class InterfaceSviVrrp2:
        group_id: Union[
            LanVpnInterfaceSviOneOfIpv4VrrpGrpIdOptionsDef1,
            OneOfIpv4VrrpGrpIdOptionsDef2,
        ]
        ip_address: Union[
            OneOfIpV4AddressOptionsWithoutDefault1,
            OneOfIpV4AddressOptionsWithoutDefault2,
        ]
        priority: Union[
            LanVpnInterfaceSviOneOfIpv4VrrpPriorityOptionsDef1,
            OneOfIpv4VrrpPriorityOptionsDef2,
            LanVpnInterfaceSviOneOfIpv4VrrpPriorityOptionsDef3,
        ]
        timer: Union[
            LanVpnInterfaceSviOneOfIpv4VrrpTimerOptionsDef1,
            OneOfIpv4VrrpTimerOptionsDef2,
            LanVpnInterfaceSviOneOfIpv4VrrpTimerOptionsDef3,
        ]
        tloc_pref_change: Union[
            OneOfIpv4VrrpTlocChangePrefOptionsDef1,
            OneOfIpv4VrrpTlocChangePrefOptionsDef2,
        ]
        track_omp: Union[
            OneOfIpv4VrrpTrackOmpOptionsDef1,
            OneOfIpv4VrrpTrackOmpOptionsDef2,
            OneOfIpv4VrrpTrackOmpOptionsDef3,
        ]
        follow_dual_router_ha_availability: Optional[
            Union[
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef1,
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef2,
            ]
        ]
        # VRRP Secondary IPV4 address
        ip_address_secondary: Optional[
            List[LanVpnInterfaceSviIpAddressSecondary]
        ]
        prefix_list: Optional[
            Union[
                LanVpnInterfaceSviOneOfIpv4VrrpTrackPrefixListOptionsDef1,
                OneOfIpv4VrrpTrackPrefixListOptionsDef2,
                OneOfIpv4VrrpTrackPrefixListOptionsDef3,
            ]
        ]
        tloc_pref_change_value: Optional[
            Union[
                InterfaceSviOneOfIpv4VrrpValueOptionsDef1,
                OneOfIpv4VrrpValueOptionsDef2,
            ]
        ]
        # tracking object for VRRP configuration
        tracking_object: Optional[List[LanVpnInterfaceSviTrackingObject]]


    class InterfaceSviOneOfIpv6VrrpGrpIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceSviOneOfIpv6VrrpPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceSviOneOfIpv6VrrpPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceSviOneOfIpv6VrrpTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceSviOneOfIpv6VrrpTimerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultIpv6VrrpTimerDef  # pytype: disable=annotation-type-mismatch


    class InterfaceSviOneOfIpv6VrrpTrackPrefixListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceLanVpnInterfaceSviIpv6:
        ipv6_link_local: Union[
            OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef1,
            OneOfIpv6VrrpIpv6Ipv6LinkLocalOptionsDef2,
        ]
        prefix: Optional[
            Union[
                OneOfIpv6VrrpIpv6PrefixOptionsDef1,
                OneOfIpv6VrrpIpv6PrefixOptionsDef2,
                OneOfIpv6VrrpIpv6PrefixOptionsDef3,
            ]
        ]


    class InterfaceSviIpv6Secondary:
        prefix: Union[
            OneOfIpv6VrrpIpv6SecondaryPrefixOptionsDef1,
            OneOfIpv6VrrpIpv6SecondaryPrefixOptionsDef2,
        ]


    class InterfaceSviVrrpIpv6:
        group_id: Union[
            InterfaceSviOneOfIpv6VrrpGrpIdOptionsDef1,
            OneOfIpv6VrrpGrpIdOptionsDef2,
        ]
        # IPv6 VRRP
        ipv6: List[ServiceLanVpnInterfaceSviIpv6]
        priority: Union[
            InterfaceSviOneOfIpv6VrrpPriorityOptionsDef1,
            OneOfIpv6VrrpPriorityOptionsDef2,
            InterfaceSviOneOfIpv6VrrpPriorityOptionsDef3,
        ]
        timer: Union[
            InterfaceSviOneOfIpv6VrrpTimerOptionsDef1,
            OneOfIpv6VrrpTimerOptionsDef2,
            InterfaceSviOneOfIpv6VrrpTimerOptionsDef3,
        ]
        track_omp: Union[
            OneOfIpv6VrrpTrackOmpOptionsDef1,
            OneOfIpv6VrrpTrackOmpOptionsDef2,
            OneOfIpv6VrrpTrackOmpOptionsDef3,
        ]
        follow_dual_router_ha_availability: Optional[
            Union[
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef1,
                OneOfOnBooleanDefaultTrueNoVariableOptionsDef2,
            ]
        ]
        # IPv6 Secondary IP address
        ipv6_secondary: Optional[List[InterfaceSviIpv6Secondary]]
        track_prefix_list: Optional[
            Union[
                InterfaceSviOneOfIpv6VrrpTrackPrefixListOptionsDef1,
                OneOfIpv6VrrpTrackPrefixListOptionsDef2,
                OneOfIpv6VrrpTrackPrefixListOptionsDef3,
            ]
        ]


    class InterfaceSviOneOfTcpMssOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceSviOneOfArpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceSviOneOfArpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceSviAdvanced:
        """
        Advanced Attributes
        """

        arp_timeout: Union[
            InterfaceSviOneOfArpTimeoutOptionsDef1,
            OneOfArpTimeoutOptionsDef2,
            InterfaceSviOneOfArpTimeoutOptionsDef3,
        ]
        ip_directed_broadcast: Union[
            OneOfIpDirectedBroadcastOptionsDef1,
            OneOfIpDirectedBroadcastOptionsDef2,
            OneOfIpDirectedBroadcastOptionsDef3,
        ]
        icmp_redirect_disable: Optional[
            Union[
                OneOfIcmpRedirectDisableOptionsDef1,
                OneOfIcmpRedirectDisableOptionsDef2,
                OneOfIcmpRedirectDisableOptionsDef3,
            ]
        ]
        tcp_mss: Optional[
            Union[
                InterfaceSviOneOfTcpMssOptionsDef1,
                OneOfTcpMssOptionsDef2,
                OneOfTcpMssOptionsDef3,
            ]
        ]


    class LanVpnInterfaceSviData:
        # Advanced Attributes
        advanced: InterfaceSviAdvanced
        interface_name: Union[
            InterfaceSviOneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        # ACL
        acl_qos: Optional[AclQos]
        # Configure static ARP entries
        arp: Optional[List[InterfaceSviArp]]
        description: Optional[
            Union[
                InterfaceSviOneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]
        dhcp_client_v6: Optional[
            Union[
                OneOfDhcpClientV6OptionsDef1,
                OneOfDhcpClientV6OptionsDef2,
                OneOfDhcpClientV6OptionsDef3,
            ]
        ]
        if_mtu: Optional[
            Union[
                InterfaceSviOneOfIfMtuOptionsDef1,
                OneOfIfMtuOptionsDef2,
                InterfaceSviOneOfIfMtuOptionsDef3,
            ]
        ]
        ip_mtu: Optional[
            Union[
                InterfaceSviOneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                InterfaceSviOneOfMtuOptionsDef3,
            ]
        ]
        # ipv4 Attributes
        ipv4: Optional[InterfaceSviIpv4]
        # Advanced Attributes
        ipv6: Optional[LanVpnInterfaceSviIpv6]
        # Enable ipv4 VRRP
        vrrp: Optional[List[Union[InterfaceSviVrrp1, InterfaceSviVrrp2]]]
        # Enable ipv6 VRRP
        vrrp_ipv6: Optional[List[InterfaceSviVrrpIpv6]]


    class EditLanVpnInterfaceSviParcelForServicePutRequest:
        """
        LAN VPN Interface SVI profile parcel schema for PUT request
        """

        data: LanVpnInterfaceSviData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


