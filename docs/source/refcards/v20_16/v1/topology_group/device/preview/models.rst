======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class GetTopologyGroupDeviceConfigurationPreviewPostResponse:
        """
        topology Group preview Response schema
        """

        existing_config: str
        new_config: str
        unsupported_parcels: Optional[List[Any]]


    class GetTopologyGroupDeviceConfigurationPreviewPostRequest:
        """
        Preview POST request Schema
        """

        # Preview vSmart configuration with Topology Group config removed
        deactivate_topology: Optional[bool]


