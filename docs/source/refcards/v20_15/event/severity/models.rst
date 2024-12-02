======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    SeverityLevel = Literal["CRITICAL", "MAJOR", "MEDIUM", "MINOR"]


    class EventsBySeverity:
        component: Optional[str]
        details: Optional[str]
        entry_time: Optional[str]
        eventname: Optional[str]
        host_name: Optional[str]
        severity_level: Optional[SeverityLevel]
        system_ip: Optional[str]


