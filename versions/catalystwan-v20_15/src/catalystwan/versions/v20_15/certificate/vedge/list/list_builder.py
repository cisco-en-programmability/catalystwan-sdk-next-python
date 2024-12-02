# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class ListBuilder:
    """
    Builds and executes requests for operations under /certificate/vedge/list
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def getv_edge_list(self, state: Optional[str] = None, **kw) -> str:
        """
        get vEdge list

        :param state: Certificate State
        :returns: str
        """
        params = {
            "state": state,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/certificate/vedge/list",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def setv_edge_list(self):
        class setv_edge_list_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[str] = None, action: Optional[str] = None, **kw
            ) -> str:
                """
                Save vEdge list (send to controller)

                :param action: Action Type
                :param payload: Required only for save action
                :returns: str
                """
                params = {
                    "action": action,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/certificate/vedge/list",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return setv_edge_list_(self._request_adapter)
