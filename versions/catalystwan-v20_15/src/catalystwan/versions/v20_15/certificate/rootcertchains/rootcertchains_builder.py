# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List, Optional

from catalystwan.abc import RequestAdapterInterface


class RootcertchainsBuilder:
    """
    Builds and executes requests for operations under /certificate/rootcertchains
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_root_cert_chains(self, action: str, **kw) -> List[str]:
        """
        get root cert chain in the system

        :param action: Action Parameter to fetch root cert chains
        :returns: List[str]
        """
        params = {
            "action": action,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/certificate/rootcertchains",
            return_type=List[str],
            params=params,
            **kw,
        )

    def save_root_cert_chain(self, payload: Optional[str] = None, **kw) -> str:
        """
        save root cert chain in the system

        :param payload: JSON payload with RootCertChain and Certificate details.
        :returns: str
        """
        return self._request_adapter.request(
            "PUT", "/dataservice/certificate/rootcertchains", return_type=str, payload=payload, **kw
        )
