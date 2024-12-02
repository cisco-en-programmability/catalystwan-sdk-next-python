# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class OspfBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_service_vrf_ospf_features(self, service_id: str, **kw) -> str:
        """
        Get all SD-Routing LAN OSPF features for service VRF from a specific service feature profile

        :param service_id: Service Profile ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_service_vrf_ospf_feature(
        self, service_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing LAN OSPF feature for service VRF from a specific service feature profile

        :param service_id: Service Profile ID
        :param payload: SD-Routing LAN OSPF feature for service VRF from a specific service feature profile
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_service_vrf_ospf_feature(self, service_id: str, ospf_id: str, **kw) -> str:
        """
        Get the SD-Routing LAN OSPF feature for service VRF from a specific service feature profile

        :param service_id: Service Profile ID
        :param ospf_id: OSPF Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "ospfId": ospf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf/{ospfId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_service_vrf_ospf_feature(
        self, service_id: str, ospf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing LAN OSPF feature for service VRF from a specific service feature profile

        :param service_id: Service Profile ID
        :param ospf_id: OSPF Feature ID
        :param payload: SD-Routing LAN OSPF feature for service VRF from a specific service feature profile
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "ospfId": ospf_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf/{ospfId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_service_vrf_ospf_feature(self, service_id: str, ospf_id: str, **kw):
        """
        Delete the SD-Routing LAN OSPF feature for service VRF from a specific service feature profile

        :param service_id: Service Profile ID
        :param ospf_id: OSPF Feature ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "ospfId": ospf_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf/{ospfId}",
            params=params,
            **kw,
        )
