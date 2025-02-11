======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class AsPathListNum:
        """
        As path List Number
        """

        option_type: Optional[GlobalOptionTypeDef]
        value: Optional[int]


    class EntriesAsPathOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries:
        as_path: EntriesAsPathOptionsDef


    class Data:
        # As path List Number
        as_path_list_num: AsPathListNum
        # AS Path List
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        as path profile parcel schema
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for POST request schema for AS Path profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # as path profile parcel schema
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


