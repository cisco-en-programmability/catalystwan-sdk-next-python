======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    GlobalOptionTypeDef = Literal["global"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class OneOfEntriesUserOptionsDef:
        option_type: GlobalOptionTypeDef
        # Mustn't contain non standard unicode characters
        value: str


    class OneOfEntriesUserGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        # Mustn't contain non standard unicode characters
        value: str


    class Entries1:
        user: OneOfEntriesUserOptionsDef
        user_group: Optional[OneOfEntriesUserGroupOptionsDef]


    class Entries2:
        user_group: OneOfEntriesUserGroupOptionsDef
        user: Optional[OneOfEntriesUserOptionsDef]


    class Data:
        # Array of Users and User Groups
        entries: List[Union[Entries1, Entries2]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        security-identity profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for POST request schema for security-identity profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # security-identity profile parcel schema for POST request
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


