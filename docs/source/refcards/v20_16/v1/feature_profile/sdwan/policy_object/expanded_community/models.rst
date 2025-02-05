======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class OneOfExpandedCommunityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfExpandedCommunityOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Data:
        expanded_community_list: Union[
            OneOfExpandedCommunityOptionsDef1,
            OneOfExpandedCommunityOptionsDef2,
        ]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        expanded Community list profile parcel schema
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for expanded community profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # expanded Community list profile parcel schema
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


