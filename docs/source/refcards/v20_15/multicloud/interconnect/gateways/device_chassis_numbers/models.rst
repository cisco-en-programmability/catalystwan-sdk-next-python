======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    InterconnectTypeParam = Literal["EQUINIX", "MEGAPORT"]


    class InlineResponse2003:
        configured_hostname: Optional[str]
        configured_system_ip: Optional[str]
        device_model: Optional[str]
        uuid: Optional[str]


