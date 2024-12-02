======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class EntriesRemoteDestIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class EntriesSourceIpOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class Entries:
        remote_dest_ip: EntriesRemoteDestIpOptionsDef
        source_ip: EntriesSourceIpOptionsDef


    class Data:
        # Mirror List
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        mirror profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for POST request schema for mirror profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # mirror profile parcel schema for POST request
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


