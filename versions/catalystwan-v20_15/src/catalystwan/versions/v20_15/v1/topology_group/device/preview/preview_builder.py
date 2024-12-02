# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import GetTopologyGroupDeviceConfigurationPreviewPostRequest


class PreviewBuilder:
    """
    Builds and executes requests for operations under /v1/topology-group/{topologyGroupId}/device/{deviceId}/preview
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_topology_group_device_configuration_preview(
        self,
        topology_group_id: str,
        device_id: str,
        payload: Optional[GetTopologyGroupDeviceConfigurationPreviewPostRequest] = None,
        **kw,
    ) -> str:
        """
        Get a preview of the configuration for a device

        :param topology_group_id: Topology Group Id
        :param device_id: Device Id
        :param payload: Payload
        :returns: str
        """
        params = {
            "topologyGroupId": topology_group_id,
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/topology-group/{topologyGroupId}/device/{deviceId}/preview",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )
