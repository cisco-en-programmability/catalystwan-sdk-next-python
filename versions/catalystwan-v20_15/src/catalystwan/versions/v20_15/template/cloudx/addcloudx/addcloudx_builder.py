# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class AddcloudxBuilder:
    """
    Builds and executes requests for operations under /template/cloudx/addcloudx
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def add_cloudx_type(self, type_: str, payload: Optional[Any] = None, **kw):
        """
        Add cloudx gateway

        :param type_: Cloudx type
        :param payload: Cloudx
        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "addCloudxType")
        params = {
            "type": type_,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/template/cloudx/addcloudx/{type}",
            params=params,
            payload=payload,
            **kw,
        )
