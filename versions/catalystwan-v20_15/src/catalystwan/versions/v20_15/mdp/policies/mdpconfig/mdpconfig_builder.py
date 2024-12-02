# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type
from catalystwan.abc import RequestAdapterInterface


class MdpconfigBuilder:
    """
    Builds and executes requests for operations under /mdp/policies/mdpconfig
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def add_internal_policy(self):
        class add_internal_policy_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Add internal policy from vmanage

                :param payload: addInternalPolicy
                :returns: Any
                """
                return self._request_adapter.request(
                    "PUT", "/dataservice/mdp/policies/mdpconfig", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return add_internal_policy_(self._request_adapter)

    def retrieve_mdp_config_object(self, device_id: str, **kw) -> List[Any]:
        """
        Retrieve MDP ConfigObject

        :param device_id: Device id
        :returns: List[Any]
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/mdp/policies/mdpconfig/{deviceId}",
            return_type=List[Any],
            params=params,
            **kw,
        )
