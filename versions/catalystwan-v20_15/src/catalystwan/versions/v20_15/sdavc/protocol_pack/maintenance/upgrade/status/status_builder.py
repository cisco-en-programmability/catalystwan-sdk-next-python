# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class StatusBuilder:
    """
    Builds and executes requests for operations under /sdavc/protocol-pack/maintenance/upgrade/status
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_deploy_job_status_1(self, **kw):
        """
        Get active deploy job status

        :returns: None
        """
        return self._request_adapter.request("GET", "/dataservice/sdavc/protocol-pack/maintenance/upgrade/status", **kw)

    def get_deploy_job_status(self, uuid: str, **kw):
        """
        Get upgrade status for given Task UUID

        :param uuid: Uuid
        :returns: None
        """
        params = {
            "uuid": uuid,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/sdavc/protocol-pack/maintenance/upgrade/status/{uuid}", params=params, **kw
        )
