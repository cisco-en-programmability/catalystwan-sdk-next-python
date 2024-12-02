======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class Codes:
        """
        Response from Cisco SecureX device_authorization API
        """

        device_code: Optional[str]
        expires_in: Optional[int]
        interval: Optional[int]
        user_code: Optional[str]
        verification_uri: Optional[str]
        verification_uri_complete: Optional[str]


