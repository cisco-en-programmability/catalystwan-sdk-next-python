# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class CybervisionBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/other/{otherId}/cybervision
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cybervision_profile_feature_for_other(self, other_id: str, **kw) -> str:
        """
        Get Cybervision Profile feature for Other feature profile

        :param other_id: Feature Profile ID
        :returns: str
        """
        params = {
            "otherId": other_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision",
            return_type=str,
            params=params,
            **kw,
        )

    def create_cybervision_profile_feature_for_other(
        self, other_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a Cybervision Profile feature for Other feature profile

        :param other_id: Feature Profile ID
        :param payload: Cybervision Profile feature
        :returns: str
        """
        params = {
            "otherId": other_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_cybervision_profile_feature_by_feature_id_for_other(
        self, other_id: str, cybervision_id: str, **kw
    ) -> str:
        """
        Get Cybervision Profile feature by FeatureId for Other feature profile

        :param other_id: Feature Profile ID
        :param cybervision_id: Profile feature ID
        :returns: str
        """
        params = {
            "otherId": other_id,
            "cybervisionId": cybervision_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision/{cybervisionId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_cybervision_profile_feature_for_other(
        self, other_id: str, cybervision_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Cybervision Profile feature for Other feature profile

        :param other_id: Feature Profile ID
        :param cybervision_id: Profile feature ID
        :param payload: Cybervision Profile feature
        :returns: str
        """
        params = {
            "otherId": other_id,
            "cybervisionId": cybervision_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision/{cybervisionId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_cybervision_profile_feature_for_other(
        self, other_id: str, cybervision_id: str, **kw
    ):
        """
        Delete a Cybervision Profile feature for Other feature profile

        :param other_id: Feature Profile ID
        :param cybervision_id: Profile feature ID
        :returns: None
        """
        params = {
            "otherId": other_id,
            "cybervisionId": cybervision_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision/{cybervisionId}",
            params=params,
            **kw,
        )
