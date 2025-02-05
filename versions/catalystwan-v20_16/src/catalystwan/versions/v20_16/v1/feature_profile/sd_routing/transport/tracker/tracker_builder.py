# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class TrackerBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/tracker
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_tracker_profile_parcel_for_transport_1(self, transport_id: str, **kw) -> str:
        """
        Get Tracker Profile Features for Transport feature profile

        :param transport_id: Feature Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker",
            return_type=str,
            params=params,
            **kw,
        )

    def create_tracker_profile_parcel_for_transport_1(
        self, transport_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a Tracker Profile Feature for Transport feature profile

        :param transport_id: Feature Profile ID
        :param payload: Tracker Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_tracker_profile_parcel_by_parcel_id_for_transport_1(
        self, transport_id: str, tracker_id: str, **kw
    ) -> str:
        """
        Get Tracker Profile Feature by parcelId for Transport feature profile

        :param transport_id: Feature Profile ID
        :param tracker_id: Tracker Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "trackerId": tracker_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker/{trackerId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_tracker_profile_parcel_for_transport_1(
        self, transport_id: str, tracker_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Tracker Profile Feature for Transport feature profile

        :param transport_id: Feature Profile ID
        :param tracker_id: Tracker Profile Parcel ID
        :param payload: Tracker Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "trackerId": tracker_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker/{trackerId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_tracker_profile_parcel_for_transport_1(
        self, transport_id: str, tracker_id: str, **kw
    ):
        """
        Delete a Tracker Profile Feature for Transport feature profile

        :param transport_id: Feature Profile ID
        :param tracker_id: Tracker Profile Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "trackerId": tracker_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker/{trackerId}",
            params=params,
            **kw,
        )
