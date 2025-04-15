======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]


    class OneOfServerNameOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfServerNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfServerKeyOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfServerKeyOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfServerKeyOptionsDef3:
        option_type: DefaultOptionTypeDef


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


    class OneOfVersionOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVersionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVersionOptionsDef3:
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


    class OneOfPreferOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPreferOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfPreferOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class Server:
        name: Union[
            OneOfServerNameOptionsDef1, OneOfServerNameOptionsDef2
        ]
        prefer: Union[
            OneOfPreferOptionsDef1,
            OneOfPreferOptionsDef2,
            OneOfPreferOptionsDef3,
        ]
        version: Union[
            OneOfVersionOptionsDef1,
            OneOfVersionOptionsDef2,
            OneOfVersionOptionsDef3,
        ]
        vrf: Union[
            OneOfVrfOptionsDef1, OneOfVrfOptionsDef2, OneOfVrfOptionsDef3
        ]
        key: Optional[
            Union[
                OneOfServerKeyOptionsDef1,
                OneOfServerKeyOptionsDef2,
                OneOfServerKeyOptionsDef3,
            ]
        ]
        source_interface: Optional[
            Union[
                OneOfSourceInterfaceOptionsDef1,
                OneOfSourceInterfaceOptionsDef2,
                OneOfSourceInterfaceOptionsDef3,
            ]
        ]


    class OneOfAuthKeyIdOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAuthKeyIdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAuthKeyMd5ValueOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAuthKeyMd5ValueOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class AuthenticationKeys:
        key_id: Union[
            OneOfAuthKeyIdOptionsDef1, OneOfAuthKeyIdOptionsDef2
        ]
        md5_value: Union[
            OneOfAuthKeyMd5ValueOptionsDef1,
            OneOfAuthKeyMd5ValueOptionsDef2,
        ]


    class OneOfTrustedKeyIdOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrustedKeyIdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class OneOfTrustedKeyIdOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Authentication:
        # Set MD5 authentication key
        authentication_keys: List[AuthenticationKeys]
        trusted_keys: Optional[
            Union[
                OneOfTrustedKeyIdOptionsDef1,
                OneOfTrustedKeyIdOptionsDef2,
                OneOfTrustedKeyIdOptionsDef3,
            ]
        ]


    class OneOfLeaderEnableOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLeaderEnableOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfLeaderEnableOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfLeaderStratumOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLeaderStratumOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfLeaderStratumOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfLeaderSourceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLeaderSourceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfLeaderSourceOptionsDef3:
        option_type: DefaultOptionTypeDef


    class Leader:
        enable: Optional[
            Union[
                OneOfLeaderEnableOptionsDef1,
                OneOfLeaderEnableOptionsDef2,
                OneOfLeaderEnableOptionsDef3,
            ]
        ]
        source: Optional[
            Union[
                OneOfLeaderSourceOptionsDef1,
                OneOfLeaderSourceOptionsDef2,
                OneOfLeaderSourceOptionsDef3,
            ]
        ]
        stratum: Optional[
            Union[
                OneOfLeaderStratumOptionsDef1,
                OneOfLeaderStratumOptionsDef2,
                OneOfLeaderStratumOptionsDef3,
            ]
        ]


    class NtpData:
        # Configure NTP servers
        server: List[Server]
        authentication: Optional[Authentication]
        leader: Optional[Leader]


    class Payload:
        """
        SD-Routing NTP feature schema
        """

        data: NtpData
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
        # SD-Routing NTP feature schema
        payload: Optional[Payload]


    class GetListSdRoutingSystemNtpSdRoutingPayload:
        data: Optional[List[Data]]


    class CreateSdroutingNtpFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SystemNtpData:
        # Configure NTP servers
        server: List[Server]
        authentication: Optional[Authentication]
        leader: Optional[Leader]


    class CreateSdroutingNtpFeaturePostRequest:
        """
        SD-Routing NTP feature schema
        """

        data: SystemNtpData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingSystemNtpSdRoutingPayload:
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
        # SD-Routing NTP feature schema
        payload: Optional[Payload]


    class EditSdroutingNtpFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingSystemNtpData:
        # Configure NTP servers
        server: List[Server]
        authentication: Optional[Authentication]
        leader: Optional[Leader]


    class EditSdroutingNtpFeaturePutRequest:
        """
        SD-Routing NTP feature schema
        """

        data: SdRoutingSystemNtpData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


