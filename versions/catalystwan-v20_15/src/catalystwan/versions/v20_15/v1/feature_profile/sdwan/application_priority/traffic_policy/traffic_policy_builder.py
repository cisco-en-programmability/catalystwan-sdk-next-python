# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface


class TrafficPolicyBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/traffic-policy
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def create_traffic_policy_profile_parcel_forapplication_priority(self):
        class create_traffic_policy_profile_parcel_forapplication_priority_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, application_priority_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create a Traffic Policy Profile Parcel for application-priority feature profile

                :param application_priority_id: Feature Profile ID
                :param payload: Traffic Policy Profile Parcel
                :returns: str
                """
                params = {
                    "applicationPriorityId": application_priority_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/traffic-policy",
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

        return create_traffic_policy_profile_parcel_forapplication_priority_(
            self._request_adapter
        )

    def get_traffic_policy_profile_parcel_by_parcel_id_forapplication_priority(
        self, application_priority_id: str, traffic_policy_id: str, **kw
    ) -> str:
        """
        Get Traffic Policy Profile Parcel by parcelId for application-priority feature profile

        :param application_priority_id: Feature Profile ID
        :param traffic_policy_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "applicationPriorityId": application_priority_id,
            "trafficPolicyId": traffic_policy_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/traffic-policy/{trafficPolicyId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_traffic_policy_profile_parcel_forapplication_priority(self):
        class edit_traffic_policy_profile_parcel_forapplication_priority_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                application_priority_id: str,
                traffic_policy_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a Traffic Policy Profile Parcel for application-priority feature profile

                :param application_priority_id: Feature Profile ID
                :param traffic_policy_id: Profile Parcel ID
                :param payload: Traffic Policy Profile Parcel
                :returns: str
                """
                params = {
                    "applicationPriorityId": application_priority_id,
                    "trafficPolicyId": traffic_policy_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/traffic-policy/{trafficPolicyId}",
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

        return edit_traffic_policy_profile_parcel_forapplication_priority_(
            self._request_adapter
        )

    def delete_traffic_policy_profile_parcel_forapplication_priority(
        self, application_priority_id: str, traffic_policy_id: str, **kw
    ):
        """
        Delete a Traffic Policy Profile Parcel for application-priority feature profile

        :param application_priority_id: Feature Profile ID
        :param traffic_policy_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "applicationPriorityId": application_priority_id,
            "trafficPolicyId": traffic_policy_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/traffic-policy/{trafficPolicyId}",
            params=params,
            **kw,
        )
