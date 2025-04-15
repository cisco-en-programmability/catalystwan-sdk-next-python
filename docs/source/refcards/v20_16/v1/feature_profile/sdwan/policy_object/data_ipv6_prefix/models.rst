======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class EntriesIpv6AddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class EntriesIpv6PrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries:
        ipv6_address: EntriesIpv6AddressOptionsDef
        ipv6_prefix_length: EntriesIpv6PrefixLengthOptionsDef


    class Data:
        # IPv6 Prefix List
        entries: Optional[List[Entries]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        Ipv6 data prefix profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Payload:
        """
        Ipv6 data prefix profile parcel schema for POST request
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
        # Ipv6 data prefix profile parcel schema for POST request
        payload: Optional[Payload]


