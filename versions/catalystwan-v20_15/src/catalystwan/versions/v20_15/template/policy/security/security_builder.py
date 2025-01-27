# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import DeviceModel

if TYPE_CHECKING:
    from .definition.definition_builder import DefinitionBuilder
    from .devices.devices_builder import DevicesBuilder
    from .staging.staging_builder import StagingBuilder
    from .summary.summary_builder import SummaryBuilder


class SecurityBuilder:
    """
    Builds and executes requests for operations under /template/policy/security
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_security_template_list(self, mode: Optional[str] = None, **kw) -> List[Any]:
        """
        Generate template list

        :param mode: Mode
        :returns: List[Any]
        """
        params = {
            "mode": mode,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/policy/security",
            return_type=List[Any],
            params=params,
            **kw,
        )

    def create_security_template(self, payload: Optional[Any] = None, **kw):
        """
        Create Template

        :param payload: Policy template
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/template/policy/security", payload=payload, **kw
        )

    def get_security_templates_for_device(self, device_model: DeviceModel, **kw) -> Any:
        """
        Get templates that map a device model

        :param device_model: Device model
        :returns: Any
        """
        params = {
            "deviceModel": device_model,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/template/policy/security/{deviceModel}", params=params, **kw
        )

    def edit_security_template(self, policy_id: str, payload: Optional[Any] = None, **kw) -> Any:
        """
        Edit Template

        :param policy_id: Policy Id
        :param payload: Policy template
        :returns: Any
        """
        params = {
            "policyId": policy_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/template/policy/security/{policyId}",
            params=params,
            payload=payload,
            **kw,
        )

    def delete_security_template(self, policy_id: str, **kw):
        """
        Delete Template

        :param policy_id: Policy Id
        :returns: None
        """
        params = {
            "policyId": policy_id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/template/policy/security/{policyId}", params=params, **kw
        )

    @property
    def definition(self) -> DefinitionBuilder:
        """
        The definition property
        """
        from .definition.definition_builder import DefinitionBuilder

        return DefinitionBuilder(self._request_adapter)

    @property
    def devices(self) -> DevicesBuilder:
        """
        The devices property
        """
        from .devices.devices_builder import DevicesBuilder

        return DevicesBuilder(self._request_adapter)

    @property
    def staging(self) -> StagingBuilder:
        """
        The staging property
        """
        from .staging.staging_builder import StagingBuilder

        return StagingBuilder(self._request_adapter)

    @property
    def summary(self) -> SummaryBuilder:
        """
        The summary property
        """
        from .summary.summary_builder import SummaryBuilder

        return SummaryBuilder(self._request_adapter)
