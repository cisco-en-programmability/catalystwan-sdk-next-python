======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    TlsVersionDef = Literal["TLSv1.1", "TLSv1.2"]

    Value = Literal["TLSv1.1"]

    LoggingValue = Literal["Server"]

    CipherSuiteListDef = Literal[
        "aes-128-cbc-sha",
        "aes-256-cbc-sha",
        "dhe-aes-cbc-sha2",
        "dhe-aes-gcm-sha2",
        "ecdhe-ecdsa-aes-gcm-sha2",
        "ecdhe-rsa-aes-cbc-sha2",
        "ecdhe-rsa-aes-gcm-sha2",
        "rsa-aes-cbc-sha2",
        "rsa-aes-gcm-sha2",
    ]

    PrioritytDef = Literal[
        "alert",
        "critical",
        "debugging",
        "emergency",
        "error",
        "informational",
        "notice",
        "warn",
    ]

    SystemLoggingValue = Literal["informational"]


    class OneOfDiskEnableOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDiskEnableOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfDiskEnableOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfDiskFileSizeOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDiskFileSizeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDiskFileSizeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfDiskFileRotateOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDiskFileRotateOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDiskFileRotateOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class File:
        disk_file_rotate: Union[
            OneOfDiskFileRotateOptionsDef1,
            OneOfDiskFileRotateOptionsDef2,
            OneOfDiskFileRotateOptionsDef3,
        ]
        disk_file_size: Union[
            OneOfDiskFileSizeOptionsDef1,
            OneOfDiskFileSizeOptionsDef2,
            OneOfDiskFileSizeOptionsDef3,
        ]


    class Disk:
        file: File
        disk_enable: Optional[
            Union[
                OneOfDiskEnableOptionsDef1,
                OneOfDiskEnableOptionsDef2,
                OneOfDiskEnableOptionsDef3,
            ]
        ]


    class OneOfProfileOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfProfileOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTlsVersionOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTlsVersionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: TlsVersionDef


    class OneOfTlsVersionOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfAuthTypeOptionsDef:
        option_type: DefaultOptionTypeDef
        value: LoggingValue  # pytype: disable=annotation-type-mismatch


    class OneOfCipherSuiteListOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfCipherSuiteListOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[
            CipherSuiteListDef
        ]  # pytype: disable=annotation-type-mismatch


    class OneOfCipherSuiteListOptionsDef3:
        option_type: DefaultOptionTypeDef


    class TlsProfile:
        auth_type: OneOfAuthTypeOptionsDef
        profile: Union[OneOfProfileOptionsDef1, OneOfProfileOptionsDef2]
        cipher_suite_list: Optional[
            Union[
                OneOfCipherSuiteListOptionsDef1,
                OneOfCipherSuiteListOptionsDef2,
                OneOfCipherSuiteListOptionsDef3,
            ]
        ]
        tls_version: Optional[
            Union[
                OneOfTlsVersionOptionsDef1,
                OneOfTlsVersionOptionsDef2,
                OneOfTlsVersionOptionsDef3,
            ]
        ]


    class OneOfIpV4AddressOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIpV4AddressOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfVrfOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVrfOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVrfOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfSourceInterfaceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSourceInterfaceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSourceInterfaceOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfPriorityOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPriorityOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: PrioritytDef


    class OneOfPriorityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: (
            SystemLoggingValue  # pytype: disable=annotation-type-mismatch
        )


    class OneOfTlsEnableOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTlsEnableOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfTlsEnableOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfTlsPropCustomProfileOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTlsPropCustomProfileOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfTlsPropCustomProfileOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfTlsPropProfileOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTlsPropProfileOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfTlsPropProfileOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Server:
        name: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        priority: Union[
            OneOfPriorityOptionsDef1,
            OneOfPriorityOptionsDef2,
            OneOfPriorityOptionsDef3,
        ]
        tls_enable: Union[
            OneOfTlsEnableOptionsDef1,
            OneOfTlsEnableOptionsDef2,
            OneOfTlsEnableOptionsDef3,
        ]
        vrf: Union[
            OneOfVrfOptionsDef1, OneOfVrfOptionsDef2, OneOfVrfOptionsDef3
        ]
        source_interface: Optional[
            Union[
                OneOfSourceInterfaceOptionsDef1,
                OneOfSourceInterfaceOptionsDef2,
                OneOfSourceInterfaceOptionsDef3,
            ]
        ]
        tls_properties_custom_profile: Optional[
            Union[
                OneOfTlsPropCustomProfileOptionsDef1,
                OneOfTlsPropCustomProfileOptionsDef2,
                OneOfTlsPropCustomProfileOptionsDef3,
            ]
        ]
        tls_properties_profile: Optional[
            Union[
                OneOfTlsPropProfileOptionsDef1,
                OneOfTlsPropProfileOptionsDef2,
                OneOfTlsPropProfileOptionsDef3,
            ]
        ]


    class OneOfIpv6AddrGlobalVariableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv6AddrGlobalVariableOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Ipv6Server:
        name: Union[
            OneOfIpv6AddrGlobalVariableOptionsDef1,
            OneOfIpv6AddrGlobalVariableOptionsDef2,
        ]
        priority: Union[
            OneOfPriorityOptionsDef1,
            OneOfPriorityOptionsDef2,
            OneOfPriorityOptionsDef3,
        ]
        tls_enable: Union[
            OneOfTlsEnableOptionsDef1,
            OneOfTlsEnableOptionsDef2,
            OneOfTlsEnableOptionsDef3,
        ]
        vrf: Union[
            OneOfVrfOptionsDef1, OneOfVrfOptionsDef2, OneOfVrfOptionsDef3
        ]
        source_interface: Optional[
            Union[
                OneOfSourceInterfaceOptionsDef1,
                OneOfSourceInterfaceOptionsDef2,
                OneOfSourceInterfaceOptionsDef3,
            ]
        ]
        tls_properties_custom_profile: Optional[
            Union[
                OneOfTlsPropCustomProfileOptionsDef1,
                OneOfTlsPropCustomProfileOptionsDef2,
                OneOfTlsPropCustomProfileOptionsDef3,
            ]
        ]
        tls_properties_profile: Optional[
            Union[
                OneOfTlsPropProfileOptionsDef1,
                OneOfTlsPropProfileOptionsDef2,
                OneOfTlsPropProfileOptionsDef3,
            ]
        ]


    class LoggingData:
        disk: Disk
        # Enable logging to remote ipv6 server
        ipv6_server: Optional[List[Ipv6Server]]
        # Enable logging to remote server
        server: Optional[List[Server]]
        # Configure a TLS profile
        tls_profile: Optional[List[TlsProfile]]


    class Payload:
        """
        SD-Routing logging feature schema
        """

        data: LoggingData
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
        # SD-Routing logging feature schema
        payload: Optional[Payload]


    class GetListSdRoutingSystemLoggingSdRoutingPayload:
        data: Optional[List[Data]]


    class CreateSdroutingLoggingFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SystemLoggingData:
        disk: Disk
        # Enable logging to remote ipv6 server
        ipv6_server: Optional[List[Ipv6Server]]
        # Enable logging to remote server
        server: Optional[List[Server]]
        # Configure a TLS profile
        tls_profile: Optional[List[TlsProfile]]


    class CreateSdroutingLoggingFeaturePostRequest:
        """
        SD-Routing logging feature schema
        """

        data: SystemLoggingData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingSystemLoggingSdRoutingPayload:
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
        # SD-Routing logging feature schema
        payload: Optional[Payload]


    class EditSdroutingLoggingFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingSystemLoggingData:
        disk: Disk
        # Enable logging to remote ipv6 server
        ipv6_server: Optional[List[Ipv6Server]]
        # Enable logging to remote server
        server: Optional[List[Server]]
        # Configure a TLS profile
        tls_profile: Optional[List[TlsProfile]]


    class EditSdroutingLoggingFeaturePutRequest:
        """
        SD-Routing logging feature schema
        """

        data: SdRoutingSystemLoggingData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


