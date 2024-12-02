# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class SyncStatusResponse:
    last_synced: Optional[str] = _field(default=None, metadata={"alias": "Last Synced"})
    webex_sync_needed: Optional[bool] = _field(
        default=None, metadata={"alias": "webexSyncNeeded"}
    )
