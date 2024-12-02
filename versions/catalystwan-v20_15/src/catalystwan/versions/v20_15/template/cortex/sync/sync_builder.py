# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class SyncBuilder:
    """
    Builds and executes requests for operations under /template/cortex/sync
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def sync_wan_resource_groups(self):
        class sync_wan_resource_groups_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Sync WAN Resource Groups

                :param payload: WAN resource group
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/template/cortex/sync", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return sync_wan_resource_groups_(self._request_adapter)
