======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class HandleFileGenerationStatusNotificationRequest:
        # Success or Failure reason in detail
        detailed_message: str
        status: str
        # Transaction Id sent in the file generation RPC
        transaction_id: str
        # MD5 checksum value of the file
        checksum: Optional[str]
        # Full path of the generated file
        file_name: Optional[str]


