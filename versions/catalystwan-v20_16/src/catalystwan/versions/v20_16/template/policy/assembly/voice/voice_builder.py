# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class VoiceBuilder:
    """
    Builds and executes requests for operations under /template/policy/assembly/voice
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def preview_2(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Get policy assembly preview

        :param payload: Policy assembly
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/template/policy/assembly/voice", payload=payload, **kw
        )

    def preview_by_id_2(self, id: str, **kw) -> Any:
        """
        Get policy assembly preview for feature policy

        :param id: Policy Id
        :returns: Any
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/template/policy/assembly/voice/{id}", params=params, **kw
        )
