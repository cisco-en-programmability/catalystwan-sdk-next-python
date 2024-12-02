# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import GetPolicyGroupDeviceConfigurationPreviewPostRequest


class PreviewBuilder:
    """
    Builds and executes requests for operations under /v1/policy-group/{policyGroupId}/device/{deviceId}/preview
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_policy_group_device_configuration_preview(self):
        class get_policy_group_device_configuration_preview_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                policy_group_id: str,
                device_id: str,
                payload: Optional[
                    GetPolicyGroupDeviceConfigurationPreviewPostRequest
                ] = None,
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

            def create_payload(
                self, *args, **kwargs
            ) -> GetPolicyGroupDeviceConfigurationPreviewPostRequest:
                return GetPolicyGroupDeviceConfigurationPreviewPostRequest(
                    *args, **kwargs
                )

            @property
            def payload_model(
                self,
            ) -> Type[GetPolicyGroupDeviceConfigurationPreviewPostRequest]:
                return GetPolicyGroupDeviceConfigurationPreviewPostRequest

        return get_policy_group_device_configuration_preview_(self._request_adapter)
