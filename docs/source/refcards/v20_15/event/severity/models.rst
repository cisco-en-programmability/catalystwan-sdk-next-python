======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    SeverityLevel = Literal["CRITICAL", "MAJOR", "MEDIUM", "MINOR"]


    class EventsBySeverity:
        component: Optional[str]
        details: Optional[str]
        entry_time: Optional[str]
        eventname: Optional[str]
        host_name: Optional[str]
        severity_level: Optional[SeverityLevel]
        system_ip: Optional[str]


