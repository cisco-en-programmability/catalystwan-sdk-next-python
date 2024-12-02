======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class PartnerSite:
        partner_id: Optional[str]
        sites: Optional[List[str]]


    class VpnListResHeader:
        generated_on: Optional[int]


    class SdaSitesRes:
        data: Optional[List[PartnerSite]]
        header: Optional[VpnListResHeader]


