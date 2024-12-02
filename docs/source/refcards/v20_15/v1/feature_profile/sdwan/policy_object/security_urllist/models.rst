======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    Type = Literal["urlallowed", "urlblocked"]

    GlobalOptionTypeDef = Literal["global"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class EntriesUrlListOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries:
        pattern: EntriesUrlListOptionsDef


    class Data:
        # URL List
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        URL List profile parcel schema for POST request
        """

        data: Data
        name: str
        type_: Type
        description: Optional[str]
        # This is the documentation for POST request schema for URL List profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # URL List profile parcel schema for POST request
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


