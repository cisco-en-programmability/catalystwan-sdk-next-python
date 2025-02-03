======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    Solution = Literal["sdwan"]


    class GetSdwanFeatureProfileBySdwanFamilyGetResponse:
        description: Optional[str]
        profile_id: Optional[str]
        profile_name: Optional[str]
        profile_type: Optional[str]
        solution: Optional[Solution]


