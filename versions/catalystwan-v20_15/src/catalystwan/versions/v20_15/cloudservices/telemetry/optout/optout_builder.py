# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class OptoutBuilder:
    """
    Builds and executes requests for operations under /cloudservices/telemetry/optout
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def opt_out(self):
        class opt_out_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> Any:
                """
                Telemetry Opt Out

                :param payload: Payload
                :returns: Any
                """
                return self._request_adapter.request(
                    "DELETE",
                    "/dataservice/cloudservices/telemetry/optout",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return opt_out_(self._request_adapter)
