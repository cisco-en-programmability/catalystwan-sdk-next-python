# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class EigrpBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_service_vrf_eigrp_features(self, service_id: str, **kw) -> str:
        """
        Get all SD-Routing VRF EIGRP features from a specific service feature profile

        :param service_id: Service Profile ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_service_vrf_eigrp_feature(
        self, service_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing VRF EIGRP feature from a specific service feature profile

        :param service_id: Service Profile ID
        :param payload: SD-Routing VRF EIGRP feature from a specific service feature profile
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_service_vrf_eigrp_feature(self, service_id: str, eigrp_id: str, **kw) -> str:
        """
        Get the SD-Routing VRF EIGRP feature from a specific service feature profile

        :param service_id: Service Profile ID
        :param eigrp_id: EIGRP Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "eigrpId": eigrp_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp/{eigrpId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_service_vrf_eigrp_feature(
        self, service_id: str, eigrp_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing VRF EIGRP feature from a specific service feature profile

        :param service_id: Service Profile ID
        :param eigrp_id: EIGRP Feature ID
        :param payload: SD-Routing VRF EIGRP feature from a specific service feature profile
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "eigrpId": eigrp_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp/{eigrpId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_service_vrf_eigrp_feature(self, service_id: str, eigrp_id: str, **kw):
        """
        Delete the SD-Routing VRF EIGRP feature from a specific service feature profile

        :param service_id: Service Profile ID
        :param eigrp_id: EIGRP Feature ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "eigrpId": eigrp_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp/{eigrpId}",
            params=params,
            **kw,
        )

    def get_service_vrf_associated_routing_eigrp_features(
        self, service_id: str, vrf_id: str, **kw
    ) -> str:
        """
        Get the LAN VRF associated EIGRP Features for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp",
            return_type=str,
            params=params,
            **kw,
        )

    def create_service_vrf_and_routing_eigrp_feature_association(
        self, service_id: str, vrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Associate a EIGRP feature with the LAN VRF feature for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param payload: New EIGRP feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_service_vrf_associated_routing_eigrp_feature_by_feature_id(
        self, service_id: str, vrf_id: str, eigrp_id: str, **kw
    ) -> str:
        """
        Get the LAN VRF associated EIGRP feature by ID for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param eigrp_id: EIGRP Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "eigrpId": eigrp_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp/{eigrpId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_service_vrf_and_routing_eigrp_feature_association(
        self, service_id: str, vrf_id: str, eigrp_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Replace the EIGRP feature for LAN VRF feature in service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param eigrp_id: Old EIGRP Feature ID
        :param payload: New EIGRP feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "eigrpId": eigrp_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp/{eigrpId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_service_vrf_and_routing_eigrp_association(
        self, service_id: str, vrf_id: str, eigrp_id: str, **kw
    ):
        """
        Delete the LAN VRF feature and EIGRP feature association for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param eigrp_id: EIGRP Feature ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "eigrpId": eigrp_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp/{eigrpId}",
            params=params,
            **kw,
        )
