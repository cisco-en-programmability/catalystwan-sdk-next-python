======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class ClusterProperties:
        account_id: Optional[str]
        account_name: Optional[str]
        account_type: Optional[str]
        discovery_status: Optional[bool]
        expiration: Optional[str]
        name: Optional[str]


    class PutProperties:
        discovery_status: Optional[bool]


