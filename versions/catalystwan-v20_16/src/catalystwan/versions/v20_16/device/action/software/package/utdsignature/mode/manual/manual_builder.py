# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import InstallPkg


class ManualBuilder:
    """
    Builds and executes requests for operations under /device/action/software/package/utdsignature/{type}/mode/manual
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def upload_utd_image(self, type_: str, payload: Optional[InstallPkg] = None, **kw):
        """
        upload Utd image

        :param type_: Type
        :param payload: Utd image File
        :returns: None
        """
        params = {
            "type": type_,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/device/action/software/package/utdsignature/{type}/mode/manual",
            params=params,
            payload=payload,
            **kw,
        )
