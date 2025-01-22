# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import InterconnectGatewayExtended, ProcessResponse


class GatewaysBuilder:
    """
    Builds and executes requests for operations under /v1/multicloud/interconnect/gateways
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def update_interconnect_gateway_1(
        self,
        interconnect_gateway_name: str,
        payload: Optional[InterconnectGatewayExtended] = None,
        **kw,
    ) -> ProcessResponse:
        """
        Asynchronous API to update the Interconnect Gateway Information in vManage.

        :param interconnect_gateway_name: Interconnect gateway name
        :param payload: Request Payload for Multicloud Interconnect Gateways
        :returns: ProcessResponse
        """
        params = {
            "interconnect-gateway-name": interconnect_gateway_name,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/multicloud/interconnect/gateways/{interconnect-gateway-name}",
            return_type=ProcessResponse,
            params=params,
            payload=payload,
            **kw,
        )
