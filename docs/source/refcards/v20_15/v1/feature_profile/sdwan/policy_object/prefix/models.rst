======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    GlobalOptionTypeDef = Literal["global"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class EntriesIpv4AddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class EntriesIpv4PrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class EntriesLeRangePrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class EntriesGeRangePrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries:
        ipv4_address: EntriesIpv4AddressOptionsDef
        ipv4_prefix_length: EntriesIpv4PrefixLengthOptionsDef
        ge_range_prefix_length: Optional[
            EntriesGeRangePrefixLengthOptionsDef
        ]
        le_range_prefix_length: Optional[
            EntriesLeRangePrefixLengthOptionsDef
        ]


    class Data:
        # IPv4 Prefix List
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        Ipv4 prefix profile parcel schema
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for POST request schema for ipv4 prefix profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # Ipv4 prefix profile parcel schema
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


