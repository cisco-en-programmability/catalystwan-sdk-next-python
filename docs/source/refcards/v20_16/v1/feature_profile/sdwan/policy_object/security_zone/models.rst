======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class Data:
        entries: List[None]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        security-zone profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Payload:
        """
        security-zone profile parcel schema for POST request
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
        # security-zone profile parcel schema for POST request
        payload: Optional[Payload]


