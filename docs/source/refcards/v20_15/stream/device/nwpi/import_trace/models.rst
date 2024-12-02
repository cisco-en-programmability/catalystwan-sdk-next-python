======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class ImportTraceResponse:
        msg: Optional[str]
        state: Optional[bool]


    class ImportTraceRequest:
        file: Optional[str]


