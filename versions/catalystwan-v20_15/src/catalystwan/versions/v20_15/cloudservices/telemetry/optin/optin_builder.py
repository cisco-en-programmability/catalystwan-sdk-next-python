# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class OptinBuilder:
    """
    Builds and executes requests for operations under /cloudservices/telemetry/optin
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def opt_in(self):
        class opt_in_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> Any:
                """
                Telemetry Opt In

                :param payload: Payload
                :returns: Any
                """
                return self._request_adapter.request(
                    "PUT", "/dataservice/cloudservices/telemetry/optin", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return opt_in_(self._request_adapter)
