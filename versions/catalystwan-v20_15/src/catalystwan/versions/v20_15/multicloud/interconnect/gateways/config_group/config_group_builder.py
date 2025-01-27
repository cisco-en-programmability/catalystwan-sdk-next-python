# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import GatewaysConfiggroupBody, InterconnectTypeParam


class ConfigGroupBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/gateways/config-group
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_interconnect_gateway_config_group(
        self,
        interconnect_type: InterconnectTypeParam,
        payload: Optional[GatewaysConfiggroupBody] = None,
        **kw,
    ) -> Any:
        """
        API to initiate a config group creation for an Interconnect gateway.

        :param interconnect_type: Interconnect provider type
        :param payload: Request Payload for Multicloud Interconnect Gateway Config Group Creation
        :returns: Any
        """
        params = {
            "interconnect-type": interconnect_type,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/multicloud/interconnect/gateways/config-group",
            params=params,
            payload=payload,
            **kw,
        )
