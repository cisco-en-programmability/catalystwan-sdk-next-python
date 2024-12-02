# Copyright 2024 Cisco Systems, Inc. and its affiliates
from dataclasses import dataclass
from dataclasses import field as _field
from typing import Literal, Optional

Solution = Literal["sdwan"]


@dataclass
class GetSdwanFeatureProfileBySdwanFamilyGetResponse:
    description: Optional[str] = _field(default=None)
    profile_id: Optional[str] = _field(default=None, metadata={"alias": "profileId"})
    profile_name: Optional[str] = _field(default=None, metadata={"alias": "profileName"})
    profile_type: Optional[str] = _field(default=None, metadata={"alias": "profileType"})
    solution: Optional[Solution] = _field(default=None)
