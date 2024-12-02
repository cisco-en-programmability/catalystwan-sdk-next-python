# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class NetworkMigrationBuilder:
    """
    Builds and executes requests for operations under /tenantmigration/networkMigration
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def re_trigger_network_migration(self, **kw) -> Any:
        """
        Re-trigger network migration

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/tenantmigration/networkMigration", **kw
        )

    @property
    def migrate_network(self):
        class migrate_network_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Migrate network

                :param payload: Network migration
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/tenantmigration/networkMigration",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return migrate_network_(self._request_adapter)
