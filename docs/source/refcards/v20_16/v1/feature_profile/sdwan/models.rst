======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    Solution = Literal["sdwan"]


    class GetSdwanFeatureProfileBySdwanFamilyGetResponse:
        description: Optional[str]
        profile_id: Optional[str]
        profile_name: Optional[str]
        profile_type: Optional[str]
        solution: Optional[Solution]


