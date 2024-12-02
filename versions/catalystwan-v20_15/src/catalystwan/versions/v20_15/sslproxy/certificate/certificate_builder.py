# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .wanedge.wanedge_builder import WanedgeBuilder


class CertificateBuilder:
    """
    Builds and executes requests for operations under /sslproxy/certificate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_proxy_cert_of_edge(self, device_id: str, **kw) -> Any:
        """
        Get edge proxy certificate

        :param device_id: Device Id
        :returns: Any
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/sslproxy/certificate", params=params, **kw
        )

    @property
    def update_certificate(self):
        class update_certificate_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Upload device certificate

                :param payload: Upload device certificate
                :returns: Any
                """
                return self._request_adapter.request(
                    "PUT", "/dataservice/sslproxy/certificate", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_certificate_(self._request_adapter)

    @property
    def wanedge(self) -> WanedgeBuilder:
        """
        The wanedge property
        """
        from .wanedge.wanedge_builder import WanedgeBuilder

        return WanedgeBuilder(self._request_adapter)
