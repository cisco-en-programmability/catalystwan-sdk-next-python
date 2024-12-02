# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class EsimcellularProfileBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_esim_cellular_profile_profile_feature_for_transport(
        self, transport_id: str, **kw
    ) -> str:
        """
        Get EsimCellular Profile Features for Transport feature profile

        :param transport_id: Feature Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_esim_cellular_profile_profile_feature_for_transport(self):
        class create_esim_cellular_profile_profile_feature_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, transport_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create a EsimCellular Profile Feature for Transport feature profile

                :param transport_id: Feature Profile ID
                :param payload: EsimCellular Profile Feature
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile",
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

        return create_esim_cellular_profile_profile_feature_for_transport_(
            self._request_adapter
        )

    def get_esim_cellular_profile_by_feature_id_for_transport(
        self, transport_id: str, esim_cellular_profile_id: str, **kw
    ) -> str:
        """
        Get EsimCellular Profile Feature by Feature Id for Transport feature profile

        :param transport_id: Feature Profile ID
        :param esim_cellular_profile_id: Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "esimCellularProfileId": esim_cellular_profile_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile/{esimCellularProfileId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_esim_cellular_profile_profile_feature_for_transport(self):
        class edit_esim_cellular_profile_profile_feature_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                esim_cellular_profile_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a EsimCellular Profile Feature for Transport feature profile

                :param transport_id: Feature Profile ID
                :param esim_cellular_profile_id: Feature ID
                :param payload: EsimCellular Profile Feature
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "esimCellularProfileId": esim_cellular_profile_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile/{esimCellularProfileId}",
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

        return edit_esim_cellular_profile_profile_feature_for_transport_(
            self._request_adapter
        )

    def delete_esim_cellular_profile_profile_feature_for_transport(
        self, transport_id: str, esim_cellular_profile_id: str, **kw
    ):
        """
        Delete a EsimCellular Profile Feature for Transport feature profile

        :param transport_id: Feature Profile ID
        :param esim_cellular_profile_id: Feature ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "esimCellularProfileId": esim_cellular_profile_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-profile/{esimCellularProfileId}",
            params=params,
            **kw,
        )
