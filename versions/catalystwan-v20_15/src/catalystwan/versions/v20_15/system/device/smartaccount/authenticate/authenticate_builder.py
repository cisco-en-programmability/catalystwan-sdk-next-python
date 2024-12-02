# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import SmartAccountAuthenticateResponse


class AuthenticateBuilder:
    """
    Builds and executes requests for operations under /system/device/smartaccount/authenticate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def smart_account_authenticate(self):
        class smart_account_authenticate_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[Any] = None, **kw
            ) -> SmartAccountAuthenticateResponse:
                """
                Authenticate vSmart user account

                :param payload: Claim device request
                :returns: SmartAccountAuthenticateResponse
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/system/device/smartaccount/authenticate",
                    return_type=SmartAccountAuthenticateResponse,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return smart_account_authenticate_(self._request_adapter)
