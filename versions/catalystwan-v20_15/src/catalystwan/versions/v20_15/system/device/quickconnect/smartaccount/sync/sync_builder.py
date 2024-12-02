# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import SmartAccountModel, SyncDevicesResp


class SyncBuilder:
    """
    Builds and executes requests for operations under /system/device/quickconnect/smartaccount/sync
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_smart_account_devices(self):
        class get_smart_account_devices_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[SmartAccountModel] = None, **kw
            ) -> SyncDevicesResp:
                """
                Sync devices from Smart-Account

                :param payload: Payload
                :returns: SyncDevicesResp
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/system/device/quickconnect/smartaccount/sync",
                    return_type=SyncDevicesResp,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> SmartAccountModel:
                return SmartAccountModel(*args, **kwargs)

            @property
            def payload_model(self) -> Type[SmartAccountModel]:
                return SmartAccountModel

        return get_smart_account_devices_(self._request_adapter)
