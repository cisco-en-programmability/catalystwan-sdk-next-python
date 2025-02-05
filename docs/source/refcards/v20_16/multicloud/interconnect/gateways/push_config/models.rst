======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class ProcessResponse:
        # Procees Id of the task
        id: Optional[str]


    class GatewaysPushconfigBody:
        edge_gateway_name: str
        edge_type: str


