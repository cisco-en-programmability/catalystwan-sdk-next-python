# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import GenerateRemovePartitionInfo
from .models import DeviceIp


class RemovepartitionBuilder:
    """
    Builds and executes requests for operations under /device/action/removepartition
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_remove_partition_info(
        self, device_id: Optional[List[DeviceIp]] = None, **kw
    ) -> GenerateRemovePartitionInfo:
        """
        Get remove partition information

        :param device_id: Device id
        :returns: GenerateRemovePartitionInfo
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/action/removepartition",
            return_type=GenerateRemovePartitionInfo,
            params=params,
            **kw,
        )

    @property
    def process_remove_partition(self):
        class process_remove_partition_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Process remove partition operation

                :param payload: Device remove partition request payload
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/action/removepartition",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return process_remove_partition_(self._request_adapter)
