# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface


class ListBuilder:
    """
    Builds and executes requests for operations under /certificate/save/vedge/list
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def save_v_edge_list(self):
        class save_v_edge_list_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> str:
                """
                change VedgeList Validity

                :param payload: JSON payload with RootCertChain and Certificate details.
                :returns: str
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/certificate/save/vedge/list",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return save_v_edge_list_(self._request_adapter)
