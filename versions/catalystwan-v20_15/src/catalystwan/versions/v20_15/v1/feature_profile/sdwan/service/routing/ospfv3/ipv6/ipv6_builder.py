# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class Ipv6Builder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv6
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_routing_ospfv3_ipv6_af_profile_parcel_for_service(self, service_id: str, **kw) -> str:
        """
        Get Routing OSPFv3 IPv6 Address Family Profile Parcels for Service feature profile

        :param service_id: Feature Profile ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv6",
            return_type=str,
            params=params,
            **kw,
        )

    def create_routing_ospfv3_ipv6_af_profile_parcel_for_service(
        self, service_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a Routing OSPFv3 IPv6 Address Family Profile Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param payload: Routing OSPFv3 IPv6 Address Family Profile Parcel
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv6",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_routing_ospfv3_i_pv6_af_profile_parcel_by_parcel_id_for_service(
        self, service_id: str, ospfv3_id: str, **kw
    ) -> str:
        """
        Get Routing OSPFv3 IPv6 Address Family Profile Parcel by parcelId for Service feature profile

        :param service_id: Feature Profile ID
        :param ospfv3_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv6/{ospfv3Id}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_routing_ospfv3_i_pv6_af_profile_parcel_for_service(
        self, service_id: str, ospfv3_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Routing OSPFv3 IPv6 Address Family Profile Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param ospfv3_id: Profile Parcel ID
        :param payload: Routing OSPFv3 IPv6 Address Family Profile Parcel
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv6/{ospfv3Id}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_routing_ospfv3_i_pv6_af_profile_parcel_for_service(
        self, service_id: str, ospfv3_id: str, **kw
    ):
        """
        Delete a Routing OSPFv3 IPv6 Address Family Profile Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param ospfv3_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv6/{ospfv3Id}",
            params=params,
            **kw,
        )
