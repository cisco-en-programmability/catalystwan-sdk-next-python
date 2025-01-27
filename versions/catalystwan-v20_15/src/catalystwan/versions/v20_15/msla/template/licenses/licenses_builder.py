# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import GetSubscriptions1PostRequest


class LicensesBuilder:
    """
    Builds and executes requests for operations under /msla/template/licenses
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_subscriptions_1(
        self, payload: Optional[GetSubscriptions1PostRequest] = None, **kw
    ) -> Any:
        """
        Retrieve MSLA subscription/licenses

        :param payload: Payload
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getSubscriptions_1")
        return self._request_adapter.request(
            "POST", "/dataservice/msla/template/licenses", payload=payload, **kw
        )
