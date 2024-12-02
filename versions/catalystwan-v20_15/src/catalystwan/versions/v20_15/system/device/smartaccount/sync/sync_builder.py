# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import SyncDevicesResp


class SyncBuilder:
    """
    Builds and executes requests for operations under /system/device/smartaccount/sync
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def sync_devices(self):
        class sync_devices_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> SyncDevicesResp:
                """
                Sync devices from Smart-Account

                :param payload: Request body for Sync devices from Smart-Account
                :returns: SyncDevicesResp
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/system/device/smartaccount/sync",
                    return_type=SyncDevicesResp,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return sync_devices_(self._request_adapter)
