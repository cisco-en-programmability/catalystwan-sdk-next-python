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


    class OneOfVrfOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVrfOptionsDef2:
        option_type: DefaultOptionTypeDef


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
        vrf: Optional[Union[OneOfVrfOptionsDef1, OneOfVrfOptionsDef2]]


    class OneOfTacacsGroupNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


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
        vrf: Optional[Union[OneOfVrfOptionsDef1, OneOfVrfOptionsDef2]]


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
        SD-Routing AAA feature schema
        """

        data: AaaData
        name: str
        # Set the feature description
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
        # SD-Routing AAA feature schema
        payload: Optional[Payload]


    class GetListSdRoutingSystemAaaSdRoutingPayload:
        data: Optional[List[Data]]


    class CreateSdroutingAaaFeaturePostResponse:
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


    class CreateSdroutingAaaFeaturePostRequest:
        """
        SD-Routing AAA feature schema
        """

        data: SystemAaaData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingSystemAaaSdRoutingPayload:
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
        # SD-Routing AAA feature schema
        payload: Optional[Payload]


    class EditSdroutingAaaFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingSystemAaaData:
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


    class EditSdroutingAaaFeaturePutRequest:
        """
        SD-Routing AAA feature schema
        """

        data: SdRoutingSystemAaaData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


