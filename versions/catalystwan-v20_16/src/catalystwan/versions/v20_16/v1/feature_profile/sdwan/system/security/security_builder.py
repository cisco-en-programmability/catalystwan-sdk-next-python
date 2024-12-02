# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class SecurityBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/system/{systemId}/security
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_security_for_system(self, system_id: str, **kw) -> str:
        """
        Get Security for System feature profile

        :param system_id: Feature Profile ID
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/security",
            return_type=str,
            params=params,
            **kw,
        )

    def create_security_for_system(
        self, system_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create Security for System feature profile

        :param system_id: Feature Profile ID
        :param payload: Security Feature
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/security",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_security_by_security_id_for_system(self, system_id: str, security_id: str, **kw) -> str:
        """
        Get Security by securityId for System feature profile

        :param system_id: Feature Profile ID
        :param security_id: Security ID
        :returns: str
        """
        params = {
            "systemId": system_id,
            "securityId": security_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/security/{securityId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_security_for_system(
        self, system_id: str, security_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update Security for System feature profile

        :param system_id: Feature Profile ID
        :param security_id: Security ID
        :param payload: Security Feature
        :returns: str
        """
        params = {
            "systemId": system_id,
            "securityId": security_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/security/{securityId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_security_for_system(self, system_id: str, security_id: str, **kw):
        """
        Delete Security for System feature profile

        :param system_id: Feature Profile ID
        :param security_id: Security ID
        :returns: None
        """
        params = {
            "systemId": system_id,
            "securityId": security_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/security/{securityId}",
            params=params,
            **kw,
        )
