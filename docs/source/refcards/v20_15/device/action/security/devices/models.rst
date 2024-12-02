======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

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


