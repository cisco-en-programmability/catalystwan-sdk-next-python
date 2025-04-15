======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class OneOfEntriesGeneratorIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEntriesSignatureIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Entries:
        generator_id: OneOfEntriesGeneratorIdOptionsDef
        signature_id: OneOfEntriesSignatureIdOptionsDef


    class Data:
        # Ips Signature
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        security-ipssignature profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Payload:
        """
        security-ipssignature profile parcel schema for POST request
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
        # security-ipssignature profile parcel schema for POST request
        payload: Optional[Payload]


