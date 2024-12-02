# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .interface.interface_builder import InterfaceBuilder


class ManagementVrfBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/management-vrf
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_management_vrf_features(self, transport_id: str, **kw) -> str:
        """
        Get all SD-Routing Management VRF features from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_management_vrf_feature(
        self, transport_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing Management VRF feature from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param payload: SD-Routing Management VRF feature from a specific transport feature profile
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_management_vrf_feature(self, transport_id: str, vrf_id: str, **kw) -> str:
        """
        Get the SD-Routing Management VRF feature from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Management VRF Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_management_vrf_feature(
        self, transport_id: str, vrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing Management VRF feature from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Management VRF Feature ID
        :param payload: SD-Routing Management VRF feature from a specific transport feature profile
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_management_vrf_feature(self, transport_id: str, vrf_id: str, **kw):
        """
        Delete the SD-Routing Management VRF feature from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Management VRF Feature ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}",
            params=params,
            **kw,
        )

    @property
    def interface(self) -> InterfaceBuilder:
        """
        The interface property
        """
        from .interface.interface_builder import InterfaceBuilder

        return InterfaceBuilder(self._request_adapter)
