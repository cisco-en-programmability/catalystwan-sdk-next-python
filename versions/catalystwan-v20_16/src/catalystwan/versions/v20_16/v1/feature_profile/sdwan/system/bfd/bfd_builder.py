# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class BfdBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/system/bfd
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_bfd_profile_parcel_for_system(self, system_id: str, **kw) -> str:
        """
        Get Bfd Profile Parcels for System feature profile

        :param system_id: Feature Profile ID
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd",
            return_type=str,
            params=params,
            **kw,
        )

    def create_bfd_profile_parcel_for_system(
        self, system_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a Bfd Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param payload: Bfd Profile Parcel
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_bfd_profile_parcel_by_parcel_id_for_system(
        self, system_id: str, bfd_id: str, **kw
    ) -> str:
        """
        Get Bfd Profile Parcel by parcelId for System feature profile

        :param system_id: Feature Profile ID
        :param bfd_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "systemId": system_id,
            "bfdId": bfd_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd/{bfdId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_bfd_profile_parcel_for_system(
        self, system_id: str, bfd_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Bfd Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param bfd_id: Profile Parcel ID
        :param payload: Bfd Profile Parcel
        :returns: str
        """
        params = {
            "systemId": system_id,
            "bfdId": bfd_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd/{bfdId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_bfd_profile_parcel_for_system(self, system_id: str, bfd_id: str, **kw):
        """
        Delete a Bfd Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param bfd_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "systemId": system_id,
            "bfdId": bfd_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd/{bfdId}",
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
