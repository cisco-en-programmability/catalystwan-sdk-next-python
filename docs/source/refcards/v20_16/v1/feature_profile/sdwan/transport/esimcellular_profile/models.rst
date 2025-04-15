======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    DefaultAuthenticationDef = Literal["none"]

    AuthenticationDef = Literal["chap", "pap", "pap_chap"]

    VariableOptionTypeDef = Literal["variable"]

    PdnTypeDef = Literal["ipv4", "ipv4v6", "ipv6"]

    DefaultPdnTypeDef = Literal["ipv4"]

    EsimcellularProfileDefaultAuthenticationDef = Literal["none"]

    EsimcellularProfileAuthenticationDef = Literal[
        "chap", "pap", "pap_chap"
    ]

    EsimcellularProfilePdnTypeDef = Literal["ipv4", "ipv4v6", "ipv6"]

    EsimcellularProfileDefaultPdnTypeDef = Literal["ipv4"]

    TransportEsimcellularProfileDefaultAuthenticationDef = Literal["none"]

    TransportEsimcellularProfileAuthenticationDef = Literal[
        "chap", "pap", "pap_chap"
    ]

    TransportEsimcellularProfilePdnTypeDef = Literal[
        "ipv4", "ipv4v6", "ipv6"
    ]

    TransportEsimcellularProfileDefaultPdnTypeDef = Literal["ipv4"]


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


    class OneOfNoOverwriteOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfNoOverwriteOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfNoOverwriteOptionsDef3:
        option_type: DefaultOptionTypeDef


    class CommonCellularProfileInfoDef:
        apn: OneOfApnOptionsDef
        authentication: Optional[Union[Authentication1, Authentication2]]
        no_overwrite: Optional[
            Union[
                OneOfNoOverwriteOptionsDef1,
                OneOfNoOverwriteOptionsDef2,
                OneOfNoOverwriteOptionsDef3,
            ]
        ]
        pdn_type: Optional[
            Union[
                OneOfPdnTypeOptionsDef1,
                OneOfPdnTypeOptionsDef2,
                OneOfPdnTypeOptionsDef3,
            ]
        ]


    class AccountId:
        """
        Set provider account Id used for this profile
        """

        option_type: GlobalOptionTypeDef
        value: str


    class CommPlan:
        """
        Set communication plan used for this profile
        """

        option_type: GlobalOptionTypeDef
        value: str


    class RatePlan:
        """
        Set rate plan used for this profile
        """

        option_type: GlobalOptionTypeDef
        value: str


    class ESimAccountInfoDef:
        # Set provider account Id used for this profile
        account_id: AccountId
        # Set communication plan used for this profile
        comm_plan: CommPlan
        # Set rate plan used for this profile
        rate_plan: RatePlan


    class EsimCellularProfileConfigDef:
        """
        eSim Cellular profile config
        """

        account_info: ESimAccountInfoDef
        profile_info: CommonCellularProfileInfoDef


    class Payload:
        """
        eSim CellularProfile feature schema for POST request
        """

        # eSim Cellular profile config
        data: EsimCellularProfileConfigDef
        name: str
        # Set the eSim CellularProfile feature description
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
        # eSim CellularProfile feature schema for POST request
        payload: Optional[Payload]


    class GetListSdwanTransportEsimcellularProfilePayload:
        data: Optional[List[Data]]


    class CreateEsimCellularProfileProfileFeatureForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateEsimCellularProfileProfileFeatureForTransportPostRequest:
        """
        eSim CellularProfile feature schema for POST request
        """

        # eSim Cellular profile config
        data: EsimCellularProfileConfigDef
        name: str
        # Set the eSim CellularProfile feature description
        description: Optional[str]
        metadata: Optional[Any]


    class EsimcellularProfileOneOfApnOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class EsimcellularProfileOneOfDefaultAuthenticationOptionsDef:
        option_type: DefaultOptionTypeDef
        value: EsimcellularProfileDefaultAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class EsimcellularProfileAuthentication1:
        no_authentication: (
            EsimcellularProfileOneOfDefaultAuthenticationOptionsDef
        )


    class EsimcellularProfileOneOfAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EsimcellularProfileAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class EsimcellularProfileOneOfUsernameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EsimcellularProfileOneOfPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class EsimcellularProfileNeedAuthentication:
        password: Union[
            EsimcellularProfileOneOfPasswordOptionsDef1,
            OneOfPasswordOptionsDef2,
        ]
        type_: Union[
            EsimcellularProfileOneOfAuthenticationOptionsDef1,
            OneOfAuthenticationOptionsDef2,
        ]
        username: Union[
            EsimcellularProfileOneOfUsernameOptionsDef1,
            OneOfUsernameOptionsDef2,
        ]


    class EsimcellularProfileAuthentication2:
        need_authentication: EsimcellularProfileNeedAuthentication


    class EsimcellularProfileOneOfPdnTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EsimcellularProfilePdnTypeDef


    class EsimcellularProfileOneOfPdnTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: EsimcellularProfileDefaultPdnTypeDef  # pytype: disable=annotation-type-mismatch


    class EsimcellularProfileCommonCellularProfileInfoDef:
        apn: EsimcellularProfileOneOfApnOptionsDef
        authentication: Optional[
            Union[
                EsimcellularProfileAuthentication1,
                EsimcellularProfileAuthentication2,
            ]
        ]
        no_overwrite: Optional[
            Union[
                OneOfNoOverwriteOptionsDef1,
                OneOfNoOverwriteOptionsDef2,
                OneOfNoOverwriteOptionsDef3,
            ]
        ]
        pdn_type: Optional[
            Union[
                EsimcellularProfileOneOfPdnTypeOptionsDef1,
                OneOfPdnTypeOptionsDef2,
                EsimcellularProfileOneOfPdnTypeOptionsDef3,
            ]
        ]


    class EsimcellularProfileESimAccountInfoDef:
        # Set provider account Id used for this profile
        account_id: AccountId
        # Set communication plan used for this profile
        comm_plan: CommPlan
        # Set rate plan used for this profile
        rate_plan: RatePlan


    class EsimcellularProfileEsimCellularProfileConfigDef:
        """
        eSim Cellular profile config
        """

        account_info: EsimcellularProfileESimAccountInfoDef
        profile_info: EsimcellularProfileCommonCellularProfileInfoDef


    class EsimcellularProfilePayload:
        """
        eSim CellularProfile feature schema for PUT request
        """

        # eSim Cellular profile config
        data: EsimcellularProfileEsimCellularProfileConfigDef
        name: str
        # Set the eSim CellularProfile feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanTransportEsimcellularProfilePayload:
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
        # eSim CellularProfile feature schema for PUT request
        payload: Optional[EsimcellularProfilePayload]


    class EditEsimCellularProfileProfileFeatureForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class TransportEsimcellularProfileOneOfApnOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportEsimcellularProfileOneOfDefaultAuthenticationOptionsDef:
        option_type: DefaultOptionTypeDef
        value: TransportEsimcellularProfileDefaultAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class TransportEsimcellularProfileAuthentication1:
        no_authentication: TransportEsimcellularProfileOneOfDefaultAuthenticationOptionsDef


    class TransportEsimcellularProfileOneOfAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TransportEsimcellularProfileAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class TransportEsimcellularProfileOneOfUsernameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportEsimcellularProfileOneOfPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportEsimcellularProfileNeedAuthentication:
        password: Union[
            TransportEsimcellularProfileOneOfPasswordOptionsDef1,
            OneOfPasswordOptionsDef2,
        ]
        type_: Union[
            TransportEsimcellularProfileOneOfAuthenticationOptionsDef1,
            OneOfAuthenticationOptionsDef2,
        ]
        username: Union[
            TransportEsimcellularProfileOneOfUsernameOptionsDef1,
            OneOfUsernameOptionsDef2,
        ]


    class TransportEsimcellularProfileAuthentication2:
        need_authentication: (
            TransportEsimcellularProfileNeedAuthentication
        )


    class TransportEsimcellularProfileOneOfPdnTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TransportEsimcellularProfilePdnTypeDef


    class TransportEsimcellularProfileOneOfPdnTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: TransportEsimcellularProfileDefaultPdnTypeDef  # pytype: disable=annotation-type-mismatch


    class TransportEsimcellularProfileCommonCellularProfileInfoDef:
        apn: TransportEsimcellularProfileOneOfApnOptionsDef
        authentication: Optional[
            Union[
                TransportEsimcellularProfileAuthentication1,
                TransportEsimcellularProfileAuthentication2,
            ]
        ]
        no_overwrite: Optional[
            Union[
                OneOfNoOverwriteOptionsDef1,
                OneOfNoOverwriteOptionsDef2,
                OneOfNoOverwriteOptionsDef3,
            ]
        ]
        pdn_type: Optional[
            Union[
                TransportEsimcellularProfileOneOfPdnTypeOptionsDef1,
                OneOfPdnTypeOptionsDef2,
                TransportEsimcellularProfileOneOfPdnTypeOptionsDef3,
            ]
        ]


    class TransportEsimcellularProfileESimAccountInfoDef:
        # Set provider account Id used for this profile
        account_id: AccountId
        # Set communication plan used for this profile
        comm_plan: CommPlan
        # Set rate plan used for this profile
        rate_plan: RatePlan


    class TransportEsimcellularProfileEsimCellularProfileConfigDef:
        """
        eSim Cellular profile config
        """

        account_info: TransportEsimcellularProfileESimAccountInfoDef
        profile_info: (
            TransportEsimcellularProfileCommonCellularProfileInfoDef
        )


    class EditEsimCellularProfileProfileFeatureForTransportPutRequest:
        """
        eSim CellularProfile feature schema for PUT request
        """

        # eSim Cellular profile config
        data: TransportEsimcellularProfileEsimCellularProfileConfigDef
        name: str
        # Set the eSim CellularProfile feature description
        description: Optional[str]
        metadata: Optional[Any]


