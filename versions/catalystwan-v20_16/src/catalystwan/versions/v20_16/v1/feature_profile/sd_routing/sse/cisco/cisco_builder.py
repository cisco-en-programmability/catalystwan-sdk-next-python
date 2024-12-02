# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class CiscoBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/sse/{sseId}/cisco
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cisco_sse_feature_for_sse(self, sse_id: str, **kw) -> str:
        """
        Get Cisco Sse feature list for Sse feature profile

        :param sse_id: Feature Profile ID
        :returns: str
        """
        params = {
            "sseId": sse_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco",
            return_type=str,
            params=params,
            **kw,
        )

    def create_cisco_sse_feature_for_sse(
        self, sse_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create Cisco Sse feature for sse feature profile type

        :param sse_id: Feature Profile ID
        :param payload: Cisco Sse feature
        :returns: str
        """
        params = {
            "sseId": sse_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_cisco_sse_feature_by_feature_id_for_sse(
        self, sse_id: str, cisco_sse_id: str, **kw
    ) -> str:
        """
        Get Cisco SSE Profile Feature by feature Id

        :param sse_id: Feature Profile ID
        :param cisco_sse_id: Feature ID
        :returns: str
        """
        params = {
            "sseId": sse_id,
            "ciscoSseId": cisco_sse_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco/{ciscoSseId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_cisco_sse_feature(
        self, sse_id: str, cisco_sse_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Cisco Sse feature

        :param sse_id: Feature Profile ID
        :param cisco_sse_id: Feature ID
        :param payload: Cisco Sse feature
        :returns: str
        """
        params = {
            "sseId": sse_id,
            "ciscoSseId": cisco_sse_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco/{ciscoSseId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_cisco_sse_feature(self, sse_id: str, cisco_sse_id: str, **kw):
        """
        Delete a Cisco Sse Feature

        :param sse_id: Feature Profile ID
        :param cisco_sse_id: Feature ID
        :returns: None
        """
        params = {
            "sseId": sse_id,
            "ciscoSseId": cisco_sse_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco/{ciscoSseId}",
            params=params,
            **kw,
        )
