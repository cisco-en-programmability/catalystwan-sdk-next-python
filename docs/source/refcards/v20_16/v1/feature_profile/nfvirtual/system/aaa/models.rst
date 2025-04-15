======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    UserRoleDef = Literal["administrators", "auditors", "operators"]

    AuthOrderAuthenticationDef = Literal["local", "tacacs"]

    TacacsKeyEnumDef = Literal["0", "7"]

    DefaultOptionTypeDef = Literal["default"]

    Value = Literal["0"]

    RadiusKeyEnumDef = Literal["0", "7"]

    AaaUserRoleDef = Literal["administrators", "auditors", "operators"]

    AaaAuthOrderAuthenticationDef = Literal["local", "tacacs"]

    AaaTacacsKeyEnumDef = Literal["0", "7"]

    AaaRadiusKeyEnumDef = Literal["0", "7"]

    SystemAaaUserRoleDef = Literal[
        "administrators", "auditors", "operators"
    ]

    SystemAaaAuthOrderAuthenticationDef = Literal["local", "tacacs"]

    SystemAaaTacacsKeyEnumDef = Literal["0", "7"]

    SystemAaaRadiusKeyEnumDef = Literal["0", "7"]


    class CreateNfvirtualAaaParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OneOfUserNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfUserNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUserPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfUserPasswordOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUserRoleOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: UserRoleDef  # pytype: disable=annotation-type-mismatch


    class OneOfUserRoleOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class User:
        name: Union[OneOfUserNameOptionsDef1, OneOfUserNameOptionsDef2]
        nfvis_password: Union[
            OneOfUserPasswordOptionsDef1, OneOfUserPasswordOptionsDef2
        ]
        role: Union[OneOfUserRoleOptionsDef1, OneOfUserRoleOptionsDef2]


    class OneOfAuthOrderAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AuthOrderAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class OneOfAuthOrderAuthenticationOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class AuthOrder:
        authentication: Union[
            OneOfAuthOrderAuthenticationOptionsDef1,
            OneOfAuthOrderAuthenticationOptionsDef2,
        ]


    class OneOfTacacsHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfTacacsHostOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTacacsKeyEnumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TacacsKeyEnumDef


    class OneOfTacacsKeyEnumOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTacacsKeyEnumOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfTacacsSharedSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTacacsSharedSecretOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTacacsAdminPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTacacsAdminPrivOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTacacsAdminPrivOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfTacacsOperPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTacacsOperPrivOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTacacsOperPrivOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Tacacs:
        host: Union[
            OneOfTacacsHostOptionsDef1, OneOfTacacsHostOptionsDef2
        ]
        shared_secret: Union[
            OneOfTacacsSharedSecretOptionsDef1,
            OneOfTacacsSharedSecretOptionsDef2,
        ]
        admin_priv: Optional[
            Union[
                OneOfTacacsAdminPrivOptionsDef1,
                OneOfTacacsAdminPrivOptionsDef2,
                OneOfTacacsAdminPrivOptionsDef3,
            ]
        ]
        key: Optional[
            Union[
                OneOfTacacsKeyEnumOptionsDef1,
                OneOfTacacsKeyEnumOptionsDef2,
                OneOfTacacsKeyEnumOptionsDef3,
            ]
        ]
        oper_priv: Optional[
            Union[
                OneOfTacacsOperPrivOptionsDef1,
                OneOfTacacsOperPrivOptionsDef2,
                OneOfTacacsOperPrivOptionsDef3,
            ]
        ]


    class OneOfRadiusHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfRadiusHostOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRadiusKeyEnumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: RadiusKeyEnumDef


    class OneOfRadiusKeyEnumOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRadiusKeyEnumOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfRadiusSharedSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRadiusSharedSecretOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRadiusAdminPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRadiusAdminPrivOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRadiusAdminPrivOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfRadiusOperPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRadiusOperPrivOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRadiusOperPrivOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Radius:
        host: Union[
            OneOfRadiusHostOptionsDef1, OneOfRadiusHostOptionsDef2
        ]
        shared_secret: Union[
            OneOfRadiusSharedSecretOptionsDef1,
            OneOfRadiusSharedSecretOptionsDef2,
        ]
        admin_priv: Optional[
            Union[
                OneOfRadiusAdminPrivOptionsDef1,
                OneOfRadiusAdminPrivOptionsDef2,
                OneOfRadiusAdminPrivOptionsDef3,
            ]
        ]
        key: Optional[
            Union[
                OneOfRadiusKeyEnumOptionsDef1,
                OneOfRadiusKeyEnumOptionsDef2,
                OneOfRadiusKeyEnumOptionsDef3,
            ]
        ]
        oper_priv: Optional[
            Union[
                OneOfRadiusOperPrivOptionsDef1,
                OneOfRadiusOperPrivOptionsDef2,
                OneOfRadiusOperPrivOptionsDef3,
            ]
        ]


    class Data:
        # Set order to try different authentication methods
        auth_order: Optional[List[AuthOrder]]
        # Configure the RADIUS server
        radius: Optional[List[Radius]]
        # Configure the TACACS server
        tacacs: Optional[List[Tacacs]]
        # Create local login account
        user: Optional[List[User]]


    class CreateNfvirtualAaaParcelPostRequest:
        """
        AAA profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class AaaOneOfUserNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaOneOfUserPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaOneOfUserRoleOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AaaUserRoleDef  # pytype: disable=annotation-type-mismatch


    class AaaUser:
        name: Union[AaaOneOfUserNameOptionsDef1, OneOfUserNameOptionsDef2]
        nfvis_password: Union[
            AaaOneOfUserPasswordOptionsDef1, OneOfUserPasswordOptionsDef2
        ]
        role: Union[AaaOneOfUserRoleOptionsDef1, OneOfUserRoleOptionsDef2]


    class AaaOneOfAuthOrderAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AaaAuthOrderAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class AaaAuthOrder:
        authentication: Union[
            AaaOneOfAuthOrderAuthenticationOptionsDef1,
            OneOfAuthOrderAuthenticationOptionsDef2,
        ]


    class AaaOneOfTacacsHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class AaaOneOfTacacsKeyEnumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AaaTacacsKeyEnumDef


    class AaaOneOfTacacsSharedSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaOneOfTacacsAdminPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class AaaOneOfTacacsOperPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class AaaTacacs:
        host: Union[
            AaaOneOfTacacsHostOptionsDef1, OneOfTacacsHostOptionsDef2
        ]
        shared_secret: Union[
            AaaOneOfTacacsSharedSecretOptionsDef1,
            OneOfTacacsSharedSecretOptionsDef2,
        ]
        admin_priv: Optional[
            Union[
                AaaOneOfTacacsAdminPrivOptionsDef1,
                OneOfTacacsAdminPrivOptionsDef2,
                OneOfTacacsAdminPrivOptionsDef3,
            ]
        ]
        key: Optional[
            Union[
                AaaOneOfTacacsKeyEnumOptionsDef1,
                OneOfTacacsKeyEnumOptionsDef2,
                OneOfTacacsKeyEnumOptionsDef3,
            ]
        ]
        oper_priv: Optional[
            Union[
                AaaOneOfTacacsOperPrivOptionsDef1,
                OneOfTacacsOperPrivOptionsDef2,
                OneOfTacacsOperPrivOptionsDef3,
            ]
        ]


    class AaaOneOfRadiusHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class AaaOneOfRadiusKeyEnumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AaaRadiusKeyEnumDef


    class AaaOneOfRadiusSharedSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaOneOfRadiusAdminPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class AaaOneOfRadiusOperPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class AaaRadius:
        host: Union[
            AaaOneOfRadiusHostOptionsDef1, OneOfRadiusHostOptionsDef2
        ]
        shared_secret: Union[
            AaaOneOfRadiusSharedSecretOptionsDef1,
            OneOfRadiusSharedSecretOptionsDef2,
        ]
        admin_priv: Optional[
            Union[
                AaaOneOfRadiusAdminPrivOptionsDef1,
                OneOfRadiusAdminPrivOptionsDef2,
                OneOfRadiusAdminPrivOptionsDef3,
            ]
        ]
        key: Optional[
            Union[
                AaaOneOfRadiusKeyEnumOptionsDef1,
                OneOfRadiusKeyEnumOptionsDef2,
                OneOfRadiusKeyEnumOptionsDef3,
            ]
        ]
        oper_priv: Optional[
            Union[
                AaaOneOfRadiusOperPrivOptionsDef1,
                OneOfRadiusOperPrivOptionsDef2,
                OneOfRadiusOperPrivOptionsDef3,
            ]
        ]


    class AaaData:
        # Set order to try different authentication methods
        auth_order: Optional[List[AaaAuthOrder]]
        # Configure the RADIUS server
        radius: Optional[List[AaaRadius]]
        # Configure the TACACS server
        tacacs: Optional[List[AaaTacacs]]
        # Create local login account
        user: Optional[List[AaaUser]]


    class Payload:
        """
        AAA profile parcel schema for PUT request
        """

        data: AaaData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleNfvirtualSystemAaaPayload:
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
        # AAA profile parcel schema for PUT request
        payload: Optional[Payload]


    class EditNfvirtualAaaParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SystemAaaOneOfUserNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemAaaOneOfUserPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemAaaOneOfUserRoleOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemAaaUserRoleDef  # pytype: disable=annotation-type-mismatch


    class SystemAaaUser:
        name: Union[
            SystemAaaOneOfUserNameOptionsDef1, OneOfUserNameOptionsDef2
        ]
        nfvis_password: Union[
            SystemAaaOneOfUserPasswordOptionsDef1,
            OneOfUserPasswordOptionsDef2,
        ]
        role: Union[
            SystemAaaOneOfUserRoleOptionsDef1, OneOfUserRoleOptionsDef2
        ]


    class SystemAaaOneOfAuthOrderAuthenticationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemAaaAuthOrderAuthenticationDef  # pytype: disable=annotation-type-mismatch


    class SystemAaaAuthOrder:
        authentication: Union[
            SystemAaaOneOfAuthOrderAuthenticationOptionsDef1,
            OneOfAuthOrderAuthenticationOptionsDef2,
        ]


    class SystemAaaOneOfTacacsHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class SystemAaaOneOfTacacsKeyEnumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemAaaTacacsKeyEnumDef


    class SystemAaaOneOfTacacsSharedSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemAaaOneOfTacacsAdminPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemAaaOneOfTacacsOperPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemAaaTacacs:
        host: Union[
            SystemAaaOneOfTacacsHostOptionsDef1,
            OneOfTacacsHostOptionsDef2,
        ]
        shared_secret: Union[
            SystemAaaOneOfTacacsSharedSecretOptionsDef1,
            OneOfTacacsSharedSecretOptionsDef2,
        ]
        admin_priv: Optional[
            Union[
                SystemAaaOneOfTacacsAdminPrivOptionsDef1,
                OneOfTacacsAdminPrivOptionsDef2,
                OneOfTacacsAdminPrivOptionsDef3,
            ]
        ]
        key: Optional[
            Union[
                SystemAaaOneOfTacacsKeyEnumOptionsDef1,
                OneOfTacacsKeyEnumOptionsDef2,
                OneOfTacacsKeyEnumOptionsDef3,
            ]
        ]
        oper_priv: Optional[
            Union[
                SystemAaaOneOfTacacsOperPrivOptionsDef1,
                OneOfTacacsOperPrivOptionsDef2,
                OneOfTacacsOperPrivOptionsDef3,
            ]
        ]


    class SystemAaaOneOfRadiusHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class SystemAaaOneOfRadiusKeyEnumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemAaaRadiusKeyEnumDef


    class SystemAaaOneOfRadiusSharedSecretOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemAaaOneOfRadiusAdminPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemAaaOneOfRadiusOperPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemAaaRadius:
        host: Union[
            SystemAaaOneOfRadiusHostOptionsDef1,
            OneOfRadiusHostOptionsDef2,
        ]
        shared_secret: Union[
            SystemAaaOneOfRadiusSharedSecretOptionsDef1,
            OneOfRadiusSharedSecretOptionsDef2,
        ]
        admin_priv: Optional[
            Union[
                SystemAaaOneOfRadiusAdminPrivOptionsDef1,
                OneOfRadiusAdminPrivOptionsDef2,
                OneOfRadiusAdminPrivOptionsDef3,
            ]
        ]
        key: Optional[
            Union[
                SystemAaaOneOfRadiusKeyEnumOptionsDef1,
                OneOfRadiusKeyEnumOptionsDef2,
                OneOfRadiusKeyEnumOptionsDef3,
            ]
        ]
        oper_priv: Optional[
            Union[
                SystemAaaOneOfRadiusOperPrivOptionsDef1,
                OneOfRadiusOperPrivOptionsDef2,
                OneOfRadiusOperPrivOptionsDef3,
            ]
        ]


    class SystemAaaData:
        # Set order to try different authentication methods
        auth_order: Optional[List[SystemAaaAuthOrder]]
        # Configure the RADIUS server
        radius: Optional[List[SystemAaaRadius]]
        # Configure the TACACS server
        tacacs: Optional[List[SystemAaaTacacs]]
        # Create local login account
        user: Optional[List[SystemAaaUser]]


    class EditNfvirtualAaaParcelPutRequest:
        """
        AAA profile parcel schema for PUT request
        """

        data: SystemAaaData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


