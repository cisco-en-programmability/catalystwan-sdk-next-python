======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    GlobalOptionTypeDef = Literal["global"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class OneOfEntriesAppOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesAppFamilyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries1:
        app: OneOfEntriesAppOptionsDef
        app_family: Optional[OneOfEntriesAppFamilyOptionsDef]


    class Entries2:
        app_family: OneOfEntriesAppFamilyOptionsDef
        app: Optional[OneOfEntriesAppOptionsDef]


    class Data:
        # Centralized Policy App List
        entries: List[Union[Entries1, Entries2]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        Centralized Policy App List profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for POST request schema for Centralized Policy App List profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # Centralized Policy App List profile parcel schema for POST request
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


