# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import MultiCloudGatewaysConfiggroupBody, PostCgwConfigGroupResponse


class ConfigGroupBuilder:
    """
    Builds and executes requests for operations under /multicloud/cloudgateway/config-group
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_cloud_gateway_config_group(
        self, cloud_type: str, payload: Optional[MultiCloudGatewaysConfiggroupBody] = None, **kw
    ) -> PostCgwConfigGroupResponse:
        """
        API to initiate a config group creation for a cloud gateway.

        :param cloud_type: Multicloud provider type
        :param payload: Request Payload for Multicloud Gateway Config Group Creation
        :returns: PostCgwConfigGroupResponse
        """
        params = {
            "cloudType": cloud_type,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/multicloud/cloudgateway/config-group",
            return_type=PostCgwConfigGroupResponse,
            params=params,
            payload=payload,
            **kw,
        )
