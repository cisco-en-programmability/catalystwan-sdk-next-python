# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .status.status_builder import StatusBuilder


class OnboardBuilder:
    """
    Builds and executes requests for operations under /mdp/onboard
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def onboard_mdp(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Start MDP onboarding operation

        :param payload: Onboard
        :returns: Any
        """
        return self._request_adapter.request("POST", "/dataservice/mdp/onboard", payload=payload, **kw)

    def update_onboarding_payload(self, nms_id: str, payload: Optional[Any] = None, **kw) -> Any:
        """
        update MDP onboarding document

        :param nms_id: Nms id
        :param payload: Onboard
        :returns: Any
        """
        params = {
            "nmsId": nms_id,
        }
        return self._request_adapter.request(
            "PUT", "/dataservice/mdp/onboard/{nmsId}", params=params, payload=payload, **kw
        )

    def offboard(self, nms_id: str, **kw):
        """
        offboard the mdp application

        :param nms_id: Nms id
        :returns: None
        """
        params = {
            "nmsId": nms_id,
        }
        return self._request_adapter.request("DELETE", "/dataservice/mdp/onboard/{nmsId}", params=params, **kw)

    @property
    def status(self) -> StatusBuilder:
        """
        The status property
        """
        from .status.status_builder import StatusBuilder

        return StatusBuilder(self._request_adapter)
