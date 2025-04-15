======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeployPolicyGroupPostResponse:
        """
        Policy Group deploy Response schema
        """

        parent_task_id: str


    class DeviceIdDef:
        id: str


    class DeployPolicyGroupPostRequest:
        """
        Policy Group Deploy Request schema
        """

        # list of device ids that policy group need to be deployed
        devices: Optional[List[DeviceIdDef]]


