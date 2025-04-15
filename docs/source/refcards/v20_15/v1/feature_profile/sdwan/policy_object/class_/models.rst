======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    EntriesQueueDef = Literal["0", "1", "2", "3", "4", "5", "6", "7"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class EntriesQueueOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EntriesQueueDef  # pytype: disable=annotation-type-mismatch


    class Entries:
        queue: EntriesQueueOptionsDef


    class Data:
        # class map List
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        class profile parcel schema
        """

        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Payload:
        """
        class profile parcel schema
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
        # class profile parcel schema
        payload: Optional[Payload]


