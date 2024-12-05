# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class WirelesslanBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/wirelesslan
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_wirelesslan_profile_parcel_for_service(self, service_id: str, **kw) -> str:
        """
        Get Wirelesslan Profile Parcels for Service feature profile

        :param service_id: Feature Profile ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_wirelesslan_profile_parcel_for_service(self):
        class create_wirelesslan_profile_parcel_for_service_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, service_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Create a Wirelesslan Profile Parcel for Service feature profile

                :param service_id: Feature Profile ID
                :param payload: Wirelesslan Profile Parcel
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan",
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

        return create_wirelesslan_profile_parcel_for_service_(self._request_adapter)

    def get_wirelesslan_profile_parcel_by_parcel_id_for_service(
        self, service_id: str, wirelesslan_id: str, **kw
    ) -> str:
        """
        Get Wirelesslan Profile Parcel by parcelId for Service feature profile

        :param service_id: Feature Profile ID
        :param wirelesslan_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "wirelesslanId": wirelesslan_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan/{wirelesslanId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_wirelesslan_profile_parcel_for_service(self):
        class edit_wirelesslan_profile_parcel_for_service_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, service_id: str, wirelesslan_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Update a Wirelesslan Profile Parcel for Service feature profile

                :param service_id: Feature Profile ID
                :param wirelesslan_id: Profile Parcel ID
                :param payload: Wirelesslan Profile Parcel
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "wirelesslanId": wirelesslan_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan/{wirelesslanId}",
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

        return edit_wirelesslan_profile_parcel_for_service_(self._request_adapter)

    def delete_wirelesslan_profile_parcel_for_service(self, service_id: str, wirelesslan_id: str, **kw):
        """
        Delete a Wirelesslan Profile Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param wirelesslan_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "wirelesslanId": wirelesslan_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan/{wirelesslanId}",
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
