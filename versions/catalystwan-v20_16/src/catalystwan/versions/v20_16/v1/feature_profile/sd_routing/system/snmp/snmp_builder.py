# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class SnmpBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/system/{systemId}/snmp
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_snmp_features(self, system_id: str, **kw) -> str:
        """
        Get all SD-Routing SNMP features from a specific system feature profile

        :param system_id: System Profile ID
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_snmp_feature(
        self, system_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing SNMP feature from a specific system feature profile

        :param system_id: System Profile ID
        :param payload: SD-Routing SNMP feature from a specific system feature profile
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_snmp_feature(self, system_id: str, snmp_id: str, **kw) -> str:
        """
        Get the SD-Routing SNMP feature from a specific system feature profile

        :param system_id: System Profile ID
        :param snmp_id: SNMP Feature ID
        :returns: str
        """
        params = {
            "systemId": system_id,
            "snmpId": snmp_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp/{snmpId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_snmp_feature(
        self, system_id: str, snmp_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing SNMP feature from a specific system feature profile

        :param system_id: System Profile ID
        :param snmp_id: SNMP Feature ID
        :param payload: SD-Routing SNMP feature from a specific system feature profile
        :returns: str
        """
        params = {
            "systemId": system_id,
            "snmpId": snmp_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp/{snmpId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_snmp_feature(self, system_id: str, snmp_id: str, **kw):
        """
        Delete the SD-Routing SNMP feature from a specific system feature profile

        :param system_id: System Profile ID
        :param snmp_id: SNMP Feature ID
        :returns: None
        """
        params = {
            "systemId": system_id,
            "snmpId": snmp_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/snmp/{snmpId}",
            params=params,
            **kw,
        )
