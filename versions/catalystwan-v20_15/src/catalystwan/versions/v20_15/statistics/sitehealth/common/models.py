# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal
from dataclasses import dataclass

AppsHealth = Literal["fair", "good", "poor"]

HealthParam = Literal["FAIR", "GOOD", "POOR"]

DeviceTypeParam = Literal["all", "controller", "vedge"]


@dataclass
class SiteHealthItem:
    apps_health: AppsHealth
    apps_usage: int
    devices_health: AppsHealth
    site_health: AppsHealth
    site_id: str
    tunnels_health: AppsHealth
