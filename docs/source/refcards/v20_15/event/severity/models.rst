======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    SeverityLevel = Literal["CRITICAL", "MAJOR", "MEDIUM", "MINOR"]


    class EventsBySeverity:
        component: Optional[str]
        details: Optional[str]
        entry_time: Optional[str]
        eventname: Optional[str]
        host_name: Optional[str]
        severity_level: Optional[SeverityLevel]
        system_ip: Optional[str]


