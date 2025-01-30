# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any

from catalystwan.abc import RequestAdapterInterface


class StatusBuilder:
    """
    Builds and executes requests for operations under /networkdesign/profile/status
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_device_profile_config_status(self, **kw) -> Any:
        """
        Get device profile configuration status

        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getDeviceProfileConfigStatus")
        return self._request_adapter.request(
            "GET", "/dataservice/networkdesign/profile/status", **kw
        )

    def get_device_profile_config_status_by_profile_id(self, profile_id: str, **kw) -> Any:
        """
        Get device profile configuration status by profile Id

        :param profile_id: Device profile Id
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getDeviceProfileConfigStatusByProfileId")
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/networkdesign/profile/status/{profileId}", params=params, **kw
        )
