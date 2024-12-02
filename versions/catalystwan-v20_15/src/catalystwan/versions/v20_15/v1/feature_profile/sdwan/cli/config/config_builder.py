# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class ConfigBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/cli/config
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_config_profile_parcel_for_cli(self, cli_id: str, **kw) -> str:
        """
        Get config Profile Parcels for cli feature profile

        :param cli_id: Feature Profile ID
        :returns: str
        """
        params = {
            "cliId": cli_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/cli/{cliId}/config",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_sdwan_config_profile_parcel_for_cli(self):
        class create_sdwan_config_profile_parcel_for_cli_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, cli_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Create a config Profile Parcel for cli feature profile

                :param cli_id: Feature Profile ID
                :param payload: cli config Profile Parcel
                :returns: str
                """
                params = {
                    "cliId": cli_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/cli/{cliId}/config",
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

        return create_sdwan_config_profile_parcel_for_cli_(self._request_adapter)

    def get_config_profile_parcel_by_parcel_id_for_cli(
        self, cli_id: str, config_id: str, **kw
    ) -> str:
        """
        Get config Profile Parcel by configId for cli feature profile

        :param cli_id: Feature Profile ID
        :param config_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "cliId": cli_id,
            "configId": config_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/cli/{cliId}/config/{configId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_config_profile_parcel_for_cli(self):
        class edit_config_profile_parcel_for_cli_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, cli_id: str, config_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Update a config Profile Parcel for cli feature profile

                :param cli_id: Feature Profile ID
                :param config_id: Profile Parcel ID
                :param payload: cli config Profile Parcel
                :returns: str
                """
                params = {
                    "cliId": cli_id,
                    "configId": config_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/cli/{cliId}/config/{configId}",
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

        return edit_config_profile_parcel_for_cli_(self._request_adapter)

    def delete_config_profile_parcel_for_cli(self, cli_id: str, config_id: str, **kw):
        """
        Delete a config Profile Parcel for cli feature profile

        :param cli_id: Feature Profile ID
        :param config_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "cliId": cli_id,
            "configId": config_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/cli/{cliId}/config/{configId}",
            params=params,
            **kw,
        )

    @property
    def schema(self) -> SchemaBuilder:
        """
        The schema property
        """
        from .schema.schema_builder import SchemaBuilder

        return SchemaBuilder(self._request_adapter)
