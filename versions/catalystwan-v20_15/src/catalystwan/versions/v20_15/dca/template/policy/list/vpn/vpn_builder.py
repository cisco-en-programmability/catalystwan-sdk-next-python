# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class VpnBuilder:
    """
    Builds and executes requests for operations under /dca/template/policy/list/vpn
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_vpn_lists_dca(self):
        class get_vpn_lists_dca_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> List[Any]:
                """
                Get VPN details

                :param payload: Query string
                :returns: List[Any]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/dca/template/policy/list/vpn",
                    return_type=List[Any],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_vpn_lists_dca_(self._request_adapter)
