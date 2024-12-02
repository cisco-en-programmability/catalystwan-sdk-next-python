# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import ExtendedApplicationRequestData, PolicyComplianceResponse

if TYPE_CHECKING:
    from .application.application_builder import ApplicationBuilder


class ComplianceBuilder:
    """
    Builds and executes requests for operations under /sdavc/cloud-sourced/compliance
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def compliance_with_extended_applications(
        self, payload: Optional[ExtendedApplicationRequestData] = None, **kw
    ) -> PolicyComplianceResponse:
        """
        Compliance with extended applications

        :param payload: Payload
        :returns: PolicyComplianceResponse
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/sdavc/cloud-sourced/compliance",
            return_type=PolicyComplianceResponse,
            payload=payload,
            **kw,
        )

    @property
    def application(self) -> ApplicationBuilder:
        """
        The application property
        """
        from .application.application_builder import ApplicationBuilder

        return ApplicationBuilder(self._request_adapter)
