# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import AssignMslaLicenses


class AssignLicensesBuilder:
    """
    Builds and executes requests for operations under /msla/assignLicenses
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def assign_msla_licenses_to_devices(self, payload: Optional[AssignMslaLicenses] = None, **kw):
        """
        Assign msla licenses to devices

        :param payload: List of devices for assigning licenses
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/msla/assignLicenses", payload=payload, **kw
        )
