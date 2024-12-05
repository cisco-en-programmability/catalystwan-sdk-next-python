# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class AttachmentBuilder:
    """
    Builds and executes requests for operations under /networkdesign/profile/attachment
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def push_device_profile_template(self, profile_id: str, payload: Optional[Any] = None, **kw) -> Any:
        """
        Attach to device profile

        :param profile_id: Device profile Id
        :param payload: Device template
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "pushDeviceProfileTemplate")
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "POST", "/dataservice/networkdesign/profile/attachment/{profileId}", params=params, payload=payload, **kw
        )
