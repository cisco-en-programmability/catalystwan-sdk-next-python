# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import BatchFlow


class BatchBuilder:
    """
    Builds and executes requests for operations under /jobs/batch
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def batch_execute(self):
        class batch_execute_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[BatchFlow] = None, **kw) -> str:
                """
                Batch processing multiple REST API calls

                :param payload: Payload for executing multiple APIs
                :returns: str
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/jobs/batch",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> BatchFlow:
                return BatchFlow(*args, **kwargs)

            @property
            def payload_model(self) -> Type[BatchFlow]:
                return BatchFlow

        return batch_execute_(self._request_adapter)
