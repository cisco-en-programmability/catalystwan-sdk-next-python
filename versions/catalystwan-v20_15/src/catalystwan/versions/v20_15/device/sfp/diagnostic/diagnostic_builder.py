# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import IfnameParam


class DiagnosticBuilder:
    """
    Builds and executes requests for operations under /device/sfp/diagnostic
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_diagnostic(
        self, device_id: str, ifname: Optional[IfnameParam] = None, **kw
    ) -> Any:
        """
        Get SFP diagnostic

        :param ifname: IF Name
        :param device_id: deviceId - Device IP
        :returns: Any
        """
        params = {
            "ifname": ifname,
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/sfp/diagnostic", params=params, **kw
        )
