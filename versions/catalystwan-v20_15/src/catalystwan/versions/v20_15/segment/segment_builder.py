# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class SegmentBuilder:
    """
    Builds and executes requests for operations under /segment
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_segments(self, **kw) -> List[Any]:
        """
        Get network segments

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/segment", return_type=List[Any], **kw
        )

    @property
    def create_segment(self):
        class create_segment_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create network segment

                :param payload: Network segment
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/segment", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_segment_(self._request_adapter)

    def get_segment(self, id: str, **kw) -> List[Any]:
        """
        Get network segment

        :param id: Segment Id
        :returns: List[Any]
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/segment/{id}",
            return_type=List[Any],
            params=params,
            **kw,
        )

    @property
    def edit_segment(self):
        class edit_segment_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, id: str, payload: Optional[Any] = None, **kw):
                """
                Edit network segment

                :param id: Segment Id
                :param payload: Network segment
                :returns: None
                """
                params = {
                    "id": id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/segment/{id}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return edit_segment_(self._request_adapter)

    def delete_segment(self, id: str, **kw):
        """
        Delete network segment

        :param id: Segment Id
        :returns: None
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/segment/{id}", params=params, **kw
        )
