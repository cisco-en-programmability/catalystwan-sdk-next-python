# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import AuditFix, CloudTypeParam, Taskid


class AuditBuilder:
    """
    Builds and executes requests for operations under /multicloud/audit
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def audit_dry_run(self, cloud_type: CloudTypeParam, cloud_region: Optional[str] = None, **kw):
        """
        Call an audit with dry run

        :param cloud_type: Cloud type
        :param cloud_region: Cloud region
        :returns: None
        """
        params = {
            "cloudType": cloud_type,
            "cloudRegion": cloud_region,
        }
        return self._request_adapter.request("GET", "/dataservice/multicloud/audit", params=params, **kw)

    @property
    def audit(self):
        class audit_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[AuditFix] = None, **kw) -> Taskid:
                """
                Call an audit

                :param payload: Audit
                :returns: Taskid
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/multicloud/audit", return_type=Taskid, payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> AuditFix:
                return AuditFix(*args, **kwargs)

            @property
            def payload_model(self) -> Type[AuditFix]:
                return AuditFix

        return audit_(self._request_adapter)
