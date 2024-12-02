# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import CellularProfile, EditCellularProfileParcelForMobilityPutRequest


class CellularBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/mobility/global/{profileId}/cellular
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cellular_profile_parcel_list_for_mobility(
        self, profile_id: str, **kw
    ) -> str:
        """
        Get an Mobility Cellular Profile Parcel list for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/cellular",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_cellular_profile_parcel_for_mobility(self):
        class create_cellular_profile_parcel_for_mobility_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, profile_id: str, payload: Optional[CellularProfile] = None, **kw
            ) -> str:
                """
                Create an cellular Profile Parcel for Mobility Global Feature Profile

                :param profile_id: Feature Profile ID
                :param payload: Cellular Profile Parcel
                :returns: str
                """
                params = {
                    "profileId": profile_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/mobility/global/{profileId}/cellular",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> CellularProfile:
                return CellularProfile(*args, **kwargs)

            @property
            def payload_model(self) -> Type[CellularProfile]:
                return CellularProfile

        return create_cellular_profile_parcel_for_mobility_(self._request_adapter)

    def get_cellular_profile_parcel_for_mobility(
        self, profile_id: str, cellular_id: str, **kw
    ) -> str:
        """
        Get an Mobility Cellular Profile Parcel for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param cellular_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
            "cellularId": cellular_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/cellular/{cellularId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_cellular_profile_parcel_for_mobility(self):
        class edit_cellular_profile_parcel_for_mobility_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                profile_id: str,
                cellular_id: str,
                payload: Optional[
                    EditCellularProfileParcelForMobilityPutRequest
                ] = None,
                **kw,
            ):
                """
                Edit an Cellular Profile Parcel for Mobility Global Feature Profile

                :param profile_id: Feature Profile ID
                :param cellular_id: Profile Parcel ID
                :param payload: Cellular Profile Parcel
                :returns: None
                """
                params = {
                    "profileId": profile_id,
                    "cellularId": cellular_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/mobility/global/{profileId}/cellular/{cellularId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(
                self, *args, **kwargs
            ) -> EditCellularProfileParcelForMobilityPutRequest:
                return EditCellularProfileParcelForMobilityPutRequest(*args, **kwargs)

            @property
            def payload_model(
                self,
            ) -> Type[EditCellularProfileParcelForMobilityPutRequest]:
                return EditCellularProfileParcelForMobilityPutRequest

        return edit_cellular_profile_parcel_for_mobility_(self._request_adapter)

    def delete_a_cellular_profile_parcel_for_mobility(
        self, profile_id: str, cellular_id: str, **kw
    ):
        """
        Delete a Cellular Profile Parcel for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param cellular_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "profileId": profile_id,
            "cellularId": cellular_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/cellular/{cellularId}",
            params=params,
            **kw,
        )
