# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List

from catalystwan.abc import RequestAdapterInterface


class DevicesBuilder:
    """
    Builds and executes requests for operations under /template/policy/vedge/devices
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_v_edge_policy_device_list(self, **kw) -> List[Any]:
        """
        Get device list

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/policy/vedge/devices",
            return_type=List[Any],
            **kw,
        )

    def get_device_list_by_policy(self, policy_id: str, **kw) -> List[Any]:
        """
        Get device list by policy

        :param policy_id: Policy Id
        :returns: List[Any]
        """
        params = {
            "policyId": policy_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/policy/vedge/devices/{policyId}",
            return_type=List[Any],
            params=params,
            **kw,
        )
