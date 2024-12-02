# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .hostvpc.hostvpc_builder import HostvpcBuilder


class DevicepairBuilder:
    """
    Builds and executes requests for operations under /template/cor/devicepair
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def add_device_pair(self):
        class add_device_pair_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Add device pair

                :param payload: Add device pair request
                :returns: Any
                """
                logging.warning("Operation: %s is deprecated", "addDevicePair")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/cor/devicepair",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return add_device_pair_(self._request_adapter)

    @property
    def hostvpc(self) -> HostvpcBuilder:
        """
        The hostvpc property
        """
        from .hostvpc.hostvpc_builder import HostvpcBuilder

        return HostvpcBuilder(self._request_adapter)
