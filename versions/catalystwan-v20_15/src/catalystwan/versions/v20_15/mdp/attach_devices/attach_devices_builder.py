# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface


class AttachDevicesBuilder:
    """
    Builds and executes requests for operations under /mdp/attachDevices
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def retrieve_mdp_attached_devices(self, nms_id: str, **kw) -> List[Any]:
        """
        Retrieve MDP attached devices

        :param nms_id: Nms id
        :returns: List[Any]
        """
        params = {
            "nmsId": nms_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/mdp/attachDevices/{nmsId}",
            return_type=List[Any],
            params=params,
            **kw,
        )

    def edit_attached_devices(self, nms_id: str, payload: Optional[Any] = None, **kw) -> Any:
        """
        Edit attached devices

        :param nms_id: Nms id
        :param payload: deviceList
        :returns: Any
        """
        params = {
            "nmsId": nms_id,
        }
        return self._request_adapter.request(
            "PUT", "/dataservice/mdp/attachDevices/{nmsId}", params=params, payload=payload, **kw
        )

    def attach_devices(self, nms_id: str, payload: Optional[Any] = None, **kw) -> Any:
        """
        Share devices with MDP

        :param nms_id: Nms id
        :param payload: deviceList
        :returns: Any
        """
        params = {
            "nmsId": nms_id,
        }
        return self._request_adapter.request(
            "POST", "/dataservice/mdp/attachDevices/{nmsId}", params=params, payload=payload, **kw
        )
