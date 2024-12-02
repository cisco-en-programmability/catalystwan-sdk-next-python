# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class ProcessGetFirmwareRemoteImageReq:
    description: Optional[str] = _field(default=None)
    file_path: Optional[str] = _field(default=None, metadata={"alias": "filePath"})
    remote_server_id: Optional[str] = _field(
        default=None, metadata={"alias": "remoteServerId"}
    )
    version_id: Optional[str] = _field(default=None, metadata={"alias": "versionId"})
