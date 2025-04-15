======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    ReplayWindowDef = Literal[
        "1024", "128", "2048", "256", "4096", "512", "64", "8192"
    ]

    DefaultReplayWindowDef = Literal["512"]

    IntegrityTypeListDef = Literal[
        "esp", "ip-udp-esp", "ip-udp-esp-no-id", "none"
    ]

    KeyTcpDef = Literal["aes-128-cmac", "hmac-sha-1", "hmac-sha-256"]


    class OneOfRekeyOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRekeyOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRekeyOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfReplayWindowOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ReplayWindowDef


    class OneOfReplayWindowOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfReplayWindowOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultReplayWindowDef  # pytype: disable=annotation-type-mismatch


    class OneOfExtendedArWindowOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfExtendedArWindowOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfExtendedArWindowOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIntegrityTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[IntegrityTypeListDef]


    class OneOfIntegrityTypeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOnBooleanDefaultFalseOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOnBooleanDefaultFalseOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultFalseOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfKeychainNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfKeychainKeyidOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Keychain:
        id: OneOfKeychainKeyidOptionsDef
        name: OneOfKeychainNameOptionsDef


    class OneOfKeyIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfKeyChainNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfKeySendIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfKeySendIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfKeyRecvIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfKeyRecvIdOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfKeyTcpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: KeyTcpDef  # pytype: disable=annotation-type-mismatch


    class OneOfKeyStringOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfKeyStringOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfKeyStartEpochOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfOnBooleanDefaultTrueOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOnBooleanDefaultTrueOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultTrueOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfendChoice1:
        infinite: Union[
            OneOfOnBooleanDefaultTrueOptionsDef1,
            OneOfOnBooleanDefaultTrueOptionsDef2,
            OneOfOnBooleanDefaultTrueOptionsDef3,
        ]


    class OneOfKeyDurationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfKeyDurationOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfendChoice2:
        duration: Union[
            OneOfKeyDurationOptionsDef1, OneOfKeyDurationOptionsDef2
        ]


    class OneOfKeyEndEpochOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfendChoice3:
        exact: OneOfKeyEndEpochOptionsDef


    class LifetimeSettings:
        start_epoch: OneOfKeyStartEpochOptionsDef
        local: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        one_ofend_choice: Optional[
            Union[OneOfendChoice1, OneOfendChoice2, OneOfendChoice3]
        ]


    class Key:
        id: OneOfKeyIdOptionsDef
        key_string: Union[
            OneOfKeyStringOptionsDef1, OneOfKeyStringOptionsDef2
        ]
        name: OneOfKeyChainNameOptionsDef
        recv_id: Union[
            OneOfKeyRecvIdOptionsDef1, OneOfKeyRecvIdOptionsDef2
        ]
        send_id: Union[
            OneOfKeySendIdOptionsDef1, OneOfKeySendIdOptionsDef2
        ]
        tcp: OneOfKeyTcpOptionsDef
        accept_ao_mismatch: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        accept_lifetime: Optional[LifetimeSettings]
        include_tcp_options: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        send_lifetime: Optional[LifetimeSettings]


    class SecurityData:
        extended_ar_window: Optional[
            Union[
                OneOfExtendedArWindowOptionsDef1,
                OneOfExtendedArWindowOptionsDef2,
                OneOfExtendedArWindowOptionsDef3,
            ]
        ]
        integrity_type: Optional[
            Union[
                OneOfIntegrityTypeOptionsDef1,
                OneOfIntegrityTypeOptionsDef2,
            ]
        ]
        # Configure a Key
        key: Optional[List[Key]]
        # Configure a Keychain
        keychain: Optional[List[Keychain]]
        pairwise_keying: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        rekey: Optional[
            Union[
                OneOfRekeyOptionsDef1,
                OneOfRekeyOptionsDef2,
                OneOfRekeyOptionsDef3,
            ]
        ]
        replay_window: Optional[
            Union[
                OneOfReplayWindowOptionsDef1,
                OneOfReplayWindowOptionsDef2,
                OneOfReplayWindowOptionsDef3,
            ]
        ]


    class Payload:
        """
        System profile Security feature schema for request
        """

        data: SecurityData
        name: str
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
        # System profile Security feature schema for request
        payload: Optional[Payload]


    class GetListSdwanSystemSecurityPayload:
        data: Optional[List[Data]]


    class CreateSecurityForSystemPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SystemSecurityData:
        extended_ar_window: Optional[
            Union[
                OneOfExtendedArWindowOptionsDef1,
                OneOfExtendedArWindowOptionsDef2,
                OneOfExtendedArWindowOptionsDef3,
            ]
        ]
        integrity_type: Optional[
            Union[
                OneOfIntegrityTypeOptionsDef1,
                OneOfIntegrityTypeOptionsDef2,
            ]
        ]
        # Configure a Key
        key: Optional[List[Key]]
        # Configure a Keychain
        keychain: Optional[List[Keychain]]
        pairwise_keying: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        rekey: Optional[
            Union[
                OneOfRekeyOptionsDef1,
                OneOfRekeyOptionsDef2,
                OneOfRekeyOptionsDef3,
            ]
        ]
        replay_window: Optional[
            Union[
                OneOfReplayWindowOptionsDef1,
                OneOfReplayWindowOptionsDef2,
                OneOfReplayWindowOptionsDef3,
            ]
        ]


    class CreateSecurityForSystemPostRequest:
        """
        System profile Security feature schema for request
        """

        data: SystemSecurityData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanSystemSecurityPayload:
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
        # System profile Security feature schema for request
        payload: Optional[Payload]


    class EditSecurityForSystemPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdwanSystemSecurityData:
        extended_ar_window: Optional[
            Union[
                OneOfExtendedArWindowOptionsDef1,
                OneOfExtendedArWindowOptionsDef2,
                OneOfExtendedArWindowOptionsDef3,
            ]
        ]
        integrity_type: Optional[
            Union[
                OneOfIntegrityTypeOptionsDef1,
                OneOfIntegrityTypeOptionsDef2,
            ]
        ]
        # Configure a Key
        key: Optional[List[Key]]
        # Configure a Keychain
        keychain: Optional[List[Keychain]]
        pairwise_keying: Optional[
            Union[
                OneOfOnBooleanDefaultFalseOptionsDef1,
                OneOfOnBooleanDefaultFalseOptionsDef2,
                OneOfOnBooleanDefaultFalseOptionsDef3,
            ]
        ]
        rekey: Optional[
            Union[
                OneOfRekeyOptionsDef1,
                OneOfRekeyOptionsDef2,
                OneOfRekeyOptionsDef3,
            ]
        ]
        replay_window: Optional[
            Union[
                OneOfReplayWindowOptionsDef1,
                OneOfReplayWindowOptionsDef2,
                OneOfReplayWindowOptionsDef3,
            ]
        ]


    class EditSecurityForSystemPutRequest:
        """
        System profile Security feature schema for request
        """

        data: SdwanSystemSecurityData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


