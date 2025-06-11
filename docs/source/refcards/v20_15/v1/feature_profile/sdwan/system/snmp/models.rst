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

    SnmpCommunityAuthorizationDef = Literal["read-only", "read-write"]

    SnmpGroupSecurityLevelDef = Literal[
        "auth-no-priv", "auth-priv", "no-auth-no-priv"
    ]

    SnmpUserAuthDef = Literal["sha"]

    SnmpUserPrivDef = Literal["aes-256-cfb-128", "aes-cfb-128"]

    SystemSnmpCommunityAuthorizationDef = Literal[
        "read-only", "read-write"
    ]

    SystemSnmpGroupSecurityLevelDef = Literal[
        "auth-no-priv", "auth-priv", "no-auth-no-priv"
    ]

    SystemSnmpUserAuthDef = Literal["sha"]

    SystemSnmpUserPrivDef = Literal["aes-256-cfb-128", "aes-cfb-128"]


    class OneOfShutdownOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfShutdownOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfShutdownOptionsDef3:
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanFalseDef]


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
        option_type: Optional[DefaultOptionTypeDef]
        value: Optional[BooleanFalseDef]


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


    class OneOfTargetVpnIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTargetVpnIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


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
        vpn_id: Union[
            OneOfTargetVpnIdOptionsDef1, OneOfTargetVpnIdOptionsDef2
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
        SNMP profile parcel schema for POST request
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
        # SNMP profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanSystemSnmpPayload:
        data: Optional[List[Data]]


    class CreateSnmpProfileParcelForSystemPostResponse:
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


    class CreateSnmpProfileParcelForSystemPostRequest:
        """
        SNMP profile parcel schema for POST request
        """

        data: SystemSnmpData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class SnmpOneOfContactOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfLocationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfViewNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfViewOidIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOid:
        id: Union[
            SnmpOneOfViewOidIdOptionsDef1, OneOfViewOidIdOptionsDef2
        ]
        exclude: Optional[
            Union[
                OneOfViewOidExcludeOptionsDef1,
                OneOfViewOidExcludeOptionsDef2,
                OneOfViewOidExcludeOptionsDef3,
            ]
        ]


    class SnmpView:
        name: SnmpOneOfViewNameOptionsDef
        # Configure SNMP object identifier
        oid: Optional[List[SnmpOid]]


    class SnmpOneOfCommunityNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfTargetCommunityNameUserLabelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfCommunityViewOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfCommunityAuthorizationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SnmpCommunityAuthorizationDef  # pytype: disable=annotation-type-mismatch


    class SnmpCommunity:
        name: Union[
            SnmpOneOfCommunityNameOptionsDef1,
            OneOfCommunityNameOptionsDef2,
        ]
        view: Union[
            SnmpOneOfCommunityViewOptionsDef1,
            OneOfCommunityViewOptionsDef2,
        ]
        authorization: Optional[
            Union[
                SnmpOneOfCommunityAuthorizationOptionsDef1,
                OneOfCommunityAuthorizationOptionsDef2,
            ]
        ]
        user_label: Optional[
            SnmpOneOfTargetCommunityNameUserLabelOptionsDef
        ]


    class SnmpOneOfGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfGroupSecurityLevelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SnmpGroupSecurityLevelDef  # pytype: disable=annotation-type-mismatch


    class SnmpOneOfGroupViewOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpGroup:
        name: SnmpOneOfGroupNameOptionsDef
        security_level: SnmpOneOfGroupSecurityLevelOptionsDef
        view: Union[
            SnmpOneOfGroupViewOptionsDef1, OneOfGroupViewOptionsDef2
        ]


    class SnmpOneOfUserNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfUserAuthOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SnmpUserAuthDef  # pytype: disable=annotation-type-mismatch


    class SnmpOneOfUserAuthPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfUserPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SnmpUserPrivDef  # pytype: disable=annotation-type-mismatch


    class SnmpOneOfUserPrivPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfUserGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpUser:
        group: Union[
            SnmpOneOfUserGroupOptionsDef1, OneOfUserGroupOptionsDef2
        ]
        name: SnmpOneOfUserNameOptionsDef
        auth: Optional[
            Union[
                SnmpOneOfUserAuthOptionsDef1,
                OneOfUserAuthOptionsDef2,
                OneOfUserAuthOptionsDef3,
            ]
        ]
        auth_password: Optional[
            Union[
                SnmpOneOfUserAuthPasswordOptionsDef1,
                OneOfUserAuthPasswordOptionsDef2,
                OneOfUserAuthPasswordOptionsDef3,
            ]
        ]
        priv: Optional[
            Union[
                SnmpOneOfUserPrivOptionsDef1,
                OneOfUserPrivOptionsDef2,
                OneOfUserPrivOptionsDef3,
            ]
        ]
        priv_password: Optional[
            Union[
                SnmpOneOfUserPrivPasswordOptionsDef1,
                OneOfUserPrivPasswordOptionsDef2,
                OneOfUserPrivPasswordOptionsDef3,
            ]
        ]


    class SnmpOneOfTargetVpnIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SnmpOneOfTargetIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class SnmpOneOfTargetPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemSnmpOneOfTargetCommunityNameUserLabelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfTargetCommunityNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfTargetUserOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfTargetSourceInterfaceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpTarget:
        ip: Union[SnmpOneOfTargetIpOptionsDef1, OneOfTargetIpOptionsDef2]
        port: Union[
            SnmpOneOfTargetPortOptionsDef1, OneOfTargetPortOptionsDef2
        ]
        vpn_id: Union[
            SnmpOneOfTargetVpnIdOptionsDef1, OneOfTargetVpnIdOptionsDef2
        ]
        community_name: Optional[
            Union[
                SnmpOneOfTargetCommunityNameOptionsDef1,
                OneOfTargetCommunityNameOptionsDef2,
            ]
        ]
        source_interface: Optional[
            Union[
                SnmpOneOfTargetSourceInterfaceOptionsDef1,
                OneOfTargetSourceInterfaceOptionsDef2,
            ]
        ]
        user: Optional[
            Union[
                SnmpOneOfTargetUserOptionsDef1, OneOfTargetUserOptionsDef2
            ]
        ]
        user_label: Optional[
            SystemSnmpOneOfTargetCommunityNameUserLabelOptionsDef
        ]


    class SdwanSystemSnmpData:
        # Configure SNMP community
        community: Optional[List[SnmpCommunity]]
        contact: Optional[
            Union[
                SnmpOneOfContactOptionsDef1,
                OneOfContactOptionsDef2,
                OneOfContactOptionsDef3,
            ]
        ]
        # Configure an SNMP group
        group: Optional[List[SnmpGroup]]
        location: Optional[
            Union[
                SnmpOneOfLocationOptionsDef1,
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
        target: Optional[List[SnmpTarget]]
        # Configure an SNMP user
        user: Optional[List[SnmpUser]]
        # Configure a view record
        view: Optional[List[SnmpView]]


    class SnmpPayload:
        """
        SNMP profile parcel schema for PUT request
        """

        data: SdwanSystemSnmpData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanSystemSnmpPayload:
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
        # SNMP profile parcel schema for PUT request
        payload: Optional[SnmpPayload]


    class EditSnmpProfileParcelForSystemPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SystemSnmpOneOfContactOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfLocationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfViewNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfViewOidIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOid:
        id: Union[
            SystemSnmpOneOfViewOidIdOptionsDef1, OneOfViewOidIdOptionsDef2
        ]
        exclude: Optional[
            Union[
                OneOfViewOidExcludeOptionsDef1,
                OneOfViewOidExcludeOptionsDef2,
                OneOfViewOidExcludeOptionsDef3,
            ]
        ]


    class SystemSnmpView:
        name: SystemSnmpOneOfViewNameOptionsDef
        # Configure SNMP object identifier
        oid: Optional[List[SystemSnmpOid]]


    class SystemSnmpOneOfCommunityNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanSystemSnmpOneOfTargetCommunityNameUserLabelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfCommunityViewOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfCommunityAuthorizationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemSnmpCommunityAuthorizationDef  # pytype: disable=annotation-type-mismatch


    class SystemSnmpCommunity:
        name: Union[
            SystemSnmpOneOfCommunityNameOptionsDef1,
            OneOfCommunityNameOptionsDef2,
        ]
        view: Union[
            SystemSnmpOneOfCommunityViewOptionsDef1,
            OneOfCommunityViewOptionsDef2,
        ]
        authorization: Optional[
            Union[
                SystemSnmpOneOfCommunityAuthorizationOptionsDef1,
                OneOfCommunityAuthorizationOptionsDef2,
            ]
        ]
        user_label: Optional[
            SdwanSystemSnmpOneOfTargetCommunityNameUserLabelOptionsDef
        ]


    class SystemSnmpOneOfGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfGroupSecurityLevelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SystemSnmpGroupSecurityLevelDef  # pytype: disable=annotation-type-mismatch


    class SystemSnmpOneOfGroupViewOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpGroup:
        name: SystemSnmpOneOfGroupNameOptionsDef
        security_level: SystemSnmpOneOfGroupSecurityLevelOptionsDef
        view: Union[
            SystemSnmpOneOfGroupViewOptionsDef1, OneOfGroupViewOptionsDef2
        ]


    class SystemSnmpOneOfUserNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfUserAuthOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemSnmpUserAuthDef  # pytype: disable=annotation-type-mismatch


    class SystemSnmpOneOfUserAuthPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfUserPrivOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemSnmpUserPrivDef  # pytype: disable=annotation-type-mismatch


    class SystemSnmpOneOfUserPrivPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfUserGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpUser:
        group: Union[
            SystemSnmpOneOfUserGroupOptionsDef1, OneOfUserGroupOptionsDef2
        ]
        name: SystemSnmpOneOfUserNameOptionsDef
        auth: Optional[
            Union[
                SystemSnmpOneOfUserAuthOptionsDef1,
                OneOfUserAuthOptionsDef2,
                OneOfUserAuthOptionsDef3,
            ]
        ]
        auth_password: Optional[
            Union[
                SystemSnmpOneOfUserAuthPasswordOptionsDef1,
                OneOfUserAuthPasswordOptionsDef2,
                OneOfUserAuthPasswordOptionsDef3,
            ]
        ]
        priv: Optional[
            Union[
                SystemSnmpOneOfUserPrivOptionsDef1,
                OneOfUserPrivOptionsDef2,
                OneOfUserPrivOptionsDef3,
            ]
        ]
        priv_password: Optional[
            Union[
                SystemSnmpOneOfUserPrivPasswordOptionsDef1,
                OneOfUserPrivPasswordOptionsDef2,
                OneOfUserPrivPasswordOptionsDef3,
            ]
        ]


    class SystemSnmpOneOfTargetVpnIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemSnmpOneOfTargetIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class SystemSnmpOneOfTargetPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class FeatureProfileSdwanSystemSnmpOneOfTargetCommunityNameUserLabelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfTargetCommunityNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfTargetUserOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfTargetSourceInterfaceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpTarget:
        ip: Union[
            SystemSnmpOneOfTargetIpOptionsDef1, OneOfTargetIpOptionsDef2
        ]
        port: Union[
            SystemSnmpOneOfTargetPortOptionsDef1,
            OneOfTargetPortOptionsDef2,
        ]
        vpn_id: Union[
            SystemSnmpOneOfTargetVpnIdOptionsDef1,
            OneOfTargetVpnIdOptionsDef2,
        ]
        community_name: Optional[
            Union[
                SystemSnmpOneOfTargetCommunityNameOptionsDef1,
                OneOfTargetCommunityNameOptionsDef2,
            ]
        ]
        source_interface: Optional[
            Union[
                SystemSnmpOneOfTargetSourceInterfaceOptionsDef1,
                OneOfTargetSourceInterfaceOptionsDef2,
            ]
        ]
        user: Optional[
            Union[
                SystemSnmpOneOfTargetUserOptionsDef1,
                OneOfTargetUserOptionsDef2,
            ]
        ]
        user_label: Optional[
            FeatureProfileSdwanSystemSnmpOneOfTargetCommunityNameUserLabelOptionsDef
        ]


    class FeatureProfileSdwanSystemSnmpData:
        # Configure SNMP community
        community: Optional[List[SystemSnmpCommunity]]
        contact: Optional[
            Union[
                SystemSnmpOneOfContactOptionsDef1,
                OneOfContactOptionsDef2,
                OneOfContactOptionsDef3,
            ]
        ]
        # Configure an SNMP group
        group: Optional[List[SystemSnmpGroup]]
        location: Optional[
            Union[
                SystemSnmpOneOfLocationOptionsDef1,
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
        target: Optional[List[SystemSnmpTarget]]
        # Configure an SNMP user
        user: Optional[List[SystemSnmpUser]]
        # Configure a view record
        view: Optional[List[SystemSnmpView]]


    class EditSnmpProfileParcelForSystemPutRequest:
        """
        SNMP profile parcel schema for PUT request
        """

        data: FeatureProfileSdwanSystemSnmpData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


