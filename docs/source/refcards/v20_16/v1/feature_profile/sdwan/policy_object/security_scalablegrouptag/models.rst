======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    GlobalOptionTypeDef = Literal["global"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class OneOfEntriesSgtNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesTagOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries:
        sgt_name: OneOfEntriesSgtNameOptionsDef
        tag: OneOfEntriesTagOptionsDef


    class Data:
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        security-scalablegrouptag profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for POST request schema for security-scalablegrouptag profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # security-scalablegrouptag profile parcel schema for POST request
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


