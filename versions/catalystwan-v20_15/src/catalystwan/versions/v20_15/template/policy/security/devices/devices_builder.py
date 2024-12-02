# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List

from catalystwan.abc import RequestAdapterInterface


class DevicesBuilder:
    """
    Builds and executes requests for operations under /template/policy/security/devices
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_security_policy_device_list_1(self, **kw) -> List[Any]:
        """
        Get device list

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/policy/security/devices",
            return_type=List[Any],
            **kw,
        )

    def get_device_list_by_id(self, policy_id: str, **kw) -> List[Any]:
        """
        Get device list by Id

        :param policy_id: Policy Id
        :returns: List[Any]
        """
        params = {
            "policyId": policy_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/policy/security/devices/{policyId}",
            return_type=List[Any],
            params=params,
            **kw,
        )
