# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class BasicBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/mobility/global/basic
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_basic_profile_parcel_for_mobility(self, profile_id: str, **kw) -> str:
        """
        Get Basic Profile Parcels for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/basic",
            return_type=str,
            params=params,
            **kw,
        )

    def create_basic_profile_parcel_for_mobility(
        self, profile_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a Basic Profile Parcel for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param payload: Basic Profile Parcel
        :returns: str
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/basic",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_basic_profile_parcel_by_parcel_id_for_mobility(
        self, profile_id: str, parcel_id: str, **kw
    ) -> str:
        """
        Get Basic Profile Parcel by parcelId for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param parcel_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
            "parcelId": parcel_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/basic/{parcelId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_basic_profile_parcel_for_mobility(
        self, profile_id: str, parcel_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Basic Profile Parcel for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param parcel_id: Profile Parcel ID
        :param payload: Basic Profile Parcel
        :returns: str
        """
        params = {
            "profileId": profile_id,
            "parcelId": parcel_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/basic/{parcelId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_basic_profile_parcel_for_mobility(self, profile_id: str, parcel_id: str, **kw):
        """
        Delete a Basic Profile Parcel for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param parcel_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "profileId": profile_id,
            "parcelId": parcel_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/basic/{parcelId}",
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
