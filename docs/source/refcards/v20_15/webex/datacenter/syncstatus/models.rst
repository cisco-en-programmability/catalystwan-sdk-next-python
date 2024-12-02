======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class SyncStatusResponse:
        last_synced: Optional[str]
        webex_sync_needed: Optional[bool]


