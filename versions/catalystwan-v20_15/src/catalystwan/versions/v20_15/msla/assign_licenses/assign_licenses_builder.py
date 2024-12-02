# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import AssignMslaLicenses


class AssignLicensesBuilder:
    """
    Builds and executes requests for operations under /msla/assignLicenses
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def assign_msla_licenses_to_devices(self):
        class assign_msla_licenses_to_devices_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[AssignMslaLicenses] = None, **kw):
                """
                Assign msla licenses to devices

                :param payload: List of devices for assigning licenses
                :returns: None
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/msla/assignLicenses", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> AssignMslaLicenses:
                return AssignMslaLicenses(*args, **kwargs)

            @property
            def payload_model(self) -> Type[AssignMslaLicenses]:
                return AssignMslaLicenses

        return assign_msla_licenses_to_devices_(self._request_adapter)
