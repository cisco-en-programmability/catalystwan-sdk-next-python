# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class SyncRootCertChain:
    sync_root_cert_chain: Optional[str] = _field(
        default=None, metadata={"alias": "syncRootCertChain"}
    )
