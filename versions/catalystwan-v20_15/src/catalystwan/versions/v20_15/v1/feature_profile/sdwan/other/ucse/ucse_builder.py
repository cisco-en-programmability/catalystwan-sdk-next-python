# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class UcseBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/other/{otherId}/ucse
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_ucse_profile_feature_for_other(self, other_id: str, **kw) -> str:
        """
        Get Ucse Profile feature for Other feature profile

        :param other_id: Feature Profile ID
        :returns: str
        """
        params = {
            "otherId": other_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse",
            return_type=str,
            params=params,
            **kw,
        )

    def create_ucse_profile_feature_for_other(
        self, other_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a Ucse Profile feature for Other feature profile

        :param other_id: Feature Profile ID
        :param payload: Ucse Profile feature
        :returns: str
        """
        params = {
            "otherId": other_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_ucse_profile_feature_by_id_f_feature_for_other(
        self, other_id: str, ucse_id: str, **kw
    ) -> str:
        """
        Get Ucse Profile feature by FeatureId for Other feature profile

        :param other_id: Feature Profile ID
        :param ucse_id: Profile feature ID
        :returns: str
        """
        params = {
            "otherId": other_id,
            "ucseId": ucse_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse/{ucseId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_ucse_profile_feature_for_other(
        self, other_id: str, ucse_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Ucse Profile feature for Other feature profile

        :param other_id: Feature Profile ID
        :param ucse_id: Profile feature ID
        :param payload: Ucse Profile feature
        :returns: str
        """
        params = {
            "otherId": other_id,
            "ucseId": ucse_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse/{ucseId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_ucse_profile_feature_for_other(self, other_id: str, ucse_id: str, **kw):
        """
        Delete a Ucse Profile feature for Other feature profile

        :param other_id: Feature Profile ID
        :param ucse_id: Profile feature ID
        :returns: None
        """
        params = {
            "otherId": other_id,
            "ucseId": ucse_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse/{ucseId}",
            params=params,
            **kw,
        )
