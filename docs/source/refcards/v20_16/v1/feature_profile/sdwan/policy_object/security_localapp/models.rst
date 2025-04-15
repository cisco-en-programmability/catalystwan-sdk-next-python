======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

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
        # Localapp list
        entries: List[Union[Entries1, Entries2]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        security-localapp profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Payload:
        """
        security-localapp profile parcel schema for POST request
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
        # security-localapp profile parcel schema for POST request
        payload: Optional[Payload]


