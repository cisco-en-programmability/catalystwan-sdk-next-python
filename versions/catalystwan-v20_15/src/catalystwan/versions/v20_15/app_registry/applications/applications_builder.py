# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import EditAppDetailsPutRequest, PayloadItems


class ApplicationsBuilder:
    """
    Builds and executes requests for operations under /app-registry/applications
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_app_list(
        self, traffic_class: Optional[str] = None, business_relevance: Optional[str] = None, **kw
    ) -> List[Any]:
        """
        Get All the App for the given conditions

        :param traffic_class: Traffic Class
        :param business_relevance: Business Relevance
        :returns: List[Any]
        """
        params = {
            "trafficClass": traffic_class,
            "businessRelevance": business_relevance,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/app-registry/applications",
            return_type=List[Any],
            params=params,
            **kw,
        )

    def edit_app_details(
        self, payload: Optional[List[EditAppDetailsPutRequest]] = None, **kw
    ) -> List[Any]:
        """
        Edit App Details

        :param payload: Payload
        :returns: List[Any]
        """
        return self._request_adapter.request(
            "PUT",
            "/dataservice/app-registry/applications",
            return_type=List[Any],
            payload=payload,
            **kw,
        )

    def edit_app_details_with_uuid(
        self, app_id: str, payload: Optional[Any] = None, **kw
    ) -> PayloadItems:
        """
        Edit App Details

        :param app_id: appId
        :param payload: Request body
        :returns: PayloadItems
        """
        params = {
            "appId": app_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/app-registry/applications/{appId}",
            return_type=PayloadItems,
            params=params,
            payload=payload,
            **kw,
        )
