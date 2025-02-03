======
Models
======


.. code:: python

    from typing import Any, Union, List, Dict, Optional, Literal

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class GetTunnelsResponsePrivateIp:
        hostname: Optional[str]
        tunnels: Optional[str]


    class GetTunnelsResponse:
        private_ip: Optional[List[GetTunnelsResponsePrivateIp]]


