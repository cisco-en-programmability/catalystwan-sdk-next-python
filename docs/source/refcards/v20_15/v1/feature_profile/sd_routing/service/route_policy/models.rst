======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    DefaultActionDef = Literal["accept", "reject"]

    DefaultOptionTypeDef = Literal["default"]

    Value = Literal["reject"]

    SequencesBaseActionDef = Literal["accept", "reject"]

    ProtocolDef = Literal["BOTH", "IPV4", "IPV6"]

    RoutePolicyValue = Literal["IPV4"]

    VariableOptionTypeDef = Literal["variable"]

    MetricTypeDef = Literal["type1", "type2"]

    OriginDef = Literal["EGP", "IGP", "Incomplete"]


    class OneOfDefaultActionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: DefaultActionDef


    class OneOfDefaultActionOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfSequencesSequenceIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSequencesSequenceNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSequencesBaseActionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SequencesBaseActionDef


    class OneOfSequencesBaseActionOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfSequencesProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ProtocolDef


    class OneOfSequencesProtocolOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: (
            RoutePolicyValue  # pytype: disable=annotation-type-mismatch
        )


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class ParcelReferenceDef:
        ref_id: RefId


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultFalseNoVariableOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfSequencesMatchEntriesCommunityListDef1:
        exact: Union[
            OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
            OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
        ]
        standard_community_list: List[ParcelReferenceDef]


    class OneOfSequencesMatchEntriesCommunityListDef2:
        expanded_community_list: List[ParcelReferenceDef]


    class OneOfSequencesMatchEntriesBgpLocalPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class OneOfSequencesMatchEntriesMetricOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class OneOfSequencesMatchEntriesOspfTagOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class OneOfSequencesMatchEntriesIpv4AddressDef1:
        prefix_list: List[ParcelReferenceDef]


    class OneOfSequencesMatchEntriesIpv4AddressDef2:
        acl_name_list: List[ParcelReferenceDef]


    class OneOfSequencesMatchEntriesIpv4NextHopDef1:
        prefix_list: List[ParcelReferenceDef]


    class OneOfSequencesMatchEntriesIpv4NextHopDef2:
        acl_name_list: List[ParcelReferenceDef]


    class OneOfSequencesInterfaceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class MatchEntries:
        as_path_list: Optional[ParcelReferenceDef]
        bgp_local_preference: Optional[
            OneOfSequencesMatchEntriesBgpLocalPreferenceOptionsDef
        ]
        community_list: Optional[
            Union[
                OneOfSequencesMatchEntriesCommunityListDef1,
                OneOfSequencesMatchEntriesCommunityListDef2,
            ]
        ]
        ext_community_list: Optional[List[ParcelReferenceDef]]
        interface: Optional[OneOfSequencesInterfaceOptionsDef]
        ipv4_address: Optional[
            Union[
                OneOfSequencesMatchEntriesIpv4AddressDef1,
                OneOfSequencesMatchEntriesIpv4AddressDef2,
            ]
        ]
        ipv4_next_hop: Optional[
            Union[
                OneOfSequencesMatchEntriesIpv4NextHopDef1,
                OneOfSequencesMatchEntriesIpv4NextHopDef2,
            ]
        ]
        ipv6_address: Optional[ParcelReferenceDef]
        ipv6_next_hop: Optional[ParcelReferenceDef]
        metric: Optional[OneOfSequencesMatchEntriesMetricOptionsDef]
        ospf_tag: Optional[OneOfSequencesMatchEntriesOspfTagOptionsDef]


    class SequencesActionsEnableAcceptOptionsDef:
        option_type: DefaultOptionTypeDef
        value: bool


    class PrependOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[Union[int, str]]


    class SequencesActionsSetAsPathOptionsDef:
        prepend: Optional[PrependOptionsDef]


    class OneOfSequencesActionsSetCommunityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[Union[str, str]]


    class OneOfSequencesActionsSetCommunityOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class SequencesActionsSetCommunityDef:
        additive: Optional[
            Union[
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef1,
                OneOfOnBooleanDefaultFalseNoVariableOptionsDef2,
            ]
        ]
        community: Optional[
            Union[
                OneOfSequencesActionsSetCommunityOptionsDef1,
                OneOfSequencesActionsSetCommunityOptionsDef2,
            ]
        ]


    class OneOfSequencesActionsSetLocalPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSequencesActionsSetMetricOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSequencesActionsSetMetricTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: MetricTypeDef  # pytype: disable=annotation-type-mismatch


    class SetOriginOptionsDef:
        option_type: GlobalOptionTypeDef
        value: OriginDef  # pytype: disable=annotation-type-mismatch


    class RemoteAsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSequencesActionsSetOriginOptionsDef:
        origin_option: SetOriginOptionsDef
        remote_as: Optional[RemoteAsDef]


    class OneOfSequencesActionsSetOspfTagOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSequencesActionsSetWeightOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSequencesActionsSetIpv4NextHopDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfSequencesActionsSetIpv6NextHopDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class Accept:
        """
        Accept Action
        """

        enable_accept_action: SequencesActionsEnableAcceptOptionsDef
        set_as_path: Optional[SequencesActionsSetAsPathOptionsDef]
        set_community: Optional[SequencesActionsSetCommunityDef]
        set_interface: Optional[OneOfSequencesInterfaceOptionsDef]
        set_ipv4_next_hop: Optional[
            OneOfSequencesActionsSetIpv4NextHopDef
        ]
        set_ipv6_next_hop: Optional[
            OneOfSequencesActionsSetIpv6NextHopDef
        ]
        set_local_preference: Optional[
            OneOfSequencesActionsSetLocalPreferenceOptionsDef
        ]
        set_metric: Optional[OneOfSequencesActionsSetMetricOptionsDef]
        set_metric_type: Optional[
            OneOfSequencesActionsSetMetricTypeOptionsDef
        ]
        set_origin: Optional[OneOfSequencesActionsSetOriginOptionsDef]
        set_ospf_tag: Optional[OneOfSequencesActionsSetOspfTagOptionsDef]
        set_weight: Optional[OneOfSequencesActionsSetWeightOptionsDef]


    class Actions1:
        # Accept Action
        accept: Accept


    class SequencesActionsRejectOptionsDef:
        option_type: DefaultOptionTypeDef
        value: bool


    class Actions2:
        reject: SequencesActionsRejectOptionsDef


    class Sequences:
        base_action: Union[
            OneOfSequencesBaseActionOptionsDef1,
            OneOfSequencesBaseActionOptionsDef2,
        ]
        protocol: Union[
            OneOfSequencesProtocolOptionsDef1,
            OneOfSequencesProtocolOptionsDef2,
        ]
        sequence_id: OneOfSequencesSequenceIdOptionsDef
        sequence_name: OneOfSequencesSequenceNameOptionsDef
        # Define list of actions
        actions: Optional[List[Union[Actions1, Actions2]]]
        # Define match conditions
        match_entries: Optional[List[MatchEntries]]


    class RoutePolicyData:
        default_action: Union[
            OneOfDefaultActionOptionsDef1, OneOfDefaultActionOptionsDef2
        ]
        # Route Policy List
        sequences: Optional[List[Sequences]]


    class Payload:
        """
        Route policy profile feature schema
        """

        data: RoutePolicyData
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
        # Route policy profile feature schema
        payload: Optional[Payload]


    class GetListSdRoutingServiceRoutePolicyPayload:
        data: Optional[List[Data]]


    class CreateSdroutingServiceRoutePolicyFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class ServiceRoutePolicyData:
        default_action: Union[
            OneOfDefaultActionOptionsDef1, OneOfDefaultActionOptionsDef2
        ]
        # Route Policy List
        sequences: Optional[List[Sequences]]


    class CreateSdroutingServiceRoutePolicyFeaturePostRequest:
        """
        Route policy profile feature schema
        """

        data: ServiceRoutePolicyData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingServiceRoutePolicyPayload:
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
        # Route policy profile feature schema
        payload: Optional[Payload]


    class EditSdroutingServiceRoutePolicyFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingServiceRoutePolicyData:
        default_action: Union[
            OneOfDefaultActionOptionsDef1, OneOfDefaultActionOptionsDef2
        ]
        # Route Policy List
        sequences: Optional[List[Sequences]]


    class EditSdroutingServiceRoutePolicyFeaturePutRequest:
        """
        Route policy profile feature schema
        """

        data: SdRoutingServiceRoutePolicyData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


