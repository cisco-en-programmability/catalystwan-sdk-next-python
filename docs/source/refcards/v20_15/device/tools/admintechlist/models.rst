======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class AdminTechListRes:
        creation_time: Optional[int]
        file_name: Optional[str]
        request_token_id: Optional[str]
        size: Optional[int]
        state: Optional[str]


    class AdminTechListReq:
        device_ip: Optional[str]


