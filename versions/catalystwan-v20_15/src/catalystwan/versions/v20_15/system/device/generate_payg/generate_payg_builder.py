# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class GeneratePaygBuilder:
    """
    Builds and executes requests for operations under /system/device/generate-payg
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def validate_user(self):
        class validate_user_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Authenticate vSmart user account

                :param payload: Request body
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/system/device/generate-payg",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return validate_user_(self._request_adapter)
