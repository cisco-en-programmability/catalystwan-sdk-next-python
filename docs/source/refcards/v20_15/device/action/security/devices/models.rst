======
Models
======


.. code:: python

    from typing import List, Dict, Optional, Union, Any, Literal

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


