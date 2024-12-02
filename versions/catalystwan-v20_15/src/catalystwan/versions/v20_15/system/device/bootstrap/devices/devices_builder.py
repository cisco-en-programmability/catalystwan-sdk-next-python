# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import GenerateBootstrapConfigForVedgesResponse, VEdgeBootstrapConfig


class DevicesBuilder:
    """
    Builds and executes requests for operations under /system/device/bootstrap/devices
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def generate_bootstrap_config_for_vedges(self):
        class generate_bootstrap_config_for_vedges_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[VEdgeBootstrapConfig] = None, **kw
            ) -> GenerateBootstrapConfigForVedgesResponse:
                """
                Create bootstrap config for software vEdges

                :param payload: Request body for Device bootstrap configuration
                :returns: GenerateBootstrapConfigForVedgesResponse
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/system/device/bootstrap/devices",
                    return_type=GenerateBootstrapConfigForVedgesResponse,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> VEdgeBootstrapConfig:
                return VEdgeBootstrapConfig(*args, **kwargs)

            @property
            def payload_model(self) -> Type[VEdgeBootstrapConfig]:
                return VEdgeBootstrapConfig

        return generate_bootstrap_config_for_vedges_(self._request_adapter)
