======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeployConfigGroupPostResponse:
        """
        Config Group deploy Response schema
        """

        parent_task_id: str


    class DeviceIdDef:
        id: str


    class DeployConfigGroupPostRequest:
        """
        Config Group Deploy Request schema
        """

        # list of device ids that config group need to be deployed
        devices: Optional[List[DeviceIdDef]]


