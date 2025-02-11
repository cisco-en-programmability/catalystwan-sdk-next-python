======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class UmtsSession:
        download_status: Optional[str]
        payload: Optional[str]
        renewal_time: Optional[int]
        request_status: Optional[str]
        session_id: Optional[str]
        start_time: Optional[int]
        status: Optional[str]
        status_message: Optional[str]
        type_: Optional[str]
        user: Optional[str]
        user_ip: Optional[str]
        uuid: Optional[str]


    class UmtsInput:
        device_uuid: Optional[str]
        local_color: Optional[str]
        remote_color: Optional[str]
        remote_system: Optional[str]


