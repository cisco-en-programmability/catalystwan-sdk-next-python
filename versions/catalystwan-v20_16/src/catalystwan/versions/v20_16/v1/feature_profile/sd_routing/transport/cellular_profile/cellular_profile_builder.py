# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class CellularProfileBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/cellular-profile
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cellular_profile_parcel_for_transport(self, transport_id: str, **kw) -> str:
        """
        Get Cellular Profile Features for Transport feature profile

        :param transport_id: Feature Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-profile",
            return_type=str,
            params=params,
            **kw,
        )

    def create_cellular_profile_parcel_for_transport(
        self, transport_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a Cellular Profile Feature for Transport feature profile

        :param transport_id: Feature Profile ID
        :param payload: Cellular Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-profile",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_cellular_profile_parcel_by_parcel_id_for_transport(
        self, transport_id: str, cellular_profile_id: str, **kw
    ) -> str:
        """
        Get Cellular Profile Feature by parcelId for Transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_profile_id: Cellular Profile Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "cellularProfileId": cellular_profile_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-profile/{cellularProfileId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_cellular_profile_parcel_for_transport(
        self, transport_id: str, cellular_profile_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Cellular Profile Feature for Transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_profile_id: Cellular Profile Feature ID
        :param payload: Cellular Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "cellularProfileId": cellular_profile_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-profile/{cellularProfileId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_cellular_profile_parcel_for_transport(
        self, transport_id: str, cellular_profile_id: str, **kw
    ):
        """
        Delete a Cellular Profile Feature for Transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_profile_id: Cellular Profile Feature ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "cellularProfileId": cellular_profile_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-profile/{cellularProfileId}",
            params=params,
            **kw,
        )
