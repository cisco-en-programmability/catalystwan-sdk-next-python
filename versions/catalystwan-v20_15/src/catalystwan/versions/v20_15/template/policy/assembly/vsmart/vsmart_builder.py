# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class VsmartBuilder:
    """
    Builds and executes requests for operations under /template/policy/assembly/vsmart
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def preview_3(self):
        class preview_3_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Get policy assembly preview

                :param payload: Policy assembly
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/policy/assembly/vsmart",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return preview_3_(self._request_adapter)

    def preview_by_id_3(self, id: str, **kw) -> Any:
        """
        Get policy assembly preview for feature policy

        :param id: Policy Id
        :returns: Any
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/policy/assembly/vsmart/{id}",
            params=params,
            **kw,
        )
