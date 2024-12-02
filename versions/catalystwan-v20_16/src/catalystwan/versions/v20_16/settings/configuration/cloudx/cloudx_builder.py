# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class CloudxBuilder:
    """
    Builds and executes requests for operations under /settings/configuration/cloudx
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cloudx_configuration(self, **kw) -> Any:
        """
        Retrieve cloudx configuration value

        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getCloudxConfiguration")
        return self._request_adapter.request(
            "GET", "/dataservice/settings/configuration/cloudx", **kw
        )

    def edit_cloudx_configuration(self, payload: Optional[str] = None, **kw) -> Any:
        """
        Update cloudx configuration setting

        :param payload: Payload
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "editCloudxConfiguration")
        return self._request_adapter.request(
            "PUT", "/dataservice/settings/configuration/cloudx", payload=payload, **kw
        )

    def new_cloudx_configuration(self, payload: Optional[str] = None, **kw) -> str:
        """
        Add new cloudx configuration

        :param payload: Payload
        :returns: str
        """
        logging.warning("Operation: %s is deprecated", "newCloudxConfiguration")
        return self._request_adapter.request(
            "POST",
            "/dataservice/settings/configuration/cloudx",
            return_type=str,
            payload=payload,
            **kw,
        )
