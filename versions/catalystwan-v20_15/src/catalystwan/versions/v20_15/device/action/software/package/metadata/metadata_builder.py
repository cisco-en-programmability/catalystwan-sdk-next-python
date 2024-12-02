# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class MetadataBuilder:
    """
    Builds and executes requests for operations under /device/action/software/package/{versionId}/metadata
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_image_metadata(self, version_id: str, **kw):
        """
        Update Package Metadata

        :param version_id: versionId
        :returns: None
        """
        params = {
            "versionId": version_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/action/software/package/{versionId}/metadata",
            params=params,
            **kw,
        )

    @property
    def edit_image_metadata(self):
        class edit_image_metadata_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, version_id: str, payload: Optional[Any] = None, **kw):
                """
                Update Package Metadata

                :param version_id: versionId
                :param payload: Request body for Device bootstrap configuration
                :returns: None
                """
                params = {
                    "versionId": version_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/device/action/software/package/{versionId}/metadata",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return edit_image_metadata_(self._request_adapter)
