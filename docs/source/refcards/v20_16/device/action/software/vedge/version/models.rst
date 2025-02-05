======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class FindVEdgeSoftwareVersionData:
        version: Optional[str]
        version_id: Optional[str]


    class FindVEdgeSoftwareVersion:
        data: Optional[List[FindVEdgeSoftwareVersionData]]


