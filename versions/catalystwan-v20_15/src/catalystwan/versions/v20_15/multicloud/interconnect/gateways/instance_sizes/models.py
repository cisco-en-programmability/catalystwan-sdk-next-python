# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional, List
from dataclasses import dataclass, field as _field

InterconnectTypeParam = Literal["EQUINIX", "MEGAPORT"]


@dataclass
class InlineResponse2004Data:
    # instance size
    size: Optional[str] = _field(default=None)
    # instance size
    spec: Optional[str] = _field(default=None)


@dataclass
class InlineResponse2004:
    data: Optional[List[InlineResponse2004Data]] = _field(default=None)
