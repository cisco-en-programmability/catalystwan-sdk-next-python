======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class NvaSkuListResponseScaleValueList:
        instance_count: Optional[int]
        instance_type: Optional[str]
        scale_unit: Optional[str]


    class NvaSkuListResponse:
        account_id: Optional[str]
        account_name: Optional[str]
        cloud_type: Optional[str]
        nva_sku_id: Optional[str]
        nva_sku_name: Optional[str]
        scale_value_list: Optional[List[NvaSkuListResponseScaleValueList]]
        version_list: Optional[List[str]]


