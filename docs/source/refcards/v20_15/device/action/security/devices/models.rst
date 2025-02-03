======
Models
======


.. code:: python

    from typing import Any, Union, List, Dict, Optional, Literal

    PolicyTypeParam = Literal[
        "advancedMalwareProtection",
        "dnsSecurity",
        "intrusionPrevention",
        "sslDecryption",
        "urlFiltering",
        "zoneBasedFW",
    ]


    class GroupId:
        """
        This is the valid GroupId
        """

        group_id: Optional[str]


