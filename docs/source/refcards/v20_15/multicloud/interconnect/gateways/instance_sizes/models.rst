======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    InterconnectTypeParam = Literal["EQUINIX", "MEGAPORT"]


    class InlineResponse2004Data:
        # instance size
        size: Optional[str]
        # instance size
        spec: Optional[str]


    class InlineResponse2004:
        data: Optional[List[InlineResponse2004Data]]


