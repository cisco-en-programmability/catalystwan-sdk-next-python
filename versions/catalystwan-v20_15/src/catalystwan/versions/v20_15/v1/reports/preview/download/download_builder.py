# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from .models import TemplateTypeParam


class DownloadBuilder:
    """
    Builds and executes requests for operations under /v1/reports/preview/download
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def download_report_preview_file(self, template_type: Optional[TemplateTypeParam] = None, **kw) -> str:
        """
        Download a report preview file

        :param template_type: Template type
        :returns: str
        """
        params = {
            "templateType": template_type,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/reports/preview/download", return_type=str, params=params, **kw
        )
