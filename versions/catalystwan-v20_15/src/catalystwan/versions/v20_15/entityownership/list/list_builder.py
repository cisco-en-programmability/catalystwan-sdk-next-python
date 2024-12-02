# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface
from .models import EntityOwnershipInfo


class ListBuilder:
    """
    Builds and executes requests for operations under /entityownership/list
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def list_entity_ownership_info(self, **kw) -> EntityOwnershipInfo:
        """
        List all entity ownership info

        :returns: EntityOwnershipInfo
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/entityownership/list",
            return_type=EntityOwnershipInfo,
            **kw,
        )
