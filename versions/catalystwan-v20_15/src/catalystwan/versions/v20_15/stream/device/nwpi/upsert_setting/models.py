# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class NwpiSettingDataPayload:
    """
    Nwpi setting data schema
    """

    peer_site_threshold: Optional[int] = _field(
        default=None, metadata={"alias": "peerSiteThreshold"}
    )
    type_: Optional[str] = _field(default=None, metadata={"alias": "type"})
