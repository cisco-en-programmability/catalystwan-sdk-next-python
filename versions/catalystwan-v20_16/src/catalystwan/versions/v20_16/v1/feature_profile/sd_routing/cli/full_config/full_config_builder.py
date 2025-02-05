# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class FullConfigBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/cli/{cliId}/full-config
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_cli_config_group_features(self, cli_id: str, **kw) -> str:
        """
        Get the CLI Configuration by CLI profile ID

        :param cli_id: Cli Profile ID
        :returns: str
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_cli_config_group_feature(
        self, cli_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing CLI Configuration Group

        :param cli_id: Cli Profile ID
        :param payload: SD-Routing CLI Configuration Group
        :returns: str
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_cli_config_group_feature(self, cli_id: str, full_config_id: str, **kw) -> str:
        """
        Get the CLI Configuration by CLI profile ID and Config Feature ID

        :param cli_id: Cli Profile ID
        :param full_config_id: Full Config Feature ID
        :returns: str
        """
        params = {
            "cliId": cli_id,
            "fullConfigId": full_config_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config/{fullConfigId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_cli_config_group_feature(
        self, cli_id: str, full_config_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a SD-Routing CLI Configuration Group

        :param cli_id: Cli Profile ID
        :param full_config_id: Full Config Feature ID
        :param payload: SD-Routing CLI Configuration Group
        :returns: str
        """
        params = {
            "cliId": cli_id,
            "fullConfigId": full_config_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config/{fullConfigId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_cli_config_group_feature(self, cli_id: str, full_config_id: str, **kw):
        """
        Delete a SD-Routing CLI Configuration Group

        :param cli_id: Cli Profile ID
        :param full_config_id: Full Config Feature ID
        :returns: None
        """
        params = {
            "cliId": cli_id,
            "fullConfigId": full_config_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config/{fullConfigId}",
            params=params,
            **kw,
        )
