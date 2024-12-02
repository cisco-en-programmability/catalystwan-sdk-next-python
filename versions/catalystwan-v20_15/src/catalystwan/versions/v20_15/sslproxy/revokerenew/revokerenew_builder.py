# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class RevokerenewBuilder:
    """
    Builds and executes requests for operations under /sslproxy/revokerenew
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def revoke_renew_certificate(self):
        class revoke_renew_certificate_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Revoke and renew device certificate

                :param payload: Revoke device certificate request
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/sslproxy/revokerenew", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return revoke_renew_certificate_(self._request_adapter)
