# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class MulticloudConnectionBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/service/multicloud-connection
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_list_of_profile_parcels(self, service_id: str, **kw) -> str:
        """
        Get Multicloud Connection Profile Parcels for Service feature profile

        :param service_id: Feature Profile ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection",
            return_type=str,
            params=params,
            **kw,
        )

    def create_multi_cloud_connection(
        self, service_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Associate a MultiCloudConnection Parcel for service feature profile

        :param service_id: Feature Profile ID
        :param payload: MultiConnection Extension Payload for defining the multicloud connection to the cloud gateway
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_multi_cloud_connection(
        self, service_id: str, multi_cloud_connection_id: str, **kw
    ) -> str:
        """
        Get a multicloud connection parcel

        :param service_id: Feature Profile ID
        :param multi_cloud_connection_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "multiCloudConnectionId": multi_cloud_connection_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection/{multiCloudConnectionId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_multi_cloud_connection(
        self, service_id: str, multi_cloud_connection_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a multicloud connection parcel

        :param service_id: Feature Profile ID
        :param multi_cloud_connection_id: Profile Parcel ID
        :param payload: Multicloud Connection Profile Parcel
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "multiCloudConnectionId": multi_cloud_connection_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection/{multiCloudConnectionId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_multi_cloud_connection_parcel_for_service(
        self, service_id: str, multi_cloud_connection_id: str, **kw
    ):
        """
        Delete a MultiCloud Connection Profile Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param multi_cloud_connection_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "multiCloudConnectionId": multi_cloud_connection_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection/{multiCloudConnectionId}",
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
