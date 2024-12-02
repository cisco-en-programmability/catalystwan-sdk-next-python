# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface
import logging


class ScmwidgetBuilder:
    """
    Builds and executes requests for operations under /opentaccase/scmwidget
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_call(self, **kw) -> List[Any]:
        """
        Proxy API for SCM Widget

        :returns: List[Any]
        """
        logging.warning("Operation: %s is deprecated", "getCall")
        return self._request_adapter.request(
            "GET",
            "/dataservice/opentaccase/scmwidget/{var}",
            return_type=List[Any],
            **kw,
        )

    def post_call(self, **kw) -> List[Any]:
        """
        Prxoy API for SCM Widget

        :returns: List[Any]
        """
        logging.warning("Operation: %s is deprecated", "postCall")
        return self._request_adapter.request(
            "POST",
            "/dataservice/opentaccase/scmwidget/{var}",
            return_type=List[Any],
            **kw,
        )

    def delete_call(self, **kw) -> List[Any]:
        """
        Proxy API for SCM Widget

        :returns: List[Any]
        """
        logging.warning("Operation: %s is deprecated", "deleteCall")
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/opentaccase/scmwidget/{var}",
            return_type=List[Any],
            **kw,
        )
