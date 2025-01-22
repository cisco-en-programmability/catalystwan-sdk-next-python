# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import BatchFlow


class BatchBuilder:
    """
    Builds and executes requests for operations under /jobs/batch
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def batch_execute(self, payload: Optional[BatchFlow] = None, **kw) -> str:
        """
        Batch processing multiple REST API calls

        :param payload: Payload for executing multiple APIs
        :returns: str
        """
        return self._request_adapter.request(
            "POST", "/dataservice/jobs/batch", return_type=str, payload=payload, **kw
        )
