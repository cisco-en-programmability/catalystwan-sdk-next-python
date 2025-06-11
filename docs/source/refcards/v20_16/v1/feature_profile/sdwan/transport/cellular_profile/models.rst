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

    SliceTypeDef = Literal[1, 2, 3]

    CellularProfileDefaultAuthenticationDef = Literal["none"]

    CellularProfileAuthenticationDef = Literal["chap", "pap", "pap_chap"]

    CellularProfilePdnTypeDef = Literal["ipv4", "ipv4v6", "ipv6"]

    CellularProfileDefaultPdnTypeDef = Literal["ipv4"]

    CellularProfileSliceTypeDef = Literal[1, 2, 3]

    TransportCellularProfileDefaultAuthenticationDef = Literal["none"]

    TransportCellularProfileAuthenticationDef = Literal[
        "chap", "pap", "pap_chap"
    ]

    TransportCellularProfilePdnTypeDef = Literal["ipv4", "ipv4v6", "ipv6"]

    TransportCellularProfileDefaultPdnTypeDef = Literal["ipv4"]

    TransportCellularProfileSliceTypeDef = Literal[1, 2, 3]


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


    class OneOfSliceTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SliceTypeDef


    class OneOfSliceTypeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSliceTypeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfSliceDifferentiatorOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSliceDifferentiatorOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSliceDifferentiatorOptionsDef3:
        option_type: DefaultOptionTypeDef


    class NetworkSlicing:
        slice_differentiator: Optional[
            Union[
                OneOfSliceDifferentiatorOptionsDef1,
                OneOfSliceDifferentiatorOptionsDef2,
                OneOfSliceDifferentiatorOptionsDef3,
            ]
        ]
        slice_type: Optional[
            Union[
                OneOfSliceTypeOptionsDef1,
                OneOfSliceTypeOptionsDef2,
                OneOfSliceTypeOptionsDef3,
            ]
        ]


    class CommonCellularProfileInfoDef:
        apn: Union[OneOfApnOptionsDef1, OneOfApnOptionsDef2]
        authentication: Optional[Union[Authentication1, Authentication2]]
        network_slicing: Optional[NetworkSlicing]
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
        # CellularProfile profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanTransportCellularProfilePayload:
        data: Optional[List[Data]]


    class CreateCellularProfileProfileParcelForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateCellularProfileProfileParcelForTransportPostRequest:
        """
        CellularProfile profile parcel schema for POST request
        """

        data: NonEsimCellularProfileConfigDef
        name: str
        # Set the parcel description
        description: Optional[str]
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


    class CellularProfileOneOfSliceTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: CellularProfileSliceTypeDef


    class CellularProfileOneOfSliceDifferentiatorOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class CellularProfileNetworkSlicing:
        slice_differentiator: Optional[
            Union[
                CellularProfileOneOfSliceDifferentiatorOptionsDef1,
                OneOfSliceDifferentiatorOptionsDef2,
                OneOfSliceDifferentiatorOptionsDef3,
            ]
        ]
        slice_type: Optional[
            Union[
                CellularProfileOneOfSliceTypeOptionsDef1,
                OneOfSliceTypeOptionsDef2,
                OneOfSliceTypeOptionsDef3,
            ]
        ]


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
        network_slicing: Optional[CellularProfileNetworkSlicing]
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


    class GetSingleSdwanTransportCellularProfilePayload:
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


    class EditCellularProfileProfileParcelForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class TransportCellularProfileOneOfIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportCellularProfileOneOfApnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportCellularProfileOneOfDefaultAuthenticationOptionsDef:
        option_type: DefaultOptionTypeDef
        value: TransportCellularProfileDefaultAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class TransportCellularProfileAuthentication1:
        no_authentication: (
            TransportCellularProfileOneOfDefaultAuthenticationOptionsDef
        )


    class TransportCellularProfileOneOfAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TransportCellularProfileAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class TransportCellularProfileOneOfUsernameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportCellularProfileOneOfPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportCellularProfileNeedAuthentication:
        password: Union[
            TransportCellularProfileOneOfPasswordOptionsDef1,
            OneOfPasswordOptionsDef2,
        ]
        type_: Union[
            TransportCellularProfileOneOfAuthenticationOptionsDef1,
            OneOfAuthenticationOptionsDef2,
        ]
        username: Union[
            TransportCellularProfileOneOfUsernameOptionsDef1,
            OneOfUsernameOptionsDef2,
        ]


    class TransportCellularProfileAuthentication2:
        need_authentication: TransportCellularProfileNeedAuthentication


    class TransportCellularProfileOneOfPdnTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TransportCellularProfilePdnTypeDef


    class TransportCellularProfileOneOfPdnTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: TransportCellularProfileDefaultPdnTypeDef  # pytype: disable=annotation-type-mismatch


    class TransportCellularProfileOneOfSliceTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TransportCellularProfileSliceTypeDef


    class TransportCellularProfileOneOfSliceDifferentiatorOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportCellularProfileNetworkSlicing:
        slice_differentiator: Optional[
            Union[
                TransportCellularProfileOneOfSliceDifferentiatorOptionsDef1,
                OneOfSliceDifferentiatorOptionsDef2,
                OneOfSliceDifferentiatorOptionsDef3,
            ]
        ]
        slice_type: Optional[
            Union[
                TransportCellularProfileOneOfSliceTypeOptionsDef1,
                OneOfSliceTypeOptionsDef2,
                OneOfSliceTypeOptionsDef3,
            ]
        ]


    class TransportCellularProfileCommonCellularProfileInfoDef:
        apn: Union[
            TransportCellularProfileOneOfApnOptionsDef1,
            OneOfApnOptionsDef2,
        ]
        authentication: Optional[
            Union[
                TransportCellularProfileAuthentication1,
                TransportCellularProfileAuthentication2,
            ]
        ]
        network_slicing: Optional[TransportCellularProfileNetworkSlicing]
        no_overwrite: Optional[
            Union[
                OneOfNoOverwriteOptionsDef1,
                OneOfNoOverwriteOptionsDef2,
                OneOfNoOverwriteOptionsDef3,
            ]
        ]
        pdn_type: Optional[
            Union[
                TransportCellularProfileOneOfPdnTypeOptionsDef1,
                OneOfPdnTypeOptionsDef2,
                TransportCellularProfileOneOfPdnTypeOptionsDef3,
            ]
        ]


    class TransportCellularProfileProfileConfig:
        id: Union[
            TransportCellularProfileOneOfIdOptionsDef1, OneOfIdOptionsDef2
        ]
        profile_info: TransportCellularProfileCommonCellularProfileInfoDef


    class TransportCellularProfileNonEsimCellularProfileConfigDef:
        """
        Regular Cellular profile (non-eSim) config
        """

        config_type: ConfigType
        profile_config: TransportCellularProfileProfileConfig


    class EditCellularProfileProfileParcelForTransportPutRequest:
        """
        CellularProfile profile parcel schema for PUT request
        """

        data: TransportCellularProfileNonEsimCellularProfileConfigDef
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


