# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class CertificateBuilder:
    """
    Builds and executes requests for operations under /certificate/revoke/enterprise/certificate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def decommission_enterprise_csr_for_vedge(self, payload: Optional[str] = None, **kw) -> str:
        """
        Revoking enterprise CSR for hardware vEdge

        :param payload: JSON parameter with Device UUID
        :returns: str
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/certificate/revoke/enterprise/certificate",
            return_type=str,
            payload=payload,
            **kw,
        )
