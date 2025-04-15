======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    SequencesBaseActionDef = Literal["accept", "drop"]

    TargetDirectionDef = Literal["all", "service", "tunnel"]

    SequencesSequenceIpTypeDef = Literal["all", "ipv4", "ipv6"]

    TrafficPolicySequencesBaseActionDef = Literal["accept", "drop"]

    TrafficPolicyTargetDirectionDef = Literal["all", "service", "tunnel"]

    ApplicationPriorityTrafficPolicyTargetDirectionDef = Literal[
        "all", "service", "tunnel"
    ]

    ApplicationPriorityTrafficPolicySequencesBaseActionDef = Literal[
        "accept", "drop"
    ]

    SdwanApplicationPriorityTrafficPolicySequencesBaseActionDef = Literal[
        "accept", "drop"
    ]

    TrafficPolicySequencesSequenceIpTypeDef = Literal[
        "all", "ipv4", "ipv6"
    ]

    FeatureProfileSdwanApplicationPriorityTrafficPolicySequencesBaseActionDef = Literal[
        "accept", "drop"
    ]

    SdwanApplicationPriorityTrafficPolicyTargetDirectionDef = Literal[
        "all", "service", "tunnel"
    ]

    FeatureProfileSdwanApplicationPriorityTrafficPolicyTargetDirectionDef = Literal[
        "all", "service", "tunnel"
    ]

    V1FeatureProfileSdwanApplicationPriorityTrafficPolicySequencesBaseActionDef = Literal[
        "accept", "drop"
    ]

    SequencesBaseActionDef1 = Literal["accept", "drop"]

    ApplicationPriorityTrafficPolicySequencesSequenceIpTypeDef = Literal[
        "all", "ipv4", "ipv6"
    ]


    class CreateTrafficPolicyProfileParcelForapplicationPriorityPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OneOfSequencesBaseActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SequencesBaseActionDef


    class BooleanGlobalOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfTargetVpnOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfTargetDirectionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: TargetDirectionDef


    class Target1:
        """
        Target vpn and direction
        """

        direction: Optional[OneOfTargetDirectionOptionsDef]
        vpn: Optional[OneOfTargetVpnOptionsDef]


    class CommonRuleDef:
        option_type: GlobalOptionTypeDef
        rule_id: List[str]


    class Target2:
        """
        rule
        """

        direction: Optional[OneOfTargetDirectionOptionsDef]
        vpn_rule: Optional[CommonRuleDef]


    class OneOfSequencesSequenceIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSequencesSequenceNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SequenceIpType:
        value: Optional[Any]


    class Match:
        entries: Optional[Any]


    class Sequences1:
        actions: Optional[Any]
        base_action: Optional[OneOfSequencesBaseActionOptionsDef]
        match_: Optional[Match]
        sequence_id: Optional[OneOfSequencesSequenceIdOptionsDef]
        sequence_ip_type: Optional[SequenceIpType]
        sequence_name: Optional[OneOfSequencesSequenceNameOptionsDef]


    class OneOfSequencesSequenceIpTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SequencesSequenceIpTypeDef


    class TrafficPolicyMatch:
        entries: Any


    class Sequences2:
        actions: Optional[Any]
        base_action: Optional[OneOfSequencesBaseActionOptionsDef]
        match_: Optional[TrafficPolicyMatch]
        sequence_id: Optional[OneOfSequencesSequenceIdOptionsDef]
        sequence_ip_type: Optional[OneOfSequencesSequenceIpTypeOptionsDef]
        sequence_name: Optional[OneOfSequencesSequenceNameOptionsDef]


    class Data:
        data_default_action: Optional[OneOfSequencesBaseActionOptionsDef]
        has_cor_via_sig: Optional[BooleanGlobalOptionsDef]
        # Traffic policy sequence list
        sequences: Optional[List[Union[Sequences1, Sequences2]]]
        simple_flow: Optional[BooleanGlobalOptionsDef]
        target: Optional[Union[Target1, Target2]]


    class CreateTrafficPolicyProfileParcelForapplicationPriorityPostRequest:
        """
        traffic policy profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class TrafficPolicyOneOfSequencesBaseActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: TrafficPolicySequencesBaseActionDef


    class TrafficPolicyOneOfTargetVpnOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class TrafficPolicyOneOfTargetDirectionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: TrafficPolicyTargetDirectionDef


    class TrafficPolicyTarget1:
        """
        Target vpn and direction
        """

        direction: Optional[TrafficPolicyOneOfTargetDirectionOptionsDef]
        vpn: Optional[TrafficPolicyOneOfTargetVpnOptionsDef]


    class ApplicationPriorityTrafficPolicyOneOfTargetDirectionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: ApplicationPriorityTrafficPolicyTargetDirectionDef


    class TrafficPolicyTarget2:
        """
        rule
        """

        direction: Optional[
            ApplicationPriorityTrafficPolicyOneOfTargetDirectionOptionsDef
        ]
        vpn_rule: Optional[CommonRuleDef]


    class TrafficPolicyOneOfSequencesSequenceIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class TrafficPolicyOneOfSequencesSequenceNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class ApplicationPriorityTrafficPolicyOneOfSequencesBaseActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: ApplicationPriorityTrafficPolicySequencesBaseActionDef


    class TrafficPolicySequences1:
        actions: Optional[Any]
        base_action: Optional[
            ApplicationPriorityTrafficPolicyOneOfSequencesBaseActionOptionsDef
        ]
        match_: Optional[Match]
        sequence_id: Optional[
            TrafficPolicyOneOfSequencesSequenceIdOptionsDef
        ]
        sequence_ip_type: Optional[SequenceIpType]
        sequence_name: Optional[
            TrafficPolicyOneOfSequencesSequenceNameOptionsDef
        ]


    class ApplicationPriorityTrafficPolicyOneOfSequencesSequenceIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class ApplicationPriorityTrafficPolicyOneOfSequencesSequenceNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanApplicationPriorityTrafficPolicyOneOfSequencesBaseActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanApplicationPriorityTrafficPolicySequencesBaseActionDef


    class TrafficPolicyOneOfSequencesSequenceIpTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: TrafficPolicySequencesSequenceIpTypeDef


    class ApplicationPriorityTrafficPolicyMatch:
        entries: Any


    class TrafficPolicySequences2:
        actions: Optional[Any]
        base_action: Optional[
            SdwanApplicationPriorityTrafficPolicyOneOfSequencesBaseActionOptionsDef
        ]
        match_: Optional[ApplicationPriorityTrafficPolicyMatch]
        sequence_id: Optional[
            ApplicationPriorityTrafficPolicyOneOfSequencesSequenceIdOptionsDef
        ]
        sequence_ip_type: Optional[
            TrafficPolicyOneOfSequencesSequenceIpTypeOptionsDef
        ]
        sequence_name: Optional[
            ApplicationPriorityTrafficPolicyOneOfSequencesSequenceNameOptionsDef
        ]


    class TrafficPolicyData:
        data_default_action: Optional[
            TrafficPolicyOneOfSequencesBaseActionOptionsDef
        ]
        has_cor_via_sig: Optional[BooleanGlobalOptionsDef]
        # Traffic policy sequence list
        sequences: Optional[
            List[Union[TrafficPolicySequences1, TrafficPolicySequences2]]
        ]
        simple_flow: Optional[BooleanGlobalOptionsDef]
        target: Optional[
            Union[TrafficPolicyTarget1, TrafficPolicyTarget2]
        ]


    class Payload:
        """
        traffic policy profile parcel schema for PUT request
        """

        data: TrafficPolicyData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanApplicationPriorityTrafficPolicyPayload:
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
        # traffic policy profile parcel schema for PUT request
        payload: Optional[Payload]


    class EditTrafficPolicyProfileParcelForapplicationPriorityPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class FeatureProfileSdwanApplicationPriorityTrafficPolicyOneOfSequencesBaseActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanApplicationPriorityTrafficPolicySequencesBaseActionDef


    class ApplicationPriorityTrafficPolicyOneOfTargetVpnOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class SdwanApplicationPriorityTrafficPolicyOneOfTargetDirectionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanApplicationPriorityTrafficPolicyTargetDirectionDef


    class ApplicationPriorityTrafficPolicyTarget1:
        """
        Target vpn and direction
        """

        direction: Optional[
            SdwanApplicationPriorityTrafficPolicyOneOfTargetDirectionOptionsDef
        ]
        vpn: Optional[
            ApplicationPriorityTrafficPolicyOneOfTargetVpnOptionsDef
        ]


    class FeatureProfileSdwanApplicationPriorityTrafficPolicyOneOfTargetDirectionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanApplicationPriorityTrafficPolicyTargetDirectionDef


    class ApplicationPriorityTrafficPolicyTarget2:
        """
        rule
        """

        direction: Optional[
            FeatureProfileSdwanApplicationPriorityTrafficPolicyOneOfTargetDirectionOptionsDef
        ]
        vpn_rule: Optional[CommonRuleDef]


    class SdwanApplicationPriorityTrafficPolicyOneOfSequencesSequenceIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SdwanApplicationPriorityTrafficPolicyOneOfSequencesSequenceNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class V1FeatureProfileSdwanApplicationPriorityTrafficPolicyOneOfSequencesBaseActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: V1FeatureProfileSdwanApplicationPriorityTrafficPolicySequencesBaseActionDef


    class ApplicationPriorityTrafficPolicySequences1:
        actions: Optional[Any]
        base_action: Optional[
            V1FeatureProfileSdwanApplicationPriorityTrafficPolicyOneOfSequencesBaseActionOptionsDef
        ]
        match_: Optional[Match]
        sequence_id: Optional[
            SdwanApplicationPriorityTrafficPolicyOneOfSequencesSequenceIdOptionsDef
        ]
        sequence_ip_type: Optional[SequenceIpType]
        sequence_name: Optional[
            SdwanApplicationPriorityTrafficPolicyOneOfSequencesSequenceNameOptionsDef
        ]


    class FeatureProfileSdwanApplicationPriorityTrafficPolicyOneOfSequencesSequenceIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdwanApplicationPriorityTrafficPolicyOneOfSequencesSequenceNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSequencesBaseActionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SequencesBaseActionDef1


    class ApplicationPriorityTrafficPolicyOneOfSequencesSequenceIpTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: ApplicationPriorityTrafficPolicySequencesSequenceIpTypeDef


    class SdwanApplicationPriorityTrafficPolicyMatch:
        entries: Any


    class ApplicationPriorityTrafficPolicySequences2:
        actions: Optional[Any]
        base_action: Optional[OneOfSequencesBaseActionOptionsDef1]
        match_: Optional[SdwanApplicationPriorityTrafficPolicyMatch]
        sequence_id: Optional[
            FeatureProfileSdwanApplicationPriorityTrafficPolicyOneOfSequencesSequenceIdOptionsDef
        ]
        sequence_ip_type: Optional[
            ApplicationPriorityTrafficPolicyOneOfSequencesSequenceIpTypeOptionsDef
        ]
        sequence_name: Optional[
            FeatureProfileSdwanApplicationPriorityTrafficPolicyOneOfSequencesSequenceNameOptionsDef
        ]


    class ApplicationPriorityTrafficPolicyData:
        data_default_action: Optional[
            FeatureProfileSdwanApplicationPriorityTrafficPolicyOneOfSequencesBaseActionOptionsDef
        ]
        has_cor_via_sig: Optional[BooleanGlobalOptionsDef]
        # Traffic policy sequence list
        sequences: Optional[
            List[
                Union[
                    ApplicationPriorityTrafficPolicySequences1,
                    ApplicationPriorityTrafficPolicySequences2,
                ]
            ]
        ]
        simple_flow: Optional[BooleanGlobalOptionsDef]
        target: Optional[
            Union[
                ApplicationPriorityTrafficPolicyTarget1,
                ApplicationPriorityTrafficPolicyTarget2,
            ]
        ]


    class EditTrafficPolicyProfileParcelForapplicationPriorityPutRequest:
        """
        traffic policy profile parcel schema for PUT request
        """

        data: ApplicationPriorityTrafficPolicyData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


