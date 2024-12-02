# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List

from catalystwan.abc import RequestAdapterInterface

from .models import GenerateDeviceStateDataFieldsInner


class FieldsBuilder:
    """
    Builds and executes requests for operations under /data/device/state/{state_data_type}/fields
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_device_state_data_fields(
        self, state_data_type: str, **kw
    ) -> List[GenerateDeviceStateDataFieldsInner]:
        """
        Get device state data fileds

        :param state_data_type: State data type
        :returns: List[GenerateDeviceStateDataFieldsInner]
        """
        params = {
            "state_data_type": state_data_type,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/data/device/state/{state_data_type}/fields",
            return_type=List[GenerateDeviceStateDataFieldsInner],
            params=params,
            **kw,
        )
