# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .activate.activate_builder import ActivateBuilder
    from .devices.devices_builder import DevicesBuilder
    from .install.install_builder import InstallBuilder
    from .remove.remove_builder import RemoveBuilder


class FirmwareBuilder:
    """
    Builds and executes requests for operations under /device/action/firmware
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_firmware_images(self, **kw):
        """
        Get list of firmware images in the repository

        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "getFirmwareImages")
        return self._request_adapter.request("GET", "/dataservice/device/action/firmware", **kw)

    def process_firmware_image(self, **kw):
        """
        Upload firmware image package

        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "processFirmwareImage")
        return self._request_adapter.request("POST", "/dataservice/device/action/firmware", **kw)

    def get_firmware_image_details(self, version_id: str, **kw):
        """
        Get firmware image details for a given version

        :param version_id: Firmware image version
        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "getFirmwareImageDetails")
        params = {
            "versionId": version_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/action/firmware/{versionId}", params=params, **kw
        )

    def delete_firmware_image(self, version_id: str, **kw):
        """
        Delete firmware image package

        :param version_id: Firmware image version
        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "deleteFirmwareImage")
        params = {
            "versionId": version_id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/device/action/firmware/{versionId}", params=params, **kw
        )

    @property
    def activate(self) -> ActivateBuilder:
        """
        The activate property
        """
        from .activate.activate_builder import ActivateBuilder

        return ActivateBuilder(self._request_adapter)

    @property
    def devices(self) -> DevicesBuilder:
        """
        The devices property
        """
        from .devices.devices_builder import DevicesBuilder

        return DevicesBuilder(self._request_adapter)

    @property
    def install(self) -> InstallBuilder:
        """
        The install property
        """
        from .install.install_builder import InstallBuilder

        return InstallBuilder(self._request_adapter)

    @property
    def remove(self) -> RemoveBuilder:
        """
        The remove property
        """
        from .remove.remove_builder import RemoveBuilder

        return RemoveBuilder(self._request_adapter)
