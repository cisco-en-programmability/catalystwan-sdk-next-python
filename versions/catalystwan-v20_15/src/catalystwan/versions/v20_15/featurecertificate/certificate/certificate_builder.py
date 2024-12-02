# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class CertificateBuilder:
    """
    Builds and executes requests for operations under /featurecertificate/certificate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_device_certificate(self, device_id: str, **kw) -> Any:
        """
        Get feature cert from cEdge device


        Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

        :param device_id: Device Id
        :returns: Any
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/featurecertificate/certificate", params=params, **kw
        )

    @property
    def install_feature_certificate(self):
        class install_feature_certificate_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Upload feature cert for cEdge device


                Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

                :param payload: Install feature cert request for cEdge
                :returns: Any
                """
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/featurecertificate/certificate",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return install_feature_certificate_(self._request_adapter)
