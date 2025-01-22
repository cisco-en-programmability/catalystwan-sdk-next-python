# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import (
    ExecutiveSummaryReport,
    ReportInfo,
    ReportSummaryResponse,
    UpdateReportTemplateResponse,
)

if TYPE_CHECKING:
    from .action.action_builder import ActionBuilder
    from .preview.preview_builder import PreviewBuilder
    from .tasks.tasks_builder import TasksBuilder


class ReportsBuilder:
    """
    Builds and executes requests for operations under /v1/reports
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_report_templates(self, **kw) -> ReportSummaryResponse:
        """
        Get all reports information

        :returns: ReportSummaryResponse
        """
        return self._request_adapter.request(
            "GET", "/dataservice/v1/reports", return_type=ReportSummaryResponse, **kw
        )

    def create_report_template(self, payload: ExecutiveSummaryReport, **kw) -> ReportInfo:
        """
        create a new report template

        :param payload: Report Template Config
        :returns: ReportInfo
        """
        return self._request_adapter.request(
            "POST", "/dataservice/v1/reports", return_type=ReportInfo, payload=payload, **kw
        )

    def get_report_template_by_id(self, report_id: str, **kw) -> ReportSummaryResponse:
        """
        Get the report template information by report ID

        :param report_id: Report id
        :returns: ReportSummaryResponse
        """
        params = {
            "reportId": report_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/reports/{reportId}",
            return_type=ReportSummaryResponse,
            params=params,
            **kw,
        )

    def update_report_template(
        self, report_id: str, payload: ExecutiveSummaryReport, **kw
    ) -> ReportInfo:
        """
        Update the report template by report ID

        :param report_id: Report id
        :param payload: updated report config
        :returns: ReportInfo
        """
        params = {
            "reportId": report_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/reports/{reportId}",
            return_type=ReportInfo,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_report_template(self, report_id: str, **kw) -> UpdateReportTemplateResponse:
        """
        Delete the report template and all report files associated with it

        :param report_id: Report id
        :returns: UpdateReportTemplateResponse
        """
        params = {
            "reportId": report_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/reports/{reportId}",
            return_type=UpdateReportTemplateResponse,
            params=params,
            **kw,
        )

    @property
    def action(self) -> ActionBuilder:
        """
        The action property
        """
        from .action.action_builder import ActionBuilder

        return ActionBuilder(self._request_adapter)

    @property
    def preview(self) -> PreviewBuilder:
        """
        The preview property
        """
        from .preview.preview_builder import PreviewBuilder

        return PreviewBuilder(self._request_adapter)

    @property
    def tasks(self) -> TasksBuilder:
        """
        The tasks property
        """
        from .tasks.tasks_builder import TasksBuilder

        return TasksBuilder(self._request_adapter)
