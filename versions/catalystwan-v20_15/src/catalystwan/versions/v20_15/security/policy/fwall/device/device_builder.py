# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import DeviceLists


class DeviceBuilder:
    """
    Builds and executes requests for operations under /security/policy/fwall/device
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_post_fwall_by_query(self):
        class get_post_fwall_by_query_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[Any] = None, **kw
            ) -> List[DeviceLists]:
                """
                Get firewall devices list

                :param payload: Stats query string
                :returns: List[DeviceLists]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/security/policy/fwall/device",
                    return_type=List[DeviceLists],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_post_fwall_by_query_(self._request_adapter)
