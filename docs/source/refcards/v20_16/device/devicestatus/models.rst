======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class StatusObject:
        count: Optional[int]
        message: Optional[str]
        name: Optional[str]
        status: Optional[str]


    class DeviceStatusData:
        count: Optional[int]
        details_url: Optional[str]
        image: Optional[str]
        name: Optional[str]
        status_list: Optional[List[StatusObject]]
        type_: Optional[str]


