# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class ConfigureBuilder:
    """
    Builds and executes requests for operations under /clusterManagement/configure
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def configure_vmanage(self):
        class configure_vmanage_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Configure vManage


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: vManage server config
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/clusterManagement/configure",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return configure_vmanage_(self._request_adapter)
