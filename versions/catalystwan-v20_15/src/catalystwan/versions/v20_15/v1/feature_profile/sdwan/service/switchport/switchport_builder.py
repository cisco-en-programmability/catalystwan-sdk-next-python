# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class SwitchportBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/switchport
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_switchport_parcels_for_service(self, service_id: str, **kw) -> str:
        """
        Get Switchport Parcels for service feature profile

        :param service_id: Feature Profile ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def cedge_service_profile_switchport_parcel_restful_resource(self):
        class cedge_service_profile_switchport_parcel_restful_resource_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, service_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create a switchport Parcel to a service feature profile

                :param service_id: Feature Profile ID
                :param payload: Feature Profile Id
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport",
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

        return cedge_service_profile_switchport_parcel_restful_resource_(
            self._request_adapter
        )

    def get_switchport_parcel_by_parcel_id_for_service(
        self, service_id: str, switchport_id: str, **kw
    ) -> str:
        """
        Get Switchport Parcel by switchportId for service feature profile

        :param service_id: Feature Profile ID
        :param switchport_id: Switchport Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "switchportId": switchport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport/{switchportId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_switchport_parcel_association_for_service(self):
        class edit_switchport_parcel_association_for_service_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                service_id: str,
                switchport_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a Switchport Parcel association for service feature profile

                :param service_id: Feature Profile ID
                :param switchport_id: Switchport ID
                :param payload: Switchport Profile Parcel
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "switchportId": switchport_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport/{switchportId}",
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

        return edit_switchport_parcel_association_for_service_(self._request_adapter)

    def delete_switchport_profile_parcel_for_service(
        self, service_id: str, switchport_id: str, **kw
    ):
        """
        Delete a Switchport Parcel for service feature profile

        :param service_id: Feature Profile ID
        :param switchport_id: Switchport Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "switchportId": switchport_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport/{switchportId}",
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
