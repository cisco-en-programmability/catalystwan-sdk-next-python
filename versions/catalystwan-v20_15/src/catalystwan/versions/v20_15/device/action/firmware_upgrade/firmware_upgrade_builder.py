# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import FirmwareImageRemoteUpgrade

if TYPE_CHECKING:
    from .devices.devices_builder import DevicesBuilder
    from .remote.remote_builder import RemoteBuilder


class FirmwareUpgradeBuilder:
    """
    Builds and executes requests for operations under /device/action/firmware-upgrade
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def remote_firmware_image_upgrade(self):
        class remote_firmware_image_upgrade_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[Any] = None, **kw
            ) -> FirmwareImageRemoteUpgrade:
                """
                Eemote firmware on device

                :param payload: Request body
                :returns: FirmwareImageRemoteUpgrade
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/action/firmware-upgrade",
                    return_type=FirmwareImageRemoteUpgrade,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return remote_firmware_image_upgrade_(self._request_adapter)

    def delete_firmware_upgarde_remote_image(self, version_id: str, **kw):
        """
        Download software package file

        :param version_id: Version id
        :returns: None
        """
        params = {
            "versionId": version_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/device/action/firmware-upgrade/{versionId}",
            params=params,
            **kw,
        )

    @property
    def devices(self) -> DevicesBuilder:
        """
        The devices property
        """
        from .devices.devices_builder import DevicesBuilder

        return DevicesBuilder(self._request_adapter)

    @property
    def remote(self) -> RemoteBuilder:
        """
        The remote property
        """
        from .remote.remote_builder import RemoteBuilder

        return RemoteBuilder(self._request_adapter)
