======
Models
======


.. code:: python

    from typing import Any, Union, List, Dict, Optional, Literal

    GlobalOptionTypeDef = Literal["global"]

    EntriesMapColorDef = Literal[
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


    class OneOfEntriesMapColorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            EntriesMapColorDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfEntriesMapDscpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Map:
        color: OneOfEntriesMapColorOptionsDef
        dscp: Optional[OneOfEntriesMapDscpOptionsDef]


    class ForwardingClass1:
        option_type: GlobalOptionTypeDef
        value: str


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class ForwardingClass2:
        ref_id: RefId


    class Entries:
        # Forwarding Class Name
        forwarding_class: Union[ForwardingClass1, ForwardingClass2]
        # Map
        map: List[Map]


    class Data:
        # App Probe List
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        app-probe profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for POST request schema for app-probe profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # app-probe profile parcel schema for POST request
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


