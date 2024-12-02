======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class Tokens:
        """
        Response from Cisco SecureX token API
        """

        access_token: Optional[str]
        expires_in: Optional[int]
        refresh_token: Optional[str]
        scope: Optional[str]
        token_type: Optional[str]


