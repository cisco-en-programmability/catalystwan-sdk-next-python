# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import SaveTemplateRequest


class TemplateBuilder:
    """
    Builds and executes requests for operations under /v1/smart-licensing/template
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def save_template(self, payload: Optional[SaveTemplateRequest] = None, **kw) -> Any:
        """
        Create and assign license template.

        :param payload: Payload
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/v1/smart-licensing/template", payload=payload, **kw
        )

    def delete_template(self, template_id: str, **kw):
        """
        Delete a license template

        :param template_id: Template id
        :returns: None
        """
        params = {
            "templateId": template_id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/v1/smart-licensing/template/{templateId}", params=params, **kw
        )
