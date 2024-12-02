======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeviceComplianceCheckListData:
        controller_count: Optional[int]
        type_: Optional[str]
        v_edge_count: Optional[int]


    class DeviceComplianceSummaryResponse:
        check_list: Optional[List[DeviceComplianceCheckListData]]


