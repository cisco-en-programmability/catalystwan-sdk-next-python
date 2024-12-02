# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class ModeBuilder:
    """
    Builds and executes requests for operations under /clusterManagement/tenancy/mode
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_tenancy_mode(self, **kw) -> Any:
        """
        Get vManage tenancy mode


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/clusterManagement/tenancy/mode", **kw
        )

    @property
    def set_tenancy_mode(self):
        class set_tenancy_mode_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Update vManage tenancy mode

                :param payload: Tenancy mode setting
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/clusterManagement/tenancy/mode",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return set_tenancy_mode_(self._request_adapter)
