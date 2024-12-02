# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import SchemaTypeParam


class SchemaBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/multicloud-connection/schema
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sd_routing_transport_multicloud_parcel_schema_by_schema_type(
        self, schema_type: SchemaTypeParam, **kw
    ) -> str:
        """
        Get a SD-Routing tranport multicloud connection Schema by Schema Type

        :param schema_type: Schema type
        :returns: str
        """
        params = {
            "schemaType": schema_type,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/multicloud-connection/schema",
            return_type=str,
            params=params,
            **kw,
        )
