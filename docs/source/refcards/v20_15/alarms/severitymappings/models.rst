======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class SimpleKeyValueMapping:
        key: Optional[str]
        value: Optional[str]


    class AlarmSeverityMapping:
        associated_alarms: Optional[List[SimpleKeyValueMapping]]
        key: Optional[str]
        value: Optional[str]


