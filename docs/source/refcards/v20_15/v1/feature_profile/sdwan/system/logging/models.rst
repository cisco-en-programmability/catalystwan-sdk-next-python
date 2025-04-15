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

    LoggingTlsVersionDef = Literal["TLSv1.1", "TLSv1.2"]

    LoggingPrioritytDef = Literal[
        "alert",
        "critical",
        "debugging",
        "emergency",
        "error",
        "informational",
        "notice",
        "warn",
    ]

    SystemLoggingPrioritytDef = Literal[
        "alert",
        "critical",
        "debugging",
        "emergency",
        "error",
        "informational",
        "notice",
        "warn",
    ]

    SystemLoggingTlsVersionDef = Literal["TLSv1.1", "TLSv1.2"]

    SdwanSystemLoggingPrioritytDef = Literal[
        "alert",
        "critical",
        "debugging",
        "emergency",
        "error",
        "informational",
        "notice",
        "warn",
    ]

    FeatureProfileSdwanSystemLoggingPrioritytDef = Literal[
        "alert",
        "critical",
        "debugging",
        "emergency",
        "error",
        "informational",
        "notice",
        "warn",
    ]


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
        value: Optional[List[None]]


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


    class OneOfVpnOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVpnOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVpnOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


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
        vpn: Union[
            OneOfVpnOptionsDef1, OneOfVpnOptionsDef2, OneOfVpnOptionsDef3
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
        vpn: Union[
            OneOfVpnOptionsDef1, OneOfVpnOptionsDef2, OneOfVpnOptionsDef3
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
        Logging profile parcel schema for POST request
        """

        data: LoggingData
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
        # Logging profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanSystemLoggingPayload:
        data: Optional[List[Data]]


    class CreateLoggingProfileParcelForSystemPostResponse:
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


    class CreateLoggingProfileParcelForSystemPostRequest:
        """
        Logging profile parcel schema for POST request
        """

        data: SystemLoggingData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class LoggingOneOfDiskFileSizeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class LoggingOneOfDiskFileRotateOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class LoggingFile:
        disk_file_rotate: Union[
            OneOfDiskFileRotateOptionsDef1,
            LoggingOneOfDiskFileRotateOptionsDef2,
            OneOfDiskFileRotateOptionsDef3,
        ]
        disk_file_size: Union[
            OneOfDiskFileSizeOptionsDef1,
            LoggingOneOfDiskFileSizeOptionsDef2,
            OneOfDiskFileSizeOptionsDef3,
        ]


    class LoggingDisk:
        file: LoggingFile
        disk_enable: Optional[
            Union[
                OneOfDiskEnableOptionsDef1,
                OneOfDiskEnableOptionsDef2,
                OneOfDiskEnableOptionsDef3,
            ]
        ]


    class LoggingOneOfProfileOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class LoggingOneOfTlsVersionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LoggingTlsVersionDef


    class LoggingOneOfCipherSuiteListOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[
            CipherSuiteListDef
        ]  # pytype: disable=annotation-type-mismatch


    class LoggingTlsProfile:
        auth_type: OneOfAuthTypeOptionsDef
        profile: Union[
            OneOfProfileOptionsDef1, LoggingOneOfProfileOptionsDef2
        ]
        cipher_suite_list: Optional[
            Union[
                OneOfCipherSuiteListOptionsDef1,
                LoggingOneOfCipherSuiteListOptionsDef2,
                OneOfCipherSuiteListOptionsDef3,
            ]
        ]
        tls_version: Optional[
            Union[
                OneOfTlsVersionOptionsDef1,
                LoggingOneOfTlsVersionOptionsDef2,
                OneOfTlsVersionOptionsDef3,
            ]
        ]


    class LoggingOneOfPriorityOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: LoggingPrioritytDef


    class LoggingServer:
        name: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        priority: Union[
            OneOfPriorityOptionsDef1,
            LoggingOneOfPriorityOptionsDef2,
            OneOfPriorityOptionsDef3,
        ]
        tls_enable: Union[
            OneOfTlsEnableOptionsDef1,
            OneOfTlsEnableOptionsDef2,
            OneOfTlsEnableOptionsDef3,
        ]
        vpn: Union[
            OneOfVpnOptionsDef1, OneOfVpnOptionsDef2, OneOfVpnOptionsDef3
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


    class SystemLoggingOneOfPriorityOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: SystemLoggingPrioritytDef


    class LoggingIpv6Server:
        name: Union[
            OneOfIpv6AddrGlobalVariableOptionsDef1,
            OneOfIpv6AddrGlobalVariableOptionsDef2,
        ]
        priority: Union[
            OneOfPriorityOptionsDef1,
            SystemLoggingOneOfPriorityOptionsDef2,
            OneOfPriorityOptionsDef3,
        ]
        tls_enable: Union[
            OneOfTlsEnableOptionsDef1,
            OneOfTlsEnableOptionsDef2,
            OneOfTlsEnableOptionsDef3,
        ]
        vpn: Union[
            OneOfVpnOptionsDef1, OneOfVpnOptionsDef2, OneOfVpnOptionsDef3
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


    class SdwanSystemLoggingData:
        disk: LoggingDisk
        # Enable logging to remote ipv6 server
        ipv6_server: Optional[List[LoggingIpv6Server]]
        # Enable logging to remote server
        server: Optional[List[LoggingServer]]
        # Configure a TLS profile
        tls_profile: Optional[List[LoggingTlsProfile]]


    class LoggingPayload:
        """
        Logging profile parcel schema for PUT request
        """

        data: SdwanSystemLoggingData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanSystemLoggingPayload:
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
        # Logging profile parcel schema for PUT request
        payload: Optional[LoggingPayload]


    class EditLoggingProfileParcelForSystemPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SystemLoggingOneOfDiskFileSizeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemLoggingOneOfDiskFileRotateOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemLoggingFile:
        disk_file_rotate: Union[
            OneOfDiskFileRotateOptionsDef1,
            SystemLoggingOneOfDiskFileRotateOptionsDef2,
            OneOfDiskFileRotateOptionsDef3,
        ]
        disk_file_size: Union[
            OneOfDiskFileSizeOptionsDef1,
            SystemLoggingOneOfDiskFileSizeOptionsDef2,
            OneOfDiskFileSizeOptionsDef3,
        ]


    class SystemLoggingDisk:
        file: SystemLoggingFile
        disk_enable: Optional[
            Union[
                OneOfDiskEnableOptionsDef1,
                OneOfDiskEnableOptionsDef2,
                OneOfDiskEnableOptionsDef3,
            ]
        ]


    class SystemLoggingOneOfProfileOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemLoggingOneOfTlsVersionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: SystemLoggingTlsVersionDef


    class SystemLoggingOneOfCipherSuiteListOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[
            CipherSuiteListDef
        ]  # pytype: disable=annotation-type-mismatch


    class SystemLoggingTlsProfile:
        auth_type: OneOfAuthTypeOptionsDef
        profile: Union[
            OneOfProfileOptionsDef1, SystemLoggingOneOfProfileOptionsDef2
        ]
        cipher_suite_list: Optional[
            Union[
                OneOfCipherSuiteListOptionsDef1,
                SystemLoggingOneOfCipherSuiteListOptionsDef2,
                OneOfCipherSuiteListOptionsDef3,
            ]
        ]
        tls_version: Optional[
            Union[
                OneOfTlsVersionOptionsDef1,
                SystemLoggingOneOfTlsVersionOptionsDef2,
                OneOfTlsVersionOptionsDef3,
            ]
        ]


    class SdwanSystemLoggingOneOfPriorityOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: SdwanSystemLoggingPrioritytDef


    class SystemLoggingServer:
        name: Union[
            OneOfIpV4AddressOptionsDef1, OneOfIpV4AddressOptionsDef2
        ]
        priority: Union[
            OneOfPriorityOptionsDef1,
            SdwanSystemLoggingOneOfPriorityOptionsDef2,
            OneOfPriorityOptionsDef3,
        ]
        tls_enable: Union[
            OneOfTlsEnableOptionsDef1,
            OneOfTlsEnableOptionsDef2,
            OneOfTlsEnableOptionsDef3,
        ]
        vpn: Union[
            OneOfVpnOptionsDef1, OneOfVpnOptionsDef2, OneOfVpnOptionsDef3
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


    class FeatureProfileSdwanSystemLoggingOneOfPriorityOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanSystemLoggingPrioritytDef


    class SystemLoggingIpv6Server:
        name: Union[
            OneOfIpv6AddrGlobalVariableOptionsDef1,
            OneOfIpv6AddrGlobalVariableOptionsDef2,
        ]
        priority: Union[
            OneOfPriorityOptionsDef1,
            FeatureProfileSdwanSystemLoggingOneOfPriorityOptionsDef2,
            OneOfPriorityOptionsDef3,
        ]
        tls_enable: Union[
            OneOfTlsEnableOptionsDef1,
            OneOfTlsEnableOptionsDef2,
            OneOfTlsEnableOptionsDef3,
        ]
        vpn: Union[
            OneOfVpnOptionsDef1, OneOfVpnOptionsDef2, OneOfVpnOptionsDef3
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


    class FeatureProfileSdwanSystemLoggingData:
        disk: SystemLoggingDisk
        # Enable logging to remote ipv6 server
        ipv6_server: Optional[List[SystemLoggingIpv6Server]]
        # Enable logging to remote server
        server: Optional[List[SystemLoggingServer]]
        # Configure a TLS profile
        tls_profile: Optional[List[SystemLoggingTlsProfile]]


    class EditLoggingProfileParcelForSystemPutRequest:
        """
        Logging profile parcel schema for PUT request
        """

        data: FeatureProfileSdwanSystemLoggingData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


