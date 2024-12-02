# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import GetConfigGroupDeviceConfigurationPreviewPostRequest


class PreviewBuilder:
    """
    Builds and executes requests for operations under /v1/config-group/{configGroupId}/device/{deviceId}/preview
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_config_group_device_configuration_preview(self):
        class get_config_group_device_configuration_preview_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                config_group_id: str,
                device_id: str,
                payload: Optional[
                    GetConfigGroupDeviceConfigurationPreviewPostRequest
                ] = None,
                **kw,
            ) -> Any:
                """
                Get a preview of the configuration for a device

                :param config_group_id: Config Group Id
                :param device_id: Device Id
                :param payload: Payload
                :returns: Any
                """
                params = {
                    "configGroupId": config_group_id,
                    "deviceId": device_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/config-group/{configGroupId}/device/{deviceId}/preview",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(
                self, *args, **kwargs
            ) -> GetConfigGroupDeviceConfigurationPreviewPostRequest:
                return GetConfigGroupDeviceConfigurationPreviewPostRequest(
                    *args, **kwargs
                )

            @property
            def payload_model(
                self,
            ) -> Type[GetConfigGroupDeviceConfigurationPreviewPostRequest]:
                return GetConfigGroupDeviceConfigurationPreviewPostRequest

        return get_config_group_device_configuration_preview_(self._request_adapter)
