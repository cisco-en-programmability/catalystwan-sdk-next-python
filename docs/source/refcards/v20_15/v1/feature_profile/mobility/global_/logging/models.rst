======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    Value = Literal["systemIp"]

    VariableOptionTypeDef = Literal["variable"]

    LoggingValue = Literal["{{logging_server_source_ip}}"]

    PrioritytDef = Literal[
        "alert",
        "critical",
        "emergency",
        "error",
        "information",
        "notice",
        "warn",
    ]

    GlobalLoggingValue = Literal["error"]

    LoggingPrioritytDef = Literal[
        "alert",
        "critical",
        "emergency",
        "error",
        "information",
        "notice",
        "warn",
    ]

    GlobalLoggingPrioritytDef = Literal[
        "alert",
        "critical",
        "emergency",
        "error",
        "information",
        "notice",
        "warn",
    ]


    class OneOfDiskFileSizeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDiskFileSizeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfDiskFileRotateOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDiskFileRotateOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: int


    class File:
        """
        File to which to log messages
        """

        disk_file_rotate: Union[
            OneOfDiskFileRotateOptionsDef1, OneOfDiskFileRotateOptionsDef2
        ]
        disk_file_size: Union[
            OneOfDiskFileSizeOptionsDef1, OneOfDiskFileSizeOptionsDef2
        ]


    class Disk:
        """
        Enable logging to disk
        """

        # File to which to log messages
        file: File


    class OneOfServerNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfsourceIpOptionsDef1:
        option_type: DefaultOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfsourceIpOptionsDef2:
        option_type: VariableOptionTypeDef
        value: LoggingValue  # pytype: disable=annotation-type-mismatch


    class OneOfPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: PrioritytDef


    class OneOfPriorityOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: (
            GlobalLoggingValue  # pytype: disable=annotation-type-mismatch
        )


    class Server:
        name: OneOfServerNameOptionsDef
        priority: Union[
            OneOfPriorityOptionsDef1, OneOfPriorityOptionsDef2
        ]
        source_ip: Union[
            OneOfsourceIpOptionsDef1, OneOfsourceIpOptionsDef2
        ]


    class LoggingData:
        # Enable logging to disk
        disk: Disk
        # Remote host logging parameters
        server: Optional[List[Server]]


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


    class GetListMobilityGlobalLoggingPayload:
        data: Optional[List[Data]]


    class CreateLoggingProfileFeatureForMobilityPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class GlobalLoggingData:
        # Enable logging to disk
        disk: Disk
        # Remote host logging parameters
        server: Optional[List[Server]]


    class CreateLoggingProfileFeatureForMobilityPostRequest:
        """
        Logging profile parcel schema for POST request
        """

        data: GlobalLoggingData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class LoggingOneOfDiskFileSizeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class LoggingOneOfDiskFileRotateOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class LoggingFile:
        """
        File to which to log messages
        """

        disk_file_rotate: Union[
            LoggingOneOfDiskFileRotateOptionsDef1,
            OneOfDiskFileRotateOptionsDef2,
        ]
        disk_file_size: Union[
            LoggingOneOfDiskFileSizeOptionsDef1,
            OneOfDiskFileSizeOptionsDef2,
        ]


    class LoggingDisk:
        """
        Enable logging to disk
        """

        # File to which to log messages
        file: LoggingFile


    class LoggingOneOfServerNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class LoggingOneOfPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: LoggingPrioritytDef


    class LoggingServer:
        name: LoggingOneOfServerNameOptionsDef
        priority: Union[
            LoggingOneOfPriorityOptionsDef1, OneOfPriorityOptionsDef2
        ]
        source_ip: Union[
            OneOfsourceIpOptionsDef1, OneOfsourceIpOptionsDef2
        ]


    class MobilityGlobalLoggingData:
        # Enable logging to disk
        disk: LoggingDisk
        # Remote host logging parameters
        server: Optional[List[LoggingServer]]


    class LoggingPayload:
        """
        Logging profile parcel schema for PUT request
        """

        data: MobilityGlobalLoggingData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleMobilityGlobalLoggingPayload:
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


    class EditLoggingProfileFeatureForMobilityPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class GlobalLoggingOneOfDiskFileSizeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalLoggingOneOfDiskFileRotateOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalLoggingFile:
        """
        File to which to log messages
        """

        disk_file_rotate: Union[
            GlobalLoggingOneOfDiskFileRotateOptionsDef1,
            OneOfDiskFileRotateOptionsDef2,
        ]
        disk_file_size: Union[
            GlobalLoggingOneOfDiskFileSizeOptionsDef1,
            OneOfDiskFileSizeOptionsDef2,
        ]


    class GlobalLoggingDisk:
        """
        Enable logging to disk
        """

        # File to which to log messages
        file: GlobalLoggingFile


    class GlobalLoggingOneOfServerNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalLoggingOneOfPriorityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: GlobalLoggingPrioritytDef


    class GlobalLoggingServer:
        name: GlobalLoggingOneOfServerNameOptionsDef
        priority: Union[
            GlobalLoggingOneOfPriorityOptionsDef1,
            OneOfPriorityOptionsDef2,
        ]
        source_ip: Union[
            OneOfsourceIpOptionsDef1, OneOfsourceIpOptionsDef2
        ]


    class FeatureProfileMobilityGlobalLoggingData:
        # Enable logging to disk
        disk: GlobalLoggingDisk
        # Remote host logging parameters
        server: Optional[List[GlobalLoggingServer]]


    class EditLoggingProfileFeatureForMobilityPutRequest:
        """
        Logging profile parcel schema for PUT request
        """

        data: FeatureProfileMobilityGlobalLoggingData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


