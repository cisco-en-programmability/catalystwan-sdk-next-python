# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import MigrateTenantModel


class ExportBuilder:
    """
    Builds and executes requests for operations under /tenantmigration/export
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def export_tenant_data(self):
        class export_tenant_data_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[MigrateTenantModel] = None, **kw) -> Any:
                """
                Export tenant data

                :param payload: Payload
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/tenantmigration/export", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> MigrateTenantModel:
                return MigrateTenantModel(*args, **kwargs)

            @property
            def payload_model(self) -> Type[MigrateTenantModel]:
                return MigrateTenantModel

        return export_tenant_data_(self._request_adapter)
