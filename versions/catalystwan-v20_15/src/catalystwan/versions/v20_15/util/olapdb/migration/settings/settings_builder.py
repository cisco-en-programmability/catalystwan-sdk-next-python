# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class SettingsBuilder:
    """
    Builds and executes requests for operations under /util/olapdb/migration/settings
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_stats_migration_settings(self, **kw) -> Any:
        """
        Get migration generic settings

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/util/olapdb/migration/settings", **kw
        )

    @property
    def post_stats_migration_settings(self):
        class post_stats_migration_settings_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> Any:
                """
                Config generic settings

                :param payload: generic settings
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/util/olapdb/migration/settings",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return post_stats_migration_settings_(self._request_adapter)
