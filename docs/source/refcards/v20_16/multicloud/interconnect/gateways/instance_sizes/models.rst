======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    InterconnectTypeParam = Literal["EQUINIX", "MEGAPORT"]


    class InlineResponse2004Data:
        # instance size
        size: Optional[str]
        # instance size
        spec: Optional[str]


    class InlineResponse2004:
        data: Optional[List[InlineResponse2004Data]]


