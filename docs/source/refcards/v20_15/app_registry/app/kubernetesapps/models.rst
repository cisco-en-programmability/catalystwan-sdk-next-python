======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DiscoveredServices:
        cluster_name: Optional[str]
        ip: Optional[List[str]]
        name: Optional[str]
        namespace: Optional[str]
        port: Optional[List[str]]
        protocol: Optional[str]
        server_name: Optional[List[str]]


