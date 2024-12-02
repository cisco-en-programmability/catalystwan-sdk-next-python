======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class UserSettingsResponse:
        is_present_credentials: Optional[bool]
        # Smart Licensing mode can be 'online', 'offline' or 'onPrem'
        mode: Optional[str]
        multiple_entitlement: Optional[bool]
        # Smart Licensing user name
        uname: Optional[str]


