# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import GetPolicyGroupDeviceConfigurationPreviewPostRequest


class PreviewBuilder:
    """
    Builds and executes requests for operations under /v1/policy-group/{policyGroupId}/device/{deviceId}/preview
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_policy_group_device_configuration_preview(
        self,
        policy_group_id: str,
        device_id: str,
        payload: Optional[GetPolicyGroupDeviceConfigurationPreviewPostRequest] = None,
        **kw,
    ) -> Any:
        """
        Get a preview of the configuration for a device

        :param policy_group_id: Policy Group Id
        :param device_id: Device Id
        :param payload: Payload
        :returns: Any
        """
        params = {
            "policyGroupId": policy_group_id,
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/policy-group/{policyGroupId}/device/{deviceId}/preview",
            params=params,
            payload=payload,
            **kw,
        )
