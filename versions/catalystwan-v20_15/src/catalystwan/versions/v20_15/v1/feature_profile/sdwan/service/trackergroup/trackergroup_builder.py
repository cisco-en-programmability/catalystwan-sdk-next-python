# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class TrackergroupBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/trackergroup
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_tracker_group_profile_parcel_for_service(self, service_id: str, **kw) -> str:
        """
        Get TrackerGroup Profile Parcels for Service feature profile

        :param service_id: Feature Profile ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup",
            return_type=str,
            params=params,
            **kw,
        )

    def create_tracker_group_profile_parcel_for_service(
        self, service_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a TrackerGroup Profile Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param payload: TrackerGroup Profile Parcel
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_tracker_group_profile_parcel_by_parcel_id_for_service(
        self, service_id: str, trackergroup_id: str, **kw
    ) -> str:
        """
        Get TrackerGroup Profile Parcel by parcelId for Service feature profile

        :param service_id: Feature Profile ID
        :param trackergroup_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "trackergroupId": trackergroup_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup/{trackergroupId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_tracker_group_profile_parcel_for_service(
        self, service_id: str, trackergroup_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a TrackerGroup Profile Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param trackergroup_id: Profile Parcel ID
        :param payload: TrackerGroup Profile Parcel
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "trackergroupId": trackergroup_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup/{trackergroupId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_tracker_group_profile_parcel_for_service(
        self, service_id: str, trackergroup_id: str, **kw
    ):
        """
        Delete a TrackerGroup Profile Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param trackergroup_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "trackergroupId": trackergroup_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup/{trackergroupId}",
            params=params,
            **kw,
        )

    @property
    def schema(self) -> SchemaBuilder:
        """
        The schema property
        """
        from .schema.schema_builder import SchemaBuilder

        return SchemaBuilder(self._request_adapter)
