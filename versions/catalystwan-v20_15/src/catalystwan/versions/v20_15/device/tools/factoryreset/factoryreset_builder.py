# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class FactoryresetBuilder:
    """
    Builds and executes requests for operations under /device/tools/factoryreset
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def factory_reset(self):
        class factory_reset_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Device factory reset

                :param payload: Device factory reset
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/tools/factoryreset",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return factory_reset_(self._request_adapter)
