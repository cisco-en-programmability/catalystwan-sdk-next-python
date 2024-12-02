# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class GenerateDeviceActionListInner:
    is_cancel_enabled: Optional[bool] = _field(
        default=None, metadata={"alias": "isCancelEnabled"}
    )
    is_parallel_execution_enabled: Optional[bool] = _field(
        default=None, metadata={"alias": "isParallelExecutionEnabled"}
    )
    name: Optional[str] = _field(default=None)
