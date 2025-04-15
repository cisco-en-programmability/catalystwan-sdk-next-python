======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeployTopologyGroupPostResponse:
        """
        Topology Group deploy Response schema
        """

        parent_task_id: str


    class DeployTopologyGroupPostRequest:
        """
        Topology Group Deploy Request schema
        """

        deactivate_topology: Optional[bool]


