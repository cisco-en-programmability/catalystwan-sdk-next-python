======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanFalseDef = Literal[False]

    CommunityAuthorizationDef = Literal["read-only", "read-write"]

    GroupSecurityLevelDef = Literal[
        "auth-no-priv", "auth-priv", "no-auth-no-priv"
    ]

    UserAuthDef = Literal["sha"]

    UserPrivDef = Literal["aes-256-cfb-128", "aes-cfb-128"]


    class OneOfShutdownOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfShutdownOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfShutdownOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfContactOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfContactOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfContactOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfLocationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfLocationOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLocationOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfViewNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfViewOidIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfViewOidIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfViewOidExcludeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfViewOidExcludeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfViewOidExcludeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class Oid:
        id: Union[OneOfViewOidIdOptionsDef1, OneOfViewOidIdOptionsDef2]
        exclude: Optional[
            Union[
                OneOfViewOidExcludeOptionsDef1,
                OneOfViewOidExcludeOptionsDef2,
                OneOfViewOidExcludeOptionsDef3,
            ]
        ]


    class View:
        name: OneOfViewNameOptionsDef
        # Configure SNMP object identifier
        oid: Optional[List[Oid]]


    class OneOfCommunityNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfCommunityNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTargetCommunityNameUserLabelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfCommunityViewOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfCommunityViewOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfCommunityAuthorizationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: CommunityAuthorizationDef  # pytype: disable=annotation-type-mismatch


    class OneOfCommunityAuthorizationOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Community:
        name: Union[
            OneOfCommunityNameOptionsDef1, OneOfCommunityNameOptionsDef2
        ]
        view: Union[
            OneOfCommunityViewOptionsDef1, OneOfCommunityViewOptionsDef2
        ]
        authorization: Optional[
            Union[
                OneOfCommunityAuthorizationOptionsDef1,
                OneOfCommunityAuthorizationOptionsDef2,
            ]
        ]
        user_label: Optional[OneOfTargetCommunityNameUserLabelOptionsDef]


    class OneOfGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfGroupSecurityLevelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: GroupSecurityLevelDef  # pytype: disable=annotation-type-mismatch


    class OneOfGroupViewOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfGroupViewOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Group:
        name: OneOfGroupNameOptionsDef
        security_level: OneOfGroupSecurityLevelOptionsDef
        view: Union[OneOfGroupViewOptionsDef1, OneOfGroupViewOptionsDef2]


    class OneOfUserNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfUserAuthOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: UserAuthDef  # pytype: disable=annotation-type-mismatch


    class OneOfUserAuthOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUserAuthOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfUserAuthPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfUserAuthPasswordOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUserAuthPasswordOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfUserPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: UserPrivDef  # pytype: disable=annotation-type-mismatch


    class OneOfUserPrivOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUserPrivOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfUserPrivPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfUserPrivPasswordOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUserPrivPasswordOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfUserGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfUserGroupOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class User:
        group: Union[OneOfUserGroupOptionsDef1, OneOfUserGroupOptionsDef2]
        name: OneOfUserNameOptionsDef
        auth: Optional[
            Union[
                OneOfUserAuthOptionsDef1,
                OneOfUserAuthOptionsDef2,
                OneOfUserAuthOptionsDef3,
            ]
        ]
        auth_password: Optional[
            Union[
                OneOfUserAuthPasswordOptionsDef1,
                OneOfUserAuthPasswordOptionsDef2,
                OneOfUserAuthPasswordOptionsDef3,
            ]
        ]
        priv: Optional[
            Union[
                OneOfUserPrivOptionsDef1,
                OneOfUserPrivOptionsDef2,
                OneOfUserPrivOptionsDef3,
            ]
        ]
        priv_password: Optional[
            Union[
                OneOfUserPrivPasswordOptionsDef1,
                OneOfUserPrivPasswordOptionsDef2,
                OneOfUserPrivPasswordOptionsDef3,
            ]
        ]


    class OneOfTargetVrfOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTargetVrfOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTargetVrfOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfTargetIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfTargetIpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTargetPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTargetPortOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTargetCommunityNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTargetCommunityNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTargetUserOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTargetUserOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTargetSourceInterfaceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTargetSourceInterfaceOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Target:
        ip: Union[OneOfTargetIpOptionsDef1, OneOfTargetIpOptionsDef2]
        port: Union[
            OneOfTargetPortOptionsDef1, OneOfTargetPortOptionsDef2
        ]
        vrf: Union[
            OneOfTargetVrfOptionsDef1,
            OneOfTargetVrfOptionsDef2,
            OneOfTargetVrfOptionsDef3,
        ]
        community_name: Optional[
            Union[
                OneOfTargetCommunityNameOptionsDef1,
                OneOfTargetCommunityNameOptionsDef2,
            ]
        ]
        source_interface: Optional[
            Union[
                OneOfTargetSourceInterfaceOptionsDef1,
                OneOfTargetSourceInterfaceOptionsDef2,
            ]
        ]
        user: Optional[
            Union[OneOfTargetUserOptionsDef1, OneOfTargetUserOptionsDef2]
        ]
        user_label: Optional[OneOfTargetCommunityNameUserLabelOptionsDef]


    class SnmpData:
        # Configure SNMP community
        community: Optional[List[Community]]
        contact: Optional[
            Union[
                OneOfContactOptionsDef1,
                OneOfContactOptionsDef2,
                OneOfContactOptionsDef3,
            ]
        ]
        # Configure an SNMP group
        group: Optional[List[Group]]
        location: Optional[
            Union[
                OneOfLocationOptionsDef1,
                OneOfLocationOptionsDef2,
                OneOfLocationOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfShutdownOptionsDef1,
                OneOfShutdownOptionsDef2,
                OneOfShutdownOptionsDef3,
            ]
        ]
        # Configure SNMP server to receive SNMP traps
        target: Optional[List[Target]]
        # Configure an SNMP user
        user: Optional[List[User]]
        # Configure a view record
        view: Optional[List[View]]


    class Payload:
        """
        SD-Routing SNMP feature schema
        """

        data: SnmpData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


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
        # SD-Routing SNMP feature schema
        payload: Optional[Payload]


    class GetListSdRoutingSystemSnmpSdRoutingPayload:
        data: Optional[List[Data]]


    class CreateSdroutingSnmpFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SystemSnmpData:
        # Configure SNMP community
        community: Optional[List[Community]]
        contact: Optional[
            Union[
                OneOfContactOptionsDef1,
                OneOfContactOptionsDef2,
                OneOfContactOptionsDef3,
            ]
        ]
        # Configure an SNMP group
        group: Optional[List[Group]]
        location: Optional[
            Union[
                OneOfLocationOptionsDef1,
                OneOfLocationOptionsDef2,
                OneOfLocationOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfShutdownOptionsDef1,
                OneOfShutdownOptionsDef2,
                OneOfShutdownOptionsDef3,
            ]
        ]
        # Configure SNMP server to receive SNMP traps
        target: Optional[List[Target]]
        # Configure an SNMP user
        user: Optional[List[User]]
        # Configure a view record
        view: Optional[List[View]]


    class CreateSdroutingSnmpFeaturePostRequest:
        """
        SD-Routing SNMP feature schema
        """

        data: SystemSnmpData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdRoutingSystemSnmpSdRoutingPayload:
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
        # SD-Routing SNMP feature schema
        payload: Optional[Payload]


    class EditSdroutingSnmpFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingSystemSnmpData:
        # Configure SNMP community
        community: Optional[List[Community]]
        contact: Optional[
            Union[
                OneOfContactOptionsDef1,
                OneOfContactOptionsDef2,
                OneOfContactOptionsDef3,
            ]
        ]
        # Configure an SNMP group
        group: Optional[List[Group]]
        location: Optional[
            Union[
                OneOfLocationOptionsDef1,
                OneOfLocationOptionsDef2,
                OneOfLocationOptionsDef3,
            ]
        ]
        shutdown: Optional[
            Union[
                OneOfShutdownOptionsDef1,
                OneOfShutdownOptionsDef2,
                OneOfShutdownOptionsDef3,
            ]
        ]
        # Configure SNMP server to receive SNMP traps
        target: Optional[List[Target]]
        # Configure an SNMP user
        user: Optional[List[User]]
        # Configure a view record
        view: Optional[List[View]]


    class EditSdroutingSnmpFeaturePutRequest:
        """
        SD-Routing SNMP feature schema
        """

        data: SdRoutingSystemSnmpData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


