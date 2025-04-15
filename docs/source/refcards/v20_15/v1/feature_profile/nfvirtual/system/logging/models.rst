======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    SeverityDef = Literal[
        "alert",
        "critical",
        "debug",
        "emergency",
        "error",
        "information",
        "notice",
        "warn",
    ]

    DefaultOptionTypeDef = Literal["default"]

    DefaultSeverityDef = Literal["information"]

    LoggingSeverityDef = Literal[
        "alert",
        "critical",
        "debug",
        "emergency",
        "error",
        "information",
        "notice",
        "warn",
    ]

    LoggingDefaultSeverityDef = Literal["information"]

    SystemLoggingSeverityDef = Literal[
        "alert",
        "critical",
        "debug",
        "emergency",
        "error",
        "information",
        "notice",
        "warn",
    ]

    SystemLoggingDefaultSeverityDef = Literal["information"]


    class CreateNfvirtualLoggingParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OneOfHostIpAddressNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfHostIpAddressNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class HostIpAddress:
        name: Union[
            OneOfHostIpAddressNameOptionsDef1,
            OneOfHostIpAddressNameOptionsDef2,
        ]


    class OneOfSeverityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SeverityDef


    class OneOfSeverityOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSeverityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[DefaultSeverityDef]


    class Data:
        # Enable logging to remote server
        host_ip_address: Optional[List[HostIpAddress]]
        severity: Optional[
            Union[
                OneOfSeverityOptionsDef1,
                OneOfSeverityOptionsDef2,
                OneOfSeverityOptionsDef3,
            ]
        ]


    class CreateNfvirtualLoggingParcelPostRequest:
        """
        Logging profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class LoggingOneOfHostIpAddressNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class LoggingHostIpAddress:
        name: Union[
            LoggingOneOfHostIpAddressNameOptionsDef1,
            OneOfHostIpAddressNameOptionsDef2,
        ]


    class LoggingOneOfSeverityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: LoggingSeverityDef


    class LoggingOneOfSeverityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[LoggingDefaultSeverityDef]


    class LoggingData:
        # Enable logging to remote server
        host_ip_address: Optional[List[LoggingHostIpAddress]]
        severity: Optional[
            Union[
                LoggingOneOfSeverityOptionsDef1,
                OneOfSeverityOptionsDef2,
                LoggingOneOfSeverityOptionsDef3,
            ]
        ]


    class Payload:
        """
        Logging profile parcel schema for PUT request
        """

        data: LoggingData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleNfvirtualSystemLoggingPayload:
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
        payload: Optional[Payload]


    class EditNfvirtualLoggingParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SystemLoggingOneOfHostIpAddressNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemLoggingHostIpAddress:
        name: Union[
            SystemLoggingOneOfHostIpAddressNameOptionsDef1,
            OneOfHostIpAddressNameOptionsDef2,
        ]


    class SystemLoggingOneOfSeverityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: SystemLoggingSeverityDef


    class SystemLoggingOneOfSeverityOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Optional[SystemLoggingDefaultSeverityDef]


    class SystemLoggingData:
        # Enable logging to remote server
        host_ip_address: Optional[List[SystemLoggingHostIpAddress]]
        severity: Optional[
            Union[
                SystemLoggingOneOfSeverityOptionsDef1,
                OneOfSeverityOptionsDef2,
                SystemLoggingOneOfSeverityOptionsDef3,
            ]
        ]


    class EditNfvirtualLoggingParcelPutRequest:
        """
        Logging profile parcel schema for PUT request
        """

        data: SystemLoggingData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


