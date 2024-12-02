# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class GenerateBootstrapConfigForVedgesResponse:
    id: Optional[str] = _field(default=None)


@dataclass
class VEdgeBootstrapConfig:
    bootstrap_config_type: Optional[str] = _field(
        default=None, metadata={"alias": "bootstrapConfigType"}
    )
    uuid: Optional[List[str]] = _field(default=None)
