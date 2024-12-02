# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class InstalledCertsInner:
    certificate: Optional[str] = _field(default=None)
    signer_vmanage_uuid: Optional[str] = _field(
        default=None, metadata={"alias": "signerVmanageUUID"}
    )
