# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class CertificatesBuilder:
    """
    Builds and executes requests for operations under /sslproxy/certificates
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def upload_certificiates(self):
        class upload_certificiates_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Upload device certificates

                :param payload: Certificate file
                :returns: None
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/sslproxy/certificates", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return upload_certificiates_(self._request_adapter)
