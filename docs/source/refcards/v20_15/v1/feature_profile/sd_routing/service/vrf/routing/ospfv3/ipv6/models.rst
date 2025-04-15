======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    OptionType = Literal["default", "global"]

    MetricTypeDef = Literal["type1", "type2"]

    Ipv6RedistributeProtocolDef = Literal[
        "bgp", "connected", "eigrp", "static"
    ]

    Value = Literal["stub"]

    Ipv6Value = Literal["nssa"]

    Ospfv3Ipv6Value = Literal["normal"]

    AreaInterfaceNetworkDef = Literal[
        "broadcast",
        "non-broadcast",
        "point-to-multipoint",
        "point-to-point",
    ]

    RoutingOspfv3Ipv6Value = Literal["no-auth"]

    VrfRoutingOspfv3Ipv6Value = Literal["ipsec-sha1"]


    class OneOfProcessIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfProcessIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressDefaultOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressDefaultOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfIpV4AddressDefaultOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfDistanceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDistanceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDistanceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfExternalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfExternalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfExternalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfInterAreaOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterAreaOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterAreaOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIntraAreaOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIntraAreaOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIntraAreaOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class BasicConfigDef:
        process_id: Union[
            OneOfProcessIdOptionsDef1, OneOfProcessIdOptionsDef2
        ]
        distance: Optional[
            Union[
                OneOfDistanceOptionsDef1,
                OneOfDistanceOptionsDef2,
                OneOfDistanceOptionsDef3,
            ]
        ]
        external_distance: Optional[
            Union[
                OneOfExternalOptionsDef1,
                OneOfExternalOptionsDef2,
                OneOfExternalOptionsDef3,
            ]
        ]
        inter_area_distance: Optional[
            Union[
                OneOfInterAreaOptionsDef1,
                OneOfInterAreaOptionsDef2,
                OneOfInterAreaOptionsDef3,
            ]
        ]
        intra_area_distance: Optional[
            Union[
                OneOfIntraAreaOptionsDef1,
                OneOfIntraAreaOptionsDef2,
                OneOfIntraAreaOptionsDef3,
            ]
        ]
        router_id: Optional[
            Union[
                OneOfIpV4AddressDefaultOptionsDef1,
                OneOfIpV4AddressDefaultOptionsDef2,
                OneOfIpV4AddressDefaultOptionsDef3,
            ]
        ]


    class OneOfReferenceBandwidthOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfReferenceBandwidthOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfReferenceBandwidthOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


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


    class Originate:
        """
        Distribute default external route into OSPF disabled
        """

        option_type: OptionType
        value: bool


    class OneOfDefaultOriginateOptionsDef1:
        # Distribute default external route into OSPF disabled
        originate: Optional[Originate]


    class Ipv6Originate:
        """
        Distribute default external route into OSPF enabled
        """

        option_type: GlobalOptionTypeDef
        value: bool


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


    class OneOfMetricOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMetricOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMetricOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfMetricTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: MetricTypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfMetricTypeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMetricTypeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfDefaultOriginateOptionsDef2:
        # Distribute default external route into OSPF enabled
        originate: Ipv6Originate
        always: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        metric: Optional[
            Union[
                OneOfMetricOptionsDef1,
                OneOfMetricOptionsDef2,
                OneOfMetricOptionsDef3,
            ]
        ]
        metric_type: Optional[
            Union[
                OneOfMetricTypeOptionsDef1,
                OneOfMetricTypeOptionsDef2,
                OneOfMetricTypeOptionsDef3,
            ]
        ]


    class OneOfDelayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDelayOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDelayOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfInitialHoldOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInitialHoldOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInitialHoldOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfMaxHoldOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMaxHoldOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMaxHoldOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SpfTimersDef:
        delay: Optional[
            Union[
                OneOfDelayOptionsDef1,
                OneOfDelayOptionsDef2,
                OneOfDelayOptionsDef3,
            ]
        ]
        initial_hold: Optional[
            Union[
                OneOfInitialHoldOptionsDef1,
                OneOfInitialHoldOptionsDef2,
                OneOfInitialHoldOptionsDef3,
            ]
        ]
        max_hold: Optional[
            Union[
                OneOfMaxHoldOptionsDef1,
                OneOfMaxHoldOptionsDef2,
                OneOfMaxHoldOptionsDef3,
            ]
        ]


    class OneOfRoutePolicyNameOptionsDef1:
        option_type: DefaultOptionTypeDef


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRoutePolicyNameOptionsDef2:
        ref_id: RefId


    class AdvancedConfigDef:
        compatible_rfc1583: Optional[
            Union[
                OneOfOnBooleanDefaultTrueOptionsDef1,
                OneOfOnBooleanDefaultTrueOptionsDef2,
                OneOfOnBooleanDefaultTrueOptionsDef3,
            ]
        ]
        default_originate: Optional[
            Union[
                OneOfDefaultOriginateOptionsDef1,
                OneOfDefaultOriginateOptionsDef2,
            ]
        ]
        filter: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        policy_name: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        reference_bandwidth: Optional[
            Union[
                OneOfReferenceBandwidthOptionsDef1,
                OneOfReferenceBandwidthOptionsDef2,
                OneOfReferenceBandwidthOptionsDef3,
            ]
        ]
        spf_timers: Optional[SpfTimersDef]


    class OneOfIpv6RedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Ipv6RedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class OneOfIpv6RedistributeProtocolOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Ipv6RedistributeProtocolsObjDef:
        protocol: Union[
            OneOfIpv6RedistributeProtocolOptionsDef1,
            OneOfIpv6RedistributeProtocolOptionsDef2,
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]


    class Action:
        """
        Not advertise maximum metric Router LSA policy by default
        """

        option_type: OptionType
        value: Any


    class OneOfMaxMetricRouterLsaOptionsDef1:
        # Not advertise maximum metric Router LSA policy by default
        action: Action


    class Ipv6Action:
        """
        Advertise maximum metric Router LSA immediately
        """

        option_type: Any
        value: Any


    class OneOfMaxMetricRouterLsaOptionsDef2:
        # Advertise maximum metric Router LSA immediately
        action: Ipv6Action


    class Ospfv3Ipv6Action:
        """
        Advertise maximum metric router LSA after router start up with configured duration time(seconds)
        """

        option_type: Any
        value: Any


    class OneOfOnStartUpTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfOnStartUpTimeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMaxMetricRouterLsaOptionsDef3:
        # Advertise maximum metric router LSA after router start up with configured duration time(seconds)
        action: Ospfv3Ipv6Action
        on_start_up_time: Union[
            OneOfOnStartUpTimeOptionsDef1, OneOfOnStartUpTimeOptionsDef2
        ]


    class OneOfAreaNumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAreaNumOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class AreaType:
        """
        stub area type
        """

        option_type: GlobalOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfAreaTypeConfigOptionsDef1:
        # stub area type
        area_type: Optional[AreaType]
        no_summary: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]


    class Ipv6AreaType:
        """
        NSSA area type
        """

        option_type: GlobalOptionTypeDef
        value: Ipv6Value  # pytype: disable=annotation-type-mismatch


    class OneOfAreaTypeConfigOptionsDef2:
        always_translate: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # NSSA area type
        area_type: Optional[Ipv6AreaType]
        no_summary: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]


    class Ospfv3Ipv6AreaType:
        """
        Normal area type, area number 0 only support normal area type
        """

        option_type: GlobalOptionTypeDef
        value: Ospfv3Ipv6Value  # pytype: disable=annotation-type-mismatch


    class OneOfAreaTypeConfigOptionsDef3:
        # Normal area type, area number 0 only support normal area type
        area_type: Optional[Ospfv3Ipv6AreaType]


    class DefaultOptionNoDefaultDef:
        option_type: DefaultOptionTypeDef


    class OneOfAreaTypeConfigOptionsDef4:
        area_type: Optional[DefaultOptionNoDefaultDef]


    class OneOfAreaInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAreaInterfaceNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaInterfaceHelloIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAreaInterfaceHelloIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaInterfaceHelloIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfAreaInterfaceDeadIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAreaInterfaceDeadIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaInterfaceDeadIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfAreaInterfaceRetransmitIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAreaInterfaceRetransmitIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaInterfaceRetransmitIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfAreaInterfaceCostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAreaInterfaceCostOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaInterfaceCostOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfAreaInterfaceNetworkOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AreaInterfaceNetworkDef  # pytype: disable=annotation-type-mismatch


    class OneOfAreaInterfaceNetworkOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaInterfaceNetworkOptionsDef3:
        option_type: DefaultOptionTypeDef


    class AreaInterfaceNoAuthTypeDef:
        option_type: OptionType
        value: RoutingOspfv3Ipv6Value  # pytype: disable=annotation-type-mismatch


    class OneOfAreaInterfaceAuthConfigOptionsDef1:
        auth_type: AreaInterfaceNoAuthTypeDef


    class AreaInterfaceIpsecSha1AuthTypeDef:
        option_type: GlobalOptionTypeDef
        value: VrfRoutingOspfv3Ipv6Value  # pytype: disable=annotation-type-mismatch


    class OneOfAreaInterfaceSpiOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAreaInterfaceSpiOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaInterfaceSha1AuthKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAreaInterfaceSha1AuthKeyOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaInterfaceAuthConfigOptionsDef2:
        auth_key: Union[
            OneOfAreaInterfaceSha1AuthKeyOptionsDef1,
            OneOfAreaInterfaceSha1AuthKeyOptionsDef2,
        ]
        auth_type: AreaInterfaceIpsecSha1AuthTypeDef
        spi: Union[
            OneOfAreaInterfaceSpiOptionsDef1,
            OneOfAreaInterfaceSpiOptionsDef2,
        ]


    class AreaInterfaceDef:
        if_name: Union[
            OneOfAreaInterfaceNameOptionsDef1,
            OneOfAreaInterfaceNameOptionsDef2,
        ]
        authentication_config: Optional[
            Union[
                OneOfAreaInterfaceAuthConfigOptionsDef1,
                OneOfAreaInterfaceAuthConfigOptionsDef2,
            ]
        ]
        cost: Optional[
            Union[
                OneOfAreaInterfaceCostOptionsDef1,
                OneOfAreaInterfaceCostOptionsDef2,
                OneOfAreaInterfaceCostOptionsDef3,
            ]
        ]
        dead_interval: Optional[
            Union[
                OneOfAreaInterfaceDeadIntervalOptionsDef1,
                OneOfAreaInterfaceDeadIntervalOptionsDef2,
                OneOfAreaInterfaceDeadIntervalOptionsDef3,
            ]
        ]
        hello_interval: Optional[
            Union[
                OneOfAreaInterfaceHelloIntervalOptionsDef1,
                OneOfAreaInterfaceHelloIntervalOptionsDef2,
                OneOfAreaInterfaceHelloIntervalOptionsDef3,
            ]
        ]
        network_type: Optional[
            Union[
                OneOfAreaInterfaceNetworkOptionsDef1,
                OneOfAreaInterfaceNetworkOptionsDef2,
                OneOfAreaInterfaceNetworkOptionsDef3,
            ]
        ]
        passive_interface: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        retransmit_interval: Optional[
            Union[
                OneOfAreaInterfaceRetransmitIntervalOptionsDef1,
                OneOfAreaInterfaceRetransmitIntervalOptionsDef2,
                OneOfAreaInterfaceRetransmitIntervalOptionsDef3,
            ]
        ]


    class OneOfIpv6PrefixGlobalVariableWithoutDefault1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6PrefixGlobalVariableWithoutDefault2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaRangeCostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAreaRangeCostOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaRangeCostOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Ipv6AreaRangeDef:
        network: Union[
            OneOfIpv6PrefixGlobalVariableWithoutDefault1,
            OneOfIpv6PrefixGlobalVariableWithoutDefault2,
        ]
        no_advertise: Union[
            OneOfOnBooleanDefaultFalseOptionsDef1,
            OneOfOnBooleanDefaultFalseOptionsDef2,
            OneOfOnBooleanDefaultFalseOptionsDef3,
        ]
        cost: Optional[
            Union[
                OneOfAreaRangeCostOptionsDef1,
                OneOfAreaRangeCostOptionsDef2,
                OneOfAreaRangeCostOptionsDef3,
            ]
        ]


    class Area:
        area_num: Union[OneOfAreaNumOptionsDef1, OneOfAreaNumOptionsDef2]
        # Set OSPF interface parameters
        interfaces: List[AreaInterfaceDef]
        area_type_config: Optional[
            Union[
                OneOfAreaTypeConfigOptionsDef1,
                OneOfAreaTypeConfigOptionsDef2,
                OneOfAreaTypeConfigOptionsDef3,
                OneOfAreaTypeConfigOptionsDef4,
            ]
        ]
        # Summarize OSPF routes at an area boundary
        ranges: Optional[List[Ipv6AreaRangeDef]]


    class Data:
        """
        IPv6 address family configuration
        """

        # Configure OSPFv3 IPv6 area
        area: List[Area]
        basic: BasicConfigDef
        advanced: Optional[AdvancedConfigDef]
        max_metric_router_lsa: Optional[
            Union[
                OneOfMaxMetricRouterLsaOptionsDef1,
                OneOfMaxMetricRouterLsaOptionsDef2,
                OneOfMaxMetricRouterLsaOptionsDef3,
            ]
        ]
        redistribute: Optional[List[Ipv6RedistributeProtocolsObjDef]]


    class Payload:
        """
        Routing protocol OSPFv3 for IPv6 Address family feature schema
        """

        # IPv6 address family configuration
        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetServiceVrfAssociatedRoutingOspfv3Ipv6ParcelsGetResponse:
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
        # Routing protocol OSPFv3 for IPv6 Address family feature schema
        payload: Optional[Payload]


    class CreateServiceVrfAndRoutingOspfv3Ipv6FeatureAssociationPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateServiceVrfAndRoutingOspfv3Ipv6FeatureAssociationPostRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class GetSingleSdRoutingServiceVrfRoutingOspfv3Ipv6Payload:
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
        # Routing protocol OSPFv3 for IPv6 Address family feature schema
        payload: Optional[Payload]


    class EditServiceVrfAndRoutingOspfv3Ipv6FeatureAssociationPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditServiceVrfAndRoutingOspfv3Ipv6FeatureAssociationPutRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


