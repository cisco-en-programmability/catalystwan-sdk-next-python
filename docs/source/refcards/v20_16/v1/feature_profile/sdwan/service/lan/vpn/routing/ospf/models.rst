======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    MetricTypeDef = Literal["type1", "type2"]

    RedistributeProtocolDef = Literal[
        "bgp", "connected", "eigrp", "nat", "omp", "static"
    ]

    RouterLsaAdTypeDef = Literal["administrative", "on-startup"]

    AreaATypeDef = Literal["nssa", "stub"]

    AreaInterfaceNetworkDef = Literal[
        "broadcast",
        "non-broadcast",
        "point-to-multipoint",
        "point-to-point",
    ]

    DefaultAreaInterfaceNetworkDef = Literal["broadcast"]

    AreaInterfaceTypeDef = Literal["message-digest"]

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


    class OneOfRouterIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRouterIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRouterIdOptionsDef3:
        option_type: DefaultOptionTypeDef


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


    class OneOfRfc1583OptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfRfc1583OptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRfc1583OptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfOriginateOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOriginateOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfAlwaysOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAlwaysOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAlwaysOptionsDef3:
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


    class OneOfRedistributeProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: RedistributeProtocolDef  # pytype: disable=annotation-type-mismatch


    class OneOfRedistributeProtocolOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRedistributeDiaOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfRedistributeDiaOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRedistributeDiaOptionsDef3:
        option_type: DefaultOptionTypeDef
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


    class OneOfRoutePolicyNameOptionsDef1:
        option_type: DefaultOptionTypeDef


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRoutePolicyNameOptionsDef2:
        ref_id: RefId


    class Redistribute:
        protocol: Union[
            OneOfRedistributeProtocolOptionsDef1,
            OneOfRedistributeProtocolOptionsDef2,
        ]
        dia: Optional[
            Union[
                OneOfRedistributeDiaOptionsDef1,
                OneOfRedistributeDiaOptionsDef2,
                OneOfRedistributeDiaOptionsDef3,
            ]
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        translate_rib_metric: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]


    class OneOfRouterLsaAdTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            RouterLsaAdTypeDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfRouterLsaTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRouterLsaTimeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class RouterLsa:
        ad_type: OneOfRouterLsaAdTypeOptionsDef
        time: Optional[
            Union[
                OneOfRouterLsaTimeOptionsDef1,
                OneOfRouterLsaTimeOptionsDef2,
            ]
        ]


    class OneOfAreaANumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAreaANumOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaATypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AreaATypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfAreaATypeOptionsDef2:
        option_type: DefaultOptionTypeDef


    class OneOfAreaNoSummaryOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAreaNoSummaryOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaNoSummaryOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


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


    class OneOfAreaInterfacePriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAreaInterfacePriorityOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaInterfacePriorityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfAreaInterfaceNetworkOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AreaInterfaceNetworkDef


    class OneOfAreaInterfaceNetworkOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaInterfaceNetworkOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultAreaInterfaceNetworkDef  # pytype: disable=annotation-type-mismatch


    class OneOfAreaInterfacePassiveInterfaceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAreaInterfacePassiveInterfaceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaInterfacePassiveInterfaceOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfAreaInterfaceTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AreaInterfaceTypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfAreaInterfaceTypeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaInterfaceTypeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfAreaInterfaceMessageDigestKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAreaInterfaceMessageDigestKeyOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaInterfaceMessageDigestKeyOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfAreaInterfaceMd5OptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAreaInterfaceMd5OptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaInterfaceMd5OptionsDef3:
        option_type: DefaultOptionTypeDef


    class Interface:
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
        md5: Optional[
            Union[
                OneOfAreaInterfaceMd5OptionsDef1,
                OneOfAreaInterfaceMd5OptionsDef2,
                OneOfAreaInterfaceMd5OptionsDef3,
            ]
        ]
        message_digest_key: Optional[
            Union[
                OneOfAreaInterfaceMessageDigestKeyOptionsDef1,
                OneOfAreaInterfaceMessageDigestKeyOptionsDef2,
                OneOfAreaInterfaceMessageDigestKeyOptionsDef3,
            ]
        ]
        name: Optional[
            Union[
                OneOfAreaInterfaceNameOptionsDef1,
                OneOfAreaInterfaceNameOptionsDef2,
            ]
        ]
        network: Optional[
            Union[
                OneOfAreaInterfaceNetworkOptionsDef1,
                OneOfAreaInterfaceNetworkOptionsDef2,
                OneOfAreaInterfaceNetworkOptionsDef3,
            ]
        ]
        passive_interface: Optional[
            Union[
                OneOfAreaInterfacePassiveInterfaceOptionsDef1,
                OneOfAreaInterfacePassiveInterfaceOptionsDef2,
                OneOfAreaInterfacePassiveInterfaceOptionsDef3,
            ]
        ]
        priority: Optional[
            Union[
                OneOfAreaInterfacePriorityOptionsDef1,
                OneOfAreaInterfacePriorityOptionsDef2,
                OneOfAreaInterfacePriorityOptionsDef3,
            ]
        ]
        retransmit_interval: Optional[
            Union[
                OneOfAreaInterfaceRetransmitIntervalOptionsDef1,
                OneOfAreaInterfaceRetransmitIntervalOptionsDef2,
                OneOfAreaInterfaceRetransmitIntervalOptionsDef3,
            ]
        ]
        type_: Optional[
            Union[
                OneOfAreaInterfaceTypeOptionsDef1,
                OneOfAreaInterfaceTypeOptionsDef2,
                OneOfAreaInterfaceTypeOptionsDef3,
            ]
        ]


    class OneOfAreaRangeIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaRangeIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAreaRangeIpV4SubnetMaskOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaRangeIpV4SubnetMaskOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: (
            Ipv4SubnetMaskDef  # pytype: disable=annotation-type-mismatch
        )


    class Address:
        """
        Set matching prefix
        """

        ip_address: Optional[
            Union[
                OneOfAreaRangeIpV4AddressOptionsDef1,
                OneOfAreaRangeIpV4AddressOptionsDef2,
            ]
        ]
        subnet_mask: Optional[
            Union[
                OneOfAreaRangeIpV4SubnetMaskOptionsDef1,
                OneOfAreaRangeIpV4SubnetMaskOptionsDef2,
            ]
        ]


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


    class OneOfAreaRangeNoAdvertiseOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAreaRangeNoAdvertiseOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAreaRangeNoAdvertiseOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class Range:
        # Set matching prefix
        address: Optional[Address]
        cost: Optional[
            Union[
                OneOfAreaRangeCostOptionsDef1,
                OneOfAreaRangeCostOptionsDef2,
                OneOfAreaRangeCostOptionsDef3,
            ]
        ]
        no_advertise: Optional[
            Union[
                OneOfAreaRangeNoAdvertiseOptionsDef1,
                OneOfAreaRangeNoAdvertiseOptionsDef2,
                OneOfAreaRangeNoAdvertiseOptionsDef3,
            ]
        ]


    class Area:
        a_num: Union[OneOfAreaANumOptionsDef1, OneOfAreaANumOptionsDef2]
        a_type: Optional[
            Union[OneOfAreaATypeOptionsDef1, OneOfAreaATypeOptionsDef2]
        ]
        # Set OSPF interface parameters
        interface: Optional[List[Interface]]
        no_summary: Optional[
            Union[
                OneOfAreaNoSummaryOptionsDef1,
                OneOfAreaNoSummaryOptionsDef2,
                OneOfAreaNoSummaryOptionsDef3,
            ]
        ]
        # Summarize OSPF routes at an area boundary
        range: Optional[List[Range]]


    class Data:
        always: Optional[
            Union[
                OneOfAlwaysOptionsDef1,
                OneOfAlwaysOptionsDef2,
                OneOfAlwaysOptionsDef3,
            ]
        ]
        # Configure OSPF area
        area: Optional[List[Area]]
        delay: Optional[
            Union[
                OneOfDelayOptionsDef1,
                OneOfDelayOptionsDef2,
                OneOfDelayOptionsDef3,
            ]
        ]
        external: Optional[
            Union[
                OneOfExternalOptionsDef1,
                OneOfExternalOptionsDef2,
                OneOfExternalOptionsDef3,
            ]
        ]
        initial_hold: Optional[
            Union[
                OneOfInitialHoldOptionsDef1,
                OneOfInitialHoldOptionsDef2,
                OneOfInitialHoldOptionsDef3,
            ]
        ]
        inter_area: Optional[
            Union[
                OneOfInterAreaOptionsDef1,
                OneOfInterAreaOptionsDef2,
                OneOfInterAreaOptionsDef3,
            ]
        ]
        intra_area: Optional[
            Union[
                OneOfIntraAreaOptionsDef1,
                OneOfIntraAreaOptionsDef2,
                OneOfIntraAreaOptionsDef3,
            ]
        ]
        max_hold: Optional[
            Union[
                OneOfMaxHoldOptionsDef1,
                OneOfMaxHoldOptionsDef2,
                OneOfMaxHoldOptionsDef3,
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
        originate: Optional[
            Union[OneOfOriginateOptionsDef1, OneOfOriginateOptionsDef2]
        ]
        # Redistribute routes
        redistribute: Optional[List[Redistribute]]
        reference_bandwidth: Optional[
            Union[
                OneOfReferenceBandwidthOptionsDef1,
                OneOfReferenceBandwidthOptionsDef2,
                OneOfReferenceBandwidthOptionsDef3,
            ]
        ]
        rfc1583: Optional[
            Union[
                OneOfRfc1583OptionsDef1,
                OneOfRfc1583OptionsDef2,
                OneOfRfc1583OptionsDef3,
            ]
        ]
        route_policy: Optional[
            Union[
                OneOfRoutePolicyNameOptionsDef1,
                OneOfRoutePolicyNameOptionsDef2,
            ]
        ]
        router_id: Optional[
            Union[
                OneOfRouterIdOptionsDef1,
                OneOfRouterIdOptionsDef2,
                OneOfRouterIdOptionsDef3,
            ]
        ]
        # Advertise own router LSA with infinite distance
        router_lsa: Optional[List[RouterLsa]]


    class Payload:
        """
        routing ospf profile parcel schema for request
        """

        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetLanVpnAssociatedRoutingOspfParcelsForServiceGetResponse:
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
        # routing ospf profile parcel schema for request
        payload: Optional[Payload]


    class CreateLanVpnAndRoutingOspfParcelAssociationForServicePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateLanVpnAndRoutingOspfParcelAssociationForServicePostRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class GetSingleSdwanServiceLanVpnRoutingOspfPayload:
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
        # routing ospf profile parcel schema for request
        payload: Optional[Payload]


    class EditLanVpnAndRoutingOspfParcelAssociationForServicePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditLanVpnAndRoutingOspfParcelAssociationForServicePutRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


