======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class InitiateFileGenerationRequest:
        # UUID of the device
        device_uuid: str
        requested_file_format: str
        stats_command: str


