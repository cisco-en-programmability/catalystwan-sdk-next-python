# Copyright 2024 Cisco Systems, Inc. and its affiliates
from dataclasses import dataclass
from dataclasses import field as _field
from typing import Literal, Optional

ProfileType = Literal["service"]

Solution = Literal["sdwan"]


@dataclass
class GetSdwanFeatureProfileBySdwanFamilyGetResponse:
    description: Optional[str] = _field(default=None)
    profile_name: Optional[str] = _field(default=None, metadata={"alias": "profileName"})
    profile_type: Optional[ProfileType] = _field(default=None, metadata={"alias": "profileType"})
    profole_id: Optional[str] = _field(default=None, metadata={"alias": "profoleId"})
    solution: Optional[Solution] = _field(default=None)
