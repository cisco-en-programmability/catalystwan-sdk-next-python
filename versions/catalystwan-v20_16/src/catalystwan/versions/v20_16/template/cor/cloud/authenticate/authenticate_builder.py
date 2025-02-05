# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class AuthenticateBuilder:
    """
    Builds and executes requests for operations under /template/cor/cloud/authenticate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def authenticate_cred_and_update(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Authenticate and update cloud account credentials

        :param payload: Cloud account credential
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "authenticateCredAndUpdate")
        return self._request_adapter.request(
            "PUT", "/dataservice/template/cor/cloud/authenticate", payload=payload, **kw
        )

    def authenticate_cloud_on_ramp_cred_and_add(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Authenticate cloud account credentials

        :param payload: Cloud account credential
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "authenticateCloudOnRampCredAndAdd")
        return self._request_adapter.request(
            "POST", "/dataservice/template/cor/cloud/authenticate", payload=payload, **kw
        )
