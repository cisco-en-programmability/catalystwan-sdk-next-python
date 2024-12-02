# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .status.status_builder import StatusBuilder


class OnboardBuilder:
    """
    Builds and executes requests for operations under /mdp/onboard
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def onboard_mdp(self):
        class onboard_mdp_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Start MDP onboarding operation

                :param payload: Onboard
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/mdp/onboard", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return onboard_mdp_(self._request_adapter)

    @property
    def update_onboarding_payload(self):
        class update_onboarding_payload_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, nms_id: str, payload: Optional[Any] = None, **kw) -> Any:
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
                    "PUT",
                    "/dataservice/mdp/onboard/{nmsId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_onboarding_payload_(self._request_adapter)

    def offboard(self, nms_id: str, **kw):
        """
        offboard the mdp application

        :param nms_id: Nms id
        :returns: None
        """
        params = {
            "nmsId": nms_id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/mdp/onboard/{nmsId}", params=params, **kw
        )

    @property
    def status(self) -> StatusBuilder:
        """
        The status property
        """
        from .status.status_builder import StatusBuilder

        return StatusBuilder(self._request_adapter)
