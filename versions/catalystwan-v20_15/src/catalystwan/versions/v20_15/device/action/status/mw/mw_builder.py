# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class MwBuilder:
    """
    Builds and executes requests for operations under /device/action/status/mw
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_maintenance_window_flag(self, **kw) -> Any:
        """
        Get status of maintenance window for vManage upgrade flag

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/device/action/status/mw", **kw
        )

    @property
    def update_maintenance_window_flag(self):
        class update_maintenance_window_flag_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Update maintenance window flag

                :param payload: Update maintenance window flag
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/action/status/mw",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_maintenance_window_flag_(self._request_adapter)
