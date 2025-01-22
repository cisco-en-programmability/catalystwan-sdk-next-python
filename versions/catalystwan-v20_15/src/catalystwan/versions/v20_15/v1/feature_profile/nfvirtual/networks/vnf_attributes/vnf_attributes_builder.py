# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .vnf.vnf_builder import VnfBuilder


class VnfAttributesBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_nfvirtual_vnf_attributes_parcel(
        self, networks_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create VNF Attributes Profile config for Networks feature profile

        :param networks_id: Feature Profile ID
        :param payload: VNF Attributes config Profile Parcel
        :returns: str
        """
        params = {
            "networksId": networks_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_nfvirtual_vnf_attributes_parcel(
        self, networks_id: str, vnf_attributes_id: str, **kw
    ) -> str:
        """
        Get VNF Attributes Profile Parcels for Networks feature profile

        :param networks_id: Feature Profile ID
        :param vnf_attributes_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "networksId": networks_id,
            "vnfAttributesId": vnf_attributes_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_nfvirtual_vnf_attributes_parcel(
        self, networks_id: str, vnf_attributes_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a VNF Attributes Profile Parcel for networks feature profile

        :param networks_id: Feature Profile ID
        :param vnf_attributes_id: Profile Parcel ID
        :param payload: VNF Attributes Profile Parcel
        :returns: str
        """
        params = {
            "networksId": networks_id,
            "vnfAttributesId": vnf_attributes_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_nfvirtual_vnf_attributes_parcel(
        self, networks_id: str, vnf_attributes_id: str, **kw
    ):
        """
        Delete VNF Attributes Profile config for Networks feature profile

        :param networks_id: Feature Profile ID
        :param vnf_attributes_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "networksId": networks_id,
            "vnfAttributesId": vnf_attributes_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}",
            params=params,
            **kw,
        )

    @property
    def vnf(self) -> VnfBuilder:
        """
        The vnf property
        """
        from .vnf.vnf_builder import VnfBuilder

        return VnfBuilder(self._request_adapter)
