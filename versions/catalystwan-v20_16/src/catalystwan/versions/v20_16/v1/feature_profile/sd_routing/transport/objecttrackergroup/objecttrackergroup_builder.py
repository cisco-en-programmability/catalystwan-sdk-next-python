# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class ObjecttrackergroupBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_transport_object_tracker_group_features(self, transport_id: str, **kw) -> str:
        """
        Get all SD-Routing object tracker group features from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_transport_object_tracker_group_feature(
        self, transport_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing object tracker group feature from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param payload: SD-Routing object tracker group feature from a specific transport feature profile
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_transport_object_tracker_group_feature(
        self, transport_id: str, object_tracker_group_id: str, **kw
    ) -> str:
        """
        Get the SD-Routing object tracker group feature from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param object_tracker_group_id: Object Tracker Group ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "objectTrackerGroupId": object_tracker_group_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup/{objectTrackerGroupId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_transport_object_tracker_group_feature(
        self, transport_id: str, object_tracker_group_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing object tracker group feature from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param object_tracker_group_id: Object Tracker Group ID
        :param payload: SD-Routing object tracker group feature from a specific transport feature profile
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "objectTrackerGroupId": object_tracker_group_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup/{objectTrackerGroupId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_transport_object_tracker_group_feature(
        self, transport_id: str, object_tracker_group_id: str, **kw
    ):
        """
        Delete the SD-Routing object tracker group feature from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param object_tracker_group_id: Object Tracker Group ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "objectTrackerGroupId": object_tracker_group_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup/{objectTrackerGroupId}",
            params=params,
            **kw,
        )
