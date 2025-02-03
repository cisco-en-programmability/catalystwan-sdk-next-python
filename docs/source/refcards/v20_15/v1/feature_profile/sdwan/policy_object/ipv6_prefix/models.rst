======
Models
======


.. code:: python

    from typing import Any, List, Dict, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class EntriesIpv6AddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class EntriesIpv6PrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class EntriesLeRangePrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class EntriesGeRangePrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries:
        ipv6_address: EntriesIpv6AddressOptionsDef
        ipv6_prefix_length: EntriesIpv6PrefixLengthOptionsDef
        ge_range_prefix_length: Optional[
            EntriesGeRangePrefixLengthOptionsDef
        ]
        le_range_prefix_length: Optional[
            EntriesLeRangePrefixLengthOptionsDef
        ]


    class Data:
        # IPv6 Prefix List
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        Ipv6 prefix profile parcel schema
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for ipv6 prefix profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # Ipv6 prefix profile parcel schema
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


