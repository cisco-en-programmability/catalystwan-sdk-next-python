======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class GetMapResponse:
        conn: Optional[str]
        dest_id: Optional[str]
        dest_type: Optional[str]
        src_id: Optional[str]
        src_type: Optional[str]


    class Taskid:
        """
        Task id for polling status
        """

        id: Optional[str]


    class PostMapRequestMapped:
        cgw_attachment: Optional[str]
        cloud_type: Optional[str]
        dest_id: Optional[str]
        dest_region: Optional[str]
        dest_tag: Optional[str]
        dest_type: Optional[str]
        region: Optional[str]
        source_region: Optional[str]
        source_tag: Optional[str]
        src_id: Optional[str]
        src_type: Optional[str]
        tunnel_id: Optional[str]


    class PostMapRequestConnMatrix:
        conn: str
        dest_id: str
        dest_type: str
        src_id: str
        src_type: str
        mapped: Optional[List[PostMapRequestMapped]]
        outstanding_mapping: Optional[List[PostMapRequestMapped]]
        unmapped: Optional[List[PostMapRequestMapped]]


    class PostMapRequest:
        cloud_type: str
        conn_matrix: Optional[List[PostMapRequestConnMatrix]]


