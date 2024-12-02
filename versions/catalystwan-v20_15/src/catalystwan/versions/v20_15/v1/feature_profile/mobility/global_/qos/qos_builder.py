# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class QosBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/mobility/global/{globalId}/qos
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_qos_feature_for_global(self, global_id: str, **kw) -> str:
        """
        Get Qos Feature for Global feature profile

        :param global_id: Feature Profile ID
        :returns: str
        """
        params = {
            "globalId": global_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{globalId}/qos",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_qos_feature_for_global(self):
        class create_qos_feature_for_global_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, global_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create a Qos Feature for Global feature profile

                :param global_id: Feature Profile ID
                :param payload: Qos Feature
                :returns: str
                """
                params = {
                    "globalId": global_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/mobility/global/{globalId}/qos",
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

        return create_qos_feature_for_global_(self._request_adapter)

    def get_qos_feature_by_parcel_id_for_global(
        self, global_id: str, qos_id: str, **kw
    ) -> str:
        """
        Get Qos Feature by parcelId for Global feature profile

        :param global_id: Feature Profile ID
        :param qos_id: Feature ID
        :returns: str
        """
        params = {
            "globalId": global_id,
            "qosId": qos_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{globalId}/qos/{qosId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_qos_feature_for_global(self):
        class edit_qos_feature_for_global_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, global_id: str, qos_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Update a Qos Feature for Global feature profile

                :param global_id: Feature Profile ID
                :param qos_id: Feature ID
                :param payload: Qos Feature
                :returns: str
                """
                params = {
                    "globalId": global_id,
                    "qosId": qos_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/mobility/global/{globalId}/qos/{qosId}",
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

        return edit_qos_feature_for_global_(self._request_adapter)

    def delete_qos_feature_for_global(self, global_id: str, qos_id: str, **kw):
        """
        Delete a Qos Feature for Global feature profile

        :param global_id: Feature Profile ID
        :param qos_id: Feature ID
        :returns: None
        """
        params = {
            "globalId": global_id,
            "qosId": qos_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/mobility/global/{globalId}/qos/{qosId}",
            params=params,
            **kw,
        )
