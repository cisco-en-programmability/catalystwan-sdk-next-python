======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

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

    EntriesEncapDef = Literal["gre", "ipsec"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class OneOfEntriesTlocOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesColorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EntriesColorDef  # pytype: disable=annotation-type-mismatch


    class OneOfEntriesEncapOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EntriesEncapDef  # pytype: disable=annotation-type-mismatch


    class OneOfEntriesPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries:
        color: OneOfEntriesColorOptionsDef
        encap: OneOfEntriesEncapOptionsDef
        tloc: OneOfEntriesTlocOptionsDef
        preference: Optional[OneOfEntriesPreferenceOptionsDef]


    class Data:
        # TLOC List
        entries: Optional[List[Entries]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        tloc profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Payload:
        """
        tloc profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # tloc profile parcel schema for POST request
        payload: Optional[Payload]


