# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional, List
from dataclasses import dataclass, field as _field

InterconnectTypeParam = Literal["EQUINIX", "MEGAPORT"]


@dataclass
class InlineResponse2005:
    data: Optional[List[str]] = _field(default=None)
