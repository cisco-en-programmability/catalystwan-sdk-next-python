# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional, List
from dataclasses import dataclass, field as _field

CloudTypeParam = Literal["AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"]


@dataclass
class Taskid:
    """
    Task id for polling status
    """

    id: Optional[str] = _field(default=None)


@dataclass
class AuditFixIssuesToSync:
    name: str
    region: str
    report_type: str = _field(metadata={"alias": "reportType"})


@dataclass
class AuditFix:
    cloud_type: str = _field(metadata={"alias": "cloudType"})
    issues_to_sync: Optional[List[AuditFixIssuesToSync]] = _field(
        default=None, metadata={"alias": "issuesToSync"}
    )
    region: Optional[str] = _field(default=None)
