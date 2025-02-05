======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class TasksStopResponsePayload:
        """
        Auto on task stop schema for POST response
        """

        action: Optional[str]
        entry_time: Optional[int]
        message: Optional[str]
        state: Optional[str]
        task_id: Optional[str]
        task_name: Optional[str]


