# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class RegisterBuilder:
    """
    Builds and executes requests for operations under /disasterrecovery/register
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def update_1(self):
        class update_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Update data centers for disaster recovery

                :param payload: Datacenter registration request
                :returns: Any
                """
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/disasterrecovery/register",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_1_(self._request_adapter)

    @property
    def register(self):
        class register_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Register data centers for disaster recovery

                :param payload: Datacenter registration request
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/disasterrecovery/register",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return register_(self._request_adapter)
