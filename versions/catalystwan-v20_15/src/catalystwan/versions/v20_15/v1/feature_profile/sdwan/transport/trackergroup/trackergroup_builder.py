# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class TrackergroupBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/trackergroup
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_tracker_group_profile_parcel_for_transport(
        self, transport_id: str, **kw
    ) -> str:
        """
        Get TrackerGroup Profile Parcels for Transport feature profile

        :param transport_id: Feature Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_tracker_group_profile_parcel_for_transport(self):
        class create_tracker_group_profile_parcel_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, transport_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create a TrackerGroup Profile Parcel for Transport feature profile

                :param transport_id: Feature Profile ID
                :param payload: TrackerGroup Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return create_tracker_group_profile_parcel_for_transport_(self._request_adapter)

    def get_tracker_group_profile_parcel_by_parcel_id_for_transport(
        self, transport_id: str, trackergroup_id: str, **kw
    ) -> str:
        """
        Get TrackerGroup Profile Parcel by parcelId for Transport feature profile

        :param transport_id: Feature Profile ID
        :param trackergroup_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "trackergroupId": trackergroup_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup/{trackergroupId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_tracker_group_profile_parcel_for_transport(self):
        class edit_tracker_group_profile_parcel_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                trackergroup_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a TrackerGroup Profile Parcel for Transport feature profile

                :param transport_id: Feature Profile ID
                :param trackergroup_id: Profile Parcel ID
                :param payload: TrackerGroup Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "trackergroupId": trackergroup_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup/{trackergroupId}",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return edit_tracker_group_profile_parcel_for_transport_(self._request_adapter)

    def delete_tracker_group_profile_parcel_for_transport(
        self, transport_id: str, trackergroup_id: str, **kw
    ):
        """
        Delete a TrackerGroup Profile Parcel for Transport feature profile

        :param transport_id: Feature Profile ID
        :param trackergroup_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "trackergroupId": trackergroup_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup/{trackergroupId}",
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
