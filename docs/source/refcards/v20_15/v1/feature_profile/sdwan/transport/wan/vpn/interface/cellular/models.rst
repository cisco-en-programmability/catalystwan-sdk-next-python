======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    ModeDef = Literal["spoke"]

    CarrierDef = Literal[
        "carrier1",
        "carrier2",
        "carrier3",
        "carrier4",
        "carrier5",
        "carrier6",
        "carrier7",
        "carrier8",
        "default",
    ]

    DefaultCarrierDef = Literal["default"]

    ColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    Value = Literal["mpls"]

    EncapsulationEncapDef = Literal["gre", "ipsec"]

    CoreRegionDef = Literal["core", "core-shared"]

    DefaultCoreRegionDef = Literal["core-shared"]

    SecondaryRegionDef = Literal["secondary-only", "secondary-shared"]

    DefaultSecondaryRegionDef = Literal["secondary-shared"]

    CellularModeDef = Literal["spoke"]

    CellularCarrierDef = Literal[
        "carrier1",
        "carrier2",
        "carrier3",
        "carrier4",
        "carrier5",
        "carrier6",
        "carrier7",
        "carrier8",
        "default",
    ]

    CellularDefaultCarrierDef = Literal["default"]

    CellularColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    CellularEncapsulationEncapDef = Literal["gre", "ipsec"]

    CellularCoreRegionDef = Literal["core", "core-shared"]

    CellularDefaultCoreRegionDef = Literal["core-shared"]

    CellularSecondaryRegionDef = Literal[
        "secondary-only", "secondary-shared"
    ]

    CellularDefaultSecondaryRegionDef = Literal["secondary-shared"]

    InterfaceCellularModeDef = Literal["spoke"]

    InterfaceCellularCarrierDef = Literal[
        "carrier1",
        "carrier2",
        "carrier3",
        "carrier4",
        "carrier5",
        "carrier6",
        "carrier7",
        "carrier8",
        "default",
    ]

    InterfaceCellularDefaultCarrierDef = Literal["default"]

    InterfaceCellularColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]

    InterfaceCellularEncapsulationEncapDef = Literal["gre", "ipsec"]

    InterfaceCellularCoreRegionDef = Literal["core", "core-shared"]

    InterfaceCellularDefaultCoreRegionDef = Literal["core-shared"]

    InterfaceCellularSecondaryRegionDef = Literal[
        "secondary-only", "secondary-shared"
    ]

    InterfaceCellularDefaultSecondaryRegionDef = Literal[
        "secondary-shared"
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
        value: bool


    class OneOfenableIpV6OptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfenableIpV6OptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfenableIpV6OptionsDef3:
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


    class OneOfServiceProviderOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfServiceProviderOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfServiceProviderOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfBandwidthUpstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfBandwidthUpstreamOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBandwidthUpstreamOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfBandwidthDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfBandwidthDownstreamOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBandwidthDownstreamOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfTunnelInterfaceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfTunnelInterfaceOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfPerTunnelQosOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfPerTunnelQosOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPerTunnelQosOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ModeDef  # pytype: disable=annotation-type-mismatch


    class OneOfModeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBindOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfBindOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBindOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfCarrierOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: CarrierDef


    class OneOfCarrierOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfCarrierOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: (
            DefaultCarrierDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfColorOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ColorDef  # pytype: disable=annotation-type-mismatch


    class OneOfColorOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfColorOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfHelloIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHelloIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHelloIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfHelloToleranceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHelloToleranceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHelloToleranceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfLastResortCircuitOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfLastResortCircuitOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLastResortCircuitOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfRestrictOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfRestrictOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRestrictOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfGroupOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfGroupOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfBorderOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfBorderOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBorderOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfMaxControlConnectionsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMaxControlConnectionsOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMaxControlConnectionsOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfNatRefreshIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfNatRefreshIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatRefreshIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfVbondAsStunServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfVbondAsStunServerOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVbondAsStunServerOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfControllerGroupListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class OneOfControllerGroupListOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfControllerGroupListOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfVmanageConnectionPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVmanageConnectionPreferenceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVmanageConnectionPreferenceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfPortHopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfPortHopOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPortHopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfLowBandwidthLinkOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfLowBandwidthLinkOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLowBandwidthLinkOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfTunnelTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTunnelTcpMssAdjustOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTunnelTcpMssAdjustOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfClearDontFragmentOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfClearDontFragmentOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfClearDontFragmentOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfNetworkBroadcastOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfNetworkBroadcastOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNetworkBroadcastOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class Tunnel:
        """
        Tunnel Interface Attributes
        """

        bind: Optional[
            Union[
                OneOfBindOptionsDef1,
                OneOfBindOptionsDef2,
                OneOfBindOptionsDef3,
            ]
        ]
        border: Optional[
            Union[
                OneOfBorderOptionsDef1,
                OneOfBorderOptionsDef2,
                OneOfBorderOptionsDef3,
            ]
        ]
        carrier: Optional[
            Union[
                OneOfCarrierOptionsDef1,
                OneOfCarrierOptionsDef2,
                OneOfCarrierOptionsDef3,
            ]
        ]
        clear_dont_fragment: Optional[
            Union[
                OneOfClearDontFragmentOptionsDef1,
                OneOfClearDontFragmentOptionsDef2,
                OneOfClearDontFragmentOptionsDef3,
            ]
        ]
        color: Optional[
            Union[
                OneOfColorOptionsDef1,
                OneOfColorOptionsDef2,
                OneOfColorOptionsDef3,
            ]
        ]
        exclude_controller_group_list: Optional[
            Union[
                OneOfControllerGroupListOptionsDef1,
                OneOfControllerGroupListOptionsDef2,
                OneOfControllerGroupListOptionsDef3,
            ]
        ]
        group: Optional[
            Union[
                OneOfGroupOptionsDef1,
                OneOfGroupOptionsDef2,
                OneOfGroupOptionsDef3,
            ]
        ]
        hello_interval: Optional[
            Union[
                OneOfHelloIntervalOptionsDef1,
                OneOfHelloIntervalOptionsDef2,
                OneOfHelloIntervalOptionsDef3,
            ]
        ]
        hello_tolerance: Optional[
            Union[
                OneOfHelloToleranceOptionsDef1,
                OneOfHelloToleranceOptionsDef2,
                OneOfHelloToleranceOptionsDef3,
            ]
        ]
        last_resort_circuit: Optional[
            Union[
                OneOfLastResortCircuitOptionsDef1,
                OneOfLastResortCircuitOptionsDef2,
                OneOfLastResortCircuitOptionsDef3,
            ]
        ]
        low_bandwidth_link: Optional[
            Union[
                OneOfLowBandwidthLinkOptionsDef1,
                OneOfLowBandwidthLinkOptionsDef2,
                OneOfLowBandwidthLinkOptionsDef3,
            ]
        ]
        max_control_connections: Optional[
            Union[
                OneOfMaxControlConnectionsOptionsDef1,
                OneOfMaxControlConnectionsOptionsDef2,
                OneOfMaxControlConnectionsOptionsDef3,
            ]
        ]
        mode: Optional[Union[OneOfModeOptionsDef1, OneOfModeOptionsDef2]]
        nat_refresh_interval: Optional[
            Union[
                OneOfNatRefreshIntervalOptionsDef1,
                OneOfNatRefreshIntervalOptionsDef2,
                OneOfNatRefreshIntervalOptionsDef3,
            ]
        ]
        network_broadcast: Optional[
            Union[
                OneOfNetworkBroadcastOptionsDef1,
                OneOfNetworkBroadcastOptionsDef2,
                OneOfNetworkBroadcastOptionsDef3,
            ]
        ]
        per_tunnel_qos: Optional[
            Union[
                OneOfPerTunnelQosOptionsDef1,
                OneOfPerTunnelQosOptionsDef2,
                OneOfPerTunnelQosOptionsDef3,
            ]
        ]
        port_hop: Optional[
            Union[
                OneOfPortHopOptionsDef1,
                OneOfPortHopOptionsDef2,
                OneOfPortHopOptionsDef3,
            ]
        ]
        restrict: Optional[
            Union[
                OneOfRestrictOptionsDef1,
                OneOfRestrictOptionsDef2,
                OneOfRestrictOptionsDef3,
            ]
        ]
        tunnel_tcp_mss: Optional[
            Union[
                OneOfTunnelTcpMssAdjustOptionsDef1,
                OneOfTunnelTcpMssAdjustOptionsDef2,
                OneOfTunnelTcpMssAdjustOptionsDef3,
            ]
        ]
        v_bond_as_stun_server: Optional[
            Union[
                OneOfVbondAsStunServerOptionsDef1,
                OneOfVbondAsStunServerOptionsDef2,
                OneOfVbondAsStunServerOptionsDef3,
            ]
        ]
        v_manage_connection_preference: Optional[
            Union[
                OneOfVmanageConnectionPreferenceOptionsDef1,
                OneOfVmanageConnectionPreferenceOptionsDef2,
                OneOfVmanageConnectionPreferenceOptionsDef3,
            ]
        ]


    class OneOfAllowAllOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowAllOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowAllOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfAllowBgpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowBgpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowBgpOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfAllowDhcpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowDhcpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowDhcpOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfAllowNtpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowNtpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowNtpOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfAllowSshOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowSshOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowSshOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfAllowServiceTrueOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowServiceTrueOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowServiceTrueOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfAllowServiceFalseOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAllowServiceFalseOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAllowServiceFalseOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class AllowService:
        """
        Tunnel Interface Attributes
        """

        all: Optional[
            Union[
                OneOfAllowAllOptionsDef1,
                OneOfAllowAllOptionsDef2,
                OneOfAllowAllOptionsDef3,
            ]
        ]
        bfd: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        bgp: Optional[
            Union[
                OneOfAllowBgpOptionsDef1,
                OneOfAllowBgpOptionsDef2,
                OneOfAllowBgpOptionsDef3,
            ]
        ]
        dhcp: Optional[
            Union[
                OneOfAllowDhcpOptionsDef1,
                OneOfAllowDhcpOptionsDef2,
                OneOfAllowDhcpOptionsDef3,
            ]
        ]
        dns: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        https: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        icmp: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        netconf: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        ntp: Optional[
            Union[
                OneOfAllowNtpOptionsDef1,
                OneOfAllowNtpOptionsDef2,
                OneOfAllowNtpOptionsDef3,
            ]
        ]
        ospf: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        snmp: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        ssh: Optional[
            Union[
                OneOfAllowSshOptionsDef1,
                OneOfAllowSshOptionsDef2,
                OneOfAllowSshOptionsDef3,
            ]
        ]
        stun: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]


    class OneOfEncapsulationEncapOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EncapsulationEncapDef  # pytype: disable=annotation-type-mismatch


    class OneOfEncapsulationPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEncapsulationPreferenceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEncapsulationPreferenceOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfEncapsulationWeightOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfEncapsulationWeightOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEncapsulationWeightOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Encapsulation:
        encap: OneOfEncapsulationEncapOptionsDef
        preference: Optional[
            Union[
                OneOfEncapsulationPreferenceOptionsDef1,
                OneOfEncapsulationPreferenceOptionsDef2,
                OneOfEncapsulationPreferenceOptionsDef3,
            ]
        ]
        weight: Optional[
            Union[
                OneOfEncapsulationWeightOptionsDef1,
                OneOfEncapsulationWeightOptionsDef2,
                OneOfEncapsulationWeightOptionsDef3,
            ]
        ]


    class OneOfEnableRegionDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfEnableRegionDef2:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfCoreRegionDef1:
        option_type: GlobalOptionTypeDef
        value: CoreRegionDef  # pytype: disable=annotation-type-mismatch


    class OneOfCoreRegionDef2:
        option_type: DefaultOptionTypeDef
        value: DefaultCoreRegionDef  # pytype: disable=annotation-type-mismatch


    class OneOfSecondaryRegionDef1:
        option_type: GlobalOptionTypeDef
        value: (
            SecondaryRegionDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfSecondaryRegionDef2:
        option_type: DefaultOptionTypeDef
        value: DefaultSecondaryRegionDef  # pytype: disable=annotation-type-mismatch


    class MultiRegionFabric:
        """
        Multi-Region Fabric
        """

        core_region: Optional[
            Union[OneOfCoreRegionDef1, OneOfCoreRegionDef2]
        ]
        enable_core_region: Optional[
            Union[OneOfEnableRegionDef1, OneOfEnableRegionDef2]
        ]
        enable_secondary_region: Optional[
            Union[OneOfEnableRegionDef1, OneOfEnableRegionDef2]
        ]
        secondary_region: Optional[
            Union[OneOfSecondaryRegionDef1, OneOfSecondaryRegionDef2]
        ]


    class OneOfNatOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfNatOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNatOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfUdpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfUdpTimeoutOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUdpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfTcpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTcpTimeoutOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTcpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class NatAttributesIpv4:
        """
        NAT Attributes
        """

        tcp_timeout: Union[
            OneOfTcpTimeoutOptionsDef1,
            OneOfTcpTimeoutOptionsDef2,
            OneOfTcpTimeoutOptionsDef3,
        ]
        udp_timeout: Union[
            OneOfUdpTimeoutOptionsDef1,
            OneOfUdpTimeoutOptionsDef2,
            OneOfUdpTimeoutOptionsDef3,
        ]


    class OneOfQosAdaptiveOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfQosAdaptiveOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfPeriodOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfPeriodOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPeriodOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class ShapingRateUpstream:
        value: Optional[Any]


    class OneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class ShapingRateUpstreamConfig:
        """
        adaptiveQoS Shaping Rate Upstream config
        """

        default_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class OneOfShapingRateDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfShapingRateDownstreamOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: bool


    class ShapingRateDownstreamConfig:
        """
        adaptiveQoS Shaping Rate Downstream config
        """

        default_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class OneOfShapingRateOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfShapingRateOptionsDef3:
        option_type: DefaultOptionTypeDef


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class ParcelReferenceDef:
        ref_id: RefId


    class AclQos1:
        adaptive_qo_s: Union[
            OneOfQosAdaptiveOptionsDef1, OneOfQosAdaptiveOptionsDef2
        ]
        shaping_rate_upstream: ShapingRateUpstream
        # adaptiveQoS Shaping Rate Upstream config
        shaping_rate_upstream_config: ShapingRateUpstreamConfig
        adapt_period: Optional[
            Union[
                OneOfPeriodOptionsDef1,
                OneOfPeriodOptionsDef2,
                OneOfPeriodOptionsDef3,
            ]
        ]
        ipv4_acl_egress: Optional[ParcelReferenceDef]
        ipv4_acl_ingress: Optional[ParcelReferenceDef]
        ipv6_acl_egress: Optional[ParcelReferenceDef]
        ipv6_acl_ingress: Optional[ParcelReferenceDef]
        shaping_rate: Optional[
            Union[
                OneOfShapingRateOptionsDef1,
                OneOfShapingRateOptionsDef2,
                OneOfShapingRateOptionsDef3,
            ]
        ]
        shaping_rate_downstream: Optional[
            Union[
                OneOfShapingRateDownstreamOptionsDef1,
                OneOfShapingRateDownstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Downstream config
        shaping_rate_downstream_config: Optional[
            ShapingRateDownstreamConfig
        ]


    class OneOfShapingRateUpstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfShapingRateUpstreamOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: bool


    class AclQos2:
        adaptive_qo_s: Union[
            OneOfQosAdaptiveOptionsDef1, OneOfQosAdaptiveOptionsDef2
        ]
        adapt_period: Optional[
            Union[
                OneOfPeriodOptionsDef1,
                OneOfPeriodOptionsDef2,
                OneOfPeriodOptionsDef3,
            ]
        ]
        ipv4_acl_egress: Optional[ParcelReferenceDef]
        ipv4_acl_ingress: Optional[ParcelReferenceDef]
        ipv6_acl_egress: Optional[ParcelReferenceDef]
        ipv6_acl_ingress: Optional[ParcelReferenceDef]
        shaping_rate: Optional[
            Union[
                OneOfShapingRateOptionsDef1,
                OneOfShapingRateOptionsDef2,
                OneOfShapingRateOptionsDef3,
            ]
        ]
        shaping_rate_downstream: Optional[
            Union[
                OneOfShapingRateDownstreamOptionsDef1,
                OneOfShapingRateDownstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Downstream config
        shaping_rate_downstream_config: Optional[
            ShapingRateDownstreamConfig
        ]
        shaping_rate_upstream: Optional[
            Union[
                OneOfShapingRateUpstreamOptionsDef1,
                OneOfShapingRateUpstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Upstream config
        shaping_rate_upstream_config: Optional[ShapingRateUpstreamConfig]


    class OneOfIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpV4AddressOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfMacAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfMacAddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMacAddressOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Arp:
        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            OneOfIpV4AddressOptionsDef2,
            OneOfIpV4AddressOptionsDef3,
        ]
        mac_address: Union[
            OneOfMacAddressOptionsDef1,
            OneOfMacAddressOptionsDef2,
            OneOfMacAddressOptionsDef3,
        ]


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


    class OneOfTlocExtensionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTlocExtensionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTlocExtensionOptionsDef3:
        option_type: DefaultOptionTypeDef


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
        tcp_mss: Optional[
            Union[
                OneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]
        tloc_extension: Optional[
            Union[
                OneOfTlocExtensionOptionsDef1,
                OneOfTlocExtensionOptionsDef2,
                OneOfTlocExtensionOptionsDef3,
            ]
        ]
        tracker: Optional[
            Union[
                OneOfTrackerOptionsDef1,
                OneOfTrackerOptionsDef2,
                OneOfTrackerOptionsDef3,
            ]
        ]


    class CellularData:
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        # Encapsulation for TLOC
        encapsulation: List[Encapsulation]
        interface_name: Union[
            OneOfInterfaceNameOptionsDef1, OneOfInterfaceNameOptionsDef2
        ]
        nat: Union[
            OneOfNatOptionsDef1, OneOfNatOptionsDef2, OneOfNatOptionsDef3
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tunnel_interface: Union[
            OneOfTunnelInterfaceOptionsDef1,
            OneOfTunnelInterfaceOptionsDef2,
        ]
        # ACL/QOS
        acl_qos: Optional[Union[AclQos1, AclQos2]]
        # Advanced Attributes
        advanced: Optional[Advanced]
        # Tunnel Interface Attributes
        allow_service: Optional[AllowService]
        # Configure ARP entries
        arp: Optional[List[Arp]]
        bandwidth_downstream: Optional[
            Union[
                OneOfBandwidthDownstreamOptionsDef1,
                OneOfBandwidthDownstreamOptionsDef2,
                OneOfBandwidthDownstreamOptionsDef3,
            ]
        ]
        bandwidth_upstream: Optional[
            Union[
                OneOfBandwidthUpstreamOptionsDef1,
                OneOfBandwidthUpstreamOptionsDef2,
                OneOfBandwidthUpstreamOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                OneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        enable_ipv6: Optional[
            Union[
                OneOfenableIpV6OptionsDef1,
                OneOfenableIpV6OptionsDef2,
                OneOfenableIpV6OptionsDef3,
            ]
        ]
        # Multi-Region Fabric
        multi_region_fabric: Optional[MultiRegionFabric]
        # NAT Attributes
        nat_attributes_ipv4: Optional[NatAttributesIpv4]
        service_provider: Optional[
            Union[
                OneOfServiceProviderOptionsDef1,
                OneOfServiceProviderOptionsDef2,
                OneOfServiceProviderOptionsDef3,
            ]
        ]
        # Tunnel Interface Attributes
        tunnel: Optional[Tunnel]


    class Payload:
        """
        WAN VPN Interface Cellular profile parcel schema for POST request
        """

        data: CellularData
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
        # WAN VPN Interface Cellular profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanTransportWanVpnInterfaceCellularPayload:
        data: Optional[List[Data]]


    class CreateWanVpnInterfaceCellularParcelForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class InterfaceCellularData:
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        # Encapsulation for TLOC
        encapsulation: List[Encapsulation]
        interface_name: Union[
            OneOfInterfaceNameOptionsDef1, OneOfInterfaceNameOptionsDef2
        ]
        nat: Union[
            OneOfNatOptionsDef1, OneOfNatOptionsDef2, OneOfNatOptionsDef3
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tunnel_interface: Union[
            OneOfTunnelInterfaceOptionsDef1,
            OneOfTunnelInterfaceOptionsDef2,
        ]
        # ACL/QOS
        acl_qos: Optional[Union[AclQos1, AclQos2]]
        # Advanced Attributes
        advanced: Optional[Advanced]
        # Tunnel Interface Attributes
        allow_service: Optional[AllowService]
        # Configure ARP entries
        arp: Optional[List[Arp]]
        bandwidth_downstream: Optional[
            Union[
                OneOfBandwidthDownstreamOptionsDef1,
                OneOfBandwidthDownstreamOptionsDef2,
                OneOfBandwidthDownstreamOptionsDef3,
            ]
        ]
        bandwidth_upstream: Optional[
            Union[
                OneOfBandwidthUpstreamOptionsDef1,
                OneOfBandwidthUpstreamOptionsDef2,
                OneOfBandwidthUpstreamOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                OneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        enable_ipv6: Optional[
            Union[
                OneOfenableIpV6OptionsDef1,
                OneOfenableIpV6OptionsDef2,
                OneOfenableIpV6OptionsDef3,
            ]
        ]
        # Multi-Region Fabric
        multi_region_fabric: Optional[MultiRegionFabric]
        # NAT Attributes
        nat_attributes_ipv4: Optional[NatAttributesIpv4]
        service_provider: Optional[
            Union[
                OneOfServiceProviderOptionsDef1,
                OneOfServiceProviderOptionsDef2,
                OneOfServiceProviderOptionsDef3,
            ]
        ]
        # Tunnel Interface Attributes
        tunnel: Optional[Tunnel]


    class CreateWanVpnInterfaceCellularParcelForTransportPostRequest:
        """
        WAN VPN Interface Cellular profile parcel schema for POST request
        """

        data: InterfaceCellularData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class CellularOneOfInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CellularOneOfDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CellularOneOfListOfIpV4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class CellularOneOfBandwidthUpstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfBandwidthDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: CellularModeDef  # pytype: disable=annotation-type-mismatch


    class CellularOneOfBindOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CellularOneOfCarrierOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: CellularCarrierDef


    class CellularOneOfCarrierOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: CellularDefaultCarrierDef  # pytype: disable=annotation-type-mismatch


    class CellularOneOfColorOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            CellularColorDef  # pytype: disable=annotation-type-mismatch
        )


    class CellularOneOfHelloIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfHelloIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class CellularOneOfHelloToleranceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfHelloToleranceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class CellularOneOfGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfMaxControlConnectionsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfNatRefreshIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfNatRefreshIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class CellularOneOfControllerGroupListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class CellularOneOfVmanageConnectionPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfVmanageConnectionPreferenceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class CellularOneOfTunnelTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularTunnel:
        """
        Tunnel Interface Attributes
        """

        bind: Optional[
            Union[
                CellularOneOfBindOptionsDef1,
                OneOfBindOptionsDef2,
                OneOfBindOptionsDef3,
            ]
        ]
        border: Optional[
            Union[
                OneOfBorderOptionsDef1,
                OneOfBorderOptionsDef2,
                OneOfBorderOptionsDef3,
            ]
        ]
        carrier: Optional[
            Union[
                CellularOneOfCarrierOptionsDef1,
                OneOfCarrierOptionsDef2,
                CellularOneOfCarrierOptionsDef3,
            ]
        ]
        clear_dont_fragment: Optional[
            Union[
                OneOfClearDontFragmentOptionsDef1,
                OneOfClearDontFragmentOptionsDef2,
                OneOfClearDontFragmentOptionsDef3,
            ]
        ]
        color: Optional[
            Union[
                CellularOneOfColorOptionsDef1,
                OneOfColorOptionsDef2,
                OneOfColorOptionsDef3,
            ]
        ]
        exclude_controller_group_list: Optional[
            Union[
                CellularOneOfControllerGroupListOptionsDef1,
                OneOfControllerGroupListOptionsDef2,
                OneOfControllerGroupListOptionsDef3,
            ]
        ]
        group: Optional[
            Union[
                CellularOneOfGroupOptionsDef1,
                OneOfGroupOptionsDef2,
                OneOfGroupOptionsDef3,
            ]
        ]
        hello_interval: Optional[
            Union[
                CellularOneOfHelloIntervalOptionsDef1,
                OneOfHelloIntervalOptionsDef2,
                CellularOneOfHelloIntervalOptionsDef3,
            ]
        ]
        hello_tolerance: Optional[
            Union[
                CellularOneOfHelloToleranceOptionsDef1,
                OneOfHelloToleranceOptionsDef2,
                CellularOneOfHelloToleranceOptionsDef3,
            ]
        ]
        last_resort_circuit: Optional[
            Union[
                OneOfLastResortCircuitOptionsDef1,
                OneOfLastResortCircuitOptionsDef2,
                OneOfLastResortCircuitOptionsDef3,
            ]
        ]
        low_bandwidth_link: Optional[
            Union[
                OneOfLowBandwidthLinkOptionsDef1,
                OneOfLowBandwidthLinkOptionsDef2,
                OneOfLowBandwidthLinkOptionsDef3,
            ]
        ]
        max_control_connections: Optional[
            Union[
                CellularOneOfMaxControlConnectionsOptionsDef1,
                OneOfMaxControlConnectionsOptionsDef2,
                OneOfMaxControlConnectionsOptionsDef3,
            ]
        ]
        mode: Optional[
            Union[CellularOneOfModeOptionsDef1, OneOfModeOptionsDef2]
        ]
        nat_refresh_interval: Optional[
            Union[
                CellularOneOfNatRefreshIntervalOptionsDef1,
                OneOfNatRefreshIntervalOptionsDef2,
                CellularOneOfNatRefreshIntervalOptionsDef3,
            ]
        ]
        network_broadcast: Optional[
            Union[
                OneOfNetworkBroadcastOptionsDef1,
                OneOfNetworkBroadcastOptionsDef2,
                OneOfNetworkBroadcastOptionsDef3,
            ]
        ]
        per_tunnel_qos: Optional[
            Union[
                OneOfPerTunnelQosOptionsDef1,
                OneOfPerTunnelQosOptionsDef2,
                OneOfPerTunnelQosOptionsDef3,
            ]
        ]
        port_hop: Optional[
            Union[
                OneOfPortHopOptionsDef1,
                OneOfPortHopOptionsDef2,
                OneOfPortHopOptionsDef3,
            ]
        ]
        restrict: Optional[
            Union[
                OneOfRestrictOptionsDef1,
                OneOfRestrictOptionsDef2,
                OneOfRestrictOptionsDef3,
            ]
        ]
        tunnel_tcp_mss: Optional[
            Union[
                CellularOneOfTunnelTcpMssAdjustOptionsDef1,
                OneOfTunnelTcpMssAdjustOptionsDef2,
                OneOfTunnelTcpMssAdjustOptionsDef3,
            ]
        ]
        v_bond_as_stun_server: Optional[
            Union[
                OneOfVbondAsStunServerOptionsDef1,
                OneOfVbondAsStunServerOptionsDef2,
                OneOfVbondAsStunServerOptionsDef3,
            ]
        ]
        v_manage_connection_preference: Optional[
            Union[
                CellularOneOfVmanageConnectionPreferenceOptionsDef1,
                OneOfVmanageConnectionPreferenceOptionsDef2,
                CellularOneOfVmanageConnectionPreferenceOptionsDef3,
            ]
        ]


    class CellularAllowService:
        """
        Tunnel Interface Attributes
        """

        all: Optional[
            Union[
                OneOfAllowAllOptionsDef1,
                OneOfAllowAllOptionsDef2,
                OneOfAllowAllOptionsDef3,
            ]
        ]
        bfd: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        bgp: Optional[
            Union[
                OneOfAllowBgpOptionsDef1,
                OneOfAllowBgpOptionsDef2,
                OneOfAllowBgpOptionsDef3,
            ]
        ]
        dhcp: Optional[
            Union[
                OneOfAllowDhcpOptionsDef1,
                OneOfAllowDhcpOptionsDef2,
                OneOfAllowDhcpOptionsDef3,
            ]
        ]
        dns: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        https: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        icmp: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        netconf: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        ntp: Optional[
            Union[
                OneOfAllowNtpOptionsDef1,
                OneOfAllowNtpOptionsDef2,
                OneOfAllowNtpOptionsDef3,
            ]
        ]
        ospf: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        snmp: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        ssh: Optional[
            Union[
                OneOfAllowSshOptionsDef1,
                OneOfAllowSshOptionsDef2,
                OneOfAllowSshOptionsDef3,
            ]
        ]
        stun: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]


    class CellularOneOfEncapsulationEncapOptionsDef:
        option_type: GlobalOptionTypeDef
        value: CellularEncapsulationEncapDef  # pytype: disable=annotation-type-mismatch


    class CellularOneOfEncapsulationPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfEncapsulationWeightOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfEncapsulationWeightOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class CellularEncapsulation:
        encap: CellularOneOfEncapsulationEncapOptionsDef
        preference: Optional[
            Union[
                CellularOneOfEncapsulationPreferenceOptionsDef1,
                OneOfEncapsulationPreferenceOptionsDef2,
                OneOfEncapsulationPreferenceOptionsDef3,
            ]
        ]
        weight: Optional[
            Union[
                CellularOneOfEncapsulationWeightOptionsDef1,
                OneOfEncapsulationWeightOptionsDef2,
                CellularOneOfEncapsulationWeightOptionsDef3,
            ]
        ]


    class CellularOneOfCoreRegionDef1:
        option_type: GlobalOptionTypeDef
        value: CellularCoreRegionDef  # pytype: disable=annotation-type-mismatch


    class CellularOneOfCoreRegionDef2:
        option_type: DefaultOptionTypeDef
        value: CellularDefaultCoreRegionDef  # pytype: disable=annotation-type-mismatch


    class CellularOneOfSecondaryRegionDef1:
        option_type: GlobalOptionTypeDef
        value: CellularSecondaryRegionDef  # pytype: disable=annotation-type-mismatch


    class CellularOneOfSecondaryRegionDef2:
        option_type: DefaultOptionTypeDef
        value: CellularDefaultSecondaryRegionDef  # pytype: disable=annotation-type-mismatch


    class CellularMultiRegionFabric:
        """
        Multi-Region Fabric
        """

        core_region: Optional[
            Union[
                CellularOneOfCoreRegionDef1, CellularOneOfCoreRegionDef2
            ]
        ]
        enable_core_region: Optional[
            Union[OneOfEnableRegionDef1, OneOfEnableRegionDef2]
        ]
        enable_secondary_region: Optional[
            Union[OneOfEnableRegionDef1, OneOfEnableRegionDef2]
        ]
        secondary_region: Optional[
            Union[
                CellularOneOfSecondaryRegionDef1,
                CellularOneOfSecondaryRegionDef2,
            ]
        ]


    class CellularOneOfUdpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfUdpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class CellularOneOfTcpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfTcpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class CellularNatAttributesIpv4:
        """
        NAT Attributes
        """

        tcp_timeout: Union[
            CellularOneOfTcpTimeoutOptionsDef1,
            OneOfTcpTimeoutOptionsDef2,
            CellularOneOfTcpTimeoutOptionsDef3,
        ]
        udp_timeout: Union[
            CellularOneOfUdpTimeoutOptionsDef1,
            OneOfUdpTimeoutOptionsDef2,
            CellularOneOfUdpTimeoutOptionsDef3,
        ]


    class CellularOneOfPeriodOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfPeriodOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class CellularOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnInterfaceCellularOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularShapingRateUpstreamConfig:
        """
        adaptiveQoS Shaping Rate Upstream config
        """

        default_shaping_rate_upstream: Union[
            VpnInterfaceCellularOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_upstream: Union[
            InterfaceCellularOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_upstream: Union[
            CellularOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class WanVpnInterfaceCellularOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportWanVpnInterfaceCellularOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanTransportWanVpnInterfaceCellularOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularShapingRateDownstreamConfig:
        """
        adaptiveQoS Shaping Rate Downstream config
        """

        default_shaping_rate_downstream: Union[
            SdwanTransportWanVpnInterfaceCellularOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_downstream: Union[
            TransportWanVpnInterfaceCellularOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_downstream: Union[
            WanVpnInterfaceCellularOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class CellularAclQos1:
        adaptive_qo_s: Union[
            OneOfQosAdaptiveOptionsDef1, OneOfQosAdaptiveOptionsDef2
        ]
        shaping_rate_upstream: ShapingRateUpstream
        # adaptiveQoS Shaping Rate Upstream config
        shaping_rate_upstream_config: CellularShapingRateUpstreamConfig
        adapt_period: Optional[
            Union[
                CellularOneOfPeriodOptionsDef1,
                OneOfPeriodOptionsDef2,
                CellularOneOfPeriodOptionsDef3,
            ]
        ]
        ipv4_acl_egress: Optional[ParcelReferenceDef]
        ipv4_acl_ingress: Optional[ParcelReferenceDef]
        ipv6_acl_egress: Optional[ParcelReferenceDef]
        ipv6_acl_ingress: Optional[ParcelReferenceDef]
        shaping_rate: Optional[
            Union[
                OneOfShapingRateOptionsDef1,
                OneOfShapingRateOptionsDef2,
                OneOfShapingRateOptionsDef3,
            ]
        ]
        shaping_rate_downstream: Optional[
            Union[
                OneOfShapingRateDownstreamOptionsDef1,
                OneOfShapingRateDownstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Downstream config
        shaping_rate_downstream_config: Optional[
            CellularShapingRateDownstreamConfig
        ]


    class InterfaceCellularOneOfPeriodOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfPeriodOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class FeatureProfileSdwanTransportWanVpnInterfaceCellularOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class V1FeatureProfileSdwanTransportWanVpnInterfaceCellularOneOfShapingRateUpOrDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef11:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularShapingRateUpstreamConfig:
        """
        adaptiveQoS Shaping Rate Upstream config
        """

        default_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef11,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_upstream: Union[
            V1FeatureProfileSdwanTransportWanVpnInterfaceCellularOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_upstream: Union[
            FeatureProfileSdwanTransportWanVpnInterfaceCellularOneOfShapingRateUpOrDownstreamOptionsDef1,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class OneOfShapingRateUpOrDownstreamOptionsDef12:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef13:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef14:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularShapingRateDownstreamConfig:
        """
        adaptiveQoS Shaping Rate Downstream config
        """

        default_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef14,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef13,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef12,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class CellularAclQos2:
        adaptive_qo_s: Union[
            OneOfQosAdaptiveOptionsDef1, OneOfQosAdaptiveOptionsDef2
        ]
        adapt_period: Optional[
            Union[
                InterfaceCellularOneOfPeriodOptionsDef1,
                OneOfPeriodOptionsDef2,
                InterfaceCellularOneOfPeriodOptionsDef3,
            ]
        ]
        ipv4_acl_egress: Optional[ParcelReferenceDef]
        ipv4_acl_ingress: Optional[ParcelReferenceDef]
        ipv6_acl_egress: Optional[ParcelReferenceDef]
        ipv6_acl_ingress: Optional[ParcelReferenceDef]
        shaping_rate: Optional[
            Union[
                OneOfShapingRateOptionsDef1,
                OneOfShapingRateOptionsDef2,
                OneOfShapingRateOptionsDef3,
            ]
        ]
        shaping_rate_downstream: Optional[
            Union[
                OneOfShapingRateDownstreamOptionsDef1,
                OneOfShapingRateDownstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Downstream config
        shaping_rate_downstream_config: Optional[
            InterfaceCellularShapingRateDownstreamConfig
        ]
        shaping_rate_upstream: Optional[
            Union[
                OneOfShapingRateUpstreamOptionsDef1,
                OneOfShapingRateUpstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Upstream config
        shaping_rate_upstream_config: Optional[
            InterfaceCellularShapingRateUpstreamConfig
        ]


    class CellularOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class CellularOneOfMacAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CellularArp:
        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            CellularOneOfIpV4AddressOptionsDef2,
            OneOfIpV4AddressOptionsDef3,
        ]
        mac_address: Union[
            CellularOneOfMacAddressOptionsDef1,
            OneOfMacAddressOptionsDef2,
            OneOfMacAddressOptionsDef3,
        ]


    class CellularOneOfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class CellularOneOfIntrfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfIntrfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class CellularOneOfTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularOneOfTlocExtensionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CellularOneOfTrackerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CellularAdvanced:
        """
        Advanced Attributes
        """

        intrf_mtu: Optional[
            Union[
                CellularOneOfIntrfMtuOptionsDef1,
                OneOfIntrfMtuOptionsDef2,
                CellularOneOfIntrfMtuOptionsDef3,
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
                CellularOneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                CellularOneOfMtuOptionsDef3,
            ]
        ]
        tcp_mss: Optional[
            Union[
                CellularOneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]
        tloc_extension: Optional[
            Union[
                CellularOneOfTlocExtensionOptionsDef1,
                OneOfTlocExtensionOptionsDef2,
                OneOfTlocExtensionOptionsDef3,
            ]
        ]
        tracker: Optional[
            Union[
                CellularOneOfTrackerOptionsDef1,
                OneOfTrackerOptionsDef2,
                OneOfTrackerOptionsDef3,
            ]
        ]


    class VpnInterfaceCellularData:
        description: Union[
            CellularOneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        # Encapsulation for TLOC
        encapsulation: List[CellularEncapsulation]
        interface_name: Union[
            CellularOneOfInterfaceNameOptionsDef1,
            OneOfInterfaceNameOptionsDef2,
        ]
        nat: Union[
            OneOfNatOptionsDef1, OneOfNatOptionsDef2, OneOfNatOptionsDef3
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tunnel_interface: Union[
            OneOfTunnelInterfaceOptionsDef1,
            OneOfTunnelInterfaceOptionsDef2,
        ]
        # ACL/QOS
        acl_qos: Optional[Union[CellularAclQos1, CellularAclQos2]]
        # Advanced Attributes
        advanced: Optional[CellularAdvanced]
        # Tunnel Interface Attributes
        allow_service: Optional[CellularAllowService]
        # Configure ARP entries
        arp: Optional[List[CellularArp]]
        bandwidth_downstream: Optional[
            Union[
                CellularOneOfBandwidthDownstreamOptionsDef1,
                OneOfBandwidthDownstreamOptionsDef2,
                OneOfBandwidthDownstreamOptionsDef3,
            ]
        ]
        bandwidth_upstream: Optional[
            Union[
                CellularOneOfBandwidthUpstreamOptionsDef1,
                OneOfBandwidthUpstreamOptionsDef2,
                OneOfBandwidthUpstreamOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                CellularOneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        enable_ipv6: Optional[
            Union[
                OneOfenableIpV6OptionsDef1,
                OneOfenableIpV6OptionsDef2,
                OneOfenableIpV6OptionsDef3,
            ]
        ]
        # Multi-Region Fabric
        multi_region_fabric: Optional[CellularMultiRegionFabric]
        # NAT Attributes
        nat_attributes_ipv4: Optional[CellularNatAttributesIpv4]
        service_provider: Optional[
            Union[
                OneOfServiceProviderOptionsDef1,
                OneOfServiceProviderOptionsDef2,
                OneOfServiceProviderOptionsDef3,
            ]
        ]
        # Tunnel Interface Attributes
        tunnel: Optional[CellularTunnel]


    class CellularPayload:
        """
        WAN VPN Interface Cellular profile parcel schema for PUT request
        """

        data: VpnInterfaceCellularData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanTransportWanVpnInterfaceCellularPayload:
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
        # WAN VPN Interface Cellular profile parcel schema for PUT request
        payload: Optional[CellularPayload]


    class EditWanVpnInterfaceCellularParcelForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class InterfaceCellularOneOfInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceCellularOneOfDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceCellularOneOfListOfIpV4OptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class InterfaceCellularOneOfBandwidthUpstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfBandwidthDownstreamOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceCellularModeDef  # pytype: disable=annotation-type-mismatch


    class InterfaceCellularOneOfBindOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceCellularOneOfCarrierOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceCellularCarrierDef


    class InterfaceCellularOneOfCarrierOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: InterfaceCellularDefaultCarrierDef  # pytype: disable=annotation-type-mismatch


    class InterfaceCellularOneOfColorOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceCellularColorDef  # pytype: disable=annotation-type-mismatch


    class InterfaceCellularOneOfHelloIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfHelloIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceCellularOneOfHelloToleranceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfHelloToleranceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceCellularOneOfGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfMaxControlConnectionsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfNatRefreshIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfNatRefreshIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceCellularOneOfControllerGroupListOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class InterfaceCellularOneOfVmanageConnectionPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfVmanageConnectionPreferenceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceCellularOneOfTunnelTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularTunnel:
        """
        Tunnel Interface Attributes
        """

        bind: Optional[
            Union[
                InterfaceCellularOneOfBindOptionsDef1,
                OneOfBindOptionsDef2,
                OneOfBindOptionsDef3,
            ]
        ]
        border: Optional[
            Union[
                OneOfBorderOptionsDef1,
                OneOfBorderOptionsDef2,
                OneOfBorderOptionsDef3,
            ]
        ]
        carrier: Optional[
            Union[
                InterfaceCellularOneOfCarrierOptionsDef1,
                OneOfCarrierOptionsDef2,
                InterfaceCellularOneOfCarrierOptionsDef3,
            ]
        ]
        clear_dont_fragment: Optional[
            Union[
                OneOfClearDontFragmentOptionsDef1,
                OneOfClearDontFragmentOptionsDef2,
                OneOfClearDontFragmentOptionsDef3,
            ]
        ]
        color: Optional[
            Union[
                InterfaceCellularOneOfColorOptionsDef1,
                OneOfColorOptionsDef2,
                OneOfColorOptionsDef3,
            ]
        ]
        exclude_controller_group_list: Optional[
            Union[
                InterfaceCellularOneOfControllerGroupListOptionsDef1,
                OneOfControllerGroupListOptionsDef2,
                OneOfControllerGroupListOptionsDef3,
            ]
        ]
        group: Optional[
            Union[
                InterfaceCellularOneOfGroupOptionsDef1,
                OneOfGroupOptionsDef2,
                OneOfGroupOptionsDef3,
            ]
        ]
        hello_interval: Optional[
            Union[
                InterfaceCellularOneOfHelloIntervalOptionsDef1,
                OneOfHelloIntervalOptionsDef2,
                InterfaceCellularOneOfHelloIntervalOptionsDef3,
            ]
        ]
        hello_tolerance: Optional[
            Union[
                InterfaceCellularOneOfHelloToleranceOptionsDef1,
                OneOfHelloToleranceOptionsDef2,
                InterfaceCellularOneOfHelloToleranceOptionsDef3,
            ]
        ]
        last_resort_circuit: Optional[
            Union[
                OneOfLastResortCircuitOptionsDef1,
                OneOfLastResortCircuitOptionsDef2,
                OneOfLastResortCircuitOptionsDef3,
            ]
        ]
        low_bandwidth_link: Optional[
            Union[
                OneOfLowBandwidthLinkOptionsDef1,
                OneOfLowBandwidthLinkOptionsDef2,
                OneOfLowBandwidthLinkOptionsDef3,
            ]
        ]
        max_control_connections: Optional[
            Union[
                InterfaceCellularOneOfMaxControlConnectionsOptionsDef1,
                OneOfMaxControlConnectionsOptionsDef2,
                OneOfMaxControlConnectionsOptionsDef3,
            ]
        ]
        mode: Optional[
            Union[
                InterfaceCellularOneOfModeOptionsDef1,
                OneOfModeOptionsDef2,
            ]
        ]
        nat_refresh_interval: Optional[
            Union[
                InterfaceCellularOneOfNatRefreshIntervalOptionsDef1,
                OneOfNatRefreshIntervalOptionsDef2,
                InterfaceCellularOneOfNatRefreshIntervalOptionsDef3,
            ]
        ]
        network_broadcast: Optional[
            Union[
                OneOfNetworkBroadcastOptionsDef1,
                OneOfNetworkBroadcastOptionsDef2,
                OneOfNetworkBroadcastOptionsDef3,
            ]
        ]
        per_tunnel_qos: Optional[
            Union[
                OneOfPerTunnelQosOptionsDef1,
                OneOfPerTunnelQosOptionsDef2,
                OneOfPerTunnelQosOptionsDef3,
            ]
        ]
        port_hop: Optional[
            Union[
                OneOfPortHopOptionsDef1,
                OneOfPortHopOptionsDef2,
                OneOfPortHopOptionsDef3,
            ]
        ]
        restrict: Optional[
            Union[
                OneOfRestrictOptionsDef1,
                OneOfRestrictOptionsDef2,
                OneOfRestrictOptionsDef3,
            ]
        ]
        tunnel_tcp_mss: Optional[
            Union[
                InterfaceCellularOneOfTunnelTcpMssAdjustOptionsDef1,
                OneOfTunnelTcpMssAdjustOptionsDef2,
                OneOfTunnelTcpMssAdjustOptionsDef3,
            ]
        ]
        v_bond_as_stun_server: Optional[
            Union[
                OneOfVbondAsStunServerOptionsDef1,
                OneOfVbondAsStunServerOptionsDef2,
                OneOfVbondAsStunServerOptionsDef3,
            ]
        ]
        v_manage_connection_preference: Optional[
            Union[
                InterfaceCellularOneOfVmanageConnectionPreferenceOptionsDef1,
                OneOfVmanageConnectionPreferenceOptionsDef2,
                InterfaceCellularOneOfVmanageConnectionPreferenceOptionsDef3,
            ]
        ]


    class InterfaceCellularAllowService:
        """
        Tunnel Interface Attributes
        """

        all: Optional[
            Union[
                OneOfAllowAllOptionsDef1,
                OneOfAllowAllOptionsDef2,
                OneOfAllowAllOptionsDef3,
            ]
        ]
        bfd: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        bgp: Optional[
            Union[
                OneOfAllowBgpOptionsDef1,
                OneOfAllowBgpOptionsDef2,
                OneOfAllowBgpOptionsDef3,
            ]
        ]
        dhcp: Optional[
            Union[
                OneOfAllowDhcpOptionsDef1,
                OneOfAllowDhcpOptionsDef2,
                OneOfAllowDhcpOptionsDef3,
            ]
        ]
        dns: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        https: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        icmp: Optional[
            Union[
                OneOfAllowServiceTrueOptionsDef1,
                OneOfAllowServiceTrueOptionsDef2,
                OneOfAllowServiceTrueOptionsDef3,
            ]
        ]
        netconf: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        ntp: Optional[
            Union[
                OneOfAllowNtpOptionsDef1,
                OneOfAllowNtpOptionsDef2,
                OneOfAllowNtpOptionsDef3,
            ]
        ]
        ospf: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        snmp: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]
        ssh: Optional[
            Union[
                OneOfAllowSshOptionsDef1,
                OneOfAllowSshOptionsDef2,
                OneOfAllowSshOptionsDef3,
            ]
        ]
        stun: Optional[
            Union[
                OneOfAllowServiceFalseOptionsDef1,
                OneOfAllowServiceFalseOptionsDef2,
                OneOfAllowServiceFalseOptionsDef3,
            ]
        ]


    class InterfaceCellularOneOfEncapsulationEncapOptionsDef:
        option_type: GlobalOptionTypeDef
        value: InterfaceCellularEncapsulationEncapDef  # pytype: disable=annotation-type-mismatch


    class InterfaceCellularOneOfEncapsulationPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfEncapsulationWeightOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfEncapsulationWeightOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceCellularEncapsulation:
        encap: InterfaceCellularOneOfEncapsulationEncapOptionsDef
        preference: Optional[
            Union[
                InterfaceCellularOneOfEncapsulationPreferenceOptionsDef1,
                OneOfEncapsulationPreferenceOptionsDef2,
                OneOfEncapsulationPreferenceOptionsDef3,
            ]
        ]
        weight: Optional[
            Union[
                InterfaceCellularOneOfEncapsulationWeightOptionsDef1,
                OneOfEncapsulationWeightOptionsDef2,
                InterfaceCellularOneOfEncapsulationWeightOptionsDef3,
            ]
        ]


    class InterfaceCellularOneOfCoreRegionDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceCellularCoreRegionDef  # pytype: disable=annotation-type-mismatch


    class InterfaceCellularOneOfCoreRegionDef2:
        option_type: DefaultOptionTypeDef
        value: InterfaceCellularDefaultCoreRegionDef  # pytype: disable=annotation-type-mismatch


    class InterfaceCellularOneOfSecondaryRegionDef1:
        option_type: GlobalOptionTypeDef
        value: InterfaceCellularSecondaryRegionDef  # pytype: disable=annotation-type-mismatch


    class InterfaceCellularOneOfSecondaryRegionDef2:
        option_type: DefaultOptionTypeDef
        value: InterfaceCellularDefaultSecondaryRegionDef  # pytype: disable=annotation-type-mismatch


    class InterfaceCellularMultiRegionFabric:
        """
        Multi-Region Fabric
        """

        core_region: Optional[
            Union[
                InterfaceCellularOneOfCoreRegionDef1,
                InterfaceCellularOneOfCoreRegionDef2,
            ]
        ]
        enable_core_region: Optional[
            Union[OneOfEnableRegionDef1, OneOfEnableRegionDef2]
        ]
        enable_secondary_region: Optional[
            Union[OneOfEnableRegionDef1, OneOfEnableRegionDef2]
        ]
        secondary_region: Optional[
            Union[
                InterfaceCellularOneOfSecondaryRegionDef1,
                InterfaceCellularOneOfSecondaryRegionDef2,
            ]
        ]


    class InterfaceCellularOneOfUdpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfUdpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceCellularOneOfTcpTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfTcpTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceCellularNatAttributesIpv4:
        """
        NAT Attributes
        """

        tcp_timeout: Union[
            InterfaceCellularOneOfTcpTimeoutOptionsDef1,
            OneOfTcpTimeoutOptionsDef2,
            InterfaceCellularOneOfTcpTimeoutOptionsDef3,
        ]
        udp_timeout: Union[
            InterfaceCellularOneOfUdpTimeoutOptionsDef1,
            OneOfUdpTimeoutOptionsDef2,
            InterfaceCellularOneOfUdpTimeoutOptionsDef3,
        ]


    class VpnInterfaceCellularOneOfPeriodOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnInterfaceCellularOneOfPeriodOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef15:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef16:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef17:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnInterfaceCellularShapingRateUpstreamConfig:
        """
        adaptiveQoS Shaping Rate Upstream config
        """

        default_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef17,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef16,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef15,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class OneOfShapingRateUpOrDownstreamOptionsDef18:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef19:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef110:
        option_type: GlobalOptionTypeDef
        value: int


    class VpnInterfaceCellularShapingRateDownstreamConfig:
        """
        adaptiveQoS Shaping Rate Downstream config
        """

        default_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef110,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef19,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef18,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class InterfaceCellularAclQos1:
        adaptive_qo_s: Union[
            OneOfQosAdaptiveOptionsDef1, OneOfQosAdaptiveOptionsDef2
        ]
        shaping_rate_upstream: ShapingRateUpstream
        # adaptiveQoS Shaping Rate Upstream config
        shaping_rate_upstream_config: (
            VpnInterfaceCellularShapingRateUpstreamConfig
        )
        adapt_period: Optional[
            Union[
                VpnInterfaceCellularOneOfPeriodOptionsDef1,
                OneOfPeriodOptionsDef2,
                VpnInterfaceCellularOneOfPeriodOptionsDef3,
            ]
        ]
        ipv4_acl_egress: Optional[ParcelReferenceDef]
        ipv4_acl_ingress: Optional[ParcelReferenceDef]
        ipv6_acl_egress: Optional[ParcelReferenceDef]
        ipv6_acl_ingress: Optional[ParcelReferenceDef]
        shaping_rate: Optional[
            Union[
                OneOfShapingRateOptionsDef1,
                OneOfShapingRateOptionsDef2,
                OneOfShapingRateOptionsDef3,
            ]
        ]
        shaping_rate_downstream: Optional[
            Union[
                OneOfShapingRateDownstreamOptionsDef1,
                OneOfShapingRateDownstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Downstream config
        shaping_rate_downstream_config: Optional[
            VpnInterfaceCellularShapingRateDownstreamConfig
        ]


    class WanVpnInterfaceCellularOneOfPeriodOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnInterfaceCellularOneOfPeriodOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef111:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef112:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef113:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnInterfaceCellularShapingRateUpstreamConfig:
        """
        adaptiveQoS Shaping Rate Upstream config
        """

        default_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef113,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef112,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_upstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef111,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class OneOfShapingRateUpOrDownstreamOptionsDef114:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef115:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfShapingRateUpOrDownstreamOptionsDef116:
        option_type: GlobalOptionTypeDef
        value: int


    class WanVpnInterfaceCellularShapingRateDownstreamConfig:
        """
        adaptiveQoS Shaping Rate Downstream config
        """

        default_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef116,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        max_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef115,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]
        min_shaping_rate_downstream: Union[
            OneOfShapingRateUpOrDownstreamOptionsDef114,
            OneOfShapingRateUpOrDownstreamOptionsDef2,
        ]


    class InterfaceCellularAclQos2:
        adaptive_qo_s: Union[
            OneOfQosAdaptiveOptionsDef1, OneOfQosAdaptiveOptionsDef2
        ]
        adapt_period: Optional[
            Union[
                WanVpnInterfaceCellularOneOfPeriodOptionsDef1,
                OneOfPeriodOptionsDef2,
                WanVpnInterfaceCellularOneOfPeriodOptionsDef3,
            ]
        ]
        ipv4_acl_egress: Optional[ParcelReferenceDef]
        ipv4_acl_ingress: Optional[ParcelReferenceDef]
        ipv6_acl_egress: Optional[ParcelReferenceDef]
        ipv6_acl_ingress: Optional[ParcelReferenceDef]
        shaping_rate: Optional[
            Union[
                OneOfShapingRateOptionsDef1,
                OneOfShapingRateOptionsDef2,
                OneOfShapingRateOptionsDef3,
            ]
        ]
        shaping_rate_downstream: Optional[
            Union[
                OneOfShapingRateDownstreamOptionsDef1,
                OneOfShapingRateDownstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Downstream config
        shaping_rate_downstream_config: Optional[
            WanVpnInterfaceCellularShapingRateDownstreamConfig
        ]
        shaping_rate_upstream: Optional[
            Union[
                OneOfShapingRateUpstreamOptionsDef1,
                OneOfShapingRateUpstreamOptionsDef2,
            ]
        ]
        # adaptiveQoS Shaping Rate Upstream config
        shaping_rate_upstream_config: Optional[
            WanVpnInterfaceCellularShapingRateUpstreamConfig
        ]


    class InterfaceCellularOneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceCellularOneOfMacAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceCellularArp:
        ip_address: Union[
            OneOfIpV4AddressOptionsDef1,
            InterfaceCellularOneOfIpV4AddressOptionsDef2,
            OneOfIpV4AddressOptionsDef3,
        ]
        mac_address: Union[
            InterfaceCellularOneOfMacAddressOptionsDef1,
            OneOfMacAddressOptionsDef2,
            OneOfMacAddressOptionsDef3,
        ]


    class InterfaceCellularOneOfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceCellularOneOfIntrfMtuOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfIntrfMtuOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class InterfaceCellularOneOfTcpMssAdjustOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class InterfaceCellularOneOfTlocExtensionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceCellularOneOfTrackerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class InterfaceCellularAdvanced:
        """
        Advanced Attributes
        """

        intrf_mtu: Optional[
            Union[
                InterfaceCellularOneOfIntrfMtuOptionsDef1,
                OneOfIntrfMtuOptionsDef2,
                InterfaceCellularOneOfIntrfMtuOptionsDef3,
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
                InterfaceCellularOneOfMtuOptionsDef1,
                OneOfMtuOptionsDef2,
                InterfaceCellularOneOfMtuOptionsDef3,
            ]
        ]
        tcp_mss: Optional[
            Union[
                InterfaceCellularOneOfTcpMssAdjustOptionsDef1,
                OneOfTcpMssAdjustOptionsDef2,
                OneOfTcpMssAdjustOptionsDef3,
            ]
        ]
        tloc_extension: Optional[
            Union[
                InterfaceCellularOneOfTlocExtensionOptionsDef1,
                OneOfTlocExtensionOptionsDef2,
                OneOfTlocExtensionOptionsDef3,
            ]
        ]
        tracker: Optional[
            Union[
                InterfaceCellularOneOfTrackerOptionsDef1,
                OneOfTrackerOptionsDef2,
                OneOfTrackerOptionsDef3,
            ]
        ]


    class WanVpnInterfaceCellularData:
        description: Union[
            InterfaceCellularOneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        # Encapsulation for TLOC
        encapsulation: List[InterfaceCellularEncapsulation]
        interface_name: Union[
            InterfaceCellularOneOfInterfaceNameOptionsDef1,
            OneOfInterfaceNameOptionsDef2,
        ]
        nat: Union[
            OneOfNatOptionsDef1, OneOfNatOptionsDef2, OneOfNatOptionsDef3
        ]
        shutdown: Union[
            OneOfShutdownOptionsDef1,
            OneOfShutdownOptionsDef2,
            OneOfShutdownOptionsDef3,
        ]
        tunnel_interface: Union[
            OneOfTunnelInterfaceOptionsDef1,
            OneOfTunnelInterfaceOptionsDef2,
        ]
        # ACL/QOS
        acl_qos: Optional[
            Union[InterfaceCellularAclQos1, InterfaceCellularAclQos2]
        ]
        # Advanced Attributes
        advanced: Optional[InterfaceCellularAdvanced]
        # Tunnel Interface Attributes
        allow_service: Optional[InterfaceCellularAllowService]
        # Configure ARP entries
        arp: Optional[List[InterfaceCellularArp]]
        bandwidth_downstream: Optional[
            Union[
                InterfaceCellularOneOfBandwidthDownstreamOptionsDef1,
                OneOfBandwidthDownstreamOptionsDef2,
                OneOfBandwidthDownstreamOptionsDef3,
            ]
        ]
        bandwidth_upstream: Optional[
            Union[
                InterfaceCellularOneOfBandwidthUpstreamOptionsDef1,
                OneOfBandwidthUpstreamOptionsDef2,
                OneOfBandwidthUpstreamOptionsDef3,
            ]
        ]
        dhcp_helper: Optional[
            Union[
                OneOfListOfIpV4OptionsDef1,
                InterfaceCellularOneOfListOfIpV4OptionsDef2,
                OneOfListOfIpV4OptionsDef3,
            ]
        ]
        enable_ipv6: Optional[
            Union[
                OneOfenableIpV6OptionsDef1,
                OneOfenableIpV6OptionsDef2,
                OneOfenableIpV6OptionsDef3,
            ]
        ]
        # Multi-Region Fabric
        multi_region_fabric: Optional[InterfaceCellularMultiRegionFabric]
        # NAT Attributes
        nat_attributes_ipv4: Optional[InterfaceCellularNatAttributesIpv4]
        service_provider: Optional[
            Union[
                OneOfServiceProviderOptionsDef1,
                OneOfServiceProviderOptionsDef2,
                OneOfServiceProviderOptionsDef3,
            ]
        ]
        # Tunnel Interface Attributes
        tunnel: Optional[InterfaceCellularTunnel]


    class EditWanVpnInterfaceCellularParcelForTransportPutRequest:
        """
        WAN VPN Interface Cellular profile parcel schema for PUT request
        """

        data: WanVpnInterfaceCellularData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


