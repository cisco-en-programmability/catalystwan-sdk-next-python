======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

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


