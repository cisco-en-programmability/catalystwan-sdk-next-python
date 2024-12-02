# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface


class ConfigBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/mobility/cli/{cliId}/config
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_config_feature_for_mobility(self, cli_id: str, **kw) -> str:
        """
        Get config Features for cli feature profile

        :param cli_id: Feature Profile ID
        :returns: str
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/cli/{cliId}/config",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_config_feature_for_mobility(self):
        class create_config_feature_for_mobility_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, cli_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Create a config Feature for cli feature profile

                :param cli_id: Feature Profile ID
                :param payload: cli config Feature
                :returns: str
                """
                params = {
                    "cliId": cli_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/mobility/cli/{cliId}/config",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return create_config_feature_for_mobility_(self._request_adapter)

    def get_config_feature_for_mobility_by_parcel_id(
        self, cli_id: str, config_id: str, **kw
    ) -> str:
        """
        Get config Feature by configId for cli feature profile

        :param cli_id: Feature Profile ID
        :param config_id: Feature ID
        :returns: str
        """
        params = {
            "cliId": cli_id,
            "configId": config_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/cli/{cliId}/config/{configId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_config_feature_for_mobility(self):
        class edit_config_feature_for_mobility_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, cli_id: str, config_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Update a config Feature for cli feature profile

                :param cli_id: Feature Profile ID
                :param config_id: Feature ID
                :param payload: cli config Feature
                :returns: str
                """
                params = {
                    "cliId": cli_id,
                    "configId": config_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/mobility/cli/{cliId}/config/{configId}",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return edit_config_feature_for_mobility_(self._request_adapter)

    def delete_config_feature_for_mobility(self, cli_id: str, config_id: str, **kw):
        """
        Delete a config Feature for cli feature profile

        :param cli_id: Feature Profile ID
        :param config_id: Feature ID
        :returns: None
        """
        params = {
            "cliId": cli_id,
            "configId": config_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/mobility/cli/{cliId}/config/{configId}",
            params=params,
            **kw,
        )
