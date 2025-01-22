# Copyright 2024 Cisco Systems, Inc. and its affiliates
from dataclasses import dataclass
from dataclasses import field as _field
from typing import List, Literal, Optional, Union

Solution = Literal["sd-routing", "sdwan"]


@dataclass
class Variables:
    name: str
    value: Union[str, int, int, bool, List[None]]


@dataclass
class Devices:
    # Device unique id
    device_id: str = _field(metadata={"alias": "device-id"})
    # Variable object for the device
    variables: List[Variables]


@dataclass
class Default:
    """
    Variables PUT request Schema
    """

    # Variables for devices
    devices: List[Devices]
    solution: Solution  # pytype: disable=annotation-type-mismatch


@dataclass
class VariablesDefault:
    """
    Variables POST request Schema
    """

    # ID of devices for which Variables need to be fetched
    device_ids: Optional[List[str]] = _field(default=None, metadata={"alias": "deviceIds"})
    # Variable object for the device
    suggestions: Optional[bool] = _field(default=None)
