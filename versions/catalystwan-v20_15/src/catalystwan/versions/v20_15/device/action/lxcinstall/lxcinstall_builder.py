# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class LxcinstallBuilder:
    """
    Builds and executes requests for operations under /device/action/lxcinstall
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def process_lxc_install(self):
        class process_lxc_install_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Process an installation operation

                :param payload: Installation request payload
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/action/lxcinstall",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return process_lxc_install_(self._request_adapter)
