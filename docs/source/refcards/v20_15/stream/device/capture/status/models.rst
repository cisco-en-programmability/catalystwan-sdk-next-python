======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    FileDownloadStatus = Literal[
        "COMPLETED", "ERROR", "IN_PROGRESS", "NOT_STARTED", "STARTED"
    ]

    SessionStatus = Literal["IN_PROGRESS", "NOT_STARTED", "START", "STOP"]


    class GetFileDownloadStatusRes:
        file_download_status: Optional[FileDownloadStatus]
        session_status: Optional[SessionStatus]


