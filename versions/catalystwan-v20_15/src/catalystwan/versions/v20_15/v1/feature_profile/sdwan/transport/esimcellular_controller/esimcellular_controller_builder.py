# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface


class EsimcellularControllerBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_esim_cellular_controller_profile_feature_for_transport(
        self, transport_id: str, **kw
    ) -> str:
        """
        Get eSim Cellular Controller Features for Transport feature profile

        :param transport_id: Feature Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_esim_cellular_controller_profile_feature_for_transport(self):
        class create_esim_cellular_controller_profile_feature_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, transport_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create a eSim Cellular Controller Feature for Transport feature profile

                :param transport_id: Feature Profile ID
                :param payload: eSim Cellular Controller Feature
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller",
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

        return create_esim_cellular_controller_profile_feature_for_transport_(
            self._request_adapter
        )

    def get_esim_cellular_controller_profile_feature_by_feature_id_for_transport(
        self, transport_id: str, esim_cellular_controller_id: str, **kw
    ) -> str:
        """
        Get eSim Cellular Controller Feature by Feature Id for Transport feature profile

        :param transport_id: Feature Profile ID
        :param esim_cellular_controller_id: Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "esimCellularControllerId": esim_cellular_controller_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller/{esimCellularControllerId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_esim_cellular_controller_profile_feature_for_transport(self):
        class edit_esim_cellular_controller_profile_feature_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                esim_cellular_controller_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a eSim Cellular Controller Feature for Transport feature profile

                :param transport_id: Feature Profile ID
                :param esim_cellular_controller_id: Feature ID
                :param payload: EsimCellular Controller Feature
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "esimCellularControllerId": esim_cellular_controller_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller/{esimCellularControllerId}",
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

        return edit_esim_cellular_controller_profile_feature_for_transport_(
            self._request_adapter
        )

    def delete_esim_cellular_controller_profile_feature_for_transport(
        self, transport_id: str, esim_cellular_controller_id: str, **kw
    ):
        """
        Delete a eSim Cellular Controller Feature for Transport feature profile

        :param transport_id: Feature Profile ID
        :param esim_cellular_controller_id: Feature ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "esimCellularControllerId": esim_cellular_controller_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/esimcellular-controller/{esimCellularControllerId}",
            params=params,
            **kw,
        )
