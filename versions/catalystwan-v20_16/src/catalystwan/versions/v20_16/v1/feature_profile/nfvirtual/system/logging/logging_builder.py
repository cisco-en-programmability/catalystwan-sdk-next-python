# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class LoggingBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/system/{systemId}/logging
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_nfvirtual_logging_parcel(
        self, system_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create Logging Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param payload: Logging config Profile Parcel
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/logging",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_nfvirtual_logging_parcel(self, system_id: str, logging_id: str, **kw) -> str:
        """
        Get Logging Profile Parcels for System feature profile

        :param system_id: Feature Profile ID
        :param logging_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "systemId": system_id,
            "loggingId": logging_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/logging/{loggingId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_nfvirtual_logging_parcel(
        self, system_id: str, logging_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a  Logging Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param logging_id: Profile Parcel ID
        :param payload: Logging Profile Parcel
        :returns: str
        """
        params = {
            "systemId": system_id,
            "loggingId": logging_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/logging/{loggingId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_nfvirtual_logging_parcel(self, system_id: str, logging_id: str, **kw):
        """
        Delete a Logging Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param logging_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "systemId": system_id,
            "loggingId": logging_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/logging/{loggingId}",
            params=params,
            **kw,
        )
