======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    DefaultOptionTypeDef = Literal["default"]

    Value = Literal["non-eSim"]

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultAuthenticationDef = Literal["none"]

    AuthenticationDef = Literal["chap", "pap", "pap_chap"]

    PdnTypeDef = Literal["ipv4", "ipv4v6", "ipv6"]

    DefaultPdnTypeDef = Literal["ipv4"]

    CellularProfileDefaultAuthenticationDef = Literal["none"]

    CellularProfileAuthenticationDef = Literal["chap", "pap", "pap_chap"]

    CellularProfilePdnTypeDef = Literal["ipv4", "ipv4v6", "ipv6"]

    CellularProfileDefaultPdnTypeDef = Literal["ipv4"]


    class ConfigType:
        option_type: DefaultOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfApnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfApnOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


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
        apn: Union[OneOfApnOptionsDef1, OneOfApnOptionsDef2]
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


    class ProfileConfig:
        id: Union[OneOfIdOptionsDef1, OneOfIdOptionsDef2]
        profile_info: CommonCellularProfileInfoDef


    class NonEsimCellularProfileConfigDef:
        """
        Regular Cellular profile (non-eSim) config
        """

        config_type: ConfigType
        profile_config: ProfileConfig


    class Payload:
        """
        CellularProfile profile parcel schema for POST request
        """

        data: NonEsimCellularProfileConfigDef
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetCellularControllerAssociatedCellularProfileParcelsForTransportGetResponse:
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
        # CellularProfile profile parcel schema for POST request
        payload: Optional[Payload]


    class CreateCellularControllerAndCellularProfileParcelAssociationForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateCellularControllerAndCellularProfileParcelAssociationForTransportPostRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CellularProfileOneOfIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularProfileOneOfApnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CellularProfileOneOfDefaultAuthenticationOptionsDef:
        option_type: DefaultOptionTypeDef
        value: CellularProfileDefaultAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class CellularProfileAuthentication1:
        no_authentication: (
            CellularProfileOneOfDefaultAuthenticationOptionsDef
        )


    class CellularProfileOneOfAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: CellularProfileAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class CellularProfileOneOfUsernameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CellularProfileOneOfPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class CellularProfileNeedAuthentication:
        password: Union[
            CellularProfileOneOfPasswordOptionsDef1,
            OneOfPasswordOptionsDef2,
        ]
        type_: Union[
            CellularProfileOneOfAuthenticationOptionsDef1,
            OneOfAuthenticationOptionsDef2,
        ]
        username: Union[
            CellularProfileOneOfUsernameOptionsDef1,
            OneOfUsernameOptionsDef2,
        ]


    class CellularProfileAuthentication2:
        need_authentication: CellularProfileNeedAuthentication


    class CellularProfileOneOfPdnTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: CellularProfilePdnTypeDef


    class CellularProfileOneOfPdnTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: CellularProfileDefaultPdnTypeDef  # pytype: disable=annotation-type-mismatch


    class CellularProfileCommonCellularProfileInfoDef:
        apn: Union[
            CellularProfileOneOfApnOptionsDef1, OneOfApnOptionsDef2
        ]
        authentication: Optional[
            Union[
                CellularProfileAuthentication1,
                CellularProfileAuthentication2,
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
                CellularProfileOneOfPdnTypeOptionsDef1,
                OneOfPdnTypeOptionsDef2,
                CellularProfileOneOfPdnTypeOptionsDef3,
            ]
        ]


    class CellularProfileProfileConfig:
        id: Union[CellularProfileOneOfIdOptionsDef1, OneOfIdOptionsDef2]
        profile_info: CellularProfileCommonCellularProfileInfoDef


    class CellularProfileNonEsimCellularProfileConfigDef:
        """
        Regular Cellular profile (non-eSim) config
        """

        config_type: ConfigType
        profile_config: CellularProfileProfileConfig


    class CellularProfilePayload:
        """
        CellularProfile profile parcel schema for PUT request
        """

        data: CellularProfileNonEsimCellularProfileConfigDef
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanTransportCellularControllerCellularProfilePayload:
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
        # CellularProfile profile parcel schema for PUT request
        payload: Optional[CellularProfilePayload]


    class EditCellularControllerAndCellularProfileParcelAssociationForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditCellularControllerAndCellularProfileParcelAssociationForTransportPutRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


