# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class GetControllerClientTokenBuilder:
    """
    Builds and executes requests for operations under /dashboard/getControllerClientToken
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_controller_client_token(self):
        class get_controller_client_token_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Register Controller to BiFrost Dashboard (by Controller)

                :param payload: CD profile to be registered
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/dashboard/getControllerClientToken",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_controller_client_token_(self._request_adapter)
