# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class LoggingBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/system/logging
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_logging_profile_parcel_for_system(self, system_id: str, **kw) -> str:
        """
        Get Logging Profile Parcels for System feature profile

        :param system_id: Feature Profile ID
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/logging",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_logging_profile_parcel_for_system(self):
        class create_logging_profile_parcel_for_system_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, system_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Create a Logging Profile Parcel for System feature profile

                :param system_id: Feature Profile ID
                :param payload: Logging Profile Parcel
                :returns: str
                """
                params = {
                    "systemId": system_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/system/{systemId}/logging",
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

        return create_logging_profile_parcel_for_system_(self._request_adapter)

    def get_logging_profile_parcel_by_parcel_id_for_system(self, system_id: str, logging_id: str, **kw) -> str:
        """
        Get Logging Profile Parcel by parcelId for System feature profile

        :param system_id: Feature Profile ID
        :param logging_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "systemId": system_id,
            "loggingId": logging_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/logging/{loggingId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_logging_profile_parcel_for_system(self):
        class edit_logging_profile_parcel_for_system_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, system_id: str, logging_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Update a Logging Profile Parcel for System feature profile

                :param system_id: Feature Profile ID
                :param logging_id: Profile Parcel ID
                :param payload: Logging Profile Parcel
                :returns: str
                """
                params = {
                    "systemId": system_id,
                    "loggingId": logging_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/system/{systemId}/logging/{loggingId}",
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

        return edit_logging_profile_parcel_for_system_(self._request_adapter)

    def delete_logging_profile_parcel_for_system(self, system_id: str, logging_id: str, **kw):
        """
        Delete a Logging Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param logging_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "systemId": system_id,
            "loggingId": logging_id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/v1/feature-profile/sdwan/system/{systemId}/logging/{loggingId}", params=params, **kw
        )

    @property
    def schema(self) -> SchemaBuilder:
        """
        The schema property
        """
        from .schema.schema_builder import SchemaBuilder

        return SchemaBuilder(self._request_adapter)
