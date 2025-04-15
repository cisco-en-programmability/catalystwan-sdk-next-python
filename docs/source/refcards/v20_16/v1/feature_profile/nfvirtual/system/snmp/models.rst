======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    GroupSecurityLevelDef = Literal[
        "authNoPriv", "authPriv", "noAuthNoPriv"
    ]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    DefaultUserVersionDef = Literal["1"]

    UserAuthProtocolDef = Literal["md5", "sha"]

    UserPrivProtocolDef = Literal["aes", "des"]

    HostHostSecurityLevelDef = Literal[
        "authNoPriv", "authPriv", "noAuthNoPriv"
    ]

    SnmpGroupSecurityLevelDef = Literal[
        "authNoPriv", "authPriv", "noAuthNoPriv"
    ]

    SnmpDefaultUserVersionDef = Literal["1"]

    SnmpUserAuthProtocolDef = Literal["md5", "sha"]

    SnmpUserPrivProtocolDef = Literal["aes", "des"]

    SnmpHostHostSecurityLevelDef = Literal[
        "authNoPriv", "authPriv", "noAuthNoPriv"
    ]

    SystemSnmpGroupSecurityLevelDef = Literal[
        "authNoPriv", "authPriv", "noAuthNoPriv"
    ]

    SystemSnmpDefaultUserVersionDef = Literal["1"]

    SystemSnmpUserAuthProtocolDef = Literal["md5", "sha"]

    SystemSnmpUserPrivProtocolDef = Literal["aes", "des"]

    SystemSnmpHostHostSecurityLevelDef = Literal[
        "authNoPriv", "authPriv", "noAuthNoPriv"
    ]


    class CreateNfvirtualSnmpParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OneOfCommunityNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfCommunityCommunityAccessOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Community:
        community_name: OneOfCommunityNameOptionsDef
        community_access: Optional[
            OneOfCommunityCommunityAccessOptionsDef
        ]


    class OneOfGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfGroupContextOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfGroupVersionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfGroupSecurityLevelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: GroupSecurityLevelDef


    class OneOfGroupNotifyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfGroupReadOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfGroupWriteOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Group:
        context: OneOfGroupContextOptionsDef
        name: OneOfGroupNameOptionsDef
        security_level: OneOfGroupSecurityLevelOptionsDef
        notify: Optional[OneOfGroupNotifyOptionsDef]
        read: Optional[OneOfGroupReadOptionsDef]
        version: Optional[OneOfGroupVersionOptionsDef]
        write: Optional[OneOfGroupWriteOptionsDef]


    class OneOfUserUserNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfUserVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfUserVersionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUserVersionOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[DefaultUserVersionDef]


    class OneOfUserUserGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfUserAuthProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: UserAuthProtocolDef  # pytype: disable=annotation-type-mismatch


    class OneOfUserAuthProtocolOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUserPrivProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: UserPrivProtocolDef  # pytype: disable=annotation-type-mismatch


    class OneOfUserPrivProtocolOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUserPassphraseOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfUserPassphraseOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class User:
        user_group: OneOfUserUserGroupOptionsDef
        user_name: OneOfUserUserNameOptionsDef
        version: Union[
            OneOfUserVersionOptionsDef1,
            OneOfUserVersionOptionsDef2,
            OneOfUserVersionOptionsDef3,
        ]
        auth_protocol: Optional[
            Union[
                OneOfUserAuthProtocolOptionsDef1,
                OneOfUserAuthProtocolOptionsDef2,
            ]
        ]
        passphrase: Optional[
            Union[
                OneOfUserPassphraseOptionsDef1,
                OneOfUserPassphraseOptionsDef2,
            ]
        ]
        priv_protocol: Optional[
            Union[
                OneOfUserPrivProtocolOptionsDef1,
                OneOfUserPrivProtocolOptionsDef2,
            ]
        ]


    class OneOfHostHostNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfHostHostNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHostIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfHostIpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHostPortOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfHostHostUserNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfHostHostVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfHostHostVersionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfHostHostSecurityLevelOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: HostHostSecurityLevelDef  # pytype: disable=annotation-type-mismatch


    class OneOfHostHostSecurityLevelOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Host:
        host_name: Union[
            OneOfHostHostNameOptionsDef1, OneOfHostHostNameOptionsDef2
        ]
        host_security_level: Union[
            OneOfHostHostSecurityLevelOptionsDef1,
            OneOfHostHostSecurityLevelOptionsDef2,
        ]
        host_user_name: OneOfHostHostUserNameOptionsDef
        host_version: Union[
            OneOfHostHostVersionOptionsDef1,
            OneOfHostHostVersionOptionsDef2,
        ]
        ip: Union[OneOfHostIpOptionsDef1, OneOfHostIpOptionsDef2]
        port: OneOfHostPortOptionsDef


    class OneOfLinkUpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfLinkUpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLinkDownOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfLinkDownOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Data:
        # Configure SNMP community
        community: Optional[List[Community]]
        # Configure an SNMP group
        group: Optional[List[Group]]
        # Configure SNMP server to receive SNMP traps
        host: Optional[List[Host]]
        link_down: Optional[
            Union[OneOfLinkDownOptionsDef1, OneOfLinkDownOptionsDef2]
        ]
        link_up: Optional[
            Union[OneOfLinkUpOptionsDef1, OneOfLinkUpOptionsDef2]
        ]
        # Configure an SNMP user
        user: Optional[List[User]]


    class CreateNfvirtualSnmpParcelPostRequest:
        """
        SNMP profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class SnmpOneOfCommunityNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfCommunityCommunityAccessOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpCommunity:
        community_name: SnmpOneOfCommunityNameOptionsDef
        community_access: Optional[
            SnmpOneOfCommunityCommunityAccessOptionsDef
        ]


    class SnmpOneOfGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfGroupContextOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfGroupVersionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfGroupSecurityLevelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SnmpGroupSecurityLevelDef


    class SnmpOneOfGroupNotifyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfGroupReadOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfGroupWriteOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpGroup:
        context: SnmpOneOfGroupContextOptionsDef
        name: SnmpOneOfGroupNameOptionsDef
        security_level: SnmpOneOfGroupSecurityLevelOptionsDef
        notify: Optional[SnmpOneOfGroupNotifyOptionsDef]
        read: Optional[SnmpOneOfGroupReadOptionsDef]
        version: Optional[SnmpOneOfGroupVersionOptionsDef]
        write: Optional[SnmpOneOfGroupWriteOptionsDef]


    class SnmpOneOfUserUserNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfUserVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfUserVersionOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[SnmpDefaultUserVersionDef]


    class SnmpOneOfUserUserGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfUserAuthProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SnmpUserAuthProtocolDef  # pytype: disable=annotation-type-mismatch


    class SnmpOneOfUserPrivProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SnmpUserPrivProtocolDef  # pytype: disable=annotation-type-mismatch


    class SnmpOneOfUserPassphraseOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpUser:
        user_group: SnmpOneOfUserUserGroupOptionsDef
        user_name: SnmpOneOfUserUserNameOptionsDef
        version: Union[
            SnmpOneOfUserVersionOptionsDef1,
            OneOfUserVersionOptionsDef2,
            SnmpOneOfUserVersionOptionsDef3,
        ]
        auth_protocol: Optional[
            Union[
                SnmpOneOfUserAuthProtocolOptionsDef1,
                OneOfUserAuthProtocolOptionsDef2,
            ]
        ]
        passphrase: Optional[
            Union[
                SnmpOneOfUserPassphraseOptionsDef1,
                OneOfUserPassphraseOptionsDef2,
            ]
        ]
        priv_protocol: Optional[
            Union[
                SnmpOneOfUserPrivProtocolOptionsDef1,
                OneOfUserPrivProtocolOptionsDef2,
            ]
        ]


    class SnmpOneOfHostHostNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfHostIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class SnmpOneOfHostPortOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SnmpOneOfHostHostUserNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfHostHostVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SnmpOneOfHostHostSecurityLevelOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SnmpHostHostSecurityLevelDef  # pytype: disable=annotation-type-mismatch


    class SnmpHost:
        host_name: Union[
            SnmpOneOfHostHostNameOptionsDef1, OneOfHostHostNameOptionsDef2
        ]
        host_security_level: Union[
            SnmpOneOfHostHostSecurityLevelOptionsDef1,
            OneOfHostHostSecurityLevelOptionsDef2,
        ]
        host_user_name: SnmpOneOfHostHostUserNameOptionsDef
        host_version: Union[
            SnmpOneOfHostHostVersionOptionsDef1,
            OneOfHostHostVersionOptionsDef2,
        ]
        ip: Union[SnmpOneOfHostIpOptionsDef1, OneOfHostIpOptionsDef2]
        port: SnmpOneOfHostPortOptionsDef


    class SnmpData:
        # Configure SNMP community
        community: Optional[List[SnmpCommunity]]
        # Configure an SNMP group
        group: Optional[List[SnmpGroup]]
        # Configure SNMP server to receive SNMP traps
        host: Optional[List[SnmpHost]]
        link_down: Optional[
            Union[OneOfLinkDownOptionsDef1, OneOfLinkDownOptionsDef2]
        ]
        link_up: Optional[
            Union[OneOfLinkUpOptionsDef1, OneOfLinkUpOptionsDef2]
        ]
        # Configure an SNMP user
        user: Optional[List[SnmpUser]]


    class Payload:
        """
        SNMP profile parcel schema for PUT request
        """

        data: SnmpData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleNfvirtualSystemSnmpPayload:
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
        payload: Optional[Payload]


    class EditNfvirtualSnmpParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SystemSnmpOneOfCommunityNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfCommunityCommunityAccessOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpCommunity:
        community_name: SystemSnmpOneOfCommunityNameOptionsDef
        community_access: Optional[
            SystemSnmpOneOfCommunityCommunityAccessOptionsDef
        ]


    class SystemSnmpOneOfGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfGroupContextOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfGroupVersionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfGroupSecurityLevelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SystemSnmpGroupSecurityLevelDef


    class SystemSnmpOneOfGroupNotifyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfGroupReadOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfGroupWriteOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpGroup:
        context: SystemSnmpOneOfGroupContextOptionsDef
        name: SystemSnmpOneOfGroupNameOptionsDef
        security_level: SystemSnmpOneOfGroupSecurityLevelOptionsDef
        notify: Optional[SystemSnmpOneOfGroupNotifyOptionsDef]
        read: Optional[SystemSnmpOneOfGroupReadOptionsDef]
        version: Optional[SystemSnmpOneOfGroupVersionOptionsDef]
        write: Optional[SystemSnmpOneOfGroupWriteOptionsDef]


    class SystemSnmpOneOfUserUserNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfUserVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfUserVersionOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[SystemSnmpDefaultUserVersionDef]


    class SystemSnmpOneOfUserUserGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfUserAuthProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemSnmpUserAuthProtocolDef  # pytype: disable=annotation-type-mismatch


    class SystemSnmpOneOfUserPrivProtocolOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemSnmpUserPrivProtocolDef  # pytype: disable=annotation-type-mismatch


    class SystemSnmpOneOfUserPassphraseOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpUser:
        user_group: SystemSnmpOneOfUserUserGroupOptionsDef
        user_name: SystemSnmpOneOfUserUserNameOptionsDef
        version: Union[
            SystemSnmpOneOfUserVersionOptionsDef1,
            OneOfUserVersionOptionsDef2,
            SystemSnmpOneOfUserVersionOptionsDef3,
        ]
        auth_protocol: Optional[
            Union[
                SystemSnmpOneOfUserAuthProtocolOptionsDef1,
                OneOfUserAuthProtocolOptionsDef2,
            ]
        ]
        passphrase: Optional[
            Union[
                SystemSnmpOneOfUserPassphraseOptionsDef1,
                OneOfUserPassphraseOptionsDef2,
            ]
        ]
        priv_protocol: Optional[
            Union[
                SystemSnmpOneOfUserPrivProtocolOptionsDef1,
                OneOfUserPrivProtocolOptionsDef2,
            ]
        ]


    class SystemSnmpOneOfHostHostNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfHostIpOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class SystemSnmpOneOfHostPortOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemSnmpOneOfHostHostUserNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfHostHostVersionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSnmpOneOfHostHostSecurityLevelOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemSnmpHostHostSecurityLevelDef  # pytype: disable=annotation-type-mismatch


    class SystemSnmpHost:
        host_name: Union[
            SystemSnmpOneOfHostHostNameOptionsDef1,
            OneOfHostHostNameOptionsDef2,
        ]
        host_security_level: Union[
            SystemSnmpOneOfHostHostSecurityLevelOptionsDef1,
            OneOfHostHostSecurityLevelOptionsDef2,
        ]
        host_user_name: SystemSnmpOneOfHostHostUserNameOptionsDef
        host_version: Union[
            SystemSnmpOneOfHostHostVersionOptionsDef1,
            OneOfHostHostVersionOptionsDef2,
        ]
        ip: Union[
            SystemSnmpOneOfHostIpOptionsDef1, OneOfHostIpOptionsDef2
        ]
        port: SystemSnmpOneOfHostPortOptionsDef


    class SystemSnmpData:
        # Configure SNMP community
        community: Optional[List[SystemSnmpCommunity]]
        # Configure an SNMP group
        group: Optional[List[SystemSnmpGroup]]
        # Configure SNMP server to receive SNMP traps
        host: Optional[List[SystemSnmpHost]]
        link_down: Optional[
            Union[OneOfLinkDownOptionsDef1, OneOfLinkDownOptionsDef2]
        ]
        link_up: Optional[
            Union[OneOfLinkUpOptionsDef1, OneOfLinkUpOptionsDef2]
        ]
        # Configure an SNMP user
        user: Optional[List[SystemSnmpUser]]


    class EditNfvirtualSnmpParcelPutRequest:
        """
        SNMP profile parcel schema for PUT request
        """

        data: SystemSnmpData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


