======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class AppRouteTunnelSummary:
        app_probe_class: Optional[str]
        entry_time: Optional[str]
        jitter: Optional[int]
        latency: Optional[int]
        loss_percentage: Optional[int]
        name: Optional[str]
        rx_octets: Optional[int]
        tx_octets: Optional[int]


    class AppRouteTunnenSummarResp:
        data: Optional[List[AppRouteTunnelSummary]]


