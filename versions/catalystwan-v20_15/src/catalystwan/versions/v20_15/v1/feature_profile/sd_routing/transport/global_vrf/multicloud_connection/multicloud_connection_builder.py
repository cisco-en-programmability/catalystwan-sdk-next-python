# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface


class MulticloudConnectionBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/multicloud-connection
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def create_transport_global_vrf_and_multicloud_connection_parcel_association(self):
        class create_transport_global_vrf_and_multicloud_connection_parcel_association_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                vrf_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Associate a Global VRF parcel with a Multicloud Connection Parcel for transport feature profile

                :param transport_id: Feature Profile ID
                :param vrf_id: Global VRF Profile Parcel ID
                :param payload: Multicloud Connection Profile Parcel Id
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "vrfId": vrf_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/multicloud-connection",
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

        return (
            create_transport_global_vrf_and_multicloud_connection_parcel_association_(
                self._request_adapter
            )
        )
