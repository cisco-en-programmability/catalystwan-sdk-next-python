# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .initiate_compliance.initiate_compliance_builder import InitiateComplianceBuilder
    from .is_compliance_detected.is_compliance_detected_builder import IsComplianceDetectedBuilder
    from .status.status_builder import StatusBuilder


class ApplicationBuilder:
    """
    Builds and executes requests for operations under /sdavc/protocol-pack/compliance/application
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_default_application_compliance_details(self, **kw) -> Any:
        """
        Get default application name compliance details

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/sdavc/protocol-pack/compliance/application", **kw
        )

    def get_application_compliance_details(self, uuid: str, **kw) -> Any:
        """
        Get application name compliance details for given task uuid

        :param uuid: Uuid
        :returns: Any
        """
        params = {
            "uuid": uuid,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/sdavc/protocol-pack/compliance/application/{uuid}",
            params=params,
            **kw,
        )

    @property
    def initiate_compliance(self) -> InitiateComplianceBuilder:
        """
        The initiate-compliance property
        """
        from .initiate_compliance.initiate_compliance_builder import InitiateComplianceBuilder

        return InitiateComplianceBuilder(self._request_adapter)

    @property
    def is_compliance_detected(self) -> IsComplianceDetectedBuilder:
        """
        The is-compliance-detected property
        """
        from .is_compliance_detected.is_compliance_detected_builder import (
            IsComplianceDetectedBuilder,
        )

        return IsComplianceDetectedBuilder(self._request_adapter)

    @property
    def status(self) -> StatusBuilder:
        """
        The status property
        """
        from .status.status_builder import StatusBuilder

        return StatusBuilder(self._request_adapter)
