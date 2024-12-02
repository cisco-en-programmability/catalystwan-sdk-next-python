# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class AttachBuilder:
    """
    Builds and executes requests for operations under /template/config/attach
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def upload_config(self):
        class upload_config_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, device_id: str, payload: Optional[Any] = None, **kw):
                """
                Upload device config

                :param device_id: Device Model ID
                :param payload: Template config
                :returns: None
                """
                params = {
                    "deviceId": device_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/template/config/attach/{deviceId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return upload_config_(self._request_adapter)
