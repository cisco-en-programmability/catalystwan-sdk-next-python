======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class Taskid:
        """
        Task id for polling status
        """

        id: Optional[str]


    class PushCgwConfig:
        cloud_gateway_name: str
        cloud_type: str


