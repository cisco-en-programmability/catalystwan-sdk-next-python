======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class UrlMonitoringInfoInner:
        alarm_raised: Optional[bool]
        # VManage alarm is raised after reaching the threshold.
        threshold: Optional[int]
        # url registered for monitoring requests.
        url: Optional[str]


