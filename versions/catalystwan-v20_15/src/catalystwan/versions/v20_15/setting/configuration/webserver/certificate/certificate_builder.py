# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .getcertificate.getcertificate_builder import GetcertificateBuilder


class CertificateBuilder:
    """
    Builds and executes requests for operations under /setting/configuration/webserver/certificate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def show_info(self, **kw) -> str:
        """
        Retrieves Certificate Signing Request information

        :returns: str
        """
        return self._request_adapter.request(
            "GET", "/dataservice/setting/configuration/webserver/certificate", return_type=str, **kw
        )

    def import_certificate(self, payload: Optional[Any] = None, **kw) -> str:
        """
        Import a signed web server certificate

        :param payload: Web Server Certificate configuration
        :returns: str
        """
        return self._request_adapter.request(
            "PUT", "/dataservice/setting/configuration/webserver/certificate", return_type=str, payload=payload, **kw
        )

    def get_csr(self, payload: Optional[Any] = None, **kw) -> str:
        """
        Generate Certificate Signing Request

        :param payload: Web Server Certificate configuration
        :returns: str
        """
        return self._request_adapter.request(
            "POST", "/dataservice/setting/configuration/webserver/certificate", return_type=str, payload=payload, **kw
        )

    @property
    def getcertificate(self) -> GetcertificateBuilder:
        """
        The getcertificate property
        """
        from .getcertificate.getcertificate_builder import GetcertificateBuilder

        return GetcertificateBuilder(self._request_adapter)
