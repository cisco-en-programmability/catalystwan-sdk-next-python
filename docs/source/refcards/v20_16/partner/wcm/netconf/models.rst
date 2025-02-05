======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class WcmNetconfConfigRes:
        id: Optional[str]


    class NetconfConfig:
        device_config: Optional[str]
        device_id: Optional[str]


    class NetconfConfigHeader:
        generate_on: Optional[int]


    class WcmNetconfConfigRequest:
        data: Optional[List[NetconfConfig]]
        header: Optional[NetconfConfigHeader]


