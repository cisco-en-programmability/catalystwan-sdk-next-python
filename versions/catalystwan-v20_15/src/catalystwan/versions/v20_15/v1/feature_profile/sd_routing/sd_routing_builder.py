# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .service.service_builder import ServiceBuilder
    from .transport.transport_builder import TransportBuilder


class SdRoutingBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def service(self) -> ServiceBuilder:
        """
        The service property
        """
        from .service.service_builder import ServiceBuilder

        return ServiceBuilder(self._request_adapter)

    @property
    def transport(self) -> TransportBuilder:
        """
        The transport property
        """
        from .transport.transport_builder import TransportBuilder

        return TransportBuilder(self._request_adapter)
