======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class TasksCreateResponsePayload:
        """
        Auto on task create schema for POST response
        """

        action: Optional[str]
        entry_time: Optional[int]
        expire_time: Optional[int]
        sites: Optional[List[str]]
        state: Optional[str]
        task_id: Optional[int]
        task_name: Optional[str]


