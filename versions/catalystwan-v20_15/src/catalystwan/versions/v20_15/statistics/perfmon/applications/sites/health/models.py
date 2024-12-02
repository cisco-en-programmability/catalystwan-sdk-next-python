# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal
from dataclasses import dataclass

LastNHoursParam = Literal["1", "12", "24", "3", "6"]

HealthParam = Literal["FAIR", "GOOD", "POOR"]


@dataclass
class ApplicationsSitesItem:
    application: str
    fair_site: int
    family: str
    good_site: int
    health: str
    poor_site: int
