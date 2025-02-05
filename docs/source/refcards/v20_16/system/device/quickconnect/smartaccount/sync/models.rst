======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class SyncDevicesResp:
        process_id: Optional[str]


    class SmartAccountModel:
        client_credentials: Optional[bool]
        env: Optional[str]
        organization_name: Optional[str]
        password: Optional[str]
        username: Optional[str]
        validity_string: Optional[str]


