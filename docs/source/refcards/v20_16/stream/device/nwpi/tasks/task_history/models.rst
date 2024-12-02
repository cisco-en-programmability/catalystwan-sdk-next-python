======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class TaskHistoryResponsePayloadData:
        duration: Optional[str]
        entry_time: Optional[int]
        events: Optional[List[str]]
        expire_time: Optional[int]
        sites: Optional[List[str]]
        state: Optional[str]
        task_id: Optional[int]
        task_name: Optional[str]
        traces: Optional[bool]
        type_: Optional[str]


    class TaskHistoryResponsePayload:
        """
        Auto on task schema for GET response
        """

        data: Optional[List[TaskHistoryResponsePayloadData]]


