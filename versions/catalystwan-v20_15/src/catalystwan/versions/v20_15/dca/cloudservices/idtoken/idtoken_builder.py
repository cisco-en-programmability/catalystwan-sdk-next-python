# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class IdtokenBuilder:
    """
    Builds and executes requests for operations under /dca/cloudservices/idtoken
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_id_token(self, **kw) -> Any:
        """
        Get DCA Id token

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/dca/cloudservices/idtoken", **kw
        )

    @property
    def store_id_token(self):
        class store_id_token_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Set DCA Id token

                :param payload: DCA Id token
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/dca/cloudservices/idtoken",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return store_id_token_(self._request_adapter)
