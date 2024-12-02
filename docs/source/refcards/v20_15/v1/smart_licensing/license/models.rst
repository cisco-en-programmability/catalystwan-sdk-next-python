======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class LicenseInfo:
        available: Optional[str]
        billing_model: Optional[str]
        billing_type: Optional[str]
        display_name: Optional[str]
        in_use: Optional[str]
        purchased: Optional[int]
        quantity: Optional[str]
        tag: Optional[str]


    class GetLicenseResponseInner:
        billing_model: Optional[str]
        billing_type: Optional[str]
        licenses: Optional[List[LicenseInfo]]
        subscription_id: Optional[str]


