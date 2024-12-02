======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class FecAndPktDupResponseHeader:
        columns: Optional[List[str]]
        fields: Optional[List[str]]
        generated_on: Optional[int]


    class FecAndPktDupResponse:
        data: Optional[List[str]]
        header: Optional[FecAndPktDupResponseHeader]


