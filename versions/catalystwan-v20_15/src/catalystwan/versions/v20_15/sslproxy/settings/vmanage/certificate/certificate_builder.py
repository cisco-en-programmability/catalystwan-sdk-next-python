# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class CertificateBuilder:
    """
    Builds and executes requests for operations under /sslproxy/settings/vmanage/certificate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def getv_manage_certificate(self, **kw) -> Any:
        """
        Get vManage intermediate certificate

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/sslproxy/settings/vmanage/certificate", **kw
        )

    def setv_manageintermediate_cert(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Set vManage root certificate

        :param payload: Set vManage intermediate CA request
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/sslproxy/settings/vmanage/certificate", payload=payload, **kw
        )
