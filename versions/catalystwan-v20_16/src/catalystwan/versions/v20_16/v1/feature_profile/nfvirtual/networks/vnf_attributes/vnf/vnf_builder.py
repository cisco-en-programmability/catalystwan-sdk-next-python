# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class VnfBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}/vnf
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_nfvirtual_vnf_parcel(
        self, networks_id: str, vnf_attributes_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create VNF Profile Parcel for Networks feature profile

        :param networks_id: Feature Profile ID
        :param vnf_attributes_id: Profile Parcel ID
        :param payload: VNF config Profile Parcel
        :returns: str
        """
        params = {
            "networksId": networks_id,
            "vnfAttributesId": vnf_attributes_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}/vnf",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_nfvirtual_vnf_parcel(
        self, networks_id: str, vnf_attributes_id: str, vnf_id: str, **kw
    ) -> str:
        """
        Get VNF Profile Parcels for Networks feature profile

        :param networks_id: Feature Profile ID
        :param vnf_attributes_id: Profile Parcel ID
        :param vnf_id: VNF Parcel ID
        :returns: str
        """
        params = {
            "networksId": networks_id,
            "vnfAttributesId": vnf_attributes_id,
            "vnfId": vnf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}/vnf/{vnfId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_nfvirtual_vnf_parcel(
        self,
        networks_id: str,
        vnf_attributes_id: str,
        vnf_id: str,
        payload: Optional[str] = None,
        **kw,
    ) -> str:
        """
        Edit a VNF Profile Parcel for networks feature profile

        :param networks_id: Feature Profile ID
        :param vnf_attributes_id: Profile Parcel ID
        :param vnf_id: VNF Parcel ID
        :param payload: VNF Profile Parcel
        :returns: str
        """
        params = {
            "networksId": networks_id,
            "vnfAttributesId": vnf_attributes_id,
            "vnfId": vnf_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}/vnf/{vnfId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_nfvirtual_vnf_parcel(
        self, networks_id: str, vnf_attributes_id: str, vnf_id: str, **kw
    ):
        """
        Delete a VNF Profile Parcel for Networks feature profile

        :param networks_id: Feature Profile ID
        :param vnf_attributes_id: Profile Parcel ID
        :param vnf_id: VNF Parcel ID
        :returns: None
        """
        params = {
            "networksId": networks_id,
            "vnfAttributesId": vnf_attributes_id,
            "vnfId": vnf_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}/vnf/{vnfId}",
            params=params,
            **kw,
        )
