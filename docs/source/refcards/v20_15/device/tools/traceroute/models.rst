======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class Hops:
        error_info: Optional[str]
        hop_name: Optional[str]
        hop_number: Optional[str]
        ip_address: Optional[str]
        mean_latency: Optional[str]


    class TracerouteResponse:
        nexthops: Optional[List[Hops]]
        raw_output: Optional[List[str]]


    class TracerouteRequest:
        device_ip: Optional[str]
        host: Optional[str]
        interface: Optional[str]
        interface_ip: Optional[str]
        size: Optional[str]
        vpn: Optional[str]


