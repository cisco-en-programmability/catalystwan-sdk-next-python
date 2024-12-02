======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    Value = Literal[
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

    EntriesPathPreferenceDef = Literal[
        "all-paths", "direct-path", "multi-hop-path"
    ]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class OneOfEntriesColorPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[Value]  # pytype: disable=annotation-type-mismatch


    class OneOfEntriesPathPreferenceOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EntriesPathPreferenceDef  # pytype: disable=annotation-type-mismatch


    class PrimaryPreference1:
        color_preference: OneOfEntriesColorPreferenceOptionsDef
        path_preference: Optional[OneOfEntriesPathPreferenceOptionsDef]


    class PrimaryPreference2:
        path_preference: OneOfEntriesPathPreferenceOptionsDef
        color_preference: Optional[OneOfEntriesColorPreferenceOptionsDef]


    class SecondaryPreference:
        """
        Object with an color and path preference
        """

        color_preference: Optional[OneOfEntriesColorPreferenceOptionsDef]
        path_preference: Optional[OneOfEntriesPathPreferenceOptionsDef]


    class Entries:
        # Object with an color and path preference
        primary_preference: Union[PrimaryPreference1, PrimaryPreference2]
        # Object with an color and path preference
        secondary_preference: Optional[SecondaryPreference]
        # Object with an color and path preference
        tertiary_preference: Optional[SecondaryPreference]


    class Data:
        # Preferred Color Group List
        entries: Optional[List[Entries]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        preferred-color-group profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        # This is the documentation for POST request schema for preferred-color-group profile parcel
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
        # preferred-color-group profile parcel schema for POST request
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


