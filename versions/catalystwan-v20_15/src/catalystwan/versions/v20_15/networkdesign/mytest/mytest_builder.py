# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Any
from catalystwan.abc import RequestAdapterInterface
import logging


class MytestBuilder:
    """
    Builds and executes requests for operations under /networkdesign/mytest
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def run_my_test(self, name: str, **kw) -> Any:
        """
        Get all device templates for this feature template

        :param name: Test bane
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "runMyTest")
        params = {
            "name": name,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/networkdesign/mytest/{name}", params=params, **kw
        )
