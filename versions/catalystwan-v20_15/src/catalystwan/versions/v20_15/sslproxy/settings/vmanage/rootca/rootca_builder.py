# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class RootcaBuilder:
    """
    Builds and executes requests for operations under /sslproxy/settings/vmanage/rootca
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def getv_manage_root_ca(self, **kw) -> Any:
        """
        Get vManage root certificate

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/sslproxy/settings/vmanage/rootca", **kw
        )

    @property
    def setv_manage_root_ca(self):
        class setv_manage_root_ca_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Set vManage root certificate

                :param payload: Set vManage root CA request
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/sslproxy/settings/vmanage/rootca",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return setv_manage_root_ca_(self._request_adapter)
