# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import AssignLicensesRequest


class AssignLicensesBuilder:
    """
    Builds and executes requests for operations under /v1/licensing/assign-licenses
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def assign_msla_licenses(self):
        class assign_msla_licenses_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[AssignLicensesRequest] = None, **kw):
                """
                Assign licenses to devices

                :param payload: Payload
                :returns: None
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/v1/licensing/assign-licenses", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> AssignLicensesRequest:
                return AssignLicensesRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[AssignLicensesRequest]:
                return AssignLicensesRequest

        return assign_msla_licenses_(self._request_adapter)
