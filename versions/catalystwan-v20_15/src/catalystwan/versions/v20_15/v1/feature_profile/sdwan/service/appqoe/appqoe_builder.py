# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class AppqoeBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/{serviceId}/appqoe
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_appqoe_profile_parcel_for_service(self, service_id: str, **kw) -> str:
        """
        Get Appqoe Profile Parcels for Service feature profile

        :param service_id: Feature Profile ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe",
            return_type=str,
            params=params,
            **kw,
        )

    def create_appqoe_profile_parcel_for_service(
        self, service_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a Appqoe Profile Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param payload: Appqoe Profile Parcel
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_appqoe_profile_parcel_by_parcel_id_for_service(
        self, service_id: str, appqoe_id: str, **kw
    ) -> str:
        """
        Get Appqoe Profile Parcel by parcelId for Service feature profile

        :param service_id: Feature Profile ID
        :param appqoe_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "appqoeId": appqoe_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe/{appqoeId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_appqoe_profile_parcel_for_service(
        self, service_id: str, appqoe_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Appqoe Profile Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param appqoe_id: Profile Parcel ID
        :param payload: Appqoe Profile Parcel
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "appqoeId": appqoe_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe/{appqoeId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_appqoe_profile_parcel_for_service(self, service_id: str, appqoe_id: str, **kw):
        """
        Delete a Appqoe Profile Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param appqoe_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "appqoeId": appqoe_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe/{appqoeId}",
            params=params,
            **kw,
        )
