# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class LoggingBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/mobility/global/{profileId}/logging
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_logging_profile_feature_for_mobility(self, profile_id: str, **kw) -> str:
        """
        Get Logging Profile Features for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/logging",
            return_type=str,
            params=params,
            **kw,
        )

    def create_logging_profile_feature_for_mobility(
        self, profile_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a Logging Profile Feature for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param payload: Logging Profile Feature
        :returns: str
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/logging",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_logging_profile_feature_by_feature_id_for_mobility(
        self, profile_id: str, logging_id: str, **kw
    ) -> str:
        """
        Get Logging Profile Feature by parcelId for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param logging_id: Profile Feature ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
            "loggingId": logging_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/logging/{loggingId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_logging_profile_feature_for_mobility(
        self, profile_id: str, logging_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Logging Profile Feature for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param logging_id: Profile Feature ID
        :param payload: Logging Profile Feature
        :returns: str
        """
        params = {
            "profileId": profile_id,
            "loggingId": logging_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/logging/{loggingId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_logging_profile_feature_for_mobility(self, profile_id: str, logging_id: str, **kw):
        """
        Delete a Logging Profile Feature for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param logging_id: Profile Feature ID
        :returns: None
        """
        params = {
            "profileId": profile_id,
            "loggingId": logging_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/logging/{loggingId}",
            params=params,
            **kw,
        )
