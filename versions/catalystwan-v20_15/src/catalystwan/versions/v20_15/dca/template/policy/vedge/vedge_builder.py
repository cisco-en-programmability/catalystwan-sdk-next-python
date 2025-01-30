# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface


class VedgeBuilder:
    """
    Builds and executes requests for operations under /dca/template/policy/vedge
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_vedge_template_list_dca(self, payload: Optional[Any] = None, **kw) -> List[Any]:
        """
        Get vEdge template list

        :param payload: Query string
        :returns: List[Any]
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/dca/template/policy/vedge",
            return_type=List[Any],
            payload=payload,
            **kw,
        )
