# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class SpeedTestStatusResponse:
    """
    This is valid speedTestStatusResponse
    """

    status: Optional[str] = _field(default=None)


@dataclass
class Uuid:
    """
    This is valid uuid
    """

    uuid: Optional[str] = _field(default=None)
