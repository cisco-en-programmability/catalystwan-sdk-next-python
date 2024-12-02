# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class SnmpBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/system/{systemId}/snmp
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_nfvirtual_snmp_parcel(
        self, system_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create SNMP Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param payload: SNMP config Profile Parcel
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/snmp",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_nfvirtual_snmp_parcel(self, system_id: str, snmp_id: str, **kw) -> str:
        """
        Get SNMP Profile Parcels for System feature profile

        :param system_id: Feature Profile ID
        :param snmp_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "systemId": system_id,
            "snmpId": snmp_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/snmp/{snmpId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_nfvirtual_snmp_parcel(
        self, system_id: str, snmp_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a  SNMP Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param snmp_id: Profile Parcel ID
        :param payload: SNMP Profile Parcel
        :returns: str
        """
        params = {
            "systemId": system_id,
            "snmpId": snmp_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/snmp/{snmpId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_nfvirtual_snmp_parcel(self, system_id: str, snmp_id: str, **kw):
        """
        Delete a SNMP Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param snmp_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "systemId": system_id,
            "snmpId": snmp_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/snmp/{snmpId}",
            params=params,
            **kw,
        )
