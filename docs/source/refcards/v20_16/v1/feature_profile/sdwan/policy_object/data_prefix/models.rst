======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    GlobalOptionTypeDef = Literal["global"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class EntriesIpv4AddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class EntriesIpv4PrefixLengthOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class Entries:
        ipv4_address: EntriesIpv4AddressOptionsDef
        ipv4_prefix_length: EntriesIpv4PrefixLengthOptionsDef


    class Data:
        # IPv4 Data Prefix List
        entries: Optional[List[Entries]]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        ipv4 data prefix profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for POST request schema for ipv4 data prefix profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # ipv4 data prefix profile parcel schema for POST request
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


