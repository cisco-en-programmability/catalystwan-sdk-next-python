# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class CertdetailsBuilder:
    """
    Builds and executes requests for operations under /certificate/certdetails
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_cert_details(self):
        class get_cert_details_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> str:
                """
                get certificaate details

                :param payload: Payload
                :returns: str
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/certificate/certdetails", return_type=str, payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return get_cert_details_(self._request_adapter)
