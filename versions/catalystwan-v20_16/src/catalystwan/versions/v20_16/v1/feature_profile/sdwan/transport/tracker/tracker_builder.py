# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class TrackerBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/tracker
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_tracker_profile_parcel_for_transport(self, transport_id: str, **kw) -> str:
        """
        Get Tracker Profile Parcels for Transport feature profile

        :param transport_id: Feature Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker",
            return_type=str,
            params=params,
            **kw,
        )

    def create_tracker_profile_parcel_for_transport(
        self, transport_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a Tracker Profile Parcel for Transport feature profile

        :param transport_id: Feature Profile ID
        :param payload: Tracker Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_tracker_profile_parcel_by_parcel_id_for_transport(
        self, transport_id: str, tracker_id: str, **kw
    ) -> str:
        """
        Get Tracker Profile Parcel by parcelId for Transport feature profile

        :param transport_id: Feature Profile ID
        :param tracker_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "trackerId": tracker_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker/{trackerId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_tracker_profile_parcel_for_transport(
        self, transport_id: str, tracker_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Tracker Profile Parcel for Transport feature profile

        :param transport_id: Feature Profile ID
        :param tracker_id: Profile Parcel ID
        :param payload: Tracker Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "trackerId": tracker_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker/{trackerId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_tracker_profile_parcel_for_transport(self, transport_id: str, tracker_id: str, **kw):
        """
        Delete a Tracker Profile Parcel for Transport feature profile

        :param transport_id: Feature Profile ID
        :param tracker_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "trackerId": tracker_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker/{trackerId}",
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
