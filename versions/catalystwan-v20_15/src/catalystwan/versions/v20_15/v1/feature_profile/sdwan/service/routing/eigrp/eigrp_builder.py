# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class EigrpBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_routing_eigrp_profile_parcel_for_service(self, service_id: str, **kw) -> str:
        """
        Get Routing Eigrp Profile Features for Service feature profile

        :param service_id: Feature Profile ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp",
            return_type=str,
            params=params,
            **kw,
        )

    def create_routing_eigrp_profile_parcel_for_service(
        self, service_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a Routing Eigrp Profile Feature for Service feature profile

        :param service_id: Feature Profile ID
        :param payload: Routing Eigrp Profile Feature
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_routing_eigrp_profile_parcel_by_parcel_id_for_service(
        self, service_id: str, eigrp_id: str, **kw
    ) -> str:
        """
        Get Routing Eigrp Profile Feature by parcelId for Service feature profile

        :param service_id: Feature Profile ID
        :param eigrp_id: Profile Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "eigrpId": eigrp_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp/{eigrpId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_routing_eigrp_profile_parcel_for_service(
        self, service_id: str, eigrp_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Routing Eigrp Profile Feature for Service feature profile

        :param service_id: Feature Profile ID
        :param eigrp_id: Profile Feature ID
        :param payload: Routing Eigrp Profile Feature
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "eigrpId": eigrp_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp/{eigrpId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_routing_eigrp_profile_parcel_for_service(self, service_id: str, eigrp_id: str, **kw):
        """
        Delete a Routing Eigrp Profile Feature for Service feature profile

        :param service_id: Feature Profile ID
        :param eigrp_id: Profile Feature ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "eigrpId": eigrp_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp/{eigrpId}",
            params=params,
            **kw,
        )
