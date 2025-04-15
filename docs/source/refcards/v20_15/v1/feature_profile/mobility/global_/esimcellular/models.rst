======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    WanConfigDef = Literal["Active", "Standby"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    DefaultAuthenticationDef = Literal["none"]

    AuthenticationDef = Literal["chap", "pap", "pap_chap"]

    PdnTypeDef = Literal["IPv4", "IPv4v6", "IPv6"]

    DefaultPdnTypeDef = Literal["IPv4"]

    EsimcellularWanConfigDef = Literal["Active", "Standby"]

    EsimcellularDefaultAuthenticationDef = Literal["none"]

    EsimcellularAuthenticationDef = Literal["chap", "pap", "pap_chap"]

    EsimcellularPdnTypeDef = Literal["IPv4", "IPv4v6", "IPv6"]

    EsimcellularDefaultPdnTypeDef = Literal["IPv4"]

    GlobalEsimcellularDefaultAuthenticationDef = Literal["none"]

    GlobalEsimcellularAuthenticationDef = Literal[
        "chap", "pap", "pap_chap"
    ]

    GlobalEsimcellularPdnTypeDef = Literal["IPv4", "IPv4v6", "IPv6"]

    GlobalEsimcellularDefaultPdnTypeDef = Literal["IPv4"]

    GlobalEsimcellularWanConfigDef = Literal["Active", "Standby"]

    MobilityGlobalEsimcellularDefaultAuthenticationDef = Literal["none"]

    MobilityGlobalEsimcellularAuthenticationDef = Literal[
        "chap", "pap", "pap_chap"
    ]

    MobilityGlobalEsimcellularPdnTypeDef = Literal[
        "IPv4", "IPv4v6", "IPv6"
    ]

    MobilityGlobalEsimcellularDefaultPdnTypeDef = Literal["IPv4"]

    FeatureProfileMobilityGlobalEsimcellularDefaultAuthenticationDef = (
        Literal["none"]
    )

    FeatureProfileMobilityGlobalEsimcellularAuthenticationDef = Literal[
        "chap", "pap", "pap_chap"
    ]

    FeatureProfileMobilityGlobalEsimcellularPdnTypeDef = Literal[
        "IPv4", "IPv4v6", "IPv6"
    ]

    FeatureProfileMobilityGlobalEsimcellularDefaultPdnTypeDef = Literal[
        "IPv4"
    ]


    class WanConfigOptionTypesDef1:
        option_type: GlobalOptionTypeDef
        value: WanConfigDef  # pytype: disable=annotation-type-mismatch


    class WanConfigOptionTypesDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class AccountId:
        """
        Set provider account Id used for this configuration
        """

        option_type: GlobalOptionTypeDef
        value: str


    class CommPlan:
        """
        Set communication plan used for this configuration
        """

        option_type: GlobalOptionTypeDef
        value: str


    class RatePlan:
        """
        Set rate plan used for this configuration
        """

        option_type: GlobalOptionTypeDef
        value: str


    class ESimAccountInfoDef:
        # Set provider account Id used for this configuration
        account_id: AccountId
        # Set communication plan used for this configuration
        comm_plan: CommPlan
        # Set rate plan used for this configuration
        rate_plan: RatePlan


    class OneOfApnOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDefaultAuthenticationOptionsDef:
        option_type: DefaultOptionTypeDef
        value: DefaultAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class Authentication1:
        no_authentication: OneOfDefaultAuthenticationOptionsDef


    class OneOfAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: (
            AuthenticationDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfAuthenticationOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUsernameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfUsernameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfPasswordOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class NeedAuthentication:
        password: Union[
            OneOfPasswordOptionsDef1, OneOfPasswordOptionsDef2
        ]
        type_: Union[
            OneOfAuthenticationOptionsDef1, OneOfAuthenticationOptionsDef2
        ]
        username: Union[
            OneOfUsernameOptionsDef1, OneOfUsernameOptionsDef2
        ]


    class Authentication2:
        need_authentication: NeedAuthentication


    class OneOfPdnTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: PdnTypeDef


    class OneOfPdnTypeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPdnTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: (
            DefaultPdnTypeDef  # pytype: disable=annotation-type-mismatch
        )


    class CommonCellularProfileInfoDef:
        apn: OneOfApnOptionsDef
        authentication: Optional[Union[Authentication1, Authentication2]]
        pdn_type: Optional[
            Union[
                OneOfPdnTypeOptionsDef1,
                OneOfPdnTypeOptionsDef2,
                OneOfPdnTypeOptionsDef3,
            ]
        ]


    class ESimCellularSlotConfigDef:
        account_info: ESimAccountInfoDef
        attach_profile_config: CommonCellularProfileInfoDef
        data_profile_config: Optional[CommonCellularProfileInfoDef]


    class SlotConfigDef:
        """
        Set the slot specific eSim cellular configuration
        """

        slot0_config: ESimCellularSlotConfigDef


    class EsimcellularData:
        # Set the slot specific eSim cellular configuration
        slot_config: SlotConfigDef
        wan_config: Optional[
            Union[WanConfigOptionTypesDef1, WanConfigOptionTypesDef2]
        ]


    class Payload:
        """
        eSim Cellular profile feature schema for POST request
        """

        data: EsimcellularData
        name: str
        # Set the eSim Cellular profile feature description
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
        # eSim Cellular profile feature schema for POST request
        payload: Optional[Payload]


    class GetListMobilityGlobalEsimcellularPayload:
        data: Optional[List[Data]]


    class CreateEsimCellularProfileFeatureForMobilityPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class GlobalEsimcellularData:
        # Set the slot specific eSim cellular configuration
        slot_config: SlotConfigDef
        wan_config: Optional[
            Union[WanConfigOptionTypesDef1, WanConfigOptionTypesDef2]
        ]


    class CreateEsimCellularProfileFeatureForMobilityPostRequest:
        """
        eSim Cellular profile feature schema for POST request
        """

        data: GlobalEsimcellularData
        name: str
        # Set the eSim Cellular profile feature description
        description: Optional[str]
        metadata: Optional[Any]


    class EsimcellularWanConfigOptionTypesDef1:
        option_type: GlobalOptionTypeDef
        value: EsimcellularWanConfigDef  # pytype: disable=annotation-type-mismatch


    class EsimcellularESimAccountInfoDef:
        # Set provider account Id used for this configuration
        account_id: AccountId
        # Set communication plan used for this configuration
        comm_plan: CommPlan
        # Set rate plan used for this configuration
        rate_plan: RatePlan


    class EsimcellularOneOfApnOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class EsimcellularOneOfDefaultAuthenticationOptionsDef:
        option_type: DefaultOptionTypeDef
        value: EsimcellularDefaultAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class EsimcellularAuthentication1:
        no_authentication: (
            EsimcellularOneOfDefaultAuthenticationOptionsDef
        )


    class EsimcellularOneOfAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EsimcellularAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class EsimcellularOneOfUsernameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EsimcellularOneOfPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EsimcellularNeedAuthentication:
        password: Union[
            EsimcellularOneOfPasswordOptionsDef1, OneOfPasswordOptionsDef2
        ]
        type_: Union[
            EsimcellularOneOfAuthenticationOptionsDef1,
            OneOfAuthenticationOptionsDef2,
        ]
        username: Union[
            EsimcellularOneOfUsernameOptionsDef1, OneOfUsernameOptionsDef2
        ]


    class EsimcellularAuthentication2:
        need_authentication: EsimcellularNeedAuthentication


    class EsimcellularOneOfPdnTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EsimcellularPdnTypeDef


    class EsimcellularOneOfPdnTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: EsimcellularDefaultPdnTypeDef  # pytype: disable=annotation-type-mismatch


    class EsimcellularCommonCellularProfileInfoDef:
        apn: EsimcellularOneOfApnOptionsDef
        authentication: Optional[
            Union[
                EsimcellularAuthentication1, EsimcellularAuthentication2
            ]
        ]
        pdn_type: Optional[
            Union[
                EsimcellularOneOfPdnTypeOptionsDef1,
                OneOfPdnTypeOptionsDef2,
                EsimcellularOneOfPdnTypeOptionsDef3,
            ]
        ]


    class GlobalEsimcellularOneOfApnOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalEsimcellularOneOfDefaultAuthenticationOptionsDef:
        option_type: DefaultOptionTypeDef
        value: GlobalEsimcellularDefaultAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class GlobalEsimcellularAuthentication1:
        no_authentication: (
            GlobalEsimcellularOneOfDefaultAuthenticationOptionsDef
        )


    class GlobalEsimcellularOneOfAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: GlobalEsimcellularAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class GlobalEsimcellularOneOfUsernameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalEsimcellularOneOfPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalEsimcellularNeedAuthentication:
        password: Union[
            GlobalEsimcellularOneOfPasswordOptionsDef1,
            OneOfPasswordOptionsDef2,
        ]
        type_: Union[
            GlobalEsimcellularOneOfAuthenticationOptionsDef1,
            OneOfAuthenticationOptionsDef2,
        ]
        username: Union[
            GlobalEsimcellularOneOfUsernameOptionsDef1,
            OneOfUsernameOptionsDef2,
        ]


    class GlobalEsimcellularAuthentication2:
        need_authentication: GlobalEsimcellularNeedAuthentication


    class GlobalEsimcellularOneOfPdnTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: GlobalEsimcellularPdnTypeDef


    class GlobalEsimcellularOneOfPdnTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: GlobalEsimcellularDefaultPdnTypeDef  # pytype: disable=annotation-type-mismatch


    class GlobalEsimcellularCommonCellularProfileInfoDef:
        apn: GlobalEsimcellularOneOfApnOptionsDef
        authentication: Optional[
            Union[
                GlobalEsimcellularAuthentication1,
                GlobalEsimcellularAuthentication2,
            ]
        ]
        pdn_type: Optional[
            Union[
                GlobalEsimcellularOneOfPdnTypeOptionsDef1,
                OneOfPdnTypeOptionsDef2,
                GlobalEsimcellularOneOfPdnTypeOptionsDef3,
            ]
        ]


    class EsimcellularESimCellularSlotConfigDef:
        account_info: EsimcellularESimAccountInfoDef
        attach_profile_config: EsimcellularCommonCellularProfileInfoDef
        data_profile_config: Optional[
            GlobalEsimcellularCommonCellularProfileInfoDef
        ]


    class EsimcellularSlotConfigDef:
        """
        Set the slot specific eSim cellular configuration
        """

        slot0_config: EsimcellularESimCellularSlotConfigDef


    class MobilityGlobalEsimcellularData:
        # Set the slot specific eSim cellular configuration
        slot_config: EsimcellularSlotConfigDef
        wan_config: Optional[
            Union[
                EsimcellularWanConfigOptionTypesDef1,
                WanConfigOptionTypesDef2,
            ]
        ]


    class EsimcellularPayload:
        """
        eSim Cellular profile feature schema for PUT request
        """

        data: MobilityGlobalEsimcellularData
        name: str
        # Set the eSim Cellular profile feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleMobilityGlobalEsimcellularPayload:
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
        # eSim Cellular profile feature schema for PUT request
        payload: Optional[EsimcellularPayload]


    class EditEsimCellularProfileFeatureForMobilityPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class GlobalEsimcellularWanConfigOptionTypesDef1:
        option_type: GlobalOptionTypeDef
        value: GlobalEsimcellularWanConfigDef  # pytype: disable=annotation-type-mismatch


    class GlobalEsimcellularESimAccountInfoDef:
        # Set provider account Id used for this configuration
        account_id: AccountId
        # Set communication plan used for this configuration
        comm_plan: CommPlan
        # Set rate plan used for this configuration
        rate_plan: RatePlan


    class MobilityGlobalEsimcellularOneOfApnOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class MobilityGlobalEsimcellularOneOfDefaultAuthenticationOptionsDef:
        option_type: DefaultOptionTypeDef
        value: MobilityGlobalEsimcellularDefaultAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class MobilityGlobalEsimcellularAuthentication1:
        no_authentication: (
            MobilityGlobalEsimcellularOneOfDefaultAuthenticationOptionsDef
        )


    class MobilityGlobalEsimcellularOneOfAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: MobilityGlobalEsimcellularAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class MobilityGlobalEsimcellularOneOfUsernameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class MobilityGlobalEsimcellularOneOfPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class MobilityGlobalEsimcellularNeedAuthentication:
        password: Union[
            MobilityGlobalEsimcellularOneOfPasswordOptionsDef1,
            OneOfPasswordOptionsDef2,
        ]
        type_: Union[
            MobilityGlobalEsimcellularOneOfAuthenticationOptionsDef1,
            OneOfAuthenticationOptionsDef2,
        ]
        username: Union[
            MobilityGlobalEsimcellularOneOfUsernameOptionsDef1,
            OneOfUsernameOptionsDef2,
        ]


    class MobilityGlobalEsimcellularAuthentication2:
        need_authentication: MobilityGlobalEsimcellularNeedAuthentication


    class MobilityGlobalEsimcellularOneOfPdnTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: MobilityGlobalEsimcellularPdnTypeDef


    class MobilityGlobalEsimcellularOneOfPdnTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: MobilityGlobalEsimcellularDefaultPdnTypeDef  # pytype: disable=annotation-type-mismatch


    class MobilityGlobalEsimcellularCommonCellularProfileInfoDef:
        apn: MobilityGlobalEsimcellularOneOfApnOptionsDef
        authentication: Optional[
            Union[
                MobilityGlobalEsimcellularAuthentication1,
                MobilityGlobalEsimcellularAuthentication2,
            ]
        ]
        pdn_type: Optional[
            Union[
                MobilityGlobalEsimcellularOneOfPdnTypeOptionsDef1,
                OneOfPdnTypeOptionsDef2,
                MobilityGlobalEsimcellularOneOfPdnTypeOptionsDef3,
            ]
        ]


    class FeatureProfileMobilityGlobalEsimcellularOneOfApnOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileMobilityGlobalEsimcellularOneOfDefaultAuthenticationOptionsDef:
        option_type: DefaultOptionTypeDef
        value: FeatureProfileMobilityGlobalEsimcellularDefaultAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class FeatureProfileMobilityGlobalEsimcellularAuthentication1:
        no_authentication: FeatureProfileMobilityGlobalEsimcellularOneOfDefaultAuthenticationOptionsDef


    class FeatureProfileMobilityGlobalEsimcellularOneOfAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileMobilityGlobalEsimcellularAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class FeatureProfileMobilityGlobalEsimcellularOneOfUsernameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileMobilityGlobalEsimcellularOneOfPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileMobilityGlobalEsimcellularNeedAuthentication:
        password: Union[
            FeatureProfileMobilityGlobalEsimcellularOneOfPasswordOptionsDef1,
            OneOfPasswordOptionsDef2,
        ]
        type_: Union[
            FeatureProfileMobilityGlobalEsimcellularOneOfAuthenticationOptionsDef1,
            OneOfAuthenticationOptionsDef2,
        ]
        username: Union[
            FeatureProfileMobilityGlobalEsimcellularOneOfUsernameOptionsDef1,
            OneOfUsernameOptionsDef2,
        ]


    class FeatureProfileMobilityGlobalEsimcellularAuthentication2:
        need_authentication: (
            FeatureProfileMobilityGlobalEsimcellularNeedAuthentication
        )


    class FeatureProfileMobilityGlobalEsimcellularOneOfPdnTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileMobilityGlobalEsimcellularPdnTypeDef


    class FeatureProfileMobilityGlobalEsimcellularOneOfPdnTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: FeatureProfileMobilityGlobalEsimcellularDefaultPdnTypeDef  # pytype: disable=annotation-type-mismatch


    class FeatureProfileMobilityGlobalEsimcellularCommonCellularProfileInfoDef:
        apn: FeatureProfileMobilityGlobalEsimcellularOneOfApnOptionsDef
        authentication: Optional[
            Union[
                FeatureProfileMobilityGlobalEsimcellularAuthentication1,
                FeatureProfileMobilityGlobalEsimcellularAuthentication2,
            ]
        ]
        pdn_type: Optional[
            Union[
                FeatureProfileMobilityGlobalEsimcellularOneOfPdnTypeOptionsDef1,
                OneOfPdnTypeOptionsDef2,
                FeatureProfileMobilityGlobalEsimcellularOneOfPdnTypeOptionsDef3,
            ]
        ]


    class GlobalEsimcellularESimCellularSlotConfigDef:
        account_info: GlobalEsimcellularESimAccountInfoDef
        attach_profile_config: (
            MobilityGlobalEsimcellularCommonCellularProfileInfoDef
        )
        data_profile_config: Optional[
            FeatureProfileMobilityGlobalEsimcellularCommonCellularProfileInfoDef
        ]


    class GlobalEsimcellularSlotConfigDef:
        """
        Set the slot specific eSim cellular configuration
        """

        slot0_config: GlobalEsimcellularESimCellularSlotConfigDef


    class FeatureProfileMobilityGlobalEsimcellularData:
        # Set the slot specific eSim cellular configuration
        slot_config: GlobalEsimcellularSlotConfigDef
        wan_config: Optional[
            Union[
                GlobalEsimcellularWanConfigOptionTypesDef1,
                WanConfigOptionTypesDef2,
            ]
        ]


    class EditEsimCellularProfileFeatureForMobilityPutRequest:
        """
        eSim Cellular profile feature schema for PUT request
        """

        data: FeatureProfileMobilityGlobalEsimcellularData
        name: str
        # Set the eSim Cellular profile feature description
        description: Optional[str]
        metadata: Optional[Any]


