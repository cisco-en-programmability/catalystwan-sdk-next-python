# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class IosConfigBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/cli/{cliId}/ios-config
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_ios_c_lassic_cli_add_on_features(self, cli_id: str, **kw) -> str:
        """
        SD-Routing Ios Classic CLI Add-On Features for CLI Feature Profile for GET requests

        :param cli_id: Feature Profile ID
        :returns: str
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_ios_classic_cli_add_on_feature(
        self, cli_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        SD-Routing Ios Classic CLI Add-On Feature for CLI Feature Profile for POST requests

        :param cli_id: Feature Profile ID
        :param payload: SD-Routing Ios Classic CLI Add-On Feature for CLI Feature Profile
        :returns: str
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_ios_classic_cli_add_on_feature(
        self, cli_id: str, ios_config_id: str, **kw
    ) -> str:
        """
        SD-Routing Ios Classic CLI Add-On Feature for CLI Feature Profile for GET requests

        :param cli_id: Feature Profile ID
        :param ios_config_id: Ios Config ID
        :returns: str
        """
        params = {
            "cliId": cli_id,
            "iosConfigId": ios_config_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config/{iosConfigId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_ios_classic_cli_add_on_feature(
        self, cli_id: str, ios_config_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        SD-Routing Ios Classic CLI Add-On Feature for CLI Feature Profile for PUT requests

        :param cli_id: Feature Profile ID
        :param ios_config_id: Ios Config ID
        :param payload: SD-Routing Ios Classic CLI Add-On Feature for CLI Feature Profile
        :returns: str
        """
        params = {
            "cliId": cli_id,
            "iosConfigId": ios_config_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config/{iosConfigId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_ios_classic_cli_add_on_feature(
        self, cli_id: str, ios_config_id: str, **kw
    ):
        """
        Delete a SD-Routing Ios Classic CLI Add-On Feature for CLI Feature Profile

        :param cli_id: Feature Profile ID
        :param ios_config_id: Ios Config ID
        :returns: None
        """
        params = {
            "cliId": cli_id,
            "iosConfigId": ios_config_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config/{iosConfigId}",
            params=params,
            **kw,
        )
