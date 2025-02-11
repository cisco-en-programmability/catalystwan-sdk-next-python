======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class MapStatusMapped:
        cloud_type: Optional[str]
        dest_id: Optional[str]
        dest_region: Optional[str]
        dest_type: Optional[str]
        source_region: Optional[str]
        source_tag: Optional[str]
        src_id: Optional[str]
        src_type: Optional[str]
        tunnel_id: Optional[str]


    class MapStatus:
        dest_id: Optional[str]
        dest_type: Optional[str]
        mapped: Optional[List[MapStatusMapped]]
        outstanding_mapping: Optional[str]
        src_id: Optional[str]
        src_type: Optional[str]
        unmapped: Optional[str]


