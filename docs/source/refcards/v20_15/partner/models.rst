======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    Type = Literal["aci", "dnac", "mdp", "wcm"]


    class PartnerRes:
        description: Optional[str]
        devices_attached: Optional[int]
        id: Optional[str]
        name: Optional[str]
        owner: Optional[str]
        partner_id: Optional[str]
        registration_date: Optional[int]
        type_: Optional[Type]


    class RegisterPartnerRes:
        id: Optional[str]


    class RegisterPartnerRequest:
        description: Optional[str]
        name: Optional[str]
        partner_id: Optional[str]


    class UpdatePartnerRequest:
        description: Optional[str]
        name: Optional[str]


    class StatusResponse:
        status: Optional[str]


