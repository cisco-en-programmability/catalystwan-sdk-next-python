======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class MigrateTenantModel:
        desc: Optional[str]
        is_destination_overlay_mt: Optional[bool]
        migration_key: Optional[str]
        name: Optional[str]
        org_name: Optional[str]
        sub_domain: Optional[str]
        wan_edge_forecast: Optional[str]


