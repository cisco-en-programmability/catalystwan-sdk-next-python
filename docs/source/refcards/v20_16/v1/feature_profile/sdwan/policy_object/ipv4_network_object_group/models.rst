======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class OneOfDescriptionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDescriptionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDescriptionOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfEntriesAddressTypeHostOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfEntriesHostOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class Entries1:
        address_type: OneOfEntriesAddressTypeHostOptionsDef
        host: Union[
            OneOfEntriesHostOptionsDef1, OneOfDescriptionOptionsDef2
        ]


    class OneOfEntriesAddressTypeIpPrefixOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfEntriesIpPrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries2:
        address_type: OneOfEntriesAddressTypeIpPrefixOptionsDef
        ip_prefix: Union[
            OneOfEntriesIpPrefixOptionsDef1, OneOfDescriptionOptionsDef2
        ]


    class OneOfEntriesAddressTypeObjectGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class RefId:
        option_type: GlobalOptionTypeDef
        value: str


    class ParcelReferenceDef:
        ref_id: RefId


    class Entries3:
        address_type: OneOfEntriesAddressTypeObjectGroupOptionsDef
        object_group: ParcelReferenceDef


    class OneOfEntriesAddressTypeHostRangeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class HostRange:
        """
        Host Address Range
        """

        end: Union[
            OneOfEntriesHostOptionsDef1, OneOfDescriptionOptionsDef2
        ]
        start: Union[
            OneOfEntriesHostOptionsDef1, OneOfDescriptionOptionsDef2
        ]


    class Entries4:
        address_type: OneOfEntriesAddressTypeHostRangeOptionsDef
        # Host Address Range
        host_range: HostRange


    class Data:
        # object-group Entries
        entries: List[Union[Entries1, Entries2, Entries3, Entries4]]
        description: Optional[
            Union[
                OneOfDescriptionOptionsDef1,
                OneOfDescriptionOptionsDef2,
                OneOfDescriptionOptionsDef3,
            ]
        ]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        Ipv4 Network Object Group profile parcel schema
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for POST/PUT request schema for Ipv4 Network Object Group profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # Ipv4 Network Object Group profile parcel schema
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


