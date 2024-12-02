# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal
from dataclasses import dataclass, field as _field

ActionParam = Literal["runnow", "start", "stop"]


@dataclass
class UpdateReportTemplateResponse:
    # Report ID
    report_id: str = _field(metadata={"alias": "reportId"})
