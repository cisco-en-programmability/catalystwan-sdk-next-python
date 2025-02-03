======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    RequestStatus = Literal["IN_PROGRESS", "NOT_STARTED", "START", "STOP"]

    Status = Literal["failure", "success"]


    class PacketCaptureInfo:
        _rid: Optional[int]
        is_new_session: Optional[bool]
        is_owner: Optional[bool]
        j_session_id: Optional[str]
        renewal_time: Optional[int]
        request_status: Optional[RequestStatus]
        session_id: Optional[str]
        start_time: Optional[int]
        status: Optional[Status]
        status_message: Optional[str]
        type_: Optional[str]
        user: Optional[str]
        user_ip: Optional[str]
        uuid: Optional[str]


