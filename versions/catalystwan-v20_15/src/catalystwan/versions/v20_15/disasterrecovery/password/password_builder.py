# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class PasswordBuilder:
    """
    Builds and executes requests for operations under /disasterrecovery/password
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def update(self):
        class update_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Update data centers and vBonds passwords for disaster recovery

                :param payload: Datacenter/vBond password update request
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/disasterrecovery/password",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_(self._request_adapter)
