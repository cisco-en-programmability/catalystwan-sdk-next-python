======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    Solution = Literal["sdwan"]


    class GetSdwanFeatureProfileBySdwanFamilyGetResponse:
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        description: Optional[str]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        profile_id: Optional[str]
        profile_name: Optional[str]
        profile_type: Optional[str]
        solution: Optional[Solution]


