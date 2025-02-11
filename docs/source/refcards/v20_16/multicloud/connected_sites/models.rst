======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class ConnectedSitesResponse:
        bfd_sessions: Optional[int]
        bfd_sessions_up: Optional[int]
        device_model: Optional[str]
        device_type: Optional[str]
        host_name: Optional[str]
        last_updated: Optional[int]
        local_system_ip: Optional[str]
        reachability: Optional[str]
        site_id: Optional[str]
        status: Optional[str]
        status_bfd: Optional[str]
        system_ip: Optional[str]
        uuid: Optional[str]
        version: Optional[str]


