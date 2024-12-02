# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type
from catalystwan.abc import RequestAdapterInterface


class UniquevpnlistBuilder:
    """
    Builds and executes requests for operations under /device/action/uniquevpnlist
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def create_unique_vpn_list(self):
        class create_unique_vpn_list_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> List[Any]:
                """
                Create unique VPN list

                :param payload: Device IPs
                :returns: List[Any]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/action/uniquevpnlist",
                    return_type=List[Any],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_unique_vpn_list_(self._request_adapter)
