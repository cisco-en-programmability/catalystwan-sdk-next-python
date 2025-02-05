======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class TasksDeleteResponsePayloadMessage:
        duration: Optional[str]
        entry_time: Optional[int]
        events: Optional[str]
        expire_time: Optional[int]
        message: Optional[str]
        sites: Optional[str]
        state: Optional[str]
        task_id: Optional[int]
        task_name: Optional[str]
        traces: Optional[bool]


    class TasksDeleteResponsePayload:
        """
        Auto on task schema for DELETE response
        """

        action: Optional[str]
        message: Optional[TasksDeleteResponsePayloadMessage]
        task_id: Optional[str]


