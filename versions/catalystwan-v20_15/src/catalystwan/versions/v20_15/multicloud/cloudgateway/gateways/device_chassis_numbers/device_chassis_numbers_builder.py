# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import InlineResponse200


class DeviceChassisNumbersBuilder:
    """
    Builds and executes requests for operations under /multicloud/cloudgateway/{cloudType}/gateways/device-chassis-numbers
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_available_devices_or_by_cg_id(
        self, cloud_type: str, config_group_id: Optional[str] = None, device_solution_type: Optional[str] = None, **kw
    ) -> List[InlineResponse200]:
        """
        API to retrieve available devices or devices associated to a config group.

        :param cloud_type: Multicloud provider type
        :param config_group_id: Multicloud config group id
        :param device_solution_type: Multicloud device solution type
        :returns: List[InlineResponse200]
        """
        params = {
            "cloudType": cloud_type,
            "config-group-id": config_group_id,
            "device-solution-type": device_solution_type,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/cloudgateway/{cloudType}/gateways/device-chassis-numbers",
            return_type=List[InlineResponse200],
            params=params,
            **kw,
        )
