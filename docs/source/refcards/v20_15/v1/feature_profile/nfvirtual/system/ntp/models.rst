======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]


    class CreateNfvirtualNtpParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OneOfPreferredServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfPreferredServerOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfBackupServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfBackupServerOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Data:
        preferred_server: Union[
            OneOfPreferredServerOptionsDef1,
            OneOfPreferredServerOptionsDef2,
        ]
        backup_server: Optional[
            Union[
                OneOfBackupServerOptionsDef1, OneOfBackupServerOptionsDef2
            ]
        ]


    class CreateNfvirtualNtpParcelPostRequest:
        """
        Ntp profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class NtpOneOfPreferredServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class NtpOneOfBackupServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class NtpData:
        preferred_server: Union[
            NtpOneOfPreferredServerOptionsDef1,
            OneOfPreferredServerOptionsDef2,
        ]
        backup_server: Optional[
            Union[
                NtpOneOfBackupServerOptionsDef1,
                OneOfBackupServerOptionsDef2,
            ]
        ]


    class Payload:
        """
        Ntp profile parcel schema for PUT request
        """

        data: NtpData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleNfvirtualSystemNtpPayload:
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
        # Ntp profile parcel schema for PUT request
        payload: Optional[Payload]


    class EditNfvirtualNtpParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SystemNtpOneOfPreferredServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class SystemNtpOneOfBackupServerOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class SystemNtpData:
        preferred_server: Union[
            SystemNtpOneOfPreferredServerOptionsDef1,
            OneOfPreferredServerOptionsDef2,
        ]
        backup_server: Optional[
            Union[
                SystemNtpOneOfBackupServerOptionsDef1,
                OneOfBackupServerOptionsDef2,
            ]
        ]


    class EditNfvirtualNtpParcelPutRequest:
        """
        Ntp profile parcel schema for PUT request
        """

        data: SystemNtpData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


