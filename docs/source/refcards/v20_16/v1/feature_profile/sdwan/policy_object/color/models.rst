======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    GlobalOptionTypeDef = Literal["global"]

    EntriesColorDef = Literal[
        "3g",
        "biz-internet",
        "blue",
        "bronze",
        "custom1",
        "custom2",
        "custom3",
        "default",
        "gold",
        "green",
        "lte",
        "metro-ethernet",
        "mpls",
        "private1",
        "private2",
        "private3",
        "private4",
        "private5",
        "private6",
        "public-internet",
        "red",
        "silver",
    ]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class OneOfEntriesColorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EntriesColorDef  # pytype: disable=annotation-type-mismatch


    class Entries:
        color: OneOfEntriesColorOptionsDef


    class Data:
        # Color List
        entries: Optional[List[Entries]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        color profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        # This is the documentation for POST request schema for color profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]
        name: Optional[str]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # color profile parcel schema for POST request
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


