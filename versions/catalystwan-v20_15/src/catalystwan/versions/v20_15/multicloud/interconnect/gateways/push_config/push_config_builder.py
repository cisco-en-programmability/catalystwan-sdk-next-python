# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import GatewaysPushconfigBody, ProcessResponse


class PushConfigBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/gateways/push-config
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def push_interconnect_gateway_config(self):
        class push_interconnect_gateway_config_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[GatewaysPushconfigBody] = None, **kw
            ) -> ProcessResponse:
                """
                API to initiate a configuration push for an Interconnect gateway.

                :param payload: Request Payload for Multicloud Interconnect Gateway Configuration Push
                :returns: ProcessResponse
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/interconnect/gateways/push-config",
                    return_type=ProcessResponse,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> GatewaysPushconfigBody:
                return GatewaysPushconfigBody(*args, **kwargs)

            @property
            def payload_model(self) -> Type[GatewaysPushconfigBody]:
                return GatewaysPushconfigBody

        return push_interconnect_gateway_config_(self._request_adapter)
