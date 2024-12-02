# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List

from catalystwan.abc import RequestAdapterInterface


class RootcertificateBuilder:
    """
    Builds and executes requests for operations under /certificate/rootcertificate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_root_certificate(self, **kw) -> List[str]:
        """
        Get device root certificate detail view

        :returns: List[str]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/certificate/rootcertificate",
            return_type=List[str],
            **kw,
        )
