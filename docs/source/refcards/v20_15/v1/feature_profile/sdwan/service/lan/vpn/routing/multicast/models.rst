======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanFalseDef = Literal[False]

    OptionType = Literal["default", "global"]

    BooleanTrueDef = Literal[True]

    SptThresholdDef = Literal["0", "infinity"]

    DefaultSptThresholdDef = Literal["0"]


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
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfThresholdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef


    class LocalConfigDef:
        local: Union[
            OneOfOnBooleanDefaultFalseOptionsDef1,
            OneOfOnBooleanDefaultFalseOptionsDef2,
            OneOfOnBooleanDefaultFalseOptionsDef3,
        ]
        threshold: Optional[
            Union[
                OneOfThresholdOptionsDef1,
                OneOfThresholdOptionsDef2,
                OneOfThresholdOptionsDef3,
            ]
        ]


    class Basic:
        """
        multicast basic Attributes
        """

        local_config: LocalConfigDef
        spt_only: Union[
            OneOfOnBooleanDefaultFalseOptionsDef1,
            OneOfOnBooleanDefaultFalseOptionsDef2,
            OneOfOnBooleanDefaultFalseOptionsDef3,
        ]


    class OneOfIfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIfNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIgmpVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIgmpVersionOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfMulticastIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMulticastIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


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


    class JoinGroup:
        group_address: Union[
            OneOfMulticastIpV4AddressOptionsDef1,
            OneOfMulticastIpV4AddressOptionsDef2,
        ]
        source_address: Optional[
            Union[
                OneOfIpV4AddressDefaultOptionsDef1,
                OneOfIpV4AddressDefaultOptionsDef2,
                OneOfIpV4AddressDefaultOptionsDef3,
            ]
        ]


    class Interface:
        interface_name: Union[
            OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2
        ]
        version: Union[
            OneOfIgmpVersionOptionsDef1, OneOfIgmpVersionOptionsDef2
        ]
        # Configure static joins
        join_group: Optional[List[JoinGroup]]


    class Igmp:
        """
        set igmp Attributes
        """

        # Set IGMP interface parameters
        interface: List[Interface]


    class EnableSsmFlag:
        """
        turn SSM on/off
        """

        option_type: OptionType
        value: Any


    class SsmRangeConfigDef1:
        # turn SSM on/off
        enable_ssm_flag: EnableSsmFlag


    class BooleanGlobalTrueOptionsDef:
        option_type: GlobalOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfRangeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRangeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRangeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class SsmRangeConfigDef2:
        enable_ssm_flag: BooleanGlobalTrueOptionsDef
        range: Optional[
            Union[
                OneOfRangeOptionsDef1,
                OneOfRangeOptionsDef2,
                OneOfRangeOptionsDef3,
            ]
        ]


    class OneOfSptThresholdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SptThresholdDef


    class OneOfSptThresholdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSptThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultSptThresholdDef  # pytype: disable=annotation-type-mismatch


    class Ssm:
        """
        ssm Attributes
        """

        ssm_range_config: Union[SsmRangeConfigDef1, SsmRangeConfigDef2]
        spt_threshold: Optional[
            Union[
                OneOfSptThresholdOptionsDef1,
                OneOfSptThresholdOptionsDef2,
                OneOfSptThresholdOptionsDef3,
            ]
        ]


    class OneOfInterfaceQueryIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceQueryIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceQueryIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfInterfaceJoinPruneIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfaceJoinPruneIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceJoinPruneIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class MulticastInterface:
        interface_name: Union[
            OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2
        ]
        join_prune_interval: Union[
            OneOfInterfaceJoinPruneIntervalOptionsDef1,
            OneOfInterfaceJoinPruneIntervalOptionsDef2,
            OneOfInterfaceJoinPruneIntervalOptionsDef3,
        ]
        query_interval: Union[
            OneOfInterfaceQueryIntervalOptionsDef1,
            OneOfInterfaceQueryIntervalOptionsDef2,
            OneOfInterfaceQueryIntervalOptionsDef3,
        ]


    class OneOfIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfAclOptionsNoDefaultDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAclOptionsNoDefaultDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class RpAddr:
        access_list: Union[
            OneOfAclOptionsNoDefaultDef1, OneOfAclOptionsNoDefaultDef2
        ]
        address: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        override: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]


    class OneOfSendRpAnnounceListScopeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSendRpAnnounceListScopeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class SendRpAnnounceList:
        interface_name: Union[
            OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2
        ]
        scope: Union[
            OneOfSendRpAnnounceListScopeOptionsDef1,
            OneOfSendRpAnnounceListScopeOptionsDef2,
        ]


    class OneOfScopeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfScopeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class SendRpDiscovery:
        interface_name: Union[
            OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2
        ]
        scope: Union[OneOfScopeOptionsDef1, OneOfScopeOptionsDef2]


    class AutoRp:
        """
        autoRp Attributes
        """

        enable_auto_rp_flag: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        # Enable or disable RP Announce
        send_rp_announce_list: Optional[List[SendRpAnnounceList]]
        # Enable or disable RP Discovery
        send_rp_discovery: Optional[List[SendRpDiscovery]]


    class OneOfRpCandidateIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRpCandidateIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRpCandidateIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfRpCandidatePriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRpCandidatePriorityOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRpCandidatePriorityOptionsDef3:
        option_type: DefaultOptionTypeDef


    class RpCandidate:
        interface_name: Union[
            OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2
        ]
        group_list: Optional[
            Union[
                OneOfRangeOptionsDef1,
                OneOfRangeOptionsDef2,
                OneOfRangeOptionsDef3,
            ]
        ]
        interval: Optional[
            Union[
                OneOfRpCandidateIntervalOptionsDef1,
                OneOfRpCandidateIntervalOptionsDef2,
                OneOfRpCandidateIntervalOptionsDef3,
            ]
        ]
        priority: Optional[
            Union[
                OneOfRpCandidatePriorityOptionsDef1,
                OneOfRpCandidatePriorityOptionsDef2,
                OneOfRpCandidatePriorityOptionsDef3,
            ]
        ]


    class OneOfMaskOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMaskOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMaskOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfPriorityOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfAcceptRpCandidateOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAcceptRpCandidateOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAcceptRpCandidateOptionsDef3:
        option_type: DefaultOptionTypeDef


    class BsrCandidate:
        interface_name: Union[
            OneOfIfNameOptionsDef1, OneOfIfNameOptionsDef2
        ]
        accept_rp_candidate: Optional[
            Union[
                OneOfAcceptRpCandidateOptionsDef1,
                OneOfAcceptRpCandidateOptionsDef2,
                OneOfAcceptRpCandidateOptionsDef3,
            ]
        ]
        mask: Optional[
            Union[
                OneOfMaskOptionsDef1,
                OneOfMaskOptionsDef2,
                OneOfMaskOptionsDef3,
            ]
        ]
        priority: Optional[
            Union[
                OneOfPriorityOptionsDef1,
                OneOfPriorityOptionsDef2,
                OneOfPriorityOptionsDef3,
            ]
        ]


    class PimBsr:
        """
        pimBSR Attributes
        """

        # bsr candidate Attributes
        bsr_candidate: Optional[List[BsrCandidate]]
        # Set RP Discovery Scope
        rp_candidate: Optional[List[RpCandidate]]


    class Pim:
        """
        multicast pim Attributes
        """

        # ssm Attributes
        ssm: Ssm
        # autoRp Attributes
        auto_rp: Optional[AutoRp]
        # Set PIM interface parameters
        interface: Optional[List[MulticastInterface]]
        # pimBSR Attributes
        pim_bsr: Optional[PimBsr]
        # Set Static RP Address(es)
        rp_addr: Optional[List[RpAddr]]


    class OneOfMeshGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfMeshGroupOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMeshGroupOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfPeerIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfPeerIpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPeerConnectSourceIntfOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfPeerConnectSourceIntfOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPeerConnectSourceIntfOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfPeerRemoteAsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfPeerRemoteAsOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPeerRemoteAsOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfPeerPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfPeerPasswordOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPeerPasswordOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfPeerKeepaliveIntervalOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfPeerKeepaliveIntervalOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPeerKeepaliveIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfPeerKeepaliveHoldTimeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfPeerKeepaliveHoldTimeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPeerKeepaliveHoldTimeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfSaLimitOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSaLimitOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSaLimitOptionsDef3:
        option_type: DefaultOptionTypeDef


    class DefaultPeer:
        """
        Set MSDP default peer
        """

        option_type: OptionType
        value: Any


    class OneOfPeerDefaultDef1:
        # Set MSDP default peer
        default_peer: DefaultPeer


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class ParcelReferenceDef:
        ref_id: RefId


    class OneOfPeerDefaultDef2:
        default_peer: BooleanGlobalTrueOptionsDef
        prefix_list: Optional[ParcelReferenceDef]


    class Peer:
        peer_ip: Union[OneOfPeerIpOptionsDef1, OneOfPeerIpOptionsDef2]
        connect_source_intf: Optional[
            Union[
                OneOfPeerConnectSourceIntfOptionsDef1,
                OneOfPeerConnectSourceIntfOptionsDef2,
                OneOfPeerConnectSourceIntfOptionsDef3,
            ]
        ]
        default: Optional[
            Union[OneOfPeerDefaultDef1, OneOfPeerDefaultDef2]
        ]
        keepalive_hold_time: Optional[
            Union[
                OneOfPeerKeepaliveHoldTimeOptionsDef1,
                OneOfPeerKeepaliveHoldTimeOptionsDef2,
                OneOfPeerKeepaliveHoldTimeOptionsDef3,
            ]
        ]
        keepalive_interval: Optional[
            Union[
                OneOfPeerKeepaliveIntervalOptionsDef1,
                OneOfPeerKeepaliveIntervalOptionsDef2,
                OneOfPeerKeepaliveIntervalOptionsDef3,
            ]
        ]
        password: Optional[
            Union[
                OneOfPeerPasswordOptionsDef1,
                OneOfPeerPasswordOptionsDef2,
                OneOfPeerPasswordOptionsDef3,
            ]
        ]
        remote_as: Optional[
            Union[
                OneOfPeerRemoteAsOptionsDef1,
                OneOfPeerRemoteAsOptionsDef2,
                OneOfPeerRemoteAsOptionsDef3,
            ]
        ]
        sa_limit: Optional[
            Union[
                OneOfSaLimitOptionsDef1,
                OneOfSaLimitOptionsDef2,
                OneOfSaLimitOptionsDef3,
            ]
        ]


    class MsdpList:
        # Configure peer
        peer: List[Peer]
        mesh_group: Optional[
            Union[
                OneOfMeshGroupOptionsDef1,
                OneOfMeshGroupOptionsDef2,
                OneOfMeshGroupOptionsDef3,
            ]
        ]


    class OneOfPeerOriginatorIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfPeerOriginatorIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPeerOriginatorIdOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfRefreshTimerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRefreshTimerOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRefreshTimerOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Msdp:
        """
        multicast MSDP
        """

        # multicast MSDP peer
        msdp_list: Optional[List[MsdpList]]
        originator_id: Optional[
            Union[
                OneOfPeerOriginatorIdOptionsDef1,
                OneOfPeerOriginatorIdOptionsDef2,
                OneOfPeerOriginatorIdOptionsDef3,
            ]
        ]
        refresh_timer: Optional[
            Union[
                OneOfRefreshTimerOptionsDef1,
                OneOfRefreshTimerOptionsDef2,
                OneOfRefreshTimerOptionsDef3,
            ]
        ]


    class Data:
        # multicast basic Attributes
        basic: Basic
        # set igmp Attributes
        igmp: Optional[Igmp]
        # multicast MSDP
        msdp: Optional[Msdp]
        # multicast pim Attributes
        pim: Optional[Pim]


    class Payload:
        """
        routing/multicast profile parcel schema for request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetLanVpnAssociatedRoutingMulticastParcelsForServiceGetResponse:
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
        # routing/multicast profile parcel schema for request
        payload: Optional[Payload]


    class CreateLanVpnAndRoutingMulticastParcelAssociationForServicePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateLanVpnAndRoutingMulticastParcelAssociationForServicePostRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class GetSingleSdwanServiceLanVpnRoutingMulticastPayload:
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
        # routing/multicast profile parcel schema for request
        payload: Optional[Payload]


    class EditLanVpnAndRoutingMulticastParcelAssociationForServicePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditLanVpnAndRoutingMulticastParcelAssociationForServicePutRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


