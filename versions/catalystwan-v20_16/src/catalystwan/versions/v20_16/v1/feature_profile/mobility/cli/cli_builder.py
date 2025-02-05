# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .config.config_builder import ConfigBuilder


class CliBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/mobility/cli
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_mobility_cli_feature_profile(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        reference_count: Optional[bool] = False,
        **kw,
    ) -> Any:
        """
        Get Mobility Cli Feature Profiles

        :param offset: Pagination offset
        :param limit: Pagination limit
        :param reference_count: get associated group details
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
            "referenceCount": reference_count,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/mobility/cli", params=params, **kw
        )

    def get_mobility_cli_feature_profile_by_cli_id(self, cli_id: str, **kw) -> Any:
        """
        Get a Mobility Feature Profile with Cli profile type

        :param cli_id: Feature Profile Id
        :returns: Any
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/mobility/cli/{cliId}", params=params, **kw
        )

    @property
    def config(self) -> ConfigBuilder:
        """
        The config property
        """
        from .config.config_builder import ConfigBuilder

        return ConfigBuilder(self._request_adapter)
