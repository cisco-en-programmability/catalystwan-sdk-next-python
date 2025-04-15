======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]


    class CreateNfvirtualSystemSettingsParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OneOfNameServerNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNameServerNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class NameServer:
        name: Union[
            OneOfNameServerNameOptionsDef1, OneOfNameServerNameOptionsDef2
        ]


    class OneOfDpdkOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfDpdkOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: Optional[bool]


    class Data:
        dpdk: Optional[Union[OneOfDpdkOptionsDef1, OneOfDpdkOptionsDef2]]
        # Name Server
        name_server: Optional[List[NameServer]]


    class CreateNfvirtualSystemSettingsParcelPostRequest:
        """
        SystemSettings profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class SystemSettingsOneOfNameServerNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSettingsNameServer:
        name: Union[
            SystemSettingsOneOfNameServerNameOptionsDef1,
            OneOfNameServerNameOptionsDef2,
        ]


    class SystemSettingsData:
        dpdk: Optional[Union[OneOfDpdkOptionsDef1, OneOfDpdkOptionsDef2]]
        # Name Server
        name_server: Optional[List[SystemSettingsNameServer]]


    class Payload:
        """
        SystemSettings profile parcel schema for PUT request
        """

        data: SystemSettingsData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleNfvirtualSystemSystemSettingsPayload:
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
        # SystemSettings profile parcel schema for PUT request
        payload: Optional[Payload]


    class EditNfvirtualSystemSettingsParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SystemSystemSettingsOneOfNameServerNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemSystemSettingsNameServer:
        name: Union[
            SystemSystemSettingsOneOfNameServerNameOptionsDef1,
            OneOfNameServerNameOptionsDef2,
        ]


    class SystemSystemSettingsData:
        dpdk: Optional[Union[OneOfDpdkOptionsDef1, OneOfDpdkOptionsDef2]]
        # Name Server
        name_server: Optional[List[SystemSystemSettingsNameServer]]


    class EditNfvirtualSystemSettingsParcelPutRequest:
        """
        SystemSettings profile parcel schema for PUT request
        """

        data: SystemSystemSettingsData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


