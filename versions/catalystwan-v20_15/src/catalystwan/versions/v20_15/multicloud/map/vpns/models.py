# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class MapVpnsResponse:
    """
    List of vpns for MultiCloud
    """

    id: Optional[str] = _field(default=None)
    reference_count: Optional[int] = _field(
        default=None, metadata={"alias": "referenceCount"}
    )
    segment_id: Optional[str] = _field(default=None, metadata={"alias": "segmentId"})
    segment_name: Optional[str] = _field(
        default=None, metadata={"alias": "segmentName"}
    )
    solution: Optional[str] = _field(default=None)
