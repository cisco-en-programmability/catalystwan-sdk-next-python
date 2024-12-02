======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class InterfaceAggResp:
        count: Optional[int]
        entry_time: Optional[str]
        interface: Optional[str]
        rx_kbps: Optional[int]
        tx_kbps: Optional[int]
        vdevice_name: Optional[str]


