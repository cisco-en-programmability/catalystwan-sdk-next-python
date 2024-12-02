# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class LanBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/networks/{networksId}/lan
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def create_nfvirtual_lan_parcel(self):
        class create_nfvirtual_lan_parcel_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, networks_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create LAN Profile Parcel for Networks feature profile

                :param networks_id: Feature Profile ID
                :param payload: LAN config Profile Parcel
                :returns: str
                """
                params = {
                    "networksId": networks_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/lan",
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

        return create_nfvirtual_lan_parcel_(self._request_adapter)

    def get_nfvirtual_lan_parcel(self, networks_id: str, lan_id: str, **kw) -> str:
        """
        Get LAN Profile Parcels for Networks feature profile

        :param networks_id: Feature Profile ID
        :param lan_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "networksId": networks_id,
            "lanId": lan_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/lan/{lanId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_nfvirtual_lan_parcel(self):
        class edit_nfvirtual_lan_parcel_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, networks_id: str, lan_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Edit a  LAN Profile Parcel for networks feature profile

                :param networks_id: Feature Profile ID
                :param lan_id: Profile Parcel ID
                :param payload: LAN Profile Parcel
                :returns: str
                """
                params = {
                    "networksId": networks_id,
                    "lanId": lan_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/lan/{lanId}",
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

        return edit_nfvirtual_lan_parcel_(self._request_adapter)

    def delete_nfvirtual_lan_parcel(self, networks_id: str, lan_id: str, **kw):
        """
        Delete a LAN Profile Parcel for Networks feature profile

        :param networks_id: Feature Profile ID
        :param lan_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "networksId": networks_id,
            "lanId": lan_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/lan/{lanId}",
            params=params,
            **kw,
        )
