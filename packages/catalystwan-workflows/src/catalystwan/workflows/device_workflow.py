from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List, Literal, Optional

from catalystwan.core.models.deserialize import deserialize

if TYPE_CHECKING:
    from catalystwan.core.loader import ApiClient


Personality = Literal["vsmart", "vedge", "vbond", "vmanage"]
Reachability = Literal["reachable", "unreachable", "unknown"]


@dataclass
class Device:
    uuid: str
    personality: Personality
    id: str = field(metadata={"alias": "deviceId"})
    hostname: str = field(metadata={"alias": "host-name"})
    reachability: Reachability
    local_system_ip: str = field(metadata={"alias": "local-system-ip"})
    status: Optional[str] = field(default=None)
    memUsage: Optional[float] = field(default=None)
    mem_state: Optional[str] = field(default=None, metadata={"alias": "memState"})
    cpu_state: Optional[str] = field(default=None, metadata={"alias": "cpuState"})
    cpu_load: Optional[float] = field(default=None, metadata={"alias": "cpuLoad"})
    state_description: Optional[str] = field(default=None)
    connected_vManages: List[str] = field(
        default_factory=list, metadata={"alias": "connectedVManages"}
    )
    model: Optional[str] = field(default=None, metadata={"alias": "device-model"})
    board_serial: Optional[str] = field(default=None, metadata={"alias": "board-serial"})
    vedgeCertificateState: Optional[str] = field(
        default=None, metadata={"alias": "vedgeCertificateState"}
    )
    chasis_number: Optional[str] = field(default=None, metadata={"alias": "chasisNumber"})
    site_id: Optional[str] = field(default=None, metadata={"alias": "site-id"})
    site_name: Optional[str] = field(default=None, metadata={"alias": "site-name"})


class DeviceWorkflow:
    supported_versions = ("20.14", "20.15", "20.16")
    PARAMS_LIMIT = 1000

    def __init__(self, client: ApiClient):
        self.client = client
        assert self.client.api_version in self.supported_versions

    def get_devices_info(self, rediscover: bool = False) -> List[Device]:
        if rediscover:
            self.client.device.action.rediscoverall.re_discover_all_device()

        devices = self.client.device.list_all_devices()
        device_ids = [device.device_id for device in devices if device.device_id is not None]
        devices_info: List[Device] = []
        for i in range(0, len(device_ids), self.PARAMS_LIMIT):
            response = self.client.device.system.info.create_device_info_list(
                device_id=device_ids[i : i + self.PARAMS_LIMIT]
            )
            devices_info.extend([deserialize(Device, **data) for data in response])

        return devices_info
