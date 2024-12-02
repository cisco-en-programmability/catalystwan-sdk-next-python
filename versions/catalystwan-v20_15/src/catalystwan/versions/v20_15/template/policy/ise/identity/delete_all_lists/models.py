# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class DeleteAllListsBody:
    """
    Body for deleteAllLists call, generic api for deleting all lists of a specified listType
    """

    type_: Optional[str] = _field(default=None, metadata={"alias": "type"})
