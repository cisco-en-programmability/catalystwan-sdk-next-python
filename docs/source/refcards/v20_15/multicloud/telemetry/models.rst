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


    class TelemetryRequests:
        cloud_type: str
        cgw_list: Optional[List[str]]


