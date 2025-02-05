======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class IseServer:
        ise_server_ip: str
        password: str
        sgt: str
        user_and_user_group: str
        user_name: str
        vpn: str
        active_directory_domain: Optional[str]
        ise_cert_name: Optional[str]
        ise_root_cert: Optional[str]
        join_point: Optional[str]
        px_grid_cert_name: Optional[str]
        px_grid_root_cert: Optional[str]


