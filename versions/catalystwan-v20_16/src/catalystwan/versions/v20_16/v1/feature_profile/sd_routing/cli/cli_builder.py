# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .config.config_builder import ConfigBuilder
    from .features.features_builder import FeaturesBuilder
    from .full_config.full_config_builder import FullConfigBuilder
    from .ios_config.ios_config_builder import IosConfigBuilder


class CliBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/cli
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_cli_feature_profiles(
        self, offset: Optional[int] = None, limit: Optional[int] = 0, **kw
    ) -> Any:
        """
        Get all SD-Routing CLI Feature Profiles

        :param offset: Pagination offset
        :param limit: Pagination limit
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sd-routing/cli", params=params, **kw
        )

    def create_sdrouting_cli_feature_profile(self, payload: Optional[str] = None, **kw) -> str:
        """
        Create a SD-Routing CLI Feature Profile

        :param payload: SD-Routing CLI Feature Profile
        :returns: str
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/cli",
            return_type=str,
            payload=payload,
            **kw,
        )

    def get_sdrouting_cli_feature_profile(self, cli_id: str, **kw) -> Any:
        """
        Get a SD-Routing CLI Feature Profile

        :param cli_id: Cli Profile Id
        :returns: Any
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sd-routing/cli/{cliId}", params=params, **kw
        )

    def edit_sdrouting_cli_feature_profile(
        self, cli_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a SD-Routing CLI Feature Profile

        :param cli_id: Cli Profile Id
        :param payload: SD-Routing CLI Feature Profile
        :returns: str
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/cli/{cliId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_cli_feature_profile(self, cli_id: str, **kw):
        """
        Delete a SD-Routing CLI Feature Profile

        :param cli_id: Cli Profile Id
        :returns: None
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/v1/feature-profile/sd-routing/cli/{cliId}", params=params, **kw
        )

    @property
    def config(self) -> ConfigBuilder:
        """
        The config property
        """
        from .config.config_builder import ConfigBuilder

        return ConfigBuilder(self._request_adapter)

    @property
    def features(self) -> FeaturesBuilder:
        """
        The features property
        """
        from .features.features_builder import FeaturesBuilder

        return FeaturesBuilder(self._request_adapter)

    @property
    def full_config(self) -> FullConfigBuilder:
        """
        The full-config property
        """
        from .full_config.full_config_builder import FullConfigBuilder

        return FullConfigBuilder(self._request_adapter)

    @property
    def ios_config(self) -> IosConfigBuilder:
        """
        The ios-config property
        """
        from .ios_config.ios_config_builder import IosConfigBuilder

        return IosConfigBuilder(self._request_adapter)
