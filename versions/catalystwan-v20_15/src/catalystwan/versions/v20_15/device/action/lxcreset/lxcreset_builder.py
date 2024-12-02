# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class LxcresetBuilder:
    """
    Builds and executes requests for operations under /device/action/lxcreset
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def process_lxc_reset(self):
        class process_lxc_reset_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Process a reset operation

                :param payload: Reset request payload
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/device/action/lxcreset", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return process_lxc_reset_(self._request_adapter)
