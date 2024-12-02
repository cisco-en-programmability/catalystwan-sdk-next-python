# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class BasicBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/system/basic
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_basic_profile_feature_for_system(self, system_id: str, **kw) -> str:
        """
        Get Basic Profile Feature for System feature profile

        :param system_id: Feature Profile ID
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/basic",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_basic_profile_feature_for_system(self):
        class create_basic_profile_feature_for_system_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, system_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create a Basic Profile Feature for System feature profile

                :param system_id: Feature Profile ID
                :param payload: Basic Profile Feature
                :returns: str
                """
                params = {
                    "systemId": system_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/system/{systemId}/basic",
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

        return create_basic_profile_feature_for_system_(self._request_adapter)

    def get_basic_profile_feature_by_feature_id_for_system(
        self, system_id: str, basic_id: str, **kw
    ) -> str:
        """
        Get Basic Profile Feature by FeatureId for System feature profile

        :param system_id: Feature Profile ID
        :param basic_id: Profile Feature ID
        :returns: str
        """
        params = {
            "systemId": system_id,
            "basicId": basic_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/basic/{basicId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_basic_profile_feature_for_system(self):
        class edit_basic_profile_feature_for_system_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, system_id: str, basic_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Update a Basic Profile Feature for System feature profile

                :param system_id: Feature Profile ID
                :param basic_id: Profile Feature ID
                :param payload: Basic Profile Feature
                :returns: str
                """
                params = {
                    "systemId": system_id,
                    "basicId": basic_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/system/{systemId}/basic/{basicId}",
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

        return edit_basic_profile_feature_for_system_(self._request_adapter)

    def delete_basic_profile_feature_for_system(
        self, system_id: str, basic_id: str, **kw
    ):
        """
        Delete a Basic Profile Feature for System feature profile

        :param system_id: Feature Profile ID
        :param basic_id: Profile Feature ID
        :returns: None
        """
        params = {
            "systemId": system_id,
            "basicId": basic_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}/basic/{basicId}",
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
