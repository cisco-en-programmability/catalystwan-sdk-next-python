======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    GlobalOptionTypeDef = Literal["global"]

    EntriesExceedDef = Literal["drop", "remark"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class EntriesBurstOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class EntriesExceedOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            EntriesExceedDef  # pytype: disable=annotation-type-mismatch
        )


    class EntriesRateOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries:
        burst: EntriesBurstOptionsDef
        exceed: EntriesExceedOptionsDef
        rate: EntriesRateOptionsDef


    class Data:
        # Policer Entries
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        policer profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for POST request schema for policer profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # policer profile parcel schema for POST request
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


