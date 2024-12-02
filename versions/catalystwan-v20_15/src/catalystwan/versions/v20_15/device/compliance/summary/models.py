# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class DeviceComplianceCheckListData:
    controller_count: Optional[int] = _field(
        default=None, metadata={"alias": "controllerCount"}
    )
    type_: Optional[str] = _field(default=None, metadata={"alias": "type"})
    v_edge_count: Optional[int] = _field(default=None, metadata={"alias": "vEdgeCount"})


@dataclass
class DeviceComplianceSummaryResponse:
    check_list: Optional[List[DeviceComplianceCheckListData]] = _field(
        default=None, metadata={"alias": "checkList"}
    )
