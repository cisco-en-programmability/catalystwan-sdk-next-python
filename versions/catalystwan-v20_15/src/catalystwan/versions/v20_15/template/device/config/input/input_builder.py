# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class InputBuilder:
    """
    Builds and executes requests for operations under /template/device/config/input
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def create_device_input(self):
        class create_device_input_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create device input


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: Template device input
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/device/config/input",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_device_input_(self._request_adapter)
