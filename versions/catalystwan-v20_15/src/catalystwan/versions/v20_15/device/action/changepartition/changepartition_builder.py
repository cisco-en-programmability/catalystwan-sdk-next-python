# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import DeviceIp


class ChangepartitionBuilder:
    """
    Builds and executes requests for operations under /device/action/changepartition
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_change_partition_info(self, device_id: List[DeviceIp], **kw):
        """
        Get change partition information

        :param device_id: deviceId - Device IP
        :returns: None
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/action/changepartition", params=params, **kw
        )

    @property
    def process_change_partition(self):
        class process_change_partition_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Process change partition operation

                :param payload: Request body for Process change partition operation
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/action/changepartition",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return process_change_partition_(self._request_adapter)
