======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeviceBlistResponsePayloadInner:
        """
        Device blist response payload
        """

        crash_time: Optional[int]
        crash_version: Optional[str]
        crashed_reason: Optional[str]
        device_blist_state: Optional[str]
        device_model: Optional[str]
        device_name: Optional[str]
        nwpi_state: Optional[str]
        site_id: Optional[int]
        system_ip: Optional[str]
        type_: Optional[int]


