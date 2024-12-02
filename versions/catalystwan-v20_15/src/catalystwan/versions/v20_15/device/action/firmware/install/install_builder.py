# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class InstallBuilder:
    """
    Builds and executes requests for operations under /device/action/firmware/install
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def install_firmware_image(self):
        class install_firmware_image_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw):
                """
                Install firmware on device

                :param payload: Payload
                :returns: None
                """
                logging.warning("Operation: %s is deprecated", "installFirmwareImage")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/action/firmware/install",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return install_firmware_image_(self._request_adapter)
