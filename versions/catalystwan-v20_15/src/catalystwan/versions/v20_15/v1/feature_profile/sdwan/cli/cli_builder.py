# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .config.config_builder import ConfigBuilder
    from .features.features_builder import FeaturesBuilder


class CliBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/cli
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdwan_feature_profiles_by_family_and_type_1(
        self, offset: Optional[int] = None, limit: Optional[int] = 0, **kw
    ) -> Any:
        """
        Get all SDWAN Feature Profiles with giving Family and profile type

        :param offset: Pagination offset
        :param limit: Pagination limit
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sdwan/cli", params=params, **kw
        )

    def create_sdwan_feature_profile(self, payload: Optional[str] = None, **kw) -> str:
        """
        Create a SDWAN  Feature Profile with profile type

        :param payload: SDWAN Feature profile
        :returns: str
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/cli",
            return_type=str,
            payload=payload,
            **kw,
        )

    def get_sdwan_feature_profile_by_profile_id(self, cli_id: str, **kw) -> Any:
        """
        Get a SDWAN Feature Profile with Cli profile type

        :param cli_id: Feature Profile Id
        :returns: Any
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sdwan/cli/{cliId}", params=params, **kw
        )

    def edit_sdwan_feature_profile(self, cli_id: str, payload: Optional[str] = None, **kw) -> str:
        """
        Edit a SDWAN Feature Profile

        :param cli_id: Feature Profile Id
        :param payload: SDWAN Feature profile
        :returns: str
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/cli/{cliId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdwan_feature_profile_for_cli(self, cli_id: str, **kw):
        """
        Delete Feature Profile

        :param cli_id: Cli id
        :returns: None
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/v1/feature-profile/sdwan/cli/{cliId}", params=params, **kw
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
