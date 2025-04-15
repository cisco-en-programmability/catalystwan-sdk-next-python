======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class OneOfIpv4PrefixOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIpv4PrefixOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Entries:
        ip_prefix: Union[
            OneOfIpv4PrefixOptionsDef1, OneOfIpv4PrefixOptionsDef2
        ]


    class Data:
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        security-data-ip-prefix profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Payload:
        """
        security-data-ip-prefix profile parcel schema for POST request
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
        # security-data-ip-prefix profile parcel schema for POST request
        payload: Optional[Payload]


