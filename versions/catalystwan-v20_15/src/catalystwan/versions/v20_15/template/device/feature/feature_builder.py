# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class FeatureBuilder:
    """
    Builds and executes requests for operations under /template/device/feature
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_master_template(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Create a device template from feature templates and sub templates


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param payload: Create template request
        :returns: Any
        """
        return self._request_adapter.request("POST", "/dataservice/template/device/feature", payload=payload, **kw)
