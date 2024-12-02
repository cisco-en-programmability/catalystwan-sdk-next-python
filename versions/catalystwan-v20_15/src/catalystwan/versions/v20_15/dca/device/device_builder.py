# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .crashlog.crashlog_builder import CrashlogBuilder


class DeviceBuilder:
    """
    Builds and executes requests for operations under /dca/device
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def list_all_devices_dca(self):
        class list_all_devices_dca_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> List[Any]:
                """
                Get all devices

                :param payload: Query string
                :returns: List[Any]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/dca/device",
                    return_type=List[Any],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return list_all_devices_dca_(self._request_adapter)

    @property
    def crashlog(self) -> CrashlogBuilder:
        """
        The crashlog property
        """
        from .crashlog.crashlog_builder import CrashlogBuilder

        return CrashlogBuilder(self._request_adapter)
