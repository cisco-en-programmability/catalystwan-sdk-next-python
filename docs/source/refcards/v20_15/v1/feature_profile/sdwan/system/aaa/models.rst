======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    UserPrivilegeDef = Literal["1", "15"]

    DefaultUserPrivilegeDef = Literal["15"]

    UserPubkeyChainKeyTypeDef = Literal["ssh-rsa"]

    RadiusServerKeyEnumDef = Literal["6", "7"]

    RadiusServerKeyTypeDef = Literal["key", "pac"]

    DefaultRadiusServerKeyTypeDef = Literal["key"]

    TacacsServerKeyEnumDef = Literal["6", "7"]

    AccountingRuleMethodDef = Literal[
        "commands", "exec", "network", "system"
    ]

    AccountingRuleLevelDef = Literal["1", "15"]

    AuthorizationRuleMethodDef = Literal["commands"]

    AuthorizationRuleLevelDef = Literal["1", "15"]

    AaaUserPrivilegeDef = Literal["1", "15"]

    AaaDefaultUserPrivilegeDef = Literal["15"]

    AaaUserPubkeyChainKeyTypeDef = Literal["ssh-rsa"]

    AaaRadiusServerKeyEnumDef = Literal["6", "7"]

    AaaRadiusServerKeyTypeDef = Literal["key", "pac"]

    AaaDefaultRadiusServerKeyTypeDef = Literal["key"]

    AaaTacacsServerKeyEnumDef = Literal["6", "7"]

    AaaAccountingRuleMethodDef = Literal[
        "commands", "exec", "network", "system"
    ]

    AaaAccountingRuleLevelDef = Literal["1", "15"]

    AaaAuthorizationRuleMethodDef = Literal["commands"]

    AaaAuthorizationRuleLevelDef = Literal["1", "15"]

    SystemAaaUserPrivilegeDef = Literal["1", "15"]

    SystemAaaDefaultUserPrivilegeDef = Literal["15"]

    SystemAaaUserPubkeyChainKeyTypeDef = Literal["ssh-rsa"]

    SystemAaaRadiusServerKeyEnumDef = Literal["6", "7"]

    SystemAaaRadiusServerKeyTypeDef = Literal["key", "pac"]

    SystemAaaDefaultRadiusServerKeyTypeDef = Literal["key"]

    SystemAaaTacacsServerKeyEnumDef = Literal["6", "7"]

    SystemAaaAccountingRuleMethodDef = Literal[
        "commands", "exec", "network", "system"
    ]

    SystemAaaAccountingRuleLevelDef = Literal["1", "15"]

    SystemAaaAuthorizationRuleMethodDef = Literal["commands"]

    SystemAaaAuthorizationRuleLevelDef = Literal["1", "15"]


    class OneOfAuthenticationGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAuthenticationGroupOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAuthenticationGroupOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfAccountingGroupOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAccountingGroupOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAccountingGroupOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfServerAuthOrderOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


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


    class OneOfUserPrivilegeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: UserPrivilegeDef


    class OneOfUserPrivilegeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUserPrivilegeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultUserPrivilegeDef  # pytype: disable=annotation-type-mismatch


    class OneOfUserPubkeyChainKeyStringOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfUserPubkeyChainKeyStringOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfUserPubkeyChainKeyTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UserPubkeyChainKeyTypeDef  # pytype: disable=annotation-type-mismatch


    class PubkeyChain:
        key_string: Union[
            OneOfUserPubkeyChainKeyStringOptionsDef1,
            OneOfUserPubkeyChainKeyStringOptionsDef2,
        ]
        key_type: Optional[OneOfUserPubkeyChainKeyTypeOptionsDef]


    class User:
        name: Union[OneOfUserNameOptionsDef1, OneOfUserNameOptionsDef2]
        password: Union[
            OneOfUserPasswordOptionsDef1, OneOfUserPasswordOptionsDef2
        ]
        privilege: Optional[
            Union[
                OneOfUserPrivilegeOptionsDef1,
                OneOfUserPrivilegeOptionsDef2,
                OneOfUserPrivilegeOptionsDef3,
            ]
        ]
        # List of RSA public-keys per user
        pubkey_chain: Optional[List[PubkeyChain]]


    class OneOfRadiusGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRadiusVpnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRadiusVpnOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfInterfaceNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfaceNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfaceNameOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfRadiusServerAddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfRadiusServerAuthPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRadiusServerAuthPortOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRadiusServerAuthPortOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfRadiusServerAcctPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRadiusServerAcctPortOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRadiusServerAcctPortOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfRadiusServerTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRadiusServerTimeoutOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRadiusServerTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfRadiusServerRetransmitOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRadiusServerRetransmitOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRadiusServerRetransmitOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfRadiusServerKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRadiusServerKeyOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRadiusServerSecretKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRadiusServerSecretKeyOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRadiusServerSecretKeyOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfRadiusServerKeyEnumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: RadiusServerKeyEnumDef  # pytype: disable=annotation-type-mismatch


    class OneOfRadiusServerKeyEnumOptionsDef2:
        option_type: DefaultOptionTypeDef


    class OneOfRadiusServerKeyTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: RadiusServerKeyTypeDef


    class OneOfRadiusServerKeyTypeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRadiusServerKeyTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultRadiusServerKeyTypeDef  # pytype: disable=annotation-type-mismatch


    class Server:
        address: OneOfRadiusServerAddressOptionsDef
        key: Union[
            OneOfRadiusServerKeyOptionsDef1,
            OneOfRadiusServerKeyOptionsDef2,
        ]
        acct_port: Optional[
            Union[
                OneOfRadiusServerAcctPortOptionsDef1,
                OneOfRadiusServerAcctPortOptionsDef2,
                OneOfRadiusServerAcctPortOptionsDef3,
            ]
        ]
        auth_port: Optional[
            Union[
                OneOfRadiusServerAuthPortOptionsDef1,
                OneOfRadiusServerAuthPortOptionsDef2,
                OneOfRadiusServerAuthPortOptionsDef3,
            ]
        ]
        key_enum: Optional[
            Union[
                OneOfRadiusServerKeyEnumOptionsDef1,
                OneOfRadiusServerKeyEnumOptionsDef2,
            ]
        ]
        key_type: Optional[
            Union[
                OneOfRadiusServerKeyTypeOptionsDef1,
                OneOfRadiusServerKeyTypeOptionsDef2,
                OneOfRadiusServerKeyTypeOptionsDef3,
            ]
        ]
        retransmit: Optional[
            Union[
                OneOfRadiusServerRetransmitOptionsDef1,
                OneOfRadiusServerRetransmitOptionsDef2,
                OneOfRadiusServerRetransmitOptionsDef3,
            ]
        ]
        secret_key: Optional[
            Union[
                OneOfRadiusServerSecretKeyOptionsDef1,
                OneOfRadiusServerSecretKeyOptionsDef2,
                OneOfRadiusServerSecretKeyOptionsDef3,
            ]
        ]
        timeout: Optional[
            Union[
                OneOfRadiusServerTimeoutOptionsDef1,
                OneOfRadiusServerTimeoutOptionsDef2,
                OneOfRadiusServerTimeoutOptionsDef3,
            ]
        ]


    class Radius:
        group_name: OneOfRadiusGroupNameOptionsDef
        # Configure the Radius server
        server: List[Server]
        source_interface: Optional[
            Union[
                OneOfInterfaceNameOptionsDef1,
                OneOfInterfaceNameOptionsDef2,
                OneOfInterfaceNameOptionsDef3,
            ]
        ]
        vpn: Optional[
            Union[OneOfRadiusVpnOptionsDef1, OneOfRadiusVpnOptionsDef2]
        ]


    class OneOfTacacsGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTacacsVpnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTacacsVpnOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfTacacsServerAddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfTacacsServerPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTacacsServerPortOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTacacsServerPortOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfTacacsServerTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTacacsServerTimeoutOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTacacsServerTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfTacacsServerKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTacacsServerKeyOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTacacsServerSecretKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTacacsServerSecretKeyOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTacacsServerKeyEnumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TacacsServerKeyEnumDef  # pytype: disable=annotation-type-mismatch


    class OneOfTacacsServerKeyEnumOptionsDef2:
        option_type: DefaultOptionTypeDef


    class AaaServer:
        address: OneOfTacacsServerAddressOptionsDef
        key: Union[
            OneOfTacacsServerKeyOptionsDef1,
            OneOfTacacsServerKeyOptionsDef2,
        ]
        key_enum: Optional[
            Union[
                OneOfTacacsServerKeyEnumOptionsDef1,
                OneOfTacacsServerKeyEnumOptionsDef2,
            ]
        ]
        port: Optional[
            Union[
                OneOfTacacsServerPortOptionsDef1,
                OneOfTacacsServerPortOptionsDef2,
                OneOfTacacsServerPortOptionsDef3,
            ]
        ]
        secret_key: Optional[
            Union[
                OneOfTacacsServerSecretKeyOptionsDef1,
                OneOfTacacsServerSecretKeyOptionsDef2,
            ]
        ]
        timeout: Optional[
            Union[
                OneOfTacacsServerTimeoutOptionsDef1,
                OneOfTacacsServerTimeoutOptionsDef2,
                OneOfTacacsServerTimeoutOptionsDef3,
            ]
        ]


    class Tacacs:
        group_name: OneOfTacacsGroupNameOptionsDef
        # Configure the TACACS server
        server: List[AaaServer]
        source_interface: Optional[
            Union[
                OneOfInterfaceNameOptionsDef1,
                OneOfInterfaceNameOptionsDef2,
                OneOfInterfaceNameOptionsDef3,
            ]
        ]
        vpn: Optional[
            Union[OneOfTacacsVpnOptionsDef1, OneOfTacacsVpnOptionsDef2]
        ]


    class OneOfAccountingRuleRuleIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAccountingRuleMethodOptionsDef:
        option_type: GlobalOptionTypeDef
        value: AccountingRuleMethodDef  # pytype: disable=annotation-type-mismatch


    class OneOfAccountingRuleLevelOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AccountingRuleLevelDef  # pytype: disable=annotation-type-mismatch


    class OneOfAccountingRuleLevelOptionsDef2:
        option_type: DefaultOptionTypeDef


    class OneOfAccountingRuleStartStopOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAccountingRuleStartStopOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAccountingRuleStartStopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfAccountingRuleGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class AccountingRule:
        group: OneOfAccountingRuleGroupOptionsDef
        method: OneOfAccountingRuleMethodOptionsDef
        rule_id: OneOfAccountingRuleRuleIdOptionsDef
        level: Optional[
            Union[
                OneOfAccountingRuleLevelOptionsDef1,
                OneOfAccountingRuleLevelOptionsDef2,
            ]
        ]
        start_stop: Optional[
            Union[
                OneOfAccountingRuleStartStopOptionsDef1,
                OneOfAccountingRuleStartStopOptionsDef2,
                OneOfAccountingRuleStartStopOptionsDef3,
            ]
        ]


    class OneOfAuthorizationConsoleOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAuthorizationConsoleOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAuthorizationConsoleOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfAuthorizationConfigCommandsOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAuthorizationConfigCommandsOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAuthorizationConfigCommandsOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfAuthorizationRuleRuleIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAuthorizationRuleMethodOptionsDef:
        option_type: GlobalOptionTypeDef
        value: AuthorizationRuleMethodDef  # pytype: disable=annotation-type-mismatch


    class OneOfAuthorizationRuleLevelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: AuthorizationRuleLevelDef  # pytype: disable=annotation-type-mismatch


    class OneOfAuthorizationRuleGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfAuthorizationRuleIfAuthenticatedOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAuthorizationRuleIfAuthenticatedOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: bool


    class AuthorizationRule:
        group: OneOfAuthorizationRuleGroupOptionsDef
        level: OneOfAuthorizationRuleLevelOptionsDef
        method: OneOfAuthorizationRuleMethodOptionsDef
        rule_id: OneOfAuthorizationRuleRuleIdOptionsDef
        if_authenticated: Optional[
            Union[
                OneOfAuthorizationRuleIfAuthenticatedOptionsDef1,
                OneOfAuthorizationRuleIfAuthenticatedOptionsDef2,
            ]
        ]


    class AaaData:
        accounting_group: Union[
            OneOfAccountingGroupOptionsDef1,
            OneOfAccountingGroupOptionsDef2,
            OneOfAccountingGroupOptionsDef3,
        ]
        authentication_group: Union[
            OneOfAuthenticationGroupOptionsDef1,
            OneOfAuthenticationGroupOptionsDef2,
            OneOfAuthenticationGroupOptionsDef3,
        ]
        authorization_config_commands: Union[
            OneOfAuthorizationConfigCommandsOptionsDef1,
            OneOfAuthorizationConfigCommandsOptionsDef2,
            OneOfAuthorizationConfigCommandsOptionsDef3,
        ]
        authorization_console: Union[
            OneOfAuthorizationConsoleOptionsDef1,
            OneOfAuthorizationConsoleOptionsDef2,
            OneOfAuthorizationConsoleOptionsDef3,
        ]
        server_auth_order: OneOfServerAuthOrderOptionsDef
        # Configure the accounting rules
        accounting_rule: Optional[List[AccountingRule]]
        # Configure the Authorization Rules
        authorization_rule: Optional[List[AuthorizationRule]]
        # Configure the Radius serverGroup
        radius: Optional[List[Radius]]
        # Configure the TACACS serverGroup
        tacacs: Optional[List[Tacacs]]
        # Create local login account
        user: Optional[List[User]]


    class Payload:
        """
        AAA profile parcel schema for POST request
        """

        data: AaaData
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
        # AAA profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanSystemAaaPayload:
        data: Optional[List[Data]]


    class CreateAaaProfileParcelForSystemPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SystemAaaData:
        accounting_group: Union[
            OneOfAccountingGroupOptionsDef1,
            OneOfAccountingGroupOptionsDef2,
            OneOfAccountingGroupOptionsDef3,
        ]
        authentication_group: Union[
            OneOfAuthenticationGroupOptionsDef1,
            OneOfAuthenticationGroupOptionsDef2,
            OneOfAuthenticationGroupOptionsDef3,
        ]
        authorization_config_commands: Union[
            OneOfAuthorizationConfigCommandsOptionsDef1,
            OneOfAuthorizationConfigCommandsOptionsDef2,
            OneOfAuthorizationConfigCommandsOptionsDef3,
        ]
        authorization_console: Union[
            OneOfAuthorizationConsoleOptionsDef1,
            OneOfAuthorizationConsoleOptionsDef2,
            OneOfAuthorizationConsoleOptionsDef3,
        ]
        server_auth_order: OneOfServerAuthOrderOptionsDef
        # Configure the accounting rules
        accounting_rule: Optional[List[AccountingRule]]
        # Configure the Authorization Rules
        authorization_rule: Optional[List[AuthorizationRule]]
        # Configure the Radius serverGroup
        radius: Optional[List[Radius]]
        # Configure the TACACS serverGroup
        tacacs: Optional[List[Tacacs]]
        # Create local login account
        user: Optional[List[User]]


    class CreateAaaProfileParcelForSystemPostRequest:
        """
        AAA profile parcel schema for POST request
        """

        data: SystemAaaData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class AaaOneOfServerAuthOrderOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class AaaOneOfUserNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaOneOfUserPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaOneOfUserPrivilegeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AaaUserPrivilegeDef


    class AaaOneOfUserPrivilegeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: AaaDefaultUserPrivilegeDef  # pytype: disable=annotation-type-mismatch


    class AaaOneOfUserPubkeyChainKeyTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: AaaUserPubkeyChainKeyTypeDef  # pytype: disable=annotation-type-mismatch


    class AaaPubkeyChain:
        key_string: Union[
            OneOfUserPubkeyChainKeyStringOptionsDef1,
            OneOfUserPubkeyChainKeyStringOptionsDef2,
        ]
        key_type: Optional[AaaOneOfUserPubkeyChainKeyTypeOptionsDef]


    class AaaUser:
        name: Union[AaaOneOfUserNameOptionsDef1, OneOfUserNameOptionsDef2]
        password: Union[
            AaaOneOfUserPasswordOptionsDef1, OneOfUserPasswordOptionsDef2
        ]
        privilege: Optional[
            Union[
                AaaOneOfUserPrivilegeOptionsDef1,
                OneOfUserPrivilegeOptionsDef2,
                AaaOneOfUserPrivilegeOptionsDef3,
            ]
        ]
        # List of RSA public-keys per user
        pubkey_chain: Optional[List[AaaPubkeyChain]]


    class AaaOneOfRadiusGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaOneOfRadiusServerAddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class AaaOneOfRadiusServerAuthPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class AaaOneOfRadiusServerAuthPortOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class AaaOneOfRadiusServerAcctPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class AaaOneOfRadiusServerAcctPortOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class AaaOneOfRadiusServerTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class AaaOneOfRadiusServerTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class AaaOneOfRadiusServerRetransmitOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class AaaOneOfRadiusServerRetransmitOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class AaaOneOfRadiusServerKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaOneOfRadiusServerSecretKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaOneOfRadiusServerKeyEnumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AaaRadiusServerKeyEnumDef  # pytype: disable=annotation-type-mismatch


    class AaaOneOfRadiusServerKeyTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AaaRadiusServerKeyTypeDef


    class AaaOneOfRadiusServerKeyTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: AaaDefaultRadiusServerKeyTypeDef  # pytype: disable=annotation-type-mismatch


    class SystemAaaServer:
        address: AaaOneOfRadiusServerAddressOptionsDef
        key: Union[
            AaaOneOfRadiusServerKeyOptionsDef1,
            OneOfRadiusServerKeyOptionsDef2,
        ]
        acct_port: Optional[
            Union[
                AaaOneOfRadiusServerAcctPortOptionsDef1,
                OneOfRadiusServerAcctPortOptionsDef2,
                AaaOneOfRadiusServerAcctPortOptionsDef3,
            ]
        ]
        auth_port: Optional[
            Union[
                AaaOneOfRadiusServerAuthPortOptionsDef1,
                OneOfRadiusServerAuthPortOptionsDef2,
                AaaOneOfRadiusServerAuthPortOptionsDef3,
            ]
        ]
        key_enum: Optional[
            Union[
                AaaOneOfRadiusServerKeyEnumOptionsDef1,
                OneOfRadiusServerKeyEnumOptionsDef2,
            ]
        ]
        key_type: Optional[
            Union[
                AaaOneOfRadiusServerKeyTypeOptionsDef1,
                OneOfRadiusServerKeyTypeOptionsDef2,
                AaaOneOfRadiusServerKeyTypeOptionsDef3,
            ]
        ]
        retransmit: Optional[
            Union[
                AaaOneOfRadiusServerRetransmitOptionsDef1,
                OneOfRadiusServerRetransmitOptionsDef2,
                AaaOneOfRadiusServerRetransmitOptionsDef3,
            ]
        ]
        secret_key: Optional[
            Union[
                AaaOneOfRadiusServerSecretKeyOptionsDef1,
                OneOfRadiusServerSecretKeyOptionsDef2,
                OneOfRadiusServerSecretKeyOptionsDef3,
            ]
        ]
        timeout: Optional[
            Union[
                AaaOneOfRadiusServerTimeoutOptionsDef1,
                OneOfRadiusServerTimeoutOptionsDef2,
                AaaOneOfRadiusServerTimeoutOptionsDef3,
            ]
        ]


    class AaaRadius:
        group_name: AaaOneOfRadiusGroupNameOptionsDef
        # Configure the Radius server
        server: List[SystemAaaServer]
        source_interface: Optional[
            Union[
                OneOfInterfaceNameOptionsDef1,
                OneOfInterfaceNameOptionsDef2,
                OneOfInterfaceNameOptionsDef3,
            ]
        ]
        vpn: Optional[
            Union[OneOfRadiusVpnOptionsDef1, OneOfRadiusVpnOptionsDef2]
        ]


    class AaaOneOfTacacsGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaOneOfTacacsServerAddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class AaaOneOfTacacsServerPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class AaaOneOfTacacsServerPortOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class AaaOneOfTacacsServerTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class AaaOneOfTacacsServerTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class AaaOneOfTacacsServerKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaOneOfTacacsServerSecretKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaOneOfTacacsServerKeyEnumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AaaTacacsServerKeyEnumDef  # pytype: disable=annotation-type-mismatch


    class SdwanSystemAaaServer:
        address: AaaOneOfTacacsServerAddressOptionsDef
        key: Union[
            AaaOneOfTacacsServerKeyOptionsDef1,
            OneOfTacacsServerKeyOptionsDef2,
        ]
        key_enum: Optional[
            Union[
                AaaOneOfTacacsServerKeyEnumOptionsDef1,
                OneOfTacacsServerKeyEnumOptionsDef2,
            ]
        ]
        port: Optional[
            Union[
                AaaOneOfTacacsServerPortOptionsDef1,
                OneOfTacacsServerPortOptionsDef2,
                AaaOneOfTacacsServerPortOptionsDef3,
            ]
        ]
        secret_key: Optional[
            Union[
                AaaOneOfTacacsServerSecretKeyOptionsDef1,
                OneOfTacacsServerSecretKeyOptionsDef2,
            ]
        ]
        timeout: Optional[
            Union[
                AaaOneOfTacacsServerTimeoutOptionsDef1,
                OneOfTacacsServerTimeoutOptionsDef2,
                AaaOneOfTacacsServerTimeoutOptionsDef3,
            ]
        ]


    class AaaTacacs:
        group_name: AaaOneOfTacacsGroupNameOptionsDef
        # Configure the TACACS server
        server: List[SdwanSystemAaaServer]
        source_interface: Optional[
            Union[
                OneOfInterfaceNameOptionsDef1,
                OneOfInterfaceNameOptionsDef2,
                OneOfInterfaceNameOptionsDef3,
            ]
        ]
        vpn: Optional[
            Union[OneOfTacacsVpnOptionsDef1, OneOfTacacsVpnOptionsDef2]
        ]


    class AaaOneOfAccountingRuleRuleIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaOneOfAccountingRuleMethodOptionsDef:
        option_type: GlobalOptionTypeDef
        value: AaaAccountingRuleMethodDef  # pytype: disable=annotation-type-mismatch


    class AaaOneOfAccountingRuleLevelOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AaaAccountingRuleLevelDef  # pytype: disable=annotation-type-mismatch


    class AaaOneOfAccountingRuleGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class AaaAccountingRule:
        group: AaaOneOfAccountingRuleGroupOptionsDef
        method: AaaOneOfAccountingRuleMethodOptionsDef
        rule_id: AaaOneOfAccountingRuleRuleIdOptionsDef
        level: Optional[
            Union[
                AaaOneOfAccountingRuleLevelOptionsDef1,
                OneOfAccountingRuleLevelOptionsDef2,
            ]
        ]
        start_stop: Optional[
            Union[
                OneOfAccountingRuleStartStopOptionsDef1,
                OneOfAccountingRuleStartStopOptionsDef2,
                OneOfAccountingRuleStartStopOptionsDef3,
            ]
        ]


    class AaaOneOfAuthorizationRuleRuleIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaOneOfAuthorizationRuleMethodOptionsDef:
        option_type: GlobalOptionTypeDef
        value: AaaAuthorizationRuleMethodDef  # pytype: disable=annotation-type-mismatch


    class AaaOneOfAuthorizationRuleLevelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: AaaAuthorizationRuleLevelDef  # pytype: disable=annotation-type-mismatch


    class AaaOneOfAuthorizationRuleGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class AaaAuthorizationRule:
        group: AaaOneOfAuthorizationRuleGroupOptionsDef
        level: AaaOneOfAuthorizationRuleLevelOptionsDef
        method: AaaOneOfAuthorizationRuleMethodOptionsDef
        rule_id: AaaOneOfAuthorizationRuleRuleIdOptionsDef
        if_authenticated: Optional[
            Union[
                OneOfAuthorizationRuleIfAuthenticatedOptionsDef1,
                OneOfAuthorizationRuleIfAuthenticatedOptionsDef2,
            ]
        ]


    class SdwanSystemAaaData:
        accounting_group: Union[
            OneOfAccountingGroupOptionsDef1,
            OneOfAccountingGroupOptionsDef2,
            OneOfAccountingGroupOptionsDef3,
        ]
        authentication_group: Union[
            OneOfAuthenticationGroupOptionsDef1,
            OneOfAuthenticationGroupOptionsDef2,
            OneOfAuthenticationGroupOptionsDef3,
        ]
        authorization_config_commands: Union[
            OneOfAuthorizationConfigCommandsOptionsDef1,
            OneOfAuthorizationConfigCommandsOptionsDef2,
            OneOfAuthorizationConfigCommandsOptionsDef3,
        ]
        authorization_console: Union[
            OneOfAuthorizationConsoleOptionsDef1,
            OneOfAuthorizationConsoleOptionsDef2,
            OneOfAuthorizationConsoleOptionsDef3,
        ]
        server_auth_order: AaaOneOfServerAuthOrderOptionsDef
        # Configure the accounting rules
        accounting_rule: Optional[List[AaaAccountingRule]]
        # Configure the Authorization Rules
        authorization_rule: Optional[List[AaaAuthorizationRule]]
        # Configure the Radius serverGroup
        radius: Optional[List[AaaRadius]]
        # Configure the TACACS serverGroup
        tacacs: Optional[List[AaaTacacs]]
        # Create local login account
        user: Optional[List[AaaUser]]


    class AaaPayload:
        """
        AAA profile parcel schema for PUT request
        """

        data: SdwanSystemAaaData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanSystemAaaPayload:
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
        payload: Optional[AaaPayload]


    class EditAaaProfileParcelForSystemPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SystemAaaOneOfServerAuthOrderOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class SystemAaaOneOfUserNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemAaaOneOfUserPasswordOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemAaaOneOfUserPrivilegeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemAaaUserPrivilegeDef


    class SystemAaaOneOfUserPrivilegeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: SystemAaaDefaultUserPrivilegeDef  # pytype: disable=annotation-type-mismatch


    class SystemAaaOneOfUserPubkeyChainKeyTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SystemAaaUserPubkeyChainKeyTypeDef  # pytype: disable=annotation-type-mismatch


    class SystemAaaPubkeyChain:
        key_string: Union[
            OneOfUserPubkeyChainKeyStringOptionsDef1,
            OneOfUserPubkeyChainKeyStringOptionsDef2,
        ]
        key_type: Optional[SystemAaaOneOfUserPubkeyChainKeyTypeOptionsDef]


    class SystemAaaUser:
        name: Union[
            SystemAaaOneOfUserNameOptionsDef1, OneOfUserNameOptionsDef2
        ]
        password: Union[
            SystemAaaOneOfUserPasswordOptionsDef1,
            OneOfUserPasswordOptionsDef2,
        ]
        privilege: Optional[
            Union[
                SystemAaaOneOfUserPrivilegeOptionsDef1,
                OneOfUserPrivilegeOptionsDef2,
                SystemAaaOneOfUserPrivilegeOptionsDef3,
            ]
        ]
        # List of RSA public-keys per user
        pubkey_chain: Optional[List[SystemAaaPubkeyChain]]


    class SystemAaaOneOfRadiusGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemAaaOneOfRadiusServerAddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class SystemAaaOneOfRadiusServerAuthPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemAaaOneOfRadiusServerAuthPortOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SystemAaaOneOfRadiusServerAcctPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemAaaOneOfRadiusServerAcctPortOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SystemAaaOneOfRadiusServerTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemAaaOneOfRadiusServerTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SystemAaaOneOfRadiusServerRetransmitOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemAaaOneOfRadiusServerRetransmitOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SystemAaaOneOfRadiusServerKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemAaaOneOfRadiusServerSecretKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemAaaOneOfRadiusServerKeyEnumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemAaaRadiusServerKeyEnumDef  # pytype: disable=annotation-type-mismatch


    class SystemAaaOneOfRadiusServerKeyTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemAaaRadiusServerKeyTypeDef


    class SystemAaaOneOfRadiusServerKeyTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: SystemAaaDefaultRadiusServerKeyTypeDef  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdwanSystemAaaServer:
        address: SystemAaaOneOfRadiusServerAddressOptionsDef
        key: Union[
            SystemAaaOneOfRadiusServerKeyOptionsDef1,
            OneOfRadiusServerKeyOptionsDef2,
        ]
        acct_port: Optional[
            Union[
                SystemAaaOneOfRadiusServerAcctPortOptionsDef1,
                OneOfRadiusServerAcctPortOptionsDef2,
                SystemAaaOneOfRadiusServerAcctPortOptionsDef3,
            ]
        ]
        auth_port: Optional[
            Union[
                SystemAaaOneOfRadiusServerAuthPortOptionsDef1,
                OneOfRadiusServerAuthPortOptionsDef2,
                SystemAaaOneOfRadiusServerAuthPortOptionsDef3,
            ]
        ]
        key_enum: Optional[
            Union[
                SystemAaaOneOfRadiusServerKeyEnumOptionsDef1,
                OneOfRadiusServerKeyEnumOptionsDef2,
            ]
        ]
        key_type: Optional[
            Union[
                SystemAaaOneOfRadiusServerKeyTypeOptionsDef1,
                OneOfRadiusServerKeyTypeOptionsDef2,
                SystemAaaOneOfRadiusServerKeyTypeOptionsDef3,
            ]
        ]
        retransmit: Optional[
            Union[
                SystemAaaOneOfRadiusServerRetransmitOptionsDef1,
                OneOfRadiusServerRetransmitOptionsDef2,
                SystemAaaOneOfRadiusServerRetransmitOptionsDef3,
            ]
        ]
        secret_key: Optional[
            Union[
                SystemAaaOneOfRadiusServerSecretKeyOptionsDef1,
                OneOfRadiusServerSecretKeyOptionsDef2,
                OneOfRadiusServerSecretKeyOptionsDef3,
            ]
        ]
        timeout: Optional[
            Union[
                SystemAaaOneOfRadiusServerTimeoutOptionsDef1,
                OneOfRadiusServerTimeoutOptionsDef2,
                SystemAaaOneOfRadiusServerTimeoutOptionsDef3,
            ]
        ]


    class SystemAaaRadius:
        group_name: SystemAaaOneOfRadiusGroupNameOptionsDef
        # Configure the Radius server
        server: List[FeatureProfileSdwanSystemAaaServer]
        source_interface: Optional[
            Union[
                OneOfInterfaceNameOptionsDef1,
                OneOfInterfaceNameOptionsDef2,
                OneOfInterfaceNameOptionsDef3,
            ]
        ]
        vpn: Optional[
            Union[OneOfRadiusVpnOptionsDef1, OneOfRadiusVpnOptionsDef2]
        ]


    class SystemAaaOneOfTacacsGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemAaaOneOfTacacsServerAddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class SystemAaaOneOfTacacsServerPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemAaaOneOfTacacsServerPortOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SystemAaaOneOfTacacsServerTimeoutOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemAaaOneOfTacacsServerTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SystemAaaOneOfTacacsServerKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemAaaOneOfTacacsServerSecretKeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemAaaOneOfTacacsServerKeyEnumOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemAaaTacacsServerKeyEnumDef  # pytype: disable=annotation-type-mismatch


    class V1FeatureProfileSdwanSystemAaaServer:
        address: SystemAaaOneOfTacacsServerAddressOptionsDef
        key: Union[
            SystemAaaOneOfTacacsServerKeyOptionsDef1,
            OneOfTacacsServerKeyOptionsDef2,
        ]
        key_enum: Optional[
            Union[
                SystemAaaOneOfTacacsServerKeyEnumOptionsDef1,
                OneOfTacacsServerKeyEnumOptionsDef2,
            ]
        ]
        port: Optional[
            Union[
                SystemAaaOneOfTacacsServerPortOptionsDef1,
                OneOfTacacsServerPortOptionsDef2,
                SystemAaaOneOfTacacsServerPortOptionsDef3,
            ]
        ]
        secret_key: Optional[
            Union[
                SystemAaaOneOfTacacsServerSecretKeyOptionsDef1,
                OneOfTacacsServerSecretKeyOptionsDef2,
            ]
        ]
        timeout: Optional[
            Union[
                SystemAaaOneOfTacacsServerTimeoutOptionsDef1,
                OneOfTacacsServerTimeoutOptionsDef2,
                SystemAaaOneOfTacacsServerTimeoutOptionsDef3,
            ]
        ]


    class SystemAaaTacacs:
        group_name: SystemAaaOneOfTacacsGroupNameOptionsDef
        # Configure the TACACS server
        server: List[V1FeatureProfileSdwanSystemAaaServer]
        source_interface: Optional[
            Union[
                OneOfInterfaceNameOptionsDef1,
                OneOfInterfaceNameOptionsDef2,
                OneOfInterfaceNameOptionsDef3,
            ]
        ]
        vpn: Optional[
            Union[OneOfTacacsVpnOptionsDef1, OneOfTacacsVpnOptionsDef2]
        ]


    class SystemAaaOneOfAccountingRuleRuleIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemAaaOneOfAccountingRuleMethodOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SystemAaaAccountingRuleMethodDef  # pytype: disable=annotation-type-mismatch


    class SystemAaaOneOfAccountingRuleLevelOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemAaaAccountingRuleLevelDef  # pytype: disable=annotation-type-mismatch


    class SystemAaaOneOfAccountingRuleGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class SystemAaaAccountingRule:
        group: SystemAaaOneOfAccountingRuleGroupOptionsDef
        method: SystemAaaOneOfAccountingRuleMethodOptionsDef
        rule_id: SystemAaaOneOfAccountingRuleRuleIdOptionsDef
        level: Optional[
            Union[
                SystemAaaOneOfAccountingRuleLevelOptionsDef1,
                OneOfAccountingRuleLevelOptionsDef2,
            ]
        ]
        start_stop: Optional[
            Union[
                OneOfAccountingRuleStartStopOptionsDef1,
                OneOfAccountingRuleStartStopOptionsDef2,
                OneOfAccountingRuleStartStopOptionsDef3,
            ]
        ]


    class SystemAaaOneOfAuthorizationRuleRuleIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemAaaOneOfAuthorizationRuleMethodOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SystemAaaAuthorizationRuleMethodDef  # pytype: disable=annotation-type-mismatch


    class SystemAaaOneOfAuthorizationRuleLevelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SystemAaaAuthorizationRuleLevelDef  # pytype: disable=annotation-type-mismatch


    class SystemAaaOneOfAuthorizationRuleGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class SystemAaaAuthorizationRule:
        group: SystemAaaOneOfAuthorizationRuleGroupOptionsDef
        level: SystemAaaOneOfAuthorizationRuleLevelOptionsDef
        method: SystemAaaOneOfAuthorizationRuleMethodOptionsDef
        rule_id: SystemAaaOneOfAuthorizationRuleRuleIdOptionsDef
        if_authenticated: Optional[
            Union[
                OneOfAuthorizationRuleIfAuthenticatedOptionsDef1,
                OneOfAuthorizationRuleIfAuthenticatedOptionsDef2,
            ]
        ]


    class FeatureProfileSdwanSystemAaaData:
        accounting_group: Union[
            OneOfAccountingGroupOptionsDef1,
            OneOfAccountingGroupOptionsDef2,
            OneOfAccountingGroupOptionsDef3,
        ]
        authentication_group: Union[
            OneOfAuthenticationGroupOptionsDef1,
            OneOfAuthenticationGroupOptionsDef2,
            OneOfAuthenticationGroupOptionsDef3,
        ]
        authorization_config_commands: Union[
            OneOfAuthorizationConfigCommandsOptionsDef1,
            OneOfAuthorizationConfigCommandsOptionsDef2,
            OneOfAuthorizationConfigCommandsOptionsDef3,
        ]
        authorization_console: Union[
            OneOfAuthorizationConsoleOptionsDef1,
            OneOfAuthorizationConsoleOptionsDef2,
            OneOfAuthorizationConsoleOptionsDef3,
        ]
        server_auth_order: SystemAaaOneOfServerAuthOrderOptionsDef
        # Configure the accounting rules
        accounting_rule: Optional[List[SystemAaaAccountingRule]]
        # Configure the Authorization Rules
        authorization_rule: Optional[List[SystemAaaAuthorizationRule]]
        # Configure the Radius serverGroup
        radius: Optional[List[SystemAaaRadius]]
        # Configure the TACACS serverGroup
        tacacs: Optional[List[SystemAaaTacacs]]
        # Create local login account
        user: Optional[List[SystemAaaUser]]


    class EditAaaProfileParcelForSystemPutRequest:
        """
        AAA profile parcel schema for PUT request
        """

        data: FeatureProfileSdwanSystemAaaData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


