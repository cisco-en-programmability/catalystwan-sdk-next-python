# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .config.config_builder import ConfigBuilder


class CliBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/cli
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_nfvirtual_cli_feature_profiles(
        self, offset: Optional[int] = None, limit: Optional[int] = 0, **kw
    ) -> Any:
        """
        Get all Nfvirtual CLI Feature Profiles

        :param offset: Pagination offset
        :param limit: Pagination limit
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/nfvirtual/cli", params=params, **kw
        )

    def create_nfvirtual_cli_feature_profile(self, payload: Optional[str] = None, **kw) -> str:
        """
        Create a Nfvirtual CLI Feature Profile

        :param payload: Nfvirtual Feature profile for CLI
        :returns: str
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/nfvirtual/cli",
            return_type=str,
            payload=payload,
            **kw,
        )

    def get_nfvirtual_cli_feature_profile_byid(self, cli_id: str, **kw) -> Any:
        """
        Get nfvirtual CLI Feature Profile with cliId

        :param cli_id: Feature Profile Id
        :returns: Any
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/nfvirtual/cli/{cliId}", params=params, **kw
        )

    def edit_nfvirtual_cli_feature_profile(
        self, cli_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a Nfvirtual CLI Feature Profile

        :param cli_id: Feature Profile Id
        :param payload: Nfvirtual Feature profile fo CLI
        :returns: str
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/nfvirtual/cli/{cliId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_nfvirtual_cli_feature_profile(self, cli_id: str, **kw):
        """
        Delete nfvirtual CLI Feature Profile

        :param cli_id: Cli id
        :returns: None
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/v1/feature-profile/nfvirtual/cli/{cliId}", params=params, **kw
        )

    @property
    def config(self) -> ConfigBuilder:
        """
        The config property
        """
        from .config.config_builder import ConfigBuilder

        return ConfigBuilder(self._request_adapter)
