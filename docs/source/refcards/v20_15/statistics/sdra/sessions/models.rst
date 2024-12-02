======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class SdraDeviceStatsShort:
        host_name: Optional[str]
        ipsec_anyconnect: Optional[int]
        ipsec_soho: Optional[int]
        ipsec_unknown: Optional[int]
        site_id: Optional[int]
        sslvpn_anyconnect: Optional[int]
        system_ip: Optional[str]


    class SdraSessionCount:
        ipsec_anyconnect: Optional[int]
        ipsec_soho: Optional[int]
        ipsec_unknown: Optional[int]
        sslvpn_anyconnect: Optional[int]


    class SdraSessionSummary:
        top: Optional[List[SdraDeviceStatsShort]]
        total: Optional[SdraSessionCount]


