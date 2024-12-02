# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class MulticloudConnectionBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/multicloud-connection
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_lan_vpn_profile_parcel_for_service_1(self, transport_id: str, **kw) -> str:
        """
        Get Lan Vpn Profile Parcels for Service feature profile

        :param transport_id: Feature Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_multi_cloud_connection_1(self):
        class create_multi_cloud_connection_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, transport_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Associate a MultiCloudConnection Parcel for transport feature profile

                :param transport_id: Feature Profile ID
                :param payload: MultiConnection Extension Payload for defining the multicloud connection to the cloud gateway
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection",
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

        return create_multi_cloud_connection_1_(self._request_adapter)

    def get_lan_vpn_profile_parcel_by_parcel_id_for_service_1(
        self, transport_id: str, multi_cloud_connection_id: str, **kw
    ) -> str:
        """
        Get Lan Vpn Profile Parcel by parcelId for Service feature profile

        :param transport_id: Feature Profile ID
        :param multi_cloud_connection_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "multiCloudConnectionId": multi_cloud_connection_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection/{multiCloudConnectionId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_multi_cloud_connection_1(self):
        class edit_multi_cloud_connection_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                multi_cloud_connection_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a multicloud connection parcel

                :param transport_id: Feature Profile ID
                :param multi_cloud_connection_id: Profile Parcel ID
                :param payload: Multicloud Connection Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "multiCloudConnectionId": multi_cloud_connection_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection/{multiCloudConnectionId}",
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

        return edit_multi_cloud_connection_1_(self._request_adapter)

    def delete_multi_cloud_connection_parcel_for_transport(
        self, transport_id: str, multi_cloud_connection_id: str, **kw
    ):
        """
        Delete a MultiCloud Connection Profile Parcel for Transport feature profile

        :param transport_id: Feature Profile ID
        :param multi_cloud_connection_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "multiCloudConnectionId": multi_cloud_connection_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection/{multiCloudConnectionId}",
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
