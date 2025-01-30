======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    GlobalOptionTypeDef = Literal["global"]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
        parcel_id: Optional[str]


    class EntriesVpnOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Union[int, str]


    class Entries:
        vpn: EntriesVpnOptionsDef


    class Data:
        # VPN List
        entries: List[Entries]


    class CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest:
        """
        vpn list profile parcel schema
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for vpn profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # vpn list profile parcel schema
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ]


