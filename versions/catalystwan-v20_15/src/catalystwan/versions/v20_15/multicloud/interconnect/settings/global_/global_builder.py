# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import InterconnectGlobalSettings, InterconnectTypeParam


class GlobalBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/settings/global
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_interconnect_global_settings(
        self, interconnect_type: InterconnectTypeParam, **kw
    ) -> InterconnectGlobalSettings:
        """
        API to retrieve global settings for an Interconnect provider type.

        :param interconnect_type: Interconnect provider type
        :returns: InterconnectGlobalSettings
        """
        params = {
            "interconnect-type": interconnect_type,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/interconnect/settings/global",
            return_type=InterconnectGlobalSettings,
            params=params,
            **kw,
        )

    @property
    def update_interconnect_global_settings(self):
        class update_interconnect_global_settings_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[InterconnectGlobalSettings] = None, **kw):
                """
                API to update global settings for an Interconnect provider.

                :param payload: Request Payload for Multicloud Interconnect Global Settings
                :returns: None
                """
                return self._request_adapter.request(
                    "PUT", "/dataservice/multicloud/interconnect/settings/global", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> InterconnectGlobalSettings:
                return InterconnectGlobalSettings(*args, **kwargs)

            @property
            def payload_model(self) -> Type[InterconnectGlobalSettings]:
                return InterconnectGlobalSettings

        return update_interconnect_global_settings_(self._request_adapter)

    @property
    def add_interconnect_global_settings(self):
        class add_interconnect_global_settings_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[InterconnectGlobalSettings] = None, **kw):
                """
                API to add global settings for an Interconnect provider.

                :param payload: Request Payload for Multicloud Interconnect Global Settings
                :returns: None
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/multicloud/interconnect/settings/global", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> InterconnectGlobalSettings:
                return InterconnectGlobalSettings(*args, **kwargs)

            @property
            def payload_model(self) -> Type[InterconnectGlobalSettings]:
                return InterconnectGlobalSettings

        return add_interconnect_global_settings_(self._request_adapter)
