# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class MrfBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/system/mrf
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_mrf_profile_parcel_for_system(self, system_id: str, **kw) -> str:
        """
        Get Mrf Profile Parcels for System feature profile

        :param system_id: Feature Profile ID
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf",
            return_type=str,
            params=params,
            **kw,
        )

    def create_mrf_profile_parcel_for_system(
        self, system_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a Mrf Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param payload: Mrf Profile Parcel
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_mrf_profile_parcel_by_parcel_id_for_system(
        self, system_id: str, mrf_id: str, **kw
    ) -> str:
        """
        Get Mrf Profile Parcel by parcelId for System feature profile

        :param system_id: Feature Profile ID
        :param mrf_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "systemId": system_id,
            "mrfId": mrf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf/{mrfId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_mrf_profile_parcel_for_system(
        self, system_id: str, mrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Mrf Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param mrf_id: Profile Parcel ID
        :param payload: Mrf Profile Parcel
        :returns: str
        """
        params = {
            "systemId": system_id,
            "mrfId": mrf_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf/{mrfId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_mrf_profile_parcel_for_system(self, system_id: str, mrf_id: str, **kw):
        """
        Delete a Mrf Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param mrf_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "systemId": system_id,
            "mrfId": mrf_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf/{mrfId}",
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
