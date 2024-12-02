# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List

from catalystwan.abc import RequestAdapterInterface


class DbrestorestatusBuilder:
    """
    Builds and executes requests for operations under /disasterrecovery/dbrestorestatus
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_config_db_restore_status(self, **kw) -> List[Any]:
        """
        Config-db restore status

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/disasterrecovery/dbrestorestatus",
            return_type=List[Any],
            **kw,
        )
