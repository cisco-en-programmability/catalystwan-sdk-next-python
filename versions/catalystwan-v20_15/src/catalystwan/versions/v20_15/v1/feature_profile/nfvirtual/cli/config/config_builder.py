# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class ConfigBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/cli/{cliId}/config
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_nfvirtual_cli_parcel(self, cli_id: str, payload: Optional[str] = None, **kw) -> str:
        """
        Create CLI Profile Parcel for CLI feature profile

        :param cli_id: CLI Feature Profile ID
        :param payload: CLI Profile Parcel
        :returns: str
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/nfvirtual/cli/{cliId}/config",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_nfvirtual_cli_parcel(self, cli_id: str, config_id: str, **kw) -> str:
        """
        Get CLI Profile Parcels for CLI feature profile

        :param cli_id: CLI Feature Profile ID
        :param config_id: CLI Parcel ID
        :returns: str
        """
        params = {
            "cliId": cli_id,
            "configId": config_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/cli/{cliId}/config/{configId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_nfvirtual_cli_parcel(
        self, cli_id: str, config_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit CLI Profile Parcel for CLI feature profile

        :param cli_id: CLI Feature Profile ID
        :param config_id: CLI Parcel ID
        :param payload: CLI Profile Parcel
        :returns: str
        """
        params = {
            "cliId": cli_id,
            "configId": config_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/nfvirtual/cli/{cliId}/config/{configId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_nfvirtual_cli_parcel(self, cli_id: str, config_id: str, **kw):
        """
        Delete CLI Profile Parcel for CLI feature profile

        :param cli_id: CLI Feature Profile ID
        :param config_id: CLI Parcel ID
        :returns: None
        """
        params = {
            "cliId": cli_id,
            "configId": config_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/nfvirtual/cli/{cliId}/config/{configId}",
            params=params,
            **kw,
        )
