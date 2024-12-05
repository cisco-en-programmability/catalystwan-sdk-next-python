# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class ThousandeyesBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/other/thousandeyes
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_thousandeyes_profile_parcel_for_other(self, other_id: str, **kw) -> str:
        """
        Get Thousandeyes Profile Parcels for Other feature profile

        :param other_id: Feature Profile ID
        :returns: str
        """
        params = {
            "otherId": other_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_thousandeyes_profile_parcel_for_other(self):
        class create_thousandeyes_profile_parcel_for_other_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, other_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Create a Thousandeyes Profile Parcel for Other feature profile

                :param other_id: Feature Profile ID
                :param payload: Thousandeyes Profile Parcel
                :returns: str
                """
                params = {
                    "otherId": other_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes",
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

        return create_thousandeyes_profile_parcel_for_other_(self._request_adapter)

    def get_thousandeyes_profile_parcel_by_parcel_id_for_other(self, other_id: str, thousandeyes_id: str, **kw) -> str:
        """
        Get Thousandeyes Profile Parcel by parcelId for Other feature profile

        :param other_id: Feature Profile ID
        :param thousandeyes_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "otherId": other_id,
            "thousandeyesId": thousandeyes_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes/{thousandeyesId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_thousandeyes_profile_parcel_for_other(self):
        class edit_thousandeyes_profile_parcel_for_other_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, other_id: str, thousandeyes_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Update a Thousandeyes Profile Parcel for Other feature profile

                :param other_id: Feature Profile ID
                :param thousandeyes_id: Profile Parcel ID
                :param payload: Thousandeyes Profile Parcel
                :returns: str
                """
                params = {
                    "otherId": other_id,
                    "thousandeyesId": thousandeyes_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes/{thousandeyesId}",
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

        return edit_thousandeyes_profile_parcel_for_other_(self._request_adapter)

    def delete_thousandeyes_profile_parcel_for_other(self, other_id: str, thousandeyes_id: str, **kw):
        """
        Delete a Thousandeyes Profile Parcel for Other feature profile

        :param other_id: Feature Profile ID
        :param thousandeyes_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "otherId": other_id,
            "thousandeyesId": thousandeyes_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes/{thousandeyesId}",
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
