======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class LicenseDistributionResult:
        display_name: Optional[str]
        last_updated: Optional[str]
        tag: Optional[str]
        total_devices: Optional[int]
        total_license: Optional[int]


    class LicenseDistribution:
        result: Optional[LicenseDistributionResult]


