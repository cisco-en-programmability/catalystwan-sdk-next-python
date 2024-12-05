# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class DevicecsrBuilder:
    """
    Builds and executes requests for operations under /featurecertificate/devicecsr
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_device_csr(self, device_id: str, **kw) -> Any:
        """
        Get CSR from cEdge device


        Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

        :param device_id: Device Id
        :returns: Any
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request("GET", "/dataservice/featurecertificate/devicecsr", params=params, **kw)

    def gen_device_csr(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Create CSR for cEdge device


        Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

        :param payload: CSR request for cEdge
        :returns: Any
        """
        return self._request_adapter.request("PUT", "/dataservice/featurecertificate/devicecsr", payload=payload, **kw)
