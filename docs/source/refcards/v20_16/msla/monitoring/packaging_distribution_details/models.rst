======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class PackagingDistributionData:
        available_cssm: Optional[int]
        license: Optional[str]
        used_cssm: Optional[str]
        used_vmanage: Optional[int]


    class PackagingDistribution:
        data: Optional[PackagingDistributionData]


