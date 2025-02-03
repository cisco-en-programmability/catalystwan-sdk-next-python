======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    Operation = Literal[
        "ControlPlane",
        "DataPlane",
        "RouterConfiguration",
        "SoftwareImageUpdate",
        "vBondAuth",
    ]

    Status = Literal["Error", "NA", "Success", "Unknown"]


    class BringupInfo:
        message: Optional[List[str]]
        name: Optional[str]
        operation: Optional[Operation]
        status: Optional[Status]
        timestamp: Optional[int]


    class GetDeviceConfiguration:
        data: Optional[List[BringupInfo]]


