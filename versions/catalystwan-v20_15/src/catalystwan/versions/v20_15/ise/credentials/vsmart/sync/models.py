# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class VsmartSyncResponse:
    """
    Response for a vsmart sync with the task id for the push from vManage to vSmarts
    """

    id: Optional[str] = _field(default=None)
