# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface


class QosPolicyBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/qos-policy
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def create_policy_application_profile_parcel(self):
        class create_policy_application_profile_parcel_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, application_priority_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create QOS Policy feature for application-priority feature profile

                :param application_priority_id: Application priority id
                :param payload: QOS Profile Parcel
                :returns: str
                """
                params = {
                    "applicationPriorityId": application_priority_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/qos-policy",
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

        return create_policy_application_profile_parcel_(self._request_adapter)

    def get_policy_application_profile_parcel(
        self, application_priority_id: str, qos_policy_id: str, **kw
    ) -> str:
        """
        Get QOS Policy feature for application-priority feature profile

        :param application_priority_id: Application priority id
        :param qos_policy_id: Qos policy id
        :returns: str
        """
        params = {
            "applicationPriorityId": application_priority_id,
            "qosPolicyId": qos_policy_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/qos-policy/{qosPolicyId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_policy_application_profile_parcel(self):
        class edit_policy_application_profile_parcel_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                application_priority_id: str,
                qos_policy_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Edit QOS Policy feature for application-priority feature profile

                :param application_priority_id: Application priority id
                :param qos_policy_id: Qos policy id
                :param payload: QOS Profile Parcel
                :returns: str
                """
                params = {
                    "applicationPriorityId": application_priority_id,
                    "qosPolicyId": qos_policy_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/qos-policy/{qosPolicyId}",
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

        return edit_policy_application_profile_parcel_(self._request_adapter)

    def delete_policy_application_profile_parcel(
        self, application_priority_id: str, qos_policy_id: str, **kw
    ):
        """
        Delete QOS Policy feature for application-priority feature profile

        :param application_priority_id: Application priority id
        :param qos_policy_id: Qos policy id
        :returns: None
        """
        params = {
            "applicationPriorityId": application_priority_id,
            "qosPolicyId": qos_policy_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/qos-policy/{qosPolicyId}",
            params=params,
            **kw,
        )
