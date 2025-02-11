======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class PxGridInfo:
        """
        pxgrid information for making pxgrid api calls
        """

        px_grid_password: str
        px_grid_server_ip: str
        px_grid_user_name: str
        status: str
        access_secret: Optional[str]
        description: Optional[str]
        device_type: Optional[str]
        node_name: Optional[str]
        px_grid_host_name: Optional[str]
        rest_base_url: Optional[str]


