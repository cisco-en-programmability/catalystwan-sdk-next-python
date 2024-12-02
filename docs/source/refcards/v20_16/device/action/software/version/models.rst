======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class FindSoftwareVersionData:
        version: Optional[str]


    class FindSoftwareVersion:
        data: Optional[List[FindSoftwareVersionData]]


