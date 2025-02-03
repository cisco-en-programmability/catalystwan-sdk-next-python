======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    GlobalOptionTypeDef = Literal["global"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class StandardCommunityOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries:
        standard_community: StandardCommunityOptionsDef


    class Data:
        # Standard Community List
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        standard Community list profile parcel schema
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for standard community profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # standard Community list profile parcel schema
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


