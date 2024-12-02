# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class UnlockBuilder:
    """
    Builds and executes requests for operations under /system/device/{uuid}/unlock
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def unlock_device(self):
        class unlock_device_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, uuid: str, payload: Optional[Any] = None, **kw):
                """
                Unlock device

                :param uuid: Device uuid
                :param payload: Device config
                :returns: None
                """
                params = {
                    "uuid": uuid,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/system/device/{uuid}/unlock",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return unlock_device_(self._request_adapter)
