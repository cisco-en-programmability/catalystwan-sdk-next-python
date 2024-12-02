from __future__ import annotations

from dataclasses import asdict, dataclass
from logging import getLogger
from pathlib import Path
from threading import Thread
from typing import TYPE_CHECKING, List, Literal, Mapping, Optional, overload
from uuid import UUID

from catalystwan.core.client import copy_client

if TYPE_CHECKING:
    from catalystwan.core.loader import ApiClient

logger = getLogger(__name__)

DeviceType = Literal["vbond", "vedge", "vmanage", "vsmart"]
CollectDeviceType = Literal["all", DeviceType]
State = Literal["inprogress", "done"]
WhenAlreadyInProgress = Literal["skip", "retry"]


@dataclass
class Info:
    creation_time: Optional[int]
    device_ip: str
    file_name: str
    local_system_ip: Optional[str]
    request_token_id: str
    size: Optional[int]
    state: State
    tac_state: Optional[str]


class AdminTech:

    supported_versions = ("20.15",)

    def __init__(self, client: ApiClient):
        manager_version = client.api_version
        assert manager_version in self.supported_versions
        self.client = client

    def bulk_collect(
        self,
        device_ips: List[str] = [],
        download_dir: Path = Path.cwd(),
        *,
        device_type: CollectDeviceType = "all",
        site_id: Optional[int] = None,
        exclude_cores: bool = True,
        exclude_logs: bool = False,
        exclude_tech: bool = False,
        custom_commands: List[str] = [],
        tech_filter: List[str] = [],
        delete_after_download: bool = True,
    ) -> List[Path]:
        filtered_ips: List[str] = list()
        threads: List[Thread] = list()
        download_paths: List[Path] = list()
        filenames: List[str] = list()

        for device in self.client.device.list_all_devices(
            site_id=str(site_id) if site_id else None
        ):
            if device.device_id in device_ips or not device_ips:
                if device.device_id is not None and (
                    device_type == "all" or device_type == device.device_type
                ):
                    filtered_ips.append(device.device_id)

        logger.info(
            f"Starting admin-tech collection from: {', '.join(filtered_ips)} to: {download_dir} ..."
        )

        def collect(client: ApiClient, device_ip: str) -> None:
            with copy_client(client) as _client:
                api = AdminTech(_client)
                filename = api.generate(
                    device_ip=device_ip,
                    exclude_cores=exclude_cores,
                    exclude_logs=exclude_logs,
                    exclude_tech=exclude_tech,
                    custom_commands=custom_commands,
                    tech_filter=tech_filter,
                )
                filenames.append(filename)
                path = api.download(filename=filename, download_dir=download_dir)
                download_paths.append(path)

        for ip in filtered_ips:
            thread = Thread(
                target=collect,
                args=(
                    self.client,
                    ip,
                ),
            )
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        if delete_after_download:
            AdminTech(self.client).delete(filenames=filenames)

        return download_paths

    def generate(
        self,
        device_ip: Optional[str] = None,
        *,
        device_type: Optional[DeviceType] = None,
        exclude_cores: bool = True,
        exclude_logs: bool = False,
        exclude_tech: bool = False,
        custom_commands: List[str] = [],
        tech_filter: List[str] = [],
    ) -> str:
        Payload = self.client.device.tools.admintech.create_admin_tech.payload_model
        payload = Payload(
            device_ip=device_ip,
            device_type=device_type,
            exclude_cores=exclude_cores,
            exclude_logs=exclude_logs,
            exclude_tech=exclude_tech,
            custom_commands=custom_commands,
            tech_filter=tech_filter,
        )
        logger.info(f"Generating admin-tech for device: {device_ip} ...")
        response = self.client.device.tools.admintech.create_admin_tech(payload)
        filename = ""
        if isinstance(response, Mapping):
            filename = response.get("fileName", "")
        logger.info(f"Generated admin-tech for device: {device_ip} {filename}")
        return filename

    def download(self, filename: str, download_dir: Path = Path.cwd()) -> Path:
        download_path = download_dir / filename
        logger.info(f"Downloading admin-tech to: {download_path} ...")
        bytes = self.client.device.tools.admintech.download.download_admin_tech_file(
            filename=filename, timeout=(4.0, None)
        )
        with open(download_path, "wb") as file:
            file.write(bytes)
        logger.info(f"Downloaded admin-tech to: {download_path}")
        return download_path

    def list(self) -> List[Info]:
        response = self.client.device.tools.admintechs.list_admin_techs()
        return [Info(**asdict(r)) for r in response]

    def wait_for_generated_token_ids(self) -> None:
        pass

    @overload
    def delete(self, filename: str) -> None: ...

    @overload
    def delete(self, *, filenames: List[str]) -> None: ...

    @overload
    def delete(self, *, id: UUID) -> None: ...

    def delete(
        self,
        filename: Optional[str] = None,
        filenames: Optional[List[str]] = None,
        id: Optional[UUID] = None,
    ) -> None:
        ids: List[UUID] = list()
        if id is not None:
            ids = [id]
        elif filename is not None:
            ids = [
                UUID(info.request_token_id)
                for info in self.list()
                if info.file_name == filename
            ]
        elif filenames is not None:
            ids = [
                UUID(info.request_token_id)
                for info in self.list()
                if info.file_name in filenames
            ]
        for id_ in ids:
            logger.info(f"Removing admin-tech file on remote: {id_}")
            self.client.device.tools.admintech.delete_admin_tech_file(
                request_id=str(id_)
            )

    def delete_all(self) -> None:
        ids = [
            UUID(info.request_token_id) for info in self.list() if info.state == "done"
        ]
        for id in ids:
            self.delete(id=id)
