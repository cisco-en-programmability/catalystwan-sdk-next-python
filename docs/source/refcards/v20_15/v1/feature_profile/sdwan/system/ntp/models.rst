======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanFalseDef = Literal[False]


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
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


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
        vpn: Union[
            OneOfVpnOptionsDef1, OneOfVpnOptionsDef2, OneOfVpnOptionsDef3
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
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


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
        NTP profile parcel schema for POST request
        """

        data: NtpData
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
        # NTP profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanSystemNtpPayload:
        data: Optional[List[Data]]


    class CreateNtpProfileParcelForSystemPostResponse:
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


    class CreateNtpProfileParcelForSystemPostRequest:
        """
        NTP profile parcel schema for POST request
        """

        data: SystemNtpData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class NtpOneOfServerNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class NtpOneOfServerKeyOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class NtpOneOfVpnOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class NtpOneOfVersionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class NtpServer:
        name: Union[
            OneOfServerNameOptionsDef1, NtpOneOfServerNameOptionsDef2
        ]
        prefer: Union[
            OneOfPreferOptionsDef1,
            OneOfPreferOptionsDef2,
            OneOfPreferOptionsDef3,
        ]
        version: Union[
            OneOfVersionOptionsDef1,
            NtpOneOfVersionOptionsDef2,
            OneOfVersionOptionsDef3,
        ]
        vpn: Union[
            OneOfVpnOptionsDef1,
            NtpOneOfVpnOptionsDef2,
            OneOfVpnOptionsDef3,
        ]
        key: Optional[
            Union[
                OneOfServerKeyOptionsDef1,
                NtpOneOfServerKeyOptionsDef2,
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


    class NtpOneOfAuthKeyIdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class NtpOneOfAuthKeyMd5ValueOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class NtpAuthenticationKeys:
        key_id: Union[
            OneOfAuthKeyIdOptionsDef1, NtpOneOfAuthKeyIdOptionsDef2
        ]
        md5_value: Union[
            OneOfAuthKeyMd5ValueOptionsDef1,
            NtpOneOfAuthKeyMd5ValueOptionsDef2,
        ]


    class NtpOneOfTrustedKeyIdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class NtpAuthentication:
        # Set MD5 authentication key
        authentication_keys: List[NtpAuthenticationKeys]
        trusted_keys: Optional[
            Union[
                OneOfTrustedKeyIdOptionsDef1,
                NtpOneOfTrustedKeyIdOptionsDef2,
                OneOfTrustedKeyIdOptionsDef3,
            ]
        ]


    class NtpOneOfLeaderStratumOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class NtpLeader:
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
                NtpOneOfLeaderStratumOptionsDef2,
                OneOfLeaderStratumOptionsDef3,
            ]
        ]


    class SdwanSystemNtpData:
        # Configure NTP servers
        server: List[NtpServer]
        authentication: Optional[NtpAuthentication]
        leader: Optional[NtpLeader]


    class NtpPayload:
        """
        NTP profile parcel schema for PUT request
        """

        data: SdwanSystemNtpData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanSystemNtpPayload:
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
        # NTP profile parcel schema for PUT request
        payload: Optional[NtpPayload]


    class EditNtpProfileParcelForSystemPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SystemNtpOneOfServerNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemNtpOneOfServerKeyOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemNtpOneOfVpnOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemNtpOneOfVersionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemNtpServer:
        name: Union[
            OneOfServerNameOptionsDef1,
            SystemNtpOneOfServerNameOptionsDef2,
        ]
        prefer: Union[
            OneOfPreferOptionsDef1,
            OneOfPreferOptionsDef2,
            OneOfPreferOptionsDef3,
        ]
        version: Union[
            OneOfVersionOptionsDef1,
            SystemNtpOneOfVersionOptionsDef2,
            OneOfVersionOptionsDef3,
        ]
        vpn: Union[
            OneOfVpnOptionsDef1,
            SystemNtpOneOfVpnOptionsDef2,
            OneOfVpnOptionsDef3,
        ]
        key: Optional[
            Union[
                OneOfServerKeyOptionsDef1,
                SystemNtpOneOfServerKeyOptionsDef2,
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


    class SystemNtpOneOfAuthKeyIdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemNtpOneOfAuthKeyMd5ValueOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemNtpAuthenticationKeys:
        key_id: Union[
            OneOfAuthKeyIdOptionsDef1, SystemNtpOneOfAuthKeyIdOptionsDef2
        ]
        md5_value: Union[
            OneOfAuthKeyMd5ValueOptionsDef1,
            SystemNtpOneOfAuthKeyMd5ValueOptionsDef2,
        ]


    class SystemNtpOneOfTrustedKeyIdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class SystemNtpAuthentication:
        # Set MD5 authentication key
        authentication_keys: List[SystemNtpAuthenticationKeys]
        trusted_keys: Optional[
            Union[
                OneOfTrustedKeyIdOptionsDef1,
                SystemNtpOneOfTrustedKeyIdOptionsDef2,
                OneOfTrustedKeyIdOptionsDef3,
            ]
        ]


    class SystemNtpOneOfLeaderStratumOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemNtpLeader:
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
                SystemNtpOneOfLeaderStratumOptionsDef2,
                OneOfLeaderStratumOptionsDef3,
            ]
        ]


    class FeatureProfileSdwanSystemNtpData:
        # Configure NTP servers
        server: List[SystemNtpServer]
        authentication: Optional[SystemNtpAuthentication]
        leader: Optional[SystemNtpLeader]


    class EditNtpProfileParcelForSystemPutRequest:
        """
        NTP profile parcel schema for PUT request
        """

        data: FeatureProfileSdwanSystemNtpData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


