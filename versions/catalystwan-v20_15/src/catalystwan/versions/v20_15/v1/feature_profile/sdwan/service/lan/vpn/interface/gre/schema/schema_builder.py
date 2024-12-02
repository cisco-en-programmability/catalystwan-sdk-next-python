# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface
from .models import SchemaTypeParam


class SchemaBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/lan/vpn/interface/gre/schema
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cedge_service_lan_vpn_interface_gre_schema_by_schema(
        self, schema_type: SchemaTypeParam, **kw
    ) -> str:
        """
        Get a Cedge Service LanVpn InterfaceGre Schema by Schema Type

        :param schema_type: Schema type
        :returns: str
        """
        params = {
            "schemaType": schema_type,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/lan/vpn/interface/gre/schema",
            return_type=str,
            params=params,
            **kw,
        )
