# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .global_vrf.global_vrf_builder import GlobalVrfBuilder
    from .multicloud_connection.multicloud_connection_builder import MulticloudConnectionBuilder


class TransportBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def global_vrf(self) -> GlobalVrfBuilder:
        """
        The global-vrf property
        """
        from .global_vrf.global_vrf_builder import GlobalVrfBuilder

        return GlobalVrfBuilder(self._request_adapter)

    @property
    def multicloud_connection(self) -> MulticloudConnectionBuilder:
        """
        The multicloud-connection property
        """
        from .multicloud_connection.multicloud_connection_builder import MulticloudConnectionBuilder

        return MulticloudConnectionBuilder(self._request_adapter)
